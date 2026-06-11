from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_ROOT = REPO_ROOT / "reports"
REPORT_DIR_RE = re.compile(
    r"^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-(?P<date>\d{8})-(?P<creator>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)
ALLOWED_TOP_LEVEL = {"大厂动态", "开源软件分析", "学术论文分析"}
IGNORED_NAMES = {".gitkeep"}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def is_valid_report_dir_name(name: str) -> bool:
    match = REPORT_DIR_RE.fullmatch(name)
    if not match:
        return False

    try:
        datetime.strptime(match.group("date"), "%Y%m%d")
    except ValueError:
        return False

    return True


def check_reports_root(errors: list[str]) -> None:
    if not REPORTS_ROOT.exists():
        fail("Missing reports/ directory.", errors)
        return

    for item in REPORTS_ROOT.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if not item.is_dir():
            fail(f"reports/ must only contain category directories: {item.relative_to(REPO_ROOT)}", errors)
            continue
        if item.name not in ALLOWED_TOP_LEVEL:
            fail(
                f"Unknown top-level category {item.relative_to(REPO_ROOT)}. "
                f"Allowed: {', '.join(sorted(ALLOWED_TOP_LEVEL))}",
                errors,
            )


def check_category(category: Path, errors: list[str]) -> None:
    for item in category.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if not item.is_dir():
            fail(f"Category directories must not contain files directly: {item.relative_to(REPO_ROOT)}", errors)
            continue

        check_subject(item, errors)


def check_subject(subject: Path, errors: list[str]) -> None:
    for item in subject.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if not item.is_dir():
            fail(f"Subject directories must only contain report directories: {item.relative_to(REPO_ROOT)}", errors)
            continue
        if not is_valid_report_dir_name(item.name):
            fail(
                f"Invalid report directory name: {item.relative_to(REPO_ROOT)}. "
                "Expected <report-slug>-<YYYYMMDD>-<creator>.",
                errors,
            )


def main() -> int:
    errors: list[str] = []
    check_reports_root(errors)

    if REPORTS_ROOT.exists():
        for category in REPORTS_ROOT.iterdir():
            if category.is_dir() and category.name in ALLOWED_TOP_LEVEL:
                check_category(category, errors)

    if errors:
        print("Report archive validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Report archive validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
