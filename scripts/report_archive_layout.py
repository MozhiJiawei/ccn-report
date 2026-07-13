from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path


REPORT_DIR_RE = re.compile(
    r"^(?P<date>\d{8})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-(?P<creator>[\w\u4e00-\u9fff-]+)$"
)
IGNORED_DIRECTORY_NAMES = {
    ".git",
    ".github",
    ".mypy_cache",
    ".pytest_cache",
    ".tmp",
    "__pycache__",
    "scripts",
    "tests",
}


def report_date(name: str) -> str | None:
    match = REPORT_DIR_RE.fullmatch(name)
    if not match:
        return None
    value = match.group("date")
    try:
        datetime.strptime(value, "%Y%m%d")
    except ValueError:
        return None
    return value


def is_valid_report_dir_name(name: str) -> bool:
    return report_date(name) is not None


def find_report_dirs(root: Path) -> list[Path]:
    """Find final report directories without assuming category root names."""
    found: list[Path] = []

    def visit(directory: Path, depth: int) -> None:
        for child in sorted(directory.iterdir(), key=lambda item: item.name):
            if child.is_symlink() or not child.is_dir() or child.name in IGNORED_DIRECTORY_NAMES:
                continue
            # Reports must remain at least two levels below the repository root.
            if depth + 1 >= 2 and is_valid_report_dir_name(child.name):
                found.append(child)
                continue
            visit(child, depth + 1)

    visit(root, 0)
    return found
