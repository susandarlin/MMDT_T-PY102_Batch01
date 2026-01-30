# autograder/grade.py
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Set

REPO_ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS_DIR = REPO_ROOT / "submissions"

# Student IDs: PY102001001 .. PY102001020
ID_PREFIX = "PY102001"
MIN_ID = 1
MAX_ID = 20

# Allowed lab filenames
ALLOWED_LABS = {"lab01.py", "lab02.py", "lab03.py"}


def run(cmd: List[str]) -> str:
    """Run a command and return stdout; exit on error."""
    p = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
    if p.returncode != 0:
        print("Command failed:", " ".join(cmd))
        print(p.stdout)
        print(p.stderr)
        sys.exit(p.returncode)
    return p.stdout.strip()


def is_valid_student_id(student_id: str) -> bool:
    if not student_id.startswith(ID_PREFIX):
        return False
    if len(student_id) != len(ID_PREFIX) + 3:
        return False
    suffix = student_id[-3:]
    if not suffix.isdigit():
        return False
    n = int(suffix)
    return MIN_ID <= n <= MAX_ID


def get_changed_files(base_ref: str) -> List[str]:
    run(["git", "fetch", "origin", base_ref])
    diff = run(["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"])
    return [line for line in diff.splitlines() if line.strip()]


def main() -> None:
    base_ref = os.environ.get("BASE_REF", "main")
    changed = get_changed_files(base_ref)

    if not changed:
        print("No changes detected. Nothing to grade.")
        return

    # 1) Forbid modifications to autograder / workflows
    forbidden_prefixes = ("autograder/", ".github/")
    forbidden = [p for p in changed if p.startswith(forbidden_prefixes)]
    if forbidden:
        print("❌ Forbidden changes detected (do not modify autograder/workflow):")
        for p in forbidden:
            print("  -", p)
        sys.exit(1)

    # 2) Only allow changes inside submissions/
    outside = [p for p in changed if not p.startswith("submissions/")]
    if outside:
        print("❌ Changes outside submissions/ are not allowed:")
        for p in outside:
            print("  -", p)
        sys.exit(1)

    # 3) Identify which student folder(s) were touched + which labs were submitted
    student_ids: Set[str] = set()
    labs_touched: Set[str] = set()

    for p in changed:
        parts = Path(p).parts  # submissions, <ID>, <file...>
        if len(parts) < 3 or parts[0] != "submissions":
            print("❌ Invalid path (expected submissions/<ID>/<file>):", p)
            sys.exit(1)

        sid = parts[1]
        filename = parts[-1]

        student_ids.add(sid)
        if filename in ALLOWED_LABS:
            labs_touched.add(filename)

    if len(student_ids) != 1:
        print("❌ This PR modifies multiple student folders. Only one is allowed.")
        print("Student folders touched:", ", ".join(sorted(student_ids)))
        sys.exit(1)

    student_id = next(iter(student_ids))

    if not is_valid_student_id(student_id):
        print(f"❌ Invalid student ID folder: {student_id}")
        print(f"Expected: {ID_PREFIX}001 .. {ID_PREFIX}{MAX_ID:03d}")
        sys.exit(1)

    student_dir = SUBMISSIONS_DIR / student_id
    if not student_dir.exists():
        print(f"❌ Student folder does not exist: {student_dir}")
        sys.exit(1)

    if not labs_touched:
        print("❌ No lab file detected in this PR.")
        print("Expected one of:", ", ".join(sorted(ALLOWED_LABS)))
        sys.exit(1)

    print(f"Student: {student_id}")
    print(f"Lab file(s) changed in PR: {', '.join(sorted(labs_touched))}")

    # 4) Export info for pytest (tests can use these)
    env = os.environ.copy()
    env["STUDENT_ID"] = student_id
    env["STUDENT_DIR"] = str(student_dir)
    env["LABS_TOUCHED"] = ",".join(sorted(labs_touched))

    # 5) Run tests
    # NOTE: You'll add pytest + pytest-timeout in autograder/requirements.txt
    cmd = ["pytest", "-q", "autograder/tests", "--timeout=5"]
    p = subprocess.run(cmd, cwd=REPO_ROOT, env=env, text=True)
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
