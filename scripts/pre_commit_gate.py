from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> int:
    print(f"$ {' '.join(command)}")
    completed = subprocess.run(command, cwd=REPO_ROOT)
    return completed.returncode


def main() -> int:
    checks = [
        [sys.executable, "scripts/check_report_archive.py"],
        [sys.executable, "scripts/check_local_media_assets.py"],
    ]

    for check in checks:
        code = run(check)
        if code != 0:
            return code

    print("Pre-commit gate passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
