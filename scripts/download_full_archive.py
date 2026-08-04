from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


DEFAULT_GITHUB_REPO = "MozhiJiawei/ccn-report"
DEFAULT_RELEASE_TAG = "latest-compressed-archive"
USER_AGENT = "ccn-report-archive-downloader"


def fail(message: str) -> None:
    raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def release_asset_url(github_repo: str, tag: str, filename: str) -> str:
    owner, separator, repo = github_repo.partition("/")
    if not separator or not owner or not repo or "/" in repo:
        fail(f"invalid GitHub repository name: {github_repo}")
    return (
        f"https://github.com/{quote(owner, safe='')}/{quote(repo, safe='')}/releases/download/"
        f"{quote(tag, safe='')}/{quote(filename, safe='')}"
    )


def download(url: str, destination: Path) -> None:
    headers = {"User-Agent": USER_AGENT}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urlopen(request) as response, destination.open("wb") as output:
            shutil.copyfileobj(response, output, length=1024 * 1024)
    except (HTTPError, URLError, OSError) as exc:
        if destination.exists():
            destination.unlink()
        fail(f"failed to download {url}: {exc}")


def load_manifest(path: Path) -> dict[str, object]:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid release manifest: {exc}")
    if not isinstance(manifest, dict) or not isinstance(manifest.get("packages"), list):
        fail("release manifest does not contain a packages list")
    return manifest


def package_records(manifest: dict[str, object]) -> list[tuple[str, str]]:
    records: list[tuple[str, str]] = []
    seen: set[str] = set()
    for item in manifest["packages"]:
        if not isinstance(item, dict):
            fail("release manifest contains an invalid package entry")
        filename = item.get("filename")
        digest = item.get("sha256")
        if not isinstance(filename, str) or not filename.endswith(".zip"):
            fail("release manifest contains an invalid package filename")
        if Path(filename).name != filename or filename in seen:
            fail(f"release manifest contains an unsafe or duplicate package filename: {filename}")
        if not isinstance(digest, str) or len(digest) != 64:
            fail(f"release manifest contains an invalid SHA256 for {filename}")
        seen.add(filename)
        records.append((filename, digest.lower()))
    if not records:
        fail("release manifest contains no monthly packages")
    return records


def safe_member_path(name: str) -> Path:
    normalized = name.replace("\\", "/")
    pure = PurePosixPath(normalized)
    if pure.is_absolute() or not pure.parts or any(part in {"", ".", ".."} for part in pure.parts):
        fail(f"unsafe ZIP entry: {name}")
    if ":" in pure.parts[0]:
        fail(f"unsafe ZIP entry: {name}")
    return Path(*pure.parts)


def extract_packages(package_paths: list[Path], destination: Path) -> int:
    extracted: set[Path] = set()
    for package_path in package_paths:
        try:
            archive = zipfile.ZipFile(package_path)
        except (OSError, zipfile.BadZipFile) as exc:
            fail(f"invalid ZIP package {package_path.name}: {exc}")
        with archive:
            for info in archive.infolist():
                relative = safe_member_path(info.filename)
                if info.is_dir():
                    (destination / relative).mkdir(parents=True, exist_ok=True)
                    continue
                if relative in extracted:
                    fail(f"duplicate archive path across monthly packages: {relative.as_posix()}")
                target = destination / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as source, target.open("wb") as output:
                    shutil.copyfileobj(source, output, length=1024 * 1024)
                extracted.add(relative)
    return len(extracted)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download every monthly ccn-report release package and assemble a full local archive."
    )
    parser.add_argument("--github-repo", default=DEFAULT_GITHUB_REPO, help="Repository in owner/name form.")
    parser.add_argument("--tag", default=DEFAULT_RELEASE_TAG, help="Release tag to download.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path.cwd() / "ccn-report-full",
        help="New directory that will contain the assembled archive (must not already exist).",
    )
    args = parser.parse_args()

    output_dir = args.output_dir.expanduser().absolute()
    if output_dir.exists():
        fail(f"output directory already exists: {output_dir}")
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="ccn-report-download-", dir=output_dir.parent) as temporary:
        temporary_root = Path(temporary)
        manifest_path = temporary_root / "manifest.json"
        download(release_asset_url(args.github_repo, args.tag, "manifest.json"), manifest_path)
        manifest = load_manifest(manifest_path)
        records = package_records(manifest)

        package_paths: list[Path] = []
        for position, (filename, expected_digest) in enumerate(records, start=1):
            print(f"[{position}/{len(records)}] Downloading {filename}")
            package_path = temporary_root / filename
            download(release_asset_url(args.github_repo, args.tag, filename), package_path)
            actual_digest = sha256(package_path)
            if actual_digest != expected_digest:
                fail(f"SHA256 mismatch for {filename}: expected {expected_digest}, got {actual_digest}")
            package_paths.append(package_path)

        assembled = temporary_root / "assembled"
        assembled.mkdir()
        file_count = extract_packages(package_paths, assembled)
        assembled.replace(output_dir)

    print(f"Assembled {len(records)} monthly packages and {file_count} files at {output_dir}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
