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


# Keep the invocation path instead of resolving it. On Windows this allows
# callers to use a short subst drive for repositories that contain very deep
# archived HTML paths.
REPO_ROOT = Path(__file__).parents[1].absolute()
REPORT_ROOTS = ("大厂动态", "开源软件分析", "学术论文分析")
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
SKIP_DIR_NAMES = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
LATEST_RELEASE_TAG = "latest-compressed-archive"


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


def copy_repo_tree(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    def ignore(_dir: str, names: list[str]) -> set[str]:
        return {name for name in names if name in SKIP_DIR_NAMES}

    for item in source.iterdir():
        if item.name in SKIP_DIR_NAMES:
            continue
        target = destination / item.name
        if item.is_dir():
            shutil.copytree(item, target, ignore=ignore)
        else:
            shutil.copy2(item, target)


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
        for report_root in REPORT_ROOTS
        for path in (root / report_root).rglob("*")
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
                target.relative_to(root.resolve())
            except ValueError:
                continue
            if not target.exists():
                missing.append({"document": str(document.relative_to(root)), "url": raw_url})

    return missing


def write_zip(source: Path, destination: Path) -> None:
    if destination.exists():
        destination.unlink()
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in source.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(source.parent))


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


def list_release_tags(github_repo: str) -> list[str]:
    completed = run(["gh", "release", "list", "--repo", github_repo, "--limit", "200"])
    if completed.returncode != 0:
        fail(completed.stderr.strip() or completed.stdout.strip() or "gh release list failed")

    tags: list[str] = []
    for line in completed.stdout.splitlines():
        columns = line.split("\t")
        if len(columns) >= 3:
            tags.append(columns[2])
    return tags


def cleanup_other_releases(github_repo: str, keep_tag: str) -> list[str]:
    deleted: list[str] = []
    for tag in list_release_tags(github_repo):
        if tag == keep_tag:
            continue
        completed = run(["gh", "release", "delete", tag, "--repo", github_repo, "--yes", "--cleanup-tag"])
        if completed.returncode != 0:
            fail(completed.stderr.strip() or completed.stdout.strip() or f"failed to delete release {tag}")
        deleted.append(tag)
    return deleted


def main() -> int:
    parser = argparse.ArgumentParser(description="Build and upload a compressed ccn-report release archive.")
    parser.add_argument("--quality", type=int, default=70, help="WebP quality for image conversion.")
    parser.add_argument("--min-gain", type=float, default=0.02, help="Minimum size reduction ratio to keep WebP output.")
    parser.add_argument("--work-dir", type=Path, default=REPO_ROOT.parent / ".tmp" / "ccn-report-full-release")
    parser.add_argument("--tag", default=LATEST_RELEASE_TAG)
    parser.add_argument("--title", default="")
    parser.add_argument("--github-repo", default="")
    parser.add_argument("--no-upload", action="store_true", help="Build assets but do not create a GitHub Release.")
    parser.add_argument("--stable", action="store_true", help="Create a normal release instead of a prerelease.")
    parser.add_argument("--snapshot", action="store_true", help="Create a timestamped immutable release instead of updating latest.")
    parser.add_argument("--force-webp", action="store_true", help="Keep WebP outputs even when they are not smaller.")
    parser.add_argument(
        "--keep-old-releases",
        action="store_true",
        help="Do not delete other releases after updating latest.",
    )
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    tag = args.tag
    if args.snapshot and tag == LATEST_RELEASE_TAG:
        tag = f"ccn-report-compressed-q{args.quality}-{timestamp}"
    title = args.title or (
        f"ccn-report latest compressed archive q{args.quality}"
        if not args.snapshot
        else f"ccn-report compressed archive q{args.quality} {timestamp}"
    )
    github_repo = args.github_repo or infer_github_repo()

    source_size = size_of(REPO_ROOT) - size_of(REPO_ROOT / ".git")
    copy_root = args.work_dir / "repo-copy"
    assets_root = args.work_dir / "assets"
    assets_root.mkdir(parents=True, exist_ok=True)

    print(f"Copying repository tree to {copy_root}")
    copy_repo_tree(REPO_ROOT, copy_root)
    copied_size = size_of(copy_root)

    converted, skipped = compress_assets(copy_root, args.quality, args.min_gain, args.force_webp)
    changed_text_files = update_text_references(copy_root, converted)
    compressed_size = size_of(copy_root)
    missing_refs = check_local_references(copy_root)

    archive_name = (
        f"ccn-report-compressed-q{args.quality}-{timestamp}.zip"
        if args.snapshot
        else f"ccn-report-latest-compressed-q{args.quality}.zip"
    )
    archive_path = assets_root / archive_name
    write_zip(copy_root, archive_path)
    archive_hash = sha256(archive_path)
    archive_size = archive_path.stat().st_size

    report = {
        "tag": tag,
        "title": title,
        "github_repo": github_repo,
        "quality": args.quality,
        "min_gain": args.min_gain,
        "source_bytes_excluding_git": source_size,
        "copied_bytes": copied_size,
        "compressed_tree_bytes": compressed_size,
        "archive_bytes": archive_size,
        "source_mb_excluding_git": round(source_size / 1024 / 1024, 2),
        "copied_mb": round(copied_size / 1024 / 1024, 2),
        "compressed_tree_mb": round(compressed_size / 1024 / 1024, 2),
        "archive_mb": round(archive_size / 1024 / 1024, 2),
        "tree_saved_percent": round((copied_size - compressed_size) * 100 / copied_size, 2) if copied_size else 0,
        "archive_sha256": archive_hash,
        "converted_count": len(converted),
        "skipped_count": len(skipped),
        "changed_text_files": changed_text_files,
        "missing_reference_count": len(missing_refs),
        "top_converted": [
            {
                "path": str(item.old_relative),
                "old_bytes": item.old_bytes,
                "new_bytes": item.new_bytes,
                "saved_bytes": item.old_bytes - item.new_bytes,
            }
            for item in sorted(converted, key=lambda entry: entry.old_bytes - entry.new_bytes, reverse=True)[:50]
        ],
        "skipped": skipped[:100],
        "missing_references": missing_refs[:100],
    }

    manifest_path = assets_root / "manifest.json"
    sums_path = assets_root / "SHA256SUMS.txt"
    notes_path = assets_root / "release-notes.md"
    manifest_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    sums_path.write_text(f"{archive_hash}  {archive_path.name}\n", encoding="ascii")
    notes_path.write_text(
        "\n".join(
            [
                f"# {title}",
                "",
                "Compressed offline HTML archive generated from the current ccn-report working tree.",
                "",
                "## Size",
                "",
                f"- Source tree excluding .git: {report['source_mb_excluding_git']} MB",
                f"- Compressed expanded tree: {report['compressed_tree_mb']} MB",
                f"- Release zip asset: {report['archive_mb']} MB",
                f"- Converted assets: {len(converted)}",
                f"- Text files with rewritten references: {changed_text_files}",
                f"- Missing local HTML/CSS references found after conversion: {len(missing_refs)}",
                "",
                "## SHA256",
                "",
                f"- `{archive_hash}`  `{archive_path.name}`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    release_url = ""
    if not args.no_upload:
        assets = [archive_path, manifest_path, sums_path]
        if args.snapshot or not release_exists(github_repo, tag):
            release_url = create_release(
                github_repo=github_repo,
                tag=tag,
                title=title,
                notes_path=notes_path,
                assets=assets,
                prerelease=not args.stable,
            )
        else:
            release_url = update_release(
                github_repo=github_repo,
                tag=tag,
                title=title,
                notes_path=notes_path,
                assets=assets,
                prerelease=not args.stable,
            )
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
        if not args.snapshot and not args.keep_old_releases:
            deleted_releases = cleanup_other_releases(github_repo, keep_tag=tag)
            report["deleted_old_releases"] = deleted_releases
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
