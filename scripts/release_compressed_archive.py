from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from PIL import Image

from report_archive_layout import find_report_dirs, report_date


# Keep the invocation path instead of resolving it. On Windows this allows
# callers to use a short subst drive for repositories that contain very deep
# archived HTML paths.
REPO_ROOT = Path(__file__).parents[1].absolute()
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}
GIF_EXTENSIONS = {".gif"}
TEXT_EXTENSIONS = {
    ".css",
    ".htm",
    ".html",
    ".js",
    ".json",
    ".markdown",
    ".md",
    ".mjs",
    ".svg",
    ".xml",
}
LATEST_RELEASE_TAG = "latest-compressed-archive"
MANIFEST_SCHEMA_VERSION = 4


@dataclass(frozen=True)
class ConvertedAsset:
    old_relative: Path
    new_relative: Path
    old_bytes: int
    new_bytes: int


def run(command: list[str], cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess[str]:
    print(f"$ {' '.join(command)}")
    return subprocess.run(command, cwd=cwd, check=False, text=True, capture_output=True)


def fail(message: str) -> None:
    raise RuntimeError(message)


def size_of(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def copy_report_dirs(source: Path, destination: Path, report_dirs: list[Path]) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    for report_dir in report_dirs:
        relative = report_dir.relative_to(source)
        shutil.copytree(report_dir, destination / relative)


def group_reports_by_month(report_dirs: list[Path]) -> dict[str, list[Path]]:
    grouped: dict[str, list[Path]] = {}
    for report_dir in report_dirs:
        date = report_date(report_dir.name)
        if date is not None:
            grouped.setdefault(date[:6], []).append(report_dir)
    return grouped


def convert_static_image(source: Path, quality: int) -> tuple[Path | None, str | None]:
    target = source.with_suffix(".webp")
    try:
        data = source.read_bytes()
        image_source: Path | BytesIO
        if data.startswith(b"\xef\xbb\xbf\x89PNG\r\n\x1a\n"):
            image_source = BytesIO(data[3:])
        elif data.startswith(b"\xef\xbb\xbf\xef\xbf\xbdPNG\r\n\x1a\n"):
            image_source = BytesIO(b"\x89PNG\r\n\x1a\n" + data[13:])
        else:
            image_source = source
        with Image.open(image_source) as image:
            if image.mode not in {"RGB", "RGBA"}:
                image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            image.save(target, "WEBP", quality=quality, method=6)
    except Exception as exc:
        if target.exists():
            target.unlink()
        return None, str(exc)
    return target, None


def convert_gif(source: Path, quality: int) -> tuple[Path | None, str | None]:
    target = source.with_suffix(".webp")
    command = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(source),
        "-loop",
        "0",
        "-q:v",
        str(quality),
        str(target),
    ]
    completed = subprocess.run(command, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        if target.exists():
            target.unlink()
        return None, completed.stderr.strip() or "ffmpeg failed"
    return target, None


def candidate_assets(root: Path) -> list[Path]:
    allowed = IMAGE_EXTENSIONS | GIF_EXTENSIONS
    return [
        path
        for report_dir in find_report_dirs(root)
        for path in report_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in allowed
    ]


def compress_assets(
    root: Path,
    quality: int,
    min_gain: float,
    force_webp: bool = False,
) -> tuple[list[ConvertedAsset], list[dict[str, object]]]:
    converted: list[ConvertedAsset] = []
    skipped: list[dict[str, object]] = []

    for asset in candidate_assets(root):
        old_bytes = asset.stat().st_size
        if asset.suffix.lower() in IMAGE_EXTENSIONS:
            output, error = convert_static_image(asset, quality)
        else:
            output, error = convert_gif(asset, quality)

        if error or output is None or not output.exists():
            skipped.append({"path": str(asset.relative_to(root)), "reason": error or "no output"})
            continue

        new_bytes = output.stat().st_size
        if force_webp or new_bytes < old_bytes * (1 - min_gain):
            old_relative = asset.relative_to(root)
            new_relative = output.relative_to(root)
            asset.unlink()
            converted.append(ConvertedAsset(old_relative, new_relative, old_bytes, new_bytes))
        else:
            output.unlink()
            skipped.append(
                {
                    "path": str(asset.relative_to(root)),
                    "reason": "webp not smaller enough",
                    "old_bytes": old_bytes,
                    "new_bytes": new_bytes,
                }
            )

    return converted, skipped


def url_variants(value: str) -> set[str]:
    variants = {value}
    variants.add(value.replace("/", "\\"))
    encoded = quote(value, safe="/#?&=%:;,+@!$'()*[]")
    variants.add(encoded)
    variants.add(encoded.replace("/", "\\"))
    return variants


def relative_url(from_file: Path, target: Path) -> str:
    raw = os.path.relpath(target, from_file.parent)
    return raw.replace(os.sep, "/")


def update_text_references(root: Path, converted: list[ConvertedAsset]) -> int:
    changed_count = 0
    converted_targets = [(root / item.old_relative, root / item.new_relative) for item in converted]

    for document in root.rglob("*"):
        if not document.is_file() or document.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = document.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = document.read_text(encoding="utf-8-sig")
            except UnicodeDecodeError:
                continue

        original = text
        for old_target, new_target in converted_targets:
            old_rel = relative_url(document, old_target)
            new_rel = relative_url(document, new_target)
            replacements = {old_rel: new_rel}
            if old_target.parent == document.parent:
                replacements[old_target.name] = new_target.name
            for old_value, new_value in replacements.items():
                for variant in url_variants(old_value):
                    replacement = new_value.replace("/", "\\") if "\\" in variant else new_value
                    text = text.replace(variant, replacement)

        if text != original:
            changed_count += 1
            document.write_text(text, encoding="utf-8", newline="")

    return changed_count


def clean_local_url(raw_url: str) -> str:
    stripped = raw_url.strip().strip("\"'")
    split = urlsplit(stripped)
    return unquote(split.path)


def is_external_or_inline(raw_url: str) -> bool:
    stripped = raw_url.strip().strip("\"'")
    if not stripped or stripped.startswith("#") or stripped.startswith("//"):
        return True
    scheme = urlsplit(stripped).scheme.lower()
    return scheme in {"data", "http", "https", "javascript", "mailto", "tel"}


def check_local_references(root: Path) -> list[dict[str, object]]:
    attr_re = re.compile(r"""(?:src|href|poster)=["'](?P<url>[^"']+)["']""", re.IGNORECASE)
    css_re = re.compile(r"""url\(\s*["']?(?P<url>[^)"']+)["']?\s*\)""", re.IGNORECASE)
    missing: list[dict[str, object]] = []
    resolved_root = root.resolve()

    for document in root.rglob("*"):
        if not document.is_file() or document.suffix.lower() not in {".html", ".htm", ".css"}:
            continue
        text = document.read_text(encoding="utf-8", errors="ignore")
        urls = [match.group("url") for match in attr_re.finditer(text)]
        urls.extend(match.group("url") for match in css_re.finditer(text))

        for raw_url in urls:
            if is_external_or_inline(raw_url):
                continue
            local_path = clean_local_url(raw_url)
            if not local_path:
                continue
            target = (document.parent / local_path).resolve()
            try:
                target.relative_to(resolved_root)
            except ValueError:
                continue
            if not target.exists():
                missing.append({"document": str(document.relative_to(root)), "url": raw_url})

    return missing


def write_zip_entries(entries: list[tuple[Path, Path]], destination: Path) -> None:
    if destination.exists():
        destination.unlink()
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, relative in sorted(entries, key=lambda item: item[1].as_posix()):
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info._compresslevel = 9
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            with path.open("rb") as source, archive.open(info, "w", force_zip64=True) as target:
                shutil.copyfileobj(source, target, length=1024 * 1024)


def write_zip(source: Path, destination: Path) -> None:
    entries = [(path, path.relative_to(source)) for path in source.rglob("*") if path.is_file()]
    write_zip_entries(entries, destination)


def write_full_zip(package_roots: list[Path], destination: Path) -> None:
    entries = [
        (path, path.relative_to(root))
        for root in package_roots
        for path in root.rglob("*")
        if path.is_file()
    ]
    write_zip_entries(entries, destination)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def infer_github_repo() -> str:
    completed = run(["git", "remote", "get-url", "origin"])
    if completed.returncode != 0:
        fail(completed.stderr.strip() or "failed to read git origin")
    remote = completed.stdout.strip()
    match = re.search(r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$", remote)
    if not match:
        fail(f"cannot infer GitHub repo from origin: {remote}")
    return f"{match.group('owner')}/{match.group('repo')}"


def create_release(
    github_repo: str,
    tag: str,
    title: str,
    notes_path: Path,
    assets: list[Path],
    prerelease: bool,
) -> str:
    command = [
        "gh",
        "release",
        "create",
        tag,
        *[str(asset) for asset in assets],
        "--repo",
        github_repo,
        "--title",
        title,
        "--notes-file",
        str(notes_path),
        "--target",
        "main",
    ]
    if prerelease:
        command.append("--prerelease")

    completed = run(command)
    if completed.returncode != 0:
        fail(completed.stderr.strip() or completed.stdout.strip() or "gh release create failed")
    return completed.stdout.strip()


def release_exists(github_repo: str, tag: str) -> bool:
    completed = run(["gh", "release", "view", tag, "--repo", github_repo])
    return completed.returncode == 0


def update_release(
    github_repo: str,
    tag: str,
    title: str,
    notes_path: Path,
    assets: list[Path],
    prerelease: bool,
) -> str:
    edit_command = [
        "gh",
        "release",
        "edit",
        tag,
        "--repo",
        github_repo,
        "--title",
        title,
        "--notes-file",
        str(notes_path),
    ]
    if prerelease:
        edit_command.append("--prerelease")
    else:
        edit_command.append("--latest")

    completed = run(edit_command)
    if completed.returncode != 0:
        fail(completed.stderr.strip() or completed.stdout.strip() or "gh release edit failed")

    upload_command = [
        "gh",
        "release",
        "upload",
        tag,
        *[str(asset) for asset in assets],
        "--repo",
        github_repo,
        "--clobber",
    ]
    completed = run(upload_command)
    if completed.returncode != 0:
        fail(completed.stderr.strip() or completed.stdout.strip() or "gh release upload failed")

    return f"https://github.com/{github_repo}/releases/tag/{tag}"


def load_release_manifest(github_repo: str, tag: str, destination: Path) -> dict[str, object]:
    destination.mkdir(parents=True, exist_ok=True)
    completed = run(
        ["gh", "release", "download", tag, "--repo", github_repo, "--pattern", "manifest.json", "--dir", str(destination), "--clobber"]
    )
    manifest = destination / "manifest.json"
    if completed.returncode != 0 or not manifest.exists():
        return {}
    try:
        return json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def list_release_assets(github_repo: str, tag: str) -> set[str]:
    completed = run(["gh", "release", "view", tag, "--repo", github_repo, "--json", "assets", "--jq", ".assets[].name"])
    if completed.returncode != 0:
        fail(completed.stderr.strip() or completed.stdout.strip() or "failed to list release assets")
    return {line.strip() for line in completed.stdout.splitlines() if line.strip()}


def delete_release_assets(github_repo: str, tag: str, names: set[str]) -> list[str]:
    deleted: list[str] = []
    for name in sorted(names):
        completed = run(["gh", "release", "delete-asset", tag, name, "--repo", github_repo, "--yes"])
        if completed.returncode != 0:
            fail(completed.stderr.strip() or completed.stdout.strip() or f"failed to delete release asset {name}")
        deleted.append(name)
    return deleted


def select_release_changes(
    package_paths: list[Path],
    packages: list[dict[str, object]],
    full_archive_path: Path,
    full_archive_info: dict[str, object],
    index_path: Path,
    index_info: dict[str, object],
    previous: dict[str, object],
    existing_assets: set[str],
) -> tuple[list[Path], list[Path], set[str]]:
    if len(package_paths) != len(packages):
        fail("package paths and manifest entries have different lengths")
    for path, package in zip(package_paths, packages):
        if path.name != package.get("filename"):
            fail(f"package path and manifest filename differ: {path.name} != {package.get('filename')}")
    if previous.get("manifest_schema_version") != MANIFEST_SCHEMA_VERSION:
        previous = {}
    previous_items = previous.get("packages", [])
    previous_packages = {
        str(item.get("filename")): str(item.get("sha256"))
        for item in previous_items
        if isinstance(item, dict)
    } if isinstance(previous_items, list) else {}
    previous_index = previous.get("index", {}) if isinstance(previous.get("index"), dict) else {}
    changed_packages = [
        path
        for path, package in zip(package_paths, packages)
        if previous_packages.get(path.name) != package["sha256"] or path.name not in existing_assets
    ]
    changed_assets = list(changed_packages)
    previous_full_archive = previous.get("full_archive", {}) if isinstance(previous.get("full_archive"), dict) else {}
    if (
        previous_full_archive.get("sha256") != full_archive_info["sha256"]
        or full_archive_path.name not in existing_assets
    ):
        changed_assets.append(full_archive_path)
    if previous_index.get("sha256") != index_info["sha256"] or index_path.name not in existing_assets:
        changed_assets.append(index_path)
    desired_zip_names = {path.name for path in package_paths} | {full_archive_path.name}
    obsolete_assets = {
        name
        for name in existing_assets
        if name not in desired_zip_names
        and (
            re.fullmatch(r"ccn-report-\d{6}(?:\d{2})?-q\d+\.zip", name)
            or re.fullmatch(r"ccn-report-full-q\d+\.zip", name)
            or re.fullmatch(r"ccn-report-(?:latest-)?compressed(?:-q\d+)?(?:-\d{8}-\d{6})?\.zip", name)
        )
    }
    return changed_packages, changed_assets, obsolete_assets


def main() -> int:
    parser = argparse.ArgumentParser(description="Build and incrementally publish month-partitioned ccn-report archives.")
    parser.add_argument("--quality", type=int, default=70, help="WebP quality for image conversion.")
    parser.add_argument("--min-gain", type=float, default=0.02, help="Minimum size reduction ratio to keep WebP output.")
    parser.add_argument("--work-dir", type=Path, default=REPO_ROOT.parent / ".tmp" / "ccn")
    parser.add_argument("--tag", default=LATEST_RELEASE_TAG)
    parser.add_argument("--title", default="")
    parser.add_argument("--github-repo", default="")
    parser.add_argument("--no-upload", action="store_true", help="Build assets but do not create a GitHub Release.")
    parser.add_argument("--stable", action="store_true", help="Create a normal release instead of a prerelease.")
    parser.add_argument("--snapshot", action="store_true", help="Create a timestamped immutable release instead of updating latest.")
    parser.add_argument("--force-webp", action="store_true", help="Keep WebP outputs even when they are not smaller.")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    tag = args.tag
    if args.snapshot and tag == LATEST_RELEASE_TAG:
        tag = f"ccn-report-monthly-archives-q{args.quality}-{timestamp}"
    title = args.title or (
        f"ccn-report full and monthly archives q{args.quality}"
        if not args.snapshot
        else f"ccn-report full and monthly archives q{args.quality} {timestamp}"
    )
    github_repo = args.github_repo or ("" if args.no_upload else infer_github_repo())

    report_dirs = find_report_dirs(REPO_ROOT)
    if not report_dirs:
        fail("no report directories found")
    grouped = group_reports_by_month(report_dirs)

    assets_root = args.work_dir / "assets"
    if args.work_dir.exists():
        shutil.rmtree(args.work_dir)
    assets_root.mkdir(parents=True, exist_ok=True)

    package_paths: list[Path] = []
    package_roots: list[Path] = []
    packages: list[dict[str, object]] = []
    total_source_size = 0
    total_compressed_size = 0
    for month, monthly_reports in sorted(grouped.items()):
        copy_root = args.work_dir / "p" / month
        print(f"Building {month} from {len(monthly_reports)} report(s)")
        copy_report_dirs(REPO_ROOT, copy_root, monthly_reports)
        copied_size = size_of(copy_root)
        total_source_size += copied_size
        converted, skipped = compress_assets(copy_root, args.quality, args.min_gain, args.force_webp)
        changed_text_files = update_text_references(copy_root, converted)
        compressed_size = size_of(copy_root)
        total_compressed_size += compressed_size
        missing_refs = check_local_references(copy_root)
        archive_path = assets_root / f"ccn-report-{month}-q{args.quality}.zip"
        write_zip(copy_root, archive_path)
        package_paths.append(archive_path)
        package_roots.append(copy_root)
        packages.append(
            {
                "month": month,
                "filename": archive_path.name,
                "sha256": sha256(archive_path),
                "bytes": archive_path.stat().st_size,
                "report_count": len(monthly_reports),
                "reports": [path.relative_to(REPO_ROOT).as_posix() for path in sorted(monthly_reports)],
                "source_bytes": copied_size,
                "compressed_tree_bytes": compressed_size,
                "converted_count": len(converted),
                "skipped_count": len(skipped),
                "changed_text_files": changed_text_files,
                "missing_reference_count": len(missing_refs),
                "missing_references": missing_refs[:100],
            }
        )

    full_archive_path = assets_root / f"ccn-report-full-q{args.quality}.zip"
    write_full_zip(package_roots, full_archive_path)
    full_archive_info = {
        "filename": full_archive_path.name,
        "sha256": sha256(full_archive_path),
        "bytes": full_archive_path.stat().st_size,
        "report_count": len(report_dirs),
    }

    index_source = REPO_ROOT / "index.html"
    if not index_source.is_file():
        fail("repository index.html not found")
    index_path = assets_root / "index.html"
    shutil.copy2(index_source, index_path)
    index_info = {"filename": index_path.name, "sha256": sha256(index_path), "bytes": index_path.stat().st_size}

    report: dict[str, object] = {
        "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
        "tag": tag,
        "title": title,
        "github_repo": github_repo,
        "quality": args.quality,
        "min_gain": args.min_gain,
        "generated_at": datetime.now().astimezone().isoformat(),
        "source_report_bytes": total_source_size,
        "compressed_tree_bytes": total_compressed_size,
        "report_count": len(report_dirs),
        "package_count": len(packages),
        "packages": packages,
        "full_archive": full_archive_info,
        "index": index_info,
    }

    manifest_path = assets_root / "manifest.json"
    sums_path = assets_root / "SHA256SUMS.txt"
    notes_path = assets_root / "release-notes.md"
    manifest_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    checksum_entries = [(str(package["sha256"]), str(package["filename"])) for package in packages]
    checksum_entries.append((str(full_archive_info["sha256"]), full_archive_path.name))
    checksum_entries.append((str(index_info["sha256"]), index_path.name))
    sums_path.write_text("".join(f"{digest}  {name}\n" for digest, name in checksum_entries), encoding="ascii")
    notes_path.write_text(
        "\n".join(
            [
                f"# {title}",
                "",
                "Full and month-partitioned offline report archives generated from the current ccn-report working tree.",
                "",
                "## Size",
                "",
                f"- Reports: {len(report_dirs)}",
                f"- Monthly packages: {len(packages)}",
                f"- Full archive: {round(full_archive_path.stat().st_size / 1024 / 1024, 2)} MB",
                f"- Source report tree: {round(total_source_size / 1024 / 1024, 2)} MB",
                f"- Compressed expanded tree: {round(total_compressed_size / 1024 / 1024, 2)} MB",
                "",
                "## SHA256",
                "",
                *[f"- `{digest}`  `{name}`" for digest, name in checksum_entries],
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    release_url = ""
    if not args.no_upload:
        exists = release_exists(github_repo, tag)
        if args.snapshot or not exists:
            assets = [*package_paths, full_archive_path, index_path, manifest_path, sums_path]
            release_url = create_release(
                github_repo=github_repo,
                tag=tag,
                title=title,
                notes_path=notes_path,
                assets=assets,
                prerelease=not args.stable,
            )
        else:
            previous = load_release_manifest(github_repo, tag, args.work_dir / "previous")
            existing_assets = list_release_assets(github_repo, tag)
            changed_packages, changed_assets, obsolete_assets = select_release_changes(
                package_paths,
                packages,
                full_archive_path,
                full_archive_info,
                index_path,
                index_info,
                previous,
                existing_assets,
            )
            report["uploaded_monthly_packages"] = [path.name for path in changed_packages]
            release_url = update_release(
                github_repo=github_repo,
                tag=tag,
                title=title,
                notes_path=notes_path,
                assets=[*changed_assets, sums_path],
                prerelease=not args.stable,
            )
            # Upload replacements before deleting obsolete archives so a failed
            # upload cannot leave the rolling release without usable packages.
            report["deleted_assets"] = delete_release_assets(github_repo, tag, obsolete_assets)
        report["release_url"] = release_url
        manifest_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        completed = run(
            [
                "gh",
                "release",
                "upload",
                tag,
                str(manifest_path),
                "--repo",
                github_repo,
                "--clobber",
            ]
        )
        if completed.returncode != 0:
            fail(completed.stderr.strip() or completed.stdout.strip() or "gh release upload manifest failed")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    if release_url:
        print(release_url)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
