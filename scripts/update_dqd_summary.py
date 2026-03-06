#!/usr/bin/env python3
"""Update Data Quality pages from release-tagged DQD and DBT artifacts.

Manages a history of DQD results and DBT artifacts per OMOP release and
generates markdown summaries with cross-release diffs for the Data Quality
Results, Known Issues, DBT Tests, and landing pages.

Usage:
    # Ingest a new release (DQD + DBT artifacts)
    uv run scripts/update_dqd_summary.py ingest --release v1.0.0 \\
        --dqd <dqd_results.json> \\
        --dbt-manifest <manifest.json> \\
        --dbt-results <run_results.json> \\
        --dbt-catalog <catalog.json>

    # Regenerate all markdown pages from history
    uv run scripts/update_dqd_summary.py generate [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
DQD_HISTORY_DIR = Path(__file__).resolve().parent / "dqd_history"
DBT_HISTORY_DIR = Path(__file__).resolve().parent / "dbt_history"

DEFAULT_RESULTS = (
    REPO_ROOT
    / "docs"
    / "Data in Enterprise OMOP"
    / "Data Quality"
    / "Data Quality Results"
    / "index.md"
)
DEFAULT_LANDING = (
    REPO_ROOT
    / "docs"
    / "Data in Enterprise OMOP"
    / "Data Quality"
    / "index.md"
)
DEFAULT_KNOWN_ISSUES = (
    REPO_ROOT
    / "docs"
    / "Data in Enterprise OMOP"
    / "Data Quality"
    / "Known Issues"
    / "index.md"
)
DEFAULT_DBT_TESTS = (
    REPO_ROOT
    / "docs"
    / "Data in Enterprise OMOP"
    / "Data Quality"
    / "DBT Tests"
    / "index.md"
)

# Marker pairs
SUMMARY_START = "<!-- DQD_SUMMARY_START -->"
SUMMARY_END = "<!-- DQD_SUMMARY_END -->"
PASS_RATE_START = "<!-- DQD_PASS_RATE_START -->"
PASS_RATE_END = "<!-- DQD_PASS_RATE_END -->"
KNOWN_ISSUES_START = "<!-- KNOWN_ISSUES_START -->"
KNOWN_ISSUES_END = "<!-- KNOWN_ISSUES_END -->"
DBT_CURRENT_START = "<!-- DBT_CURRENT_START -->"
DBT_CURRENT_END = "<!-- DBT_CURRENT_END -->"
DBT_RELEASE_LOG_START = "<!-- DBT_RELEASE_LOG_START -->"
DBT_RELEASE_LOG_END = "<!-- DBT_RELEASE_LOG_END -->"


# ---------------------------------------------------------------------------
# Semver helpers
# ---------------------------------------------------------------------------

def parse_semver(tag: str) -> tuple[int, ...]:
    """Parse 'v1.2.3' or '1.2.3' into a sortable tuple."""
    clean = tag.lstrip("v")
    parts = clean.split(".")
    return tuple(int(p) for p in parts)


def sorted_releases(tags: list[str]) -> list[str]:
    """Sort release tags by semver."""
    return sorted(tags, key=parse_semver)


# ---------------------------------------------------------------------------
# DQD JSON loading
# ---------------------------------------------------------------------------

def load_dqd_results(path: Path) -> list[dict]:
    """Load DQD JSON and return the list of check results."""
    with open(path) as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("CheckResults", "checkResults", "results"):
            if key in data and isinstance(data[key], list):
                return data[key]
        if any("checkId" in str(k) for k in data):
            return list(data.values()) if all(isinstance(v, dict) for v in data.values()) else []
    raise ValueError(
        f"Cannot parse DQD JSON from {path}. Expected a list of check results "
        "or a dict with a 'CheckResults'/'checkResults'/'results' key."
    )


def normalize_status(check: dict) -> str | None:
    """Extract pass/fail status from a check result."""
    for field in ("FAILED", "failed"):
        if field in check:
            val = check[field]
            if isinstance(val, bool):
                return "FAIL" if val else "PASS"
            if isinstance(val, (int, float)):
                return "FAIL" if val == 1 else "PASS"

    for field in ("passed", "PASSED"):
        if field in check:
            val = check[field]
            if isinstance(val, bool):
                return "PASS" if val else "FAIL"
            if isinstance(val, (int, float)):
                return "PASS" if val == 1 else "FAIL"

    for field in ("status", "STATUS", "checkStatus"):
        if field in check:
            val = str(check[field]).upper().strip()
            if val in ("PASS", "PASSED"):
                return "PASS"
            if val in ("FAIL", "FAILED", "ERROR"):
                return "FAIL"

    return None


def get_field(check: dict, *candidates: str, default: str = "Unknown") -> str:
    """Get the first matching field value from a check dict."""
    for c in candidates:
        if c in check and check[c] is not None:
            return str(check[c])
    return default


def get_check_id(check: dict) -> str:
    """Build a unique identifier for a check to track across releases."""
    check_name = get_field(check, "checkName", "check_name", "checkId", default="")
    table = get_field(check, "cdmTableName", "tableName", "table_name", default="")
    field = get_field(check, "cdmFieldName", "fieldName", "field_name", default="")
    concept = get_field(check, "conceptId", "concept_id", default="")
    return f"{check_name}|{table}|{field}|{concept}"


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def compute_stats(checks: list[dict]) -> dict:
    """Compute aggregate statistics from DQD check results."""
    total = 0
    passed = 0
    failed = 0

    category_total: Counter[str] = Counter()
    category_failed: Counter[str] = Counter()
    table_total: Counter[str] = Counter()
    table_failed: Counter[str] = Counter()
    tables_seen: set[str] = set()

    for check in checks:
        status = normalize_status(check)
        if status is None:
            continue

        total += 1
        table = get_field(check, "cdmTableName", "tableName", "table_name", default="unknown")
        category = get_field(check, "category", "checkCategory", default="Unknown")

        tables_seen.add(table)
        table_total[table] += 1
        category_total[category] += 1

        if status == "PASS":
            passed += 1
        else:
            failed += 1
            table_failed[table] += 1
            category_failed[category] += 1

    if total == 0:
        raise ValueError("No valid check results found in DQD JSON.")

    pass_rate = (passed / total) * 100

    failing_tables = []
    for table in sorted(table_failed, key=lambda t: (table_total[t] - table_failed[t]) / table_total[t]):
        t_total = table_total[table]
        t_failed = table_failed[table]
        t_rate = ((t_total - t_failed) / t_total) * 100
        failing_tables.append({
            "table": table,
            "failed": t_failed,
            "total": t_total,
            "pass_rate": t_rate,
        })

    categories = {}
    for cat in sorted(category_total):
        categories[cat] = {
            "total": category_total[cat],
            "failed": category_failed.get(cat, 0),
            "fail_rate": (category_failed.get(cat, 0) / category_total[cat]) * 100,
        }

    tables_with_zero = len(tables_seen) - len(table_failed)

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
        "num_tables": len(tables_seen),
        "failing_tables": failing_tables,
        "tables_with_zero": tables_with_zero,
        "categories": categories,
    }


def extract_metadata(checks: list[dict]) -> dict[str, str]:
    """Try to extract CDM version, DQD version, vocabulary version from checks."""
    metadata: dict[str, str] = {}
    for check in checks:
        for field in ("cdmVersion", "cdm_version"):
            if field in check and check[field]:
                metadata.setdefault("cdm_version", str(check[field]))
        for field in ("dqdVersion", "dqd_version"):
            if field in check and check[field]:
                metadata.setdefault("dqd_version", str(check[field]))
        for field in ("vocabularyVersion", "vocabulary_version"):
            if field in check and check[field]:
                metadata.setdefault("vocab_version", str(check[field]))
        if len(metadata) >= 3:
            break
    return metadata


# ---------------------------------------------------------------------------
# Cross-release diff
# ---------------------------------------------------------------------------

def get_failed_check_ids(checks: list[dict]) -> set[str]:
    """Return set of check IDs that failed."""
    failed = set()
    for check in checks:
        status = normalize_status(check)
        if status == "FAIL":
            failed.add(get_check_id(check))
    return failed


def get_check_details(checks: list[dict]) -> dict[str, dict]:
    """Return dict mapping check_id -> check details for failed checks."""
    details = {}
    for check in checks:
        status = normalize_status(check)
        if status == "FAIL":
            cid = get_check_id(check)
            details[cid] = {
                "table": get_field(check, "cdmTableName", "tableName", "table_name", default="unknown"),
                "field": get_field(check, "cdmFieldName", "fieldName", "field_name", default=""),
                "category": get_field(check, "category", "checkCategory", default="Unknown"),
                "check_name": get_field(check, "checkName", "check_name", "checkId", default=""),
                "description": get_field(check, "checkDescription", "description", default=""),
            }
    return details


def compute_diff(
    prev_checks: list[dict] | None,
    curr_checks: list[dict],
) -> dict:
    """Compute diff between two releases' check results."""
    curr_failed = get_failed_check_ids(curr_checks)
    curr_details = get_check_details(curr_checks)

    if prev_checks is None:
        return {
            "new_failures": curr_failed,
            "resolved": set(),
            "persistent": set(),
            "curr_details": curr_details,
        }

    prev_failed = get_failed_check_ids(prev_checks)

    return {
        "new_failures": curr_failed - prev_failed,
        "resolved": prev_failed - curr_failed,
        "persistent": curr_failed & prev_failed,
        "curr_details": curr_details,
    }


# ---------------------------------------------------------------------------
# Markdown generation — Results page
# ---------------------------------------------------------------------------

def format_check_list(check_ids: set[str], details: dict[str, dict], indent: str = "    ") -> list[str]:
    """Format a set of check IDs into a readable markdown list.

    Groups duplicate (field, check_name) pairs within a table and shows
    a count instead of repeating each line.
    """
    lines = []
    by_table: dict[str, list[dict]] = {}
    for cid in sorted(check_ids):
        d = details.get(cid, {})
        table = d.get("table", "unknown")
        by_table.setdefault(table, []).append(d)

    for table in sorted(by_table):
        items = by_table[table]
        # Group by (field, check_name) to collapse duplicates
        grouped: dict[tuple[str, str], int] = {}
        for d in items:
            key = (d.get("field", ""), d.get("check_name", "") or d.get("description", ""))
            grouped[key] = grouped.get(key, 0) + 1

        if len(items) == 1:
            d = items[0]
            desc = d.get("check_name", "") or d.get("description", "")
            field = d.get("field", "")
            label = f"{table}.{field}" if field else table
            if desc:
                lines.append(f"{indent}- `{label}` — {desc}")
            else:
                lines.append(f"{indent}- `{label}`")
        else:
            lines.append(f"{indent}- **{table}** ({len(items)} checks)")
            for (field, desc), count in sorted(grouped.items()):
                label = field if field else "table-level"
                suffix = f" ({count} concepts)" if count > 1 else ""
                if desc:
                    lines.append(f"{indent}    - `{label}` — {desc}{suffix}")
                else:
                    lines.append(f"{indent}    - `{label}`{suffix}")
    return lines


def generate_release_section(
    release: str,
    stats: dict,
    metadata: dict[str, str],
    diff: dict,
    prev_release: str | None,
    is_latest: bool,
) -> str:
    """Generate markdown for a single release section."""
    lines: list[str] = []

    # Collapsible wrapper — latest is expanded
    prefix = "???+" if is_latest else "???"
    lines.append(f'{prefix} abstract "{release}"')
    lines.append("")

    # Metadata line
    meta_parts = []
    if "cdm_version" in metadata:
        meta_parts.append(f"CDM v{metadata['cdm_version']}")
    if "dqd_version" in metadata:
        meta_parts.append(f"DQD v{metadata['dqd_version']}")
    if "vocab_version" in metadata:
        meta_parts.append(f"Vocabulary {metadata['vocab_version']}")
    if meta_parts:
        lines.append(f"    *{' | '.join(meta_parts)}*")
        lines.append("")

    # Pass rate summary
    lines.append(
        f"    **{stats['pass_rate']:.1f}%** pass rate "
        f"— {stats['total']:,} checks, {stats['failed']:,} failures"
    )
    lines.append("")

    # Diff from previous release
    if prev_release is not None:
        all_details = diff["curr_details"]
        # Also need prev details for resolved checks
        resolved_count = len(diff["resolved"])
        new_count = len(diff["new_failures"])
        persistent_count = len(diff["persistent"])

        lines.append(f"    #### Changes from {prev_release}")
        lines.append("")

        if resolved_count > 0:
            lines.append(f"    **{resolved_count} issue{'s' if resolved_count != 1 else ''} resolved**")
            lines.append("")

        if new_count > 0:
            lines.append(f"    **{new_count} new failure{'s' if new_count != 1 else ''}**")
            lines.append("")
            lines.extend(format_check_list(diff["new_failures"], all_details, indent="    "))
            lines.append("")

        if persistent_count > 0:
            lines.append(f"    ??? warning \"Persistent failures ({persistent_count})\"")
            lines.append("")
            lines.extend(format_check_list(diff["persistent"], all_details, indent="        "))
            lines.append("")

        if resolved_count == 0 and new_count == 0 and persistent_count == 0:
            lines.append("    No changes from previous release.")
            lines.append("")

    # Failures by table
    if stats["failing_tables"]:
        lines.append("    #### Failures by Table")
        lines.append("")
        lines.append("    | Table | Failed | Total | Pass Rate |")
        lines.append("    |-------|--------|-------|-----------|")
        for t in stats["failing_tables"]:
            lines.append(f"    | {t['table']} | {t['failed']} | {t['total']} | {t['pass_rate']:.1f}% |")
        lines.append("")
        lines.append(
            f"    {stats['tables_with_zero']} additional tables passed all checks with zero failures."
        )
        lines.append("")

    return "\n".join(lines)


def generate_results_markdown(release_data: list[dict]) -> str:
    """Generate the full DQD summary markdown for all releases."""
    lines: list[str] = []

    # Most recent first for display
    for i, rd in enumerate(reversed(release_data)):
        is_latest = i == 0
        lines.append(generate_release_section(
            release=rd["release"],
            stats=rd["stats"],
            metadata=rd["metadata"],
            diff=rd["diff"],
            prev_release=rd.get("prev_release"),
            is_latest=is_latest,
        ))
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Markdown generation — Known Issues page
# ---------------------------------------------------------------------------

def _grouped_check_lines(
    cids: list[str],
    check_details: dict[str, dict],
    indent: str = "    ",
) -> list[str]:
    """Format check IDs into markdown lines, grouping by (field, check_name).

    When multiple concept IDs share the same field + check_name, they are
    collapsed into a single line with a count suffix.
    """
    grouped: dict[tuple[str, str], int] = {}
    for cid in cids:
        d = check_details.get(cid, {})
        key = (d.get("field", ""), d.get("check_name", "") or d.get("description", ""))
        grouped[key] = grouped.get(key, 0) + 1

    lines = []
    for (field, desc), count in sorted(grouped.items()):
        label = f"`{field}`" if field else "table-level"
        suffix = f" ({count} concepts)" if count > 1 else ""
        if desc:
            lines.append(f"{indent}- {label} — {desc}{suffix}")
        else:
            lines.append(f"{indent}- {label}{suffix}")
    return lines


def generate_known_issues_markdown(release_data: list[dict]) -> str:
    """Generate known issues markdown from DQD history.

    Tracks first_observed / last_observed per failing check across releases,
    then classifies as open (still failing in latest) or resolved.
    """
    if not release_data:
        return ""

    releases = [rd["release"] for rd in release_data]
    latest = releases[-1]

    # Track first_observed and last_observed for each check
    first_observed: dict[str, str] = {}
    last_observed: dict[str, str] = {}
    check_details: dict[str, dict] = {}

    for rd in release_data:
        checks = rd["checks"]
        for check in checks:
            status = normalize_status(check)
            if status == "FAIL":
                cid = get_check_id(check)
                if cid not in first_observed:
                    first_observed[cid] = rd["release"]
                last_observed[cid] = rd["release"]
                check_details[cid] = {
                    "table": get_field(check, "cdmTableName", "tableName", "table_name", default="unknown"),
                    "field": get_field(check, "cdmFieldName", "fieldName", "field_name", default=""),
                    "category": get_field(check, "category", "checkCategory", default="Unknown"),
                    "check_name": get_field(check, "checkName", "check_name", "checkId", default=""),
                    "description": get_field(check, "checkDescription", "description", default=""),
                }

    # Split into open (still failing in latest) and resolved
    open_issues: dict[str, list[str]] = {}  # table -> [check_ids]
    resolved_issues: dict[str, list[str]] = {}  # table -> [check_ids]

    for cid in first_observed:
        d = check_details[cid]
        table = d["table"]
        if last_observed[cid] == latest:
            open_issues.setdefault(table, []).append(cid)
        else:
            resolved_issues.setdefault(table, []).append(cid)

    lines: list[str] = []

    # Open Issues
    lines.append("## Open Issues")
    lines.append("")
    lines.append(f"Issues that remain unresolved in the latest release ({latest}).")
    lines.append("")

    if open_issues:
        for table in sorted(open_issues, key=lambda t: len(open_issues[t]), reverse=True):
            cids = open_issues[table]
            # Group categories
            cats: Counter[str] = Counter()
            for cid in cids:
                cats[check_details[cid]["category"]] += 1
            cat_summary = ", ".join(f"{cat} ({n})" for cat, n in sorted(cats.items()))

            # Find earliest first_observed for this table
            earliest = min(first_observed[cid] for cid in cids)

            lines.append(f'??? warning "{table} — {len(cids)} DQD failure{"s" if len(cids) != 1 else ""}"')
            lines.append("")
            lines.append(f"    **First observed**: {earliest}")
            lines.append(f"    **Latest release**: {latest}")
            lines.append(f"    **Category**: {cat_summary}")
            lines.append("")
            lines.extend(_grouped_check_lines(cids, check_details, indent="    "))
            lines.append("")
    else:
        lines.append("No open issues.")
        lines.append("")

    # Resolved Issues
    lines.append("## Resolved Issues")
    lines.append("")
    lines.append("Issues that were observed in earlier releases but have been resolved.")
    lines.append("")

    if resolved_issues:
        for table in sorted(resolved_issues, key=lambda t: len(resolved_issues[t]), reverse=True):
            cids = resolved_issues[table]
            resolved_in = max(last_observed[cid] for cid in cids)
            # Find the release AFTER last_observed (that's when it was resolved)
            resolved_idx = releases.index(resolved_in)
            if resolved_idx + 1 < len(releases):
                resolved_release = releases[resolved_idx + 1]
            else:
                resolved_release = resolved_in  # Edge case
            earliest = min(first_observed[cid] for cid in cids)

            lines.append(f'??? success "{table} — {len(cids)} issue{"s" if len(cids) != 1 else ""} resolved"')
            lines.append("")
            lines.append(f"    **First observed**: {earliest}")
            lines.append(f"    **Resolved in**: {resolved_release}")
            lines.append("")
            lines.extend(_grouped_check_lines(cids, check_details, indent="    "))
            lines.append("")
    else:
        lines.append("No resolved issues yet.")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File update helpers
# ---------------------------------------------------------------------------

def replace_between_markers(
    content: str,
    start_marker: str,
    end_marker: str,
    replacement: str,
) -> str:
    """Replace content between start and end markers, preserving the markers."""
    pattern = re.compile(
        re.escape(start_marker) + r"\n.*?\n" + re.escape(end_marker),
        re.DOTALL,
    )
    if not pattern.search(content):
        raise ValueError(f"Markers {start_marker} / {end_marker} not found in file.")

    new_content = f"{start_marker}\n\n{replacement}\n{end_marker}"
    return pattern.sub(new_content, content)


def update_pass_rate(content: str, pass_rate: float, release: str) -> str:
    """Update the pass rate between DQD_PASS_RATE markers, including release tag."""
    pattern = re.compile(
        re.escape(PASS_RATE_START) + r".*?" + re.escape(PASS_RATE_END),
        re.DOTALL,
    )
    if not pattern.search(content):
        return content

    replacement = f"{PASS_RATE_START}{pass_rate:.1f}% ({release}){PASS_RATE_END}"
    return pattern.sub(replacement, content)


# ---------------------------------------------------------------------------
# DBT artifact loading
# ---------------------------------------------------------------------------

# OMOP tables we care about (excludes staging/intermediate models)
OMOP_TABLES = {
    "care_site", "condition_era", "condition_occurrence", "death",
    "device_exposure", "drug_era", "drug_exposure", "drug_strength",
    "location", "measurement", "observation", "observation_period",
    "person", "procedure_occurrence", "provider", "visit_detail",
    "visit_occurrence",
}


def _extract_table_name(node: dict) -> str:
    """Extract OMOP table name from a manifest test node."""
    attached = node.get("attached_node", "")
    if attached:
        name = attached.rsplit(".", 1)[-1]
        if name in OMOP_TABLES:
            return name
    return "unknown"


def _format_test_display(node: dict) -> str:
    """Format a test node into the display notation used on the DBT Tests page."""
    meta = node.get("test_metadata", {})
    test_name = meta.get("name", "")
    kwargs = meta.get("kwargs", {})

    if test_name in ("not_null", "unique"):
        return test_name

    if test_name in ("relationships", "relationships_where"):
        to_ref = kwargs.get("to", "")
        target_field = kwargs.get("field", "")
        to_condition = kwargs.get("to_condition", "")

        target_table = ""
        if "ref(" in to_ref:
            target_table = to_ref.split("'")[1] if "'" in to_ref else to_ref

        if target_table == "concept":
            if to_condition:
                domain = to_condition.split("'")[1] if "'" in to_condition else ""
                if domain:
                    return f"FK → concept ({domain})"
            return "FK → concept"
        elif target_table and target_field:
            return f"FK → {target_table}.{target_field}"

    return test_name


def load_dbt_manifest_tests(path: Path) -> dict[str, dict]:
    """Load manifest.json and extract test nodes."""
    with open(path) as f:
        data = json.load(f)

    nodes = data.get("nodes", {})
    tests = {}
    for uid, node in nodes.items():
        if node.get("resource_type") != "test":
            continue
        meta = node.get("test_metadata", {})
        tests[uid] = {
            "unique_id": uid,
            "name": node.get("name", ""),
            "test_type": meta.get("name", ""),
            "namespace": meta.get("namespace", ""),
            "table": _extract_table_name(node),
            "column_name": node.get("column_name", ""),
            "test_metadata": meta,
            "display": _format_test_display(node),
            "config_enabled": node.get("config", {}).get("enabled", True),
        }
    return tests


def load_dbt_run_results(path: Path) -> dict[str, dict]:
    """Load run_results.json and return dict keyed by unique_id."""
    with open(path) as f:
        data = json.load(f)

    results = {}
    for r in data.get("results", []):
        uid = r.get("unique_id", "")
        if not uid.startswith("test."):
            continue
        results[uid] = {
            "status": r.get("status", "unknown"),
            "failures": r.get("failures", 0),
            "execution_time": r.get("execution_time", 0),
        }
    return results


def load_dbt_catalog(path: Path) -> dict[str, dict[str, dict]]:
    """Load catalog.json and return column metadata per table."""
    with open(path) as f:
        data = json.load(f)

    catalog: dict[str, dict[str, dict]] = {}
    for uid, node in data.get("nodes", {}).items():
        table_name = node.get("metadata", {}).get("name", "")
        if table_name not in OMOP_TABLES:
            continue
        columns = {}
        for col_name, col_info in node.get("columns", {}).items():
            columns[col_name.lower()] = {
                "type": col_info.get("type", ""),
                "index": col_info.get("index", 0),
                "name": col_name.lower(),
            }
        catalog[table_name] = columns
    return catalog


def merge_dbt_artifacts(
    tests: dict[str, dict],
    results: dict[str, dict],
) -> list[dict]:
    """Merge manifest tests with run results."""
    merged = []
    for uid, test in tests.items():
        r = results.get(uid, {"status": "skipped", "failures": 0, "execution_time": 0})
        merged.append({**test, **r})
    return merged


# ---------------------------------------------------------------------------
# DBT statistics and diff
# ---------------------------------------------------------------------------

def compute_dbt_stats(tests: list[dict]) -> dict:
    """Compute aggregate DBT test statistics."""
    total = len(tests)
    by_status: Counter[str] = Counter(t.get("status", "unknown") for t in tests)
    by_table: dict[str, list[dict]] = {}
    for t in tests:
        by_table.setdefault(t["table"], []).append(t)

    return {
        "total": total,
        "passed": by_status.get("pass", 0),
        "failed": by_status.get("fail", 0),
        "errored": by_status.get("error", 0),
        "skipped": by_status.get("skipped", 0),
        "num_tables": len(by_table),
        "by_table": by_table,
    }


def compute_dbt_diff(
    prev_tests: list[dict] | None,
    curr_tests: list[dict],
) -> dict:
    """Compute diff between two releases' DBT tests."""
    curr_by_id = {t["unique_id"]: t for t in curr_tests}
    curr_ids = set(curr_by_id)

    if prev_tests is None:
        return {"added": curr_tests, "removed": [], "status_changes": []}

    prev_by_id = {t["unique_id"]: t for t in prev_tests}
    prev_ids = set(prev_by_id)

    added = [curr_by_id[uid] for uid in sorted(curr_ids - prev_ids)]
    removed = [prev_by_id[uid] for uid in sorted(prev_ids - curr_ids)]

    status_changes = []
    for uid in sorted(curr_ids & prev_ids):
        prev_status = prev_by_id[uid].get("status", "")
        curr_status = curr_by_id[uid].get("status", "")
        if prev_status != curr_status:
            status_changes.append({
                **curr_by_id[uid],
                "prev_status": prev_status,
                "curr_status": curr_status,
            })

    return {"added": added, "removed": removed, "status_changes": status_changes}


# ---------------------------------------------------------------------------
# DBT markdown generation — Current test tables
# ---------------------------------------------------------------------------

_TABLE_DESCRIPTIONS: dict[str, str] = {
    "care_site": "The CARE_SITE table contains uniquely identified institutional units where healthcare delivery is practiced (offices, wards, hospitals, clinics, etc.).",
    "condition_occurrence": "Records of events suggesting the presence of a disease or medical condition — diagnoses, signs, or symptoms observed by a provider or reported by the patient.",
    "death": "Contains the clinical event for how and when a person dies. A person can have up to one record if the source system contains evidence about the death.",
    "device_exposure": "Captures a person's exposure to a foreign physical object or instrument used for diagnostic or therapeutic purposes — implantable objects, medical equipment, supplies, and procedural instruments.",
    "drug_exposure": "Records about exposure to a drug ingested or otherwise introduced into the body — prescription and over-the-counter medicines, vaccines, and large-molecule biologic therapies.",
    "location": "Represents a generic way to capture physical location or address information of persons and care sites.",
    "measurement": "Records of structured values (numerical or categorical) obtained through systematic examination or testing — laboratory tests, vital signs, quantitative pathology findings, etc.",
    "observation": "Clinical facts about a person obtained in the context of examination, questioning, or a procedure. Captures data that cannot be represented by other domains.",
    "person": "Central identity management for all persons in the database. Contains records that uniquely identify each person or patient, along with demographic information.",
    "procedure_occurrence": "Records of activities or processes ordered by, or carried out by, a healthcare provider on the patient with a diagnostic or therapeutic purpose.",
    "provider": "Uniquely identified healthcare providers — individuals providing hands-on healthcare to patients (physicians, nurses, midwives, physical therapists, etc.).",
    "visit_detail": "Details of each record in the parent visit_occurrence table — movement between units during an inpatient stay, claim lines within an insurance claim, etc.",
    "visit_occurrence": "Events where persons engage with the healthcare system for a duration of time. Defined by whether the patient comes to an institution or vice versa.",
}


def generate_dbt_current_markdown(
    tests: list[dict],
    catalog: dict[str, dict[str, dict]],
    release: str,
    run_results: dict[str, dict],
) -> str:
    """Generate the 'Current' test definition tables from catalog + manifest."""
    lines: list[str] = []
    lines.append(f"## Current ({release})")
    lines.append("")

    # Build test index: table -> column -> [display strings]
    tests_by_table: dict[str, dict[str, list[str]]] = {}
    for t in tests:
        table = t["table"]
        col = t["column_name"].lower() if t["column_name"] else ""
        if table not in OMOP_TABLES:
            continue
        tests_by_table.setdefault(table, {}).setdefault(col, [])
        display = t["display"]
        uid = t["unique_id"]
        status = run_results.get(uid, {}).get("status", t.get("status", ""))
        if status == "skipped":
            display = f"*{display}*"
        tests_by_table[table][col].append(display)

    for table_name in sorted(catalog):
        if table_name not in OMOP_TABLES:
            continue
        columns = catalog[table_name]
        table_tests = tests_by_table.get(table_name, {})
        desc = _TABLE_DESCRIPTIONS.get(table_name, "")

        lines.append(f'??? abstract "{table_name} — column-level tests"')
        lines.append("")
        if desc:
            lines.append(f"    {desc}")
            lines.append("")
        lines.append("    | Column | Type | Tests |")
        lines.append("    |--------|------|-------|")

        for col_name, col_info in sorted(columns.items(), key=lambda x: x[1].get("index", 0)):
            col_type = col_info.get("type", "")
            col_tests = table_tests.get(col_name, [])
            tests_str = ", ".join(col_tests) if col_tests else "—"
            lines.append(f"    | {col_name} | {col_type} | {tests_str} |")

        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# DBT markdown generation — Release changelog
# ---------------------------------------------------------------------------

def _format_test_list_by_table(tests: list[dict], indent: str = "    ") -> list[str]:
    """Format a list of test dicts grouped by table."""
    by_table: dict[str, list[dict]] = {}
    for t in tests:
        by_table.setdefault(t["table"], []).append(t)

    lines = []
    for table in sorted(by_table):
        items = by_table[table]
        if len(items) == 1:
            t = items[0]
            col = t.get("column_name", "")
            display = t.get("display", t.get("test_type", ""))
            label = f"{table}.{col}" if col else table
            lines.append(f"{indent}- `{label}` — {display}")
        else:
            lines.append(f"{indent}- **{table}** ({len(items)} tests)")
            for t in sorted(items, key=lambda x: x.get("column_name", "")):
                col = t.get("column_name", "")
                display = t.get("display", t.get("test_type", ""))
                label = col if col else "table-level"
                lines.append(f"{indent}    - `{label}` — {display}")
    return lines


def generate_dbt_changelog_markdown(dbt_release_data: list[dict]) -> str:
    """Generate DBT release changelog markdown."""
    lines: list[str] = []

    for i, rd in enumerate(reversed(dbt_release_data)):
        is_latest = i == 0
        release = rd["release"]
        stats = rd["stats"]
        diff = rd["diff"]
        prev_release = rd.get("prev_release")

        added_count = len(diff["added"])
        removed_count = len(diff["removed"])
        change_count = len(diff["status_changes"])

        if prev_release is None:
            subtitle = "initial test suite"
        else:
            parts = []
            if added_count:
                parts.append(f"{added_count} added")
            if removed_count:
                parts.append(f"{removed_count} removed")
            if change_count:
                parts.append(f"{change_count} status change{'s' if change_count != 1 else ''}")
            subtitle = ", ".join(parts) if parts else "no changes"

        prefix = "???+" if is_latest else "???"
        lines.append(f'{prefix} abstract "{release} — {stats["total"]} tests ({subtitle})"')
        lines.append("")
        lines.append(
            f"    {stats['total']} tests across {stats['num_tables']} tables"
            f" — {stats['passed']} pass, {stats['failed']} fail"
        )
        lines.append("")

        if prev_release is not None:
            if added_count > 0:
                lines.append("    **Added:**")
                lines.append("")
                lines.extend(_format_test_list_by_table(diff["added"], indent="    "))
                lines.append("")
            if removed_count > 0:
                lines.append("    **Removed:**")
                lines.append("")
                lines.extend(_format_test_list_by_table(diff["removed"], indent="    "))
                lines.append("")
            if change_count > 0:
                lines.append("    **Status changes:**")
                lines.append("")
                for sc in diff["status_changes"]:
                    col = sc.get("column_name", "")
                    table = sc.get("table", "")
                    label = f"{table}.{col}" if col else table
                    lines.append(
                        f"    - `{label}`: {sc['prev_status']} → {sc['curr_status']}"
                    )
                lines.append("")

        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# DBT history loading
# ---------------------------------------------------------------------------

def load_dbt_history() -> list[dict]:
    """Load all DBT release history and compute stats + diffs."""
    if not DBT_HISTORY_DIR.exists():
        return []

    release_dirs = [d for d in DBT_HISTORY_DIR.iterdir() if d.is_dir() and d.name.startswith("v")]
    if not release_dirs:
        return []

    releases = sorted_releases([d.name for d in release_dirs])

    dbt_release_data: list[dict] = []
    prev_tests: list[dict] | None = None
    prev_release: str | None = None

    for release in releases:
        release_dir = DBT_HISTORY_DIR / release
        tests_path = release_dir / "tests.json"
        results_path = release_dir / "results.json"
        catalog_path = release_dir / "catalog.json"

        if not tests_path.exists():
            print(f"Warning: skipping DBT {release}: tests.json not found", file=sys.stderr)
            continue

        try:
            with open(tests_path) as f:
                tests_data = json.load(f)
            run_results_data: dict[str, dict] = {}
            if results_path.exists():
                run_results_data = load_dbt_run_results(results_path)

            catalog_data: dict[str, dict[str, dict]] = {}
            if catalog_path.exists():
                catalog_data = load_dbt_catalog(catalog_path)

            tests = merge_dbt_artifacts(tests_data, run_results_data)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Warning: skipping DBT {release}: {e}", file=sys.stderr)
            continue

        stats = compute_dbt_stats(tests)
        diff = compute_dbt_diff(prev_tests, tests)

        dbt_release_data.append({
            "release": release,
            "tests": tests,
            "stats": stats,
            "diff": diff,
            "prev_release": prev_release,
            "catalog": catalog_data,
            "run_results": run_results_data,
        })

        prev_tests = tests
        prev_release = release

    return dbt_release_data


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_ingest(args: argparse.Namespace) -> int:
    """Ingest DQD and/or DBT artifacts into the history directory."""
    release = args.release
    dqd_src: Path | None = args.dqd
    dbt_manifest: Path | None = args.dbt_manifest
    dbt_results: Path | None = args.dbt_results
    dbt_catalog: Path | None = args.dbt_catalog

    if not dqd_src and not dbt_manifest:
        print("Error: provide at least --dqd or --dbt-manifest", file=sys.stderr)
        return 1

    # --- DQD ingest ---
    if dqd_src:
        if not dqd_src.exists():
            print(f"Error: DQD JSON file not found: {dqd_src}", file=sys.stderr)
            return 1
        try:
            checks = load_dqd_results(dqd_src)
            stats = compute_stats(checks)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error loading DQD JSON: {e}", file=sys.stderr)
            return 1

        DQD_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
        dest = DQD_HISTORY_DIR / f"{release}.json"
        shutil.copy2(dqd_src, dest)
        print(f"Ingested DQD {dqd_src} -> {dest}")
        print(f"  {stats['total']:,} checks, {stats['pass_rate']:.1f}% pass rate")

    # --- DBT ingest ---
    if dbt_manifest:
        if not dbt_manifest.exists():
            print(f"Error: DBT manifest not found: {dbt_manifest}", file=sys.stderr)
            return 1

        # Extract test nodes from manifest
        tests = load_dbt_manifest_tests(dbt_manifest)
        if not tests:
            print("Error: no test nodes found in manifest", file=sys.stderr)
            return 1

        release_dir = DBT_HISTORY_DIR / release
        release_dir.mkdir(parents=True, exist_ok=True)

        # Save stripped tests.json
        tests_dest = release_dir / "tests.json"
        with open(tests_dest, "w") as f:
            json.dump(tests, f, indent=2)
        print(f"Ingested DBT manifest ({len(tests)} test nodes) -> {tests_dest}")

        # Copy run_results if provided
        if dbt_results:
            if not dbt_results.exists():
                print(f"Error: DBT run_results not found: {dbt_results}", file=sys.stderr)
                return 1
            results_dest = release_dir / "results.json"
            shutil.copy2(dbt_results, results_dest)
            run_res = load_dbt_run_results(dbt_results)
            print(f"Ingested DBT run_results ({len(run_res)} test results) -> {results_dest}")

        # Copy catalog if provided
        if dbt_catalog:
            if not dbt_catalog.exists():
                print(f"Error: DBT catalog not found: {dbt_catalog}", file=sys.stderr)
                return 1
            catalog_dest = release_dir / "catalog.json"
            shutil.copy2(dbt_catalog, catalog_dest)
            cat = load_dbt_catalog(dbt_catalog)
            print(f"Ingested DBT catalog ({len(cat)} tables) -> {catalog_dest}")

        # Print summary
        merged = merge_dbt_artifacts(tests, run_res if dbt_results else {})
        dbt_stats = compute_dbt_stats(merged)
        print(
            f"  {dbt_stats['total']} tests across {dbt_stats['num_tables']} tables"
            f" — {dbt_stats['passed']} pass, {dbt_stats['failed']} fail"
        )

    return 0


def cmd_generate(args: argparse.Namespace) -> int:
    """Generate markdown pages from DQD history."""
    if not DQD_HISTORY_DIR.exists():
        print(f"Error: History directory not found: {DQD_HISTORY_DIR}", file=sys.stderr)
        print("Run 'ingest' first to add DQD results.", file=sys.stderr)
        return 1

    # Find all JSON files
    json_files = list(DQD_HISTORY_DIR.glob("v*.json"))
    if not json_files:
        print(f"Error: No release JSON files found in {DQD_HISTORY_DIR}", file=sys.stderr)
        return 1

    # Sort by semver
    releases = sorted_releases([f.stem for f in json_files])

    # Load all releases and compute stats + diffs
    release_data: list[dict] = []
    prev_checks: list[dict] | None = None
    prev_release: str | None = None

    for release in releases:
        path = DQD_HISTORY_DIR / f"{release}.json"
        try:
            checks = load_dqd_results(path)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Warning: skipping {release}: {e}", file=sys.stderr)
            continue

        try:
            stats = compute_stats(checks)
        except ValueError as e:
            print(f"Warning: skipping {release}: {e}", file=sys.stderr)
            continue

        metadata = extract_metadata(checks)
        diff = compute_diff(prev_checks, checks)

        release_data.append({
            "release": release,
            "checks": checks,
            "stats": stats,
            "metadata": metadata,
            "diff": diff,
            "prev_release": prev_release,
        })

        prev_checks = checks
        prev_release = release

    if not release_data:
        print("Error: No valid releases found.", file=sys.stderr)
        return 1

    latest = release_data[-1]

    # Generate Results page markdown
    results_md = generate_results_markdown(release_data)

    # Generate Known Issues markdown
    known_issues_md = generate_known_issues_markdown(release_data)

    # --- Load DBT history ---
    dbt_release_data = load_dbt_history()
    dbt_current_md = ""
    dbt_changelog_md = ""

    if dbt_release_data:
        dbt_latest = dbt_release_data[-1]
        dbt_current_md = generate_dbt_current_markdown(
            dbt_latest["tests"],
            dbt_latest["catalog"],
            dbt_latest["release"],
            dbt_latest["run_results"],
        )
        dbt_changelog_md = generate_dbt_changelog_markdown(dbt_release_data)

    if args.dry_run:
        print("=" * 60)
        print("DATA QUALITY RESULTS (between DQD_SUMMARY markers)")
        print("=" * 60)
        print(results_md)
        print()
        print("=" * 60)
        print("KNOWN ISSUES (between KNOWN_ISSUES markers)")
        print("=" * 60)
        print(known_issues_md)
        print()
        print(f"Pass rate: {latest['stats']['pass_rate']:.1f}% ({latest['release']})")
        print(f"DQD releases processed: {', '.join(r['release'] for r in release_data)}")

        if dbt_release_data:
            print()
            print("=" * 60)
            print("DBT CURRENT TESTS (between DBT_CURRENT markers)")
            print("=" * 60)
            print(dbt_current_md)
            print()
            print("=" * 60)
            print("DBT CHANGELOG (between DBT_RELEASE_LOG markers)")
            print("=" * 60)
            print(dbt_changelog_md)
            print(
                f"DBT releases processed: "
                f"{', '.join(r['release'] for r in dbt_release_data)}"
            )
        else:
            print("\nNo DBT history found — skipping DBT pages.")

        return 0

    # Update Results page
    results_page = args.results_page
    if not results_page.exists():
        print(f"Error: Results page not found: {results_page}", file=sys.stderr)
        return 1

    results_content = results_page.read_text()
    try:
        results_content = replace_between_markers(
            results_content, SUMMARY_START, SUMMARY_END, results_md
        )
    except ValueError as e:
        print(f"Error updating results page: {e}", file=sys.stderr)
        return 1
    results_page.write_text(results_content)
    print(f"Updated: {results_page}")

    # Update Known Issues page
    known_issues_page = args.known_issues_page
    if known_issues_page.exists():
        ki_content = known_issues_page.read_text()
        try:
            ki_content = replace_between_markers(
                ki_content, KNOWN_ISSUES_START, KNOWN_ISSUES_END, known_issues_md
            )
            known_issues_page.write_text(ki_content)
            print(f"Updated: {known_issues_page}")
        except ValueError:
            print(
                f"Warning: {KNOWN_ISSUES_START} / {KNOWN_ISSUES_END} markers not found "
                f"in {known_issues_page}. Skipping Known Issues update.",
                file=sys.stderr,
            )
    else:
        print(f"Known Issues page not found: {known_issues_page} (skipped)")

    # Update landing page pass rate
    landing_page = args.landing_page
    if landing_page.exists():
        landing_content = landing_page.read_text()
        updated = update_pass_rate(
            landing_content,
            latest["stats"]["pass_rate"],
            latest["release"],
        )
        if updated != landing_content:
            landing_page.write_text(updated)
            print(f"Updated pass rate: {landing_page}")
        else:
            print(f"No pass rate markers found in: {landing_page} (skipped)")
    else:
        print(f"Landing page not found: {landing_page} (skipped)")

    # Update DBT Tests page
    if dbt_release_data:
        dbt_page = args.dbt_tests_page
        if dbt_page.exists():
            dbt_content = dbt_page.read_text()
            updated_dbt = False

            # Update current test tables
            try:
                dbt_content = replace_between_markers(
                    dbt_content, DBT_CURRENT_START, DBT_CURRENT_END, dbt_current_md
                )
                updated_dbt = True
            except ValueError:
                print(
                    f"Warning: {DBT_CURRENT_START} / {DBT_CURRENT_END} markers not found "
                    f"in {dbt_page}. Skipping current section.",
                    file=sys.stderr,
                )

            # Update release changelog
            try:
                dbt_content = replace_between_markers(
                    dbt_content, DBT_RELEASE_LOG_START, DBT_RELEASE_LOG_END, dbt_changelog_md
                )
                updated_dbt = True
            except ValueError:
                print(
                    f"Warning: {DBT_RELEASE_LOG_START} / {DBT_RELEASE_LOG_END} markers "
                    f"not found in {dbt_page}. Skipping changelog.",
                    file=sys.stderr,
                )

            if updated_dbt:
                dbt_page.write_text(dbt_content)
                print(f"Updated: {dbt_page}")
        else:
            print(f"DBT Tests page not found: {dbt_page} (skipped)")
    else:
        print("No DBT history found — skipping DBT Tests page.")

    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Manage release-tagged DQD results and generate Data Quality pages.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ingest
    ingest_parser = subparsers.add_parser(
        "ingest",
        help="Ingest DQD and/or DBT artifacts into the release history",
    )
    ingest_parser.add_argument(
        "--release",
        required=True,
        help="Release tag (e.g., v1.0.0)",
    )
    ingest_parser.add_argument(
        "--dqd",
        type=Path,
        default=None,
        help="Path to OHDSI DQD JSON results file",
    )
    ingest_parser.add_argument(
        "--dbt-manifest",
        type=Path,
        default=None,
        help="Path to DBT manifest.json (test nodes will be extracted)",
    )
    ingest_parser.add_argument(
        "--dbt-results",
        type=Path,
        default=None,
        help="Path to DBT run_results.json",
    )
    ingest_parser.add_argument(
        "--dbt-catalog",
        type=Path,
        default=None,
        help="Path to DBT catalog.json",
    )

    # generate
    gen_parser = subparsers.add_parser(
        "generate",
        help="Regenerate all markdown pages from DQD history",
    )
    gen_parser.add_argument(
        "--results-page",
        type=Path,
        default=DEFAULT_RESULTS,
        help=f"Path to Results markdown (default: {DEFAULT_RESULTS})",
    )
    gen_parser.add_argument(
        "--landing-page",
        type=Path,
        default=DEFAULT_LANDING,
        help=f"Path to landing page markdown (default: {DEFAULT_LANDING})",
    )
    gen_parser.add_argument(
        "--known-issues-page",
        type=Path,
        default=DEFAULT_KNOWN_ISSUES,
        help=f"Path to Known Issues markdown (default: {DEFAULT_KNOWN_ISSUES})",
    )
    gen_parser.add_argument(
        "--dbt-tests-page",
        type=Path,
        default=DEFAULT_DBT_TESTS,
        help=f"Path to DBT Tests markdown (default: {DEFAULT_DBT_TESTS})",
    )
    gen_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated markdown to stdout without writing files",
    )

    args = parser.parse_args()

    if args.command == "ingest":
        return cmd_ingest(args)
    elif args.command == "generate":
        return cmd_generate(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
