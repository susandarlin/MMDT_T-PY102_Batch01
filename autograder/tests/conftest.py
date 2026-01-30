# autograder/tests/conftest.py
from __future__ import annotations

import json
from pathlib import Path
import pytest

RESULTS_PATH = Path("autograder") / "results.json"


def pytest_configure(config):
    config.addinivalue_line("markers", "points(n): assign n points to a test")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only count each test once (on the "call" phase)
    if rep.when != "call":
        return

    pts = 0
    mark = item.get_closest_marker("points")
    if mark and mark.args:
        pts = int(mark.args[0])

    # Store per-test points
    item.config._points_detail = getattr(item.config, "_points_detail", [])
    item.config._points_detail.append(
        {
            "nodeid": item.nodeid,
            "outcome": rep.outcome,   # "passed", "failed", "skipped"
            "points": pts if rep.outcome == "passed" else 0,
            "max_points": pts,
        }
    )


def pytest_sessionfinish(session, exitstatus):
    details = getattr(session.config, "_points_detail", [])
    earned = sum(d["points"] for d in details)
    max_points = sum(d["max_points"] for d in details)

    payload = {
        "earned": earned,
        "max": max_points,
        "details": details,
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"\nSCORE: {earned}/{max_points}\n")
