from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from release_compressed_archive import (
    REPO_ROOT,
    check_local_references,
    compress_assets,
    size_of,
    update_text_references,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert report image assets in-place to q70 WebP.")
    parser.add_argument("--quality", type=int, default=70)
    parser.add_argument("--min-gain", type=float, default=0.02)
    parser.add_argument("--force-webp", action="store_true", default=True)
    parser.add_argument("--report", type=Path, default=REPO_ROOT / "compression-report.json")
    args = parser.parse_args()

    before = size_of(REPO_ROOT) - size_of(REPO_ROOT / ".git")
    converted, skipped = compress_assets(REPO_ROOT, args.quality, args.min_gain, args.force_webp)
    changed_text_files = update_text_references(REPO_ROOT, converted)
    after = size_of(REPO_ROOT) - size_of(REPO_ROOT / ".git")
    missing_refs = check_local_references(REPO_ROOT)

    report = {
        "quality": args.quality,
        "min_gain": args.min_gain,
        "force_webp": args.force_webp,
        "before_bytes_excluding_git": before,
        "after_bytes_excluding_git": after,
        "before_mb_excluding_git": round(before / 1024 / 1024, 2),
        "after_mb_excluding_git": round(after / 1024 / 1024, 2),
        "saved_mb": round((before - after) / 1024 / 1024, 2),
        "saved_percent": round((before - after) * 100 / before, 2) if before else 0,
        "converted_count": len(converted),
        "skipped_count": len(skipped),
        "changed_text_files": changed_text_files,
        "missing_reference_count": len(missing_refs),
        "top_converted": [
            {
                "path": str(item.old_relative),
                "new_path": str(item.new_relative),
                "old_bytes": item.old_bytes,
                "new_bytes": item.new_bytes,
                "saved_bytes": item.old_bytes - item.new_bytes,
            }
            for item in sorted(converted, key=lambda entry: entry.old_bytes - entry.new_bytes, reverse=True)[:100]
        ],
        "skipped": skipped[:100],
        "missing_references": missing_refs[:100],
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
