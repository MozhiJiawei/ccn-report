from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOTS = ("大厂动态", "开源软件分析", "学术论文分析")
UNCOMPRESSED_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png"}
MAX_DISPLAYED_ERRORS = 100


def iter_uncompressed_assets() -> list[Path]:
    assets: list[Path] = []
    for root_name in REPORT_ROOTS:
        root = REPO_ROOT / root_name
        if root.is_dir():
            assets.extend(
                path
                for path in root.rglob("*")
                if path.is_file() and path.suffix.lower() in UNCOMPRESSED_EXTENSIONS
            )
    return sorted(assets)


def main() -> int:
    assets = iter_uncompressed_assets()
    if assets:
        print("Compressed asset validation failed:")
        print("Report image assets must be archived as q70 WebP by default.")
        print("Run the archive compression flow before committing:")
        print("  python scripts/compress_report_assets.py --quality 70")
        for asset in assets[:MAX_DISPLAYED_ERRORS]:
            size_kib = asset.stat().st_size / 1024
            print(f"- {asset.relative_to(REPO_ROOT)} ({size_kib:.1f} KiB)")
        if len(assets) > MAX_DISPLAYED_ERRORS:
            print(f"- ... {len(assets) - MAX_DISPLAYED_ERRORS} more uncompressed assets")
        return 1

    print("Compressed asset validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
