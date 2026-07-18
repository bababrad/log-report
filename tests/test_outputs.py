"""Verify the access-log summary report against instruction.md success criteria.

There is exactly one test per numbered success criterion in instruction.md.

Expected values derived from environment/access.log:
  total_requests = 6   (6 non-empty request lines)
  unique_ips     = 3   (192.168.0.1, 192.168.0.2, 10.0.0.5)
  top_path       = "/index.html"  (requested 3 times; more than any other path)
"""

import json
from pathlib import Path

REPORT = Path("/app/report.json")

EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    """Load /app/report.json as a dict (shared helper, not a criterion check)."""
    assert REPORT.exists(), "no report.json found at /app/report.json"
    with REPORT.open() as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must contain a single JSON object"
    return data


def test_report_file_is_json_object():
    """Success criterion 1: a file exists at /app/report.json containing a
    single JSON object."""
    _load_report()


def test_total_requests():
    """Success criterion 2: total_requests equals the number of non-empty lines
    in /app/access.log."""
    data = _load_report()
    assert data.get("total_requests") == EXPECTED_TOTAL_REQUESTS, (
        f"total_requests should be {EXPECTED_TOTAL_REQUESTS}, "
        f"got {data.get('total_requests')!r}"
    )


def test_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct client IP
    addresses in the log."""
    data = _load_report()
    assert data.get("unique_ips") == EXPECTED_UNIQUE_IPS, (
        f"unique_ips should be {EXPECTED_UNIQUE_IPS}, got {data.get('unique_ips')!r}"
    )


def test_top_path():
    """Success criterion 4: top_path equals the most frequently requested path
    in the log."""
    data = _load_report()
    assert data.get("top_path") == EXPECTED_TOP_PATH, (
        f"top_path should be {EXPECTED_TOP_PATH!r}, got {data.get('top_path')!r}"
    )
