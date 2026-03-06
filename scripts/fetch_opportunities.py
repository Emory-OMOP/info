#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
"""Fetch funding opportunities and OMOP-related news into blog drafts.

Sources:
  - NIH Guide: NIH policy notices and funding announcements (RSS)
  - Grants.gov: federal funding opportunities matching OMOP/RWE keywords (API)
  - NIH Reporter: recently funded NIH projects in our space (API)
  - PCORI: patient-centered outcomes research funding (web scrape)
  - OHDSI Forums: community topics, network studies, tools (RSS)
  - PubMed: recent OMOP/RWE methods publications (eutils API)

Usage:
    # Fetch new opportunities into scripts/blog_drafts/
    uv run scripts/fetch_opportunities.py fetch [--dry-run]

    # Publish reviewed drafts to docs/blog/posts/
    uv run scripts/fetch_opportunities.py publish [--all | file1.md file2.md ...]

    # List current drafts
    uv run scripts/fetch_opportunities.py list
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import httpx

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = REPO_ROOT / "scripts" / "blog_drafts"
POSTS_DIR = REPO_ROOT / "docs" / "blog" / "posts"
STATE_FILE = Path(__file__).resolve().parent / "feed_state.json"

# ---------------------------------------------------------------------------
# Keywords and relevance
# ---------------------------------------------------------------------------

KEYWORDS = [
    "OMOP",
    "common data model",
    "real-world evidence",
    "real world evidence",
    "observational health",
    "OHDSI",
    "electronic health record",
    "clinical data network",
    "data standardization",
    "claims data",
    "observational study",
    "pharmacoepidemiology",
    "patient-centered outcomes",
    "comparative effectiveness",
    "health data",
    "clinical informatics",
    "biomedical informatics",
    "data harmonization",
    "federated data",
    "distributed research network",
]


def _matches_keywords(text: str) -> list[str]:
    """Return which keywords match in the given text (case-insensitive)."""
    lower = text.lower()
    return [kw for kw in KEYWORDS if kw.lower() in lower]


def _slug(title: str) -> str:
    """Generate a filename-safe slug from a title."""
    clean = re.sub(r"[^\w\s-]", "", title.lower())
    return re.sub(r"[\s_]+", "-", clean).strip("-")[:80]


def _post_id(source: str, url: str, title: str) -> str:
    """Generate a stable dedup ID from source + URL."""
    key = f"{source}:{url or title}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def _strip_html(text: str) -> str:
    """Remove HTML tags from a string."""
    return re.sub(r"<[^>]+>", "", text).strip()


# ---------------------------------------------------------------------------
# State management (deduplication)
# ---------------------------------------------------------------------------


def load_state() -> dict:
    """Load the seen-posts state file."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"seen": {}}


def save_state(state: dict) -> None:
    """Save the seen-posts state file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------------------
# Source: NIH Guide (RSS)
# ---------------------------------------------------------------------------

NIH_GUIDE_RSS = "https://grants.nih.gov/grants/guide/newsfeed/fundingopps.xml"


def fetch_nih_guide(client: httpx.Client) -> list[dict]:
    """Fetch NIH Guide funding opportunity announcements via RSS."""
    items = []
    try:
        resp = client.get(NIH_GUIDE_RSS, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"  Warning: NIH Guide fetch failed: {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(resp.text)
    except ET.ParseError as e:
        print(f"  Warning: NIH Guide XML parse failed: {e}", file=sys.stderr)
        return []

    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        description = _strip_html(item.findtext("description") or "")
        pub_date = (item.findtext("pubDate") or "").strip()

        search_text = f"{title} {description}"
        matched = _matches_keywords(search_text)
        if not matched:
            continue

        items.append({
            "source": "NIH Guide",
            "category": "Funding",
            "title": title,
            "url": link,
            "description": description,
            "date": pub_date,
            "keywords_matched": matched,
            "tags": ["nih", "funding"],
        })

    return items


# ---------------------------------------------------------------------------
# Source: OHDSI Forums (RSS)
# ---------------------------------------------------------------------------

OHDSI_RSS = "https://forums.ohdsi.org/latest.rss"


def fetch_ohdsi_forum(client: httpx.Client) -> list[dict]:
    """Fetch latest OHDSI forum topics via RSS."""
    items = []
    try:
        resp = client.get(OHDSI_RSS, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"  Warning: OHDSI forum fetch failed: {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(resp.text)
    except ET.ParseError as e:
        print(f"  Warning: OHDSI RSS parse failed: {e}", file=sys.stderr)
        return []

    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        description = _strip_html(item.findtext("description") or "")
        pub_date = (item.findtext("pubDate") or "").strip()

        # Filter OHDSI to relevant topics only (skip meeting logistics, admin, etc.)
        search_text = f"{title} {description}"
        matched = _matches_keywords(search_text)

        # Skip generic admin/meeting topics unless they match specific keywords
        skip_patterns = [
            r"^undeliverable",
            r"^reminder",
            r"^deadline",
            r"community call\s*\(",
            r"monthly meeting$",
            r"^cancellation",
        ]
        title_lower = title.lower()
        if any(re.search(p, title_lower) for p in skip_patterns):
            continue

        # Require at least one keyword match for OHDSI topics too
        if not matched:
            continue

        items.append({
            "source": "OHDSI Forums",
            "category": "OHDSI",
            "title": title,
            "url": link,
            "description": description[:500],
            "date": pub_date,
            "keywords_matched": matched,
            "tags": ["ohdsi", "community"],
        })

    return items


# ---------------------------------------------------------------------------
# Source: Grants.gov (API)
# ---------------------------------------------------------------------------

GRANTS_GOV_API = "https://api.grants.gov/v1/api/search2"

# Search terms to query grants.gov — each generates a separate API call.
# The API searches full opportunity text, so results are pre-filtered for relevance.
# We trust the API results for health-related agencies rather than re-filtering titles.
GRANTS_GOV_QUERIES = [
    '"OMOP" OR "common data model"',
    '"real world evidence" OR "real-world evidence"',
    '"observational health" OR "OHDSI"',
    '"electronic health record" AND "data harmonization"',
    '"pharmacoepidemiology" OR "comparative effectiveness research"',
]

# Only include grants from health/science agencies (by agencyCode prefix)
GRANTS_GOV_AGENCY_PREFIXES = (
    "HHS",
    "VA",
    "NSF",
    "DOD",
)


def fetch_grants_gov(client: httpx.Client) -> list[dict]:
    """Fetch relevant funding opportunities from grants.gov.

    The API searches full opportunity text by our keywords, so results are
    already relevant. We filter to health-related agencies and trust the
    API's keyword matching rather than re-checking titles.
    """
    items = []
    seen_ids: set[str] = set()

    for query in GRANTS_GOV_QUERIES:
        try:
            resp = client.post(
                GRANTS_GOV_API,
                json={
                    "keyword": query,
                    "oppStatuses": "forecasted|posted",
                    "rows": 25,
                    "sortBy": "openDate|desc",
                },
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
        except (httpx.HTTPError, json.JSONDecodeError) as e:
            print(f"  Warning: grants.gov query '{query}' failed: {e}", file=sys.stderr)
            continue

        # Results are nested under data.oppHits
        hits = data.get("data", {}).get("oppHits", data.get("oppHits", []))
        if not hits:
            continue

        for opp in hits:
            opp_id = str(opp.get("id", ""))
            if not opp_id or opp_id in seen_ids:
                continue
            seen_ids.add(opp_id)

            title = opp.get("title", "")
            number = opp.get("number", "")
            agency_code = opp.get("agencyCode", "")
            agency = opp.get("agency", "")
            open_date = opp.get("openDate", "")
            close_date = opp.get("closeDate", "")
            opp_status = opp.get("oppStatus", "")
            url = f"https://www.grants.gov/search-results-detail/{opp_id}"

            # Filter to health/science agencies by code prefix
            if not any(agency_code.startswith(p) for p in GRANTS_GOV_AGENCY_PREFIXES):
                continue

            # Check for keyword match; if none, tag with the API query term
            matched = _matches_keywords(f"{title} {agency} {number}")
            if not matched:
                matched = [query]  # trust the API's keyword search

            summary_parts = []
            if close_date:
                summary_parts.append(f"**Closes**: {close_date}")
            if agency:
                summary_parts.append(f"**Agency**: {agency}")
            if number:
                summary_parts.append(f"**Number**: {number}")
            if opp_status:
                summary_parts.append(f"**Status**: {opp_status}")
            summary = "\n".join(summary_parts)

            items.append({
                "source": "Grants.gov",
                "category": "Funding",
                "title": title,
                "url": url,
                "description": summary,
                "date": open_date,
                "keywords_matched": matched,
                "tags": ["grants-gov", "funding", "federal"],
            })

    return items


# ---------------------------------------------------------------------------
# Source: NIH Reporter (API) — active funded projects
# ---------------------------------------------------------------------------

NIH_REPORTER_API = "https://api.reporter.nih.gov/v2/projects/search"

NIH_REPORTER_QUERIES = [
    "OMOP common data model",
    "real world evidence observational",
    "clinical data harmonization standardization",
]


def fetch_nih_reporter(client: httpx.Client) -> list[dict]:
    """Fetch recently funded NIH projects matching OMOP/RWE keywords."""
    items = []
    seen_ids: set[str] = set()
    current_fy = datetime.now(timezone.utc).year

    for query in NIH_REPORTER_QUERIES:
        try:
            resp = client.post(
                NIH_REPORTER_API,
                json={
                    "criteria": {
                        "advanced_text_search": {
                            "operator": "and",
                            "search_field": "projecttitle,terms",
                            "search_text": query,
                        },
                        "fiscal_years": [current_fy, current_fy - 1],
                        "include_active_projects": True,
                        "newly_added_projects_only": False,
                        "exclude_subprojects": True,
                    },
                    "offset": 0,
                    "limit": 20,
                    "sort_field": "award_notice_date",
                    "sort_order": "desc",
                },
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
        except (httpx.HTTPError, json.JSONDecodeError) as e:
            print(f"  Warning: NIH Reporter query '{query}' failed: {e}", file=sys.stderr)
            continue

        for proj in data.get("results", []):
            # Deduplicate by core project number (strips year/suffix)
            project_num = proj.get("project_num", "")
            core_num = re.sub(r"-\d+[A-Z]?\d*$", "", project_num) if project_num else ""
            dedup_key = core_num or str(proj.get("appl_id", ""))
            if not dedup_key or dedup_key in seen_ids:
                continue
            seen_ids.add(dedup_key)

            title = (proj.get("project_title") or "").strip()
            appl_id = str(proj.get("appl_id", ""))
            org = proj.get("organization", {}).get("org_name", "")
            pis = proj.get("principal_investigators", [])
            pi_name = pis[0].get("full_name", "") if pis else ""
            award_date = proj.get("award_notice_date", "")
            abstract = (proj.get("abstract_text") or "")[:500]
            url = f"https://reporter.nih.gov/project-details/{appl_id}"

            matched = _matches_keywords(f"{title} {abstract}")
            if not matched:
                continue

            summary_parts = []
            if pi_name:
                summary_parts.append(f"**PI**: {pi_name}")
            if org:
                summary_parts.append(f"**Organization**: {org}")
            if project_num:
                summary_parts.append(f"**Project**: {project_num}")
            summary_parts.append("")
            summary_parts.append(_strip_html(abstract))
            summary = "\n".join(summary_parts)

            items.append({
                "source": "NIH Reporter",
                "category": "Funding",
                "title": f"Funded: {title}",
                "url": url,
                "description": summary,
                "date": award_date,
                "keywords_matched": matched,
                "tags": ["nih", "funded-project"],
            })

    return items


# ---------------------------------------------------------------------------
# Source: PCORI (web scrape) — patient-centered outcomes research funding
# ---------------------------------------------------------------------------

PCORI_FUNDING_URL = "https://www.pcori.org/funding-opportunities"


def fetch_pcori(client: httpx.Client) -> list[dict]:
    """Fetch open and upcoming PCORI funding opportunities.

    Parses the PCORI funding page HTML. Structure per opportunity:
      <span class="funding-row__status open">Open</span>
      <a class="funding-row__link" href="/funding-opportunities/announcement/...">
        <span>Title</span>
      </a>
      ... followed by <td> cells with LOI and application dates
    """
    items = []
    try:
        resp = client.get(PCORI_FUNDING_URL, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"  Warning: PCORI fetch failed: {e}", file=sys.stderr)
        return []

    html = resp.text

    # Each table row (<tr>) contains an <article> plus date <td> cells.
    # Split by <tr> to keep articles and their dates together.
    tr_pattern = re.compile(r"<tr>(.*?)</tr>", re.DOTALL)
    table_rows = tr_pattern.findall(html)

    for table_row in table_rows:
        # Only process rows containing funding articles
        if "funding-row" not in table_row:
            continue

        # Extract status
        status_match = re.search(
            r'funding-row__status\s+(\w+)"[^>]*>([^<]+)<', table_row
        )
        if not status_match:
            continue
        status_class = status_match.group(1).lower()
        status_text = status_match.group(2).strip()

        # Only include open, upcoming, and receiving-invited
        if status_class not in ("open", "upcoming", "receiving"):
            continue

        # Extract title and link
        link_match = re.search(
            r'funding-row__link"\s+href="([^"]+)"[^>]*>\s*<span>(.+?)</span>',
            table_row,
            re.DOTALL,
        )
        if not link_match:
            continue

        path = link_match.group(1)
        title = _strip_html(link_match.group(2)).strip()
        url = f"https://www.pcori.org{path}"

        if not title:
            continue

        # Extract dates from <td> cells in the same table row
        date_pattern = re.compile(r"(\w+ \d{1,2}, \d{4})")
        dates_found = date_pattern.findall(table_row)

        summary_parts = [f"**Status**: {status_text}"]
        post_date = ""
        if len(dates_found) >= 1:
            summary_parts.append(f"**LOI Deadline**: {dates_found[0]}")
            post_date = dates_found[0]
        if len(dates_found) >= 2:
            summary_parts.append(f"**Application Deadline**: {dates_found[1]}")

        # Extract funding type from row
        type_match = re.search(
            r"<strong>Funding Type:</strong>\s*(.+?)\s*<", table_row
        )
        if type_match:
            summary_parts.append(f"**Type**: {type_match.group(1).strip()}")

        # All PCORI opportunities are relevant — they fund CER/RWE research
        matched = _matches_keywords(title)
        if not matched:
            matched = ["patient-centered outcomes", "comparative effectiveness"]

        summary = "\n".join(summary_parts)

        items.append({
            "source": "PCORI",
            "category": "Funding",
            "title": title,
            "url": url,
            "description": summary,
            "date": post_date,
            "keywords_matched": matched,
            "tags": ["pcori", "funding", "cer"],
        })

    return items


# ---------------------------------------------------------------------------
# Source: PubMed (eutils API) — RWE/methods publications
# ---------------------------------------------------------------------------

PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

PUBMED_QUERY = (
    '("OMOP"[tiab] OR "common data model"[tiab] OR "OHDSI"[tiab] '
    'OR "real-world evidence"[tiab] OR "observational health"[tiab]) '
    "AND hasabstract[text]"
)


def fetch_pubmed(client: httpx.Client) -> list[dict]:
    """Fetch recent PubMed publications on OMOP/RWE methods."""
    items = []

    # Step 1: search for recent article IDs
    try:
        resp = client.get(
            PUBMED_ESEARCH,
            params={
                "db": "pubmed",
                "term": PUBMED_QUERY,
                "retmax": 15,
                "sort": "date",
                "retmode": "json",
                "datetype": "edat",
                "reldate": 30,  # last 30 days
            },
            timeout=30,
        )
        resp.raise_for_status()
        search_data = resp.json()
    except (httpx.HTTPError, json.JSONDecodeError) as e:
        print(f"  Warning: PubMed search failed: {e}", file=sys.stderr)
        return []

    id_list = search_data.get("esearchresult", {}).get("idlist", [])
    if not id_list:
        return []

    # Step 2: fetch summaries for those IDs
    try:
        resp = client.get(
            PUBMED_ESUMMARY,
            params={
                "db": "pubmed",
                "id": ",".join(id_list),
                "retmode": "json",
            },
            timeout=30,
        )
        resp.raise_for_status()
        summary_data = resp.json()
    except (httpx.HTTPError, json.JSONDecodeError) as e:
        print(f"  Warning: PubMed summary fetch failed: {e}", file=sys.stderr)
        return []

    results = summary_data.get("result", {})
    for pmid in id_list:
        article = results.get(pmid)
        if not article:
            continue

        title = _strip_html(article.get("title", "")).rstrip(".")
        pub_date = article.get("pubdate", "")
        source_journal = article.get("source", "")
        authors = article.get("authors", [])
        first_author = authors[0].get("name", "") if authors else ""
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

        matched = _matches_keywords(title)
        if not matched:
            continue

        summary_parts = []
        if first_author:
            author_str = f"{first_author} et al." if len(authors) > 1 else first_author
            summary_parts.append(f"**Authors**: {author_str}")
        if source_journal:
            summary_parts.append(f"**Journal**: {source_journal}")
        summary = "\n".join(summary_parts)

        items.append({
            "source": "PubMed",
            "category": "Real-World Evidence",
            "title": title,
            "url": url,
            "description": summary,
            "date": pub_date,
            "keywords_matched": matched,
            "tags": ["pubmed", "research", "methods"],
        })

    return items


# ---------------------------------------------------------------------------
# Draft generation
# ---------------------------------------------------------------------------

SOURCE_FETCHERS = {
    "nih-guide": ("NIH Guide", fetch_nih_guide),
    "ohdsi": ("OHDSI Forums", fetch_ohdsi_forum),
    "grants-gov": ("Grants.gov", fetch_grants_gov),
    "nih-reporter": ("NIH Reporter", fetch_nih_reporter),
    "pcori": ("PCORI", fetch_pcori),
    "pubmed": ("PubMed", fetch_pubmed),
}


def _parse_rss_date(date_str: str) -> str:
    """Parse an RSS date string into YYYY-MM-DD."""
    if not date_str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%B %d, %Y",
        "%b %d, %Y",
        "%m/%d/%Y",
        "%Y-%m-%d",
        "%Y %b %d",
        "%Y %b",
    ):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def generate_draft(item: dict) -> str:
    """Generate a markdown blog draft from a fetched item."""
    date = _parse_rss_date(item.get("date", ""))
    tags_yaml = "\n".join(f"  - {t}" for t in item.get("tags", []))
    matched = item.get("keywords_matched", [])
    matched_str = ", ".join(matched[:5]) if matched else "general relevance"

    return f"""---
date: {date}
draft: true
categories:
  - {item['category']}
tags:
{tags_yaml}
---

# {item['title']}

**Source**: [{item['source']}]({item['url']})
**Matched keywords**: {matched_str}

{item['description']}

<!-- more -->

[:octicons-link-external-24: Read full announcement]({item['url']}){{.md-button}}
"""


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def cmd_fetch(args: argparse.Namespace) -> int:
    """Fetch opportunities from all sources."""
    sources = args.source or list(SOURCE_FETCHERS.keys())
    state = load_state()
    seen = state.get("seen", {})

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)

    new_count = 0
    skip_count = 0

    with httpx.Client(
        headers={"User-Agent": "EmoryOMOP-FeedFetcher/1.0"},
        follow_redirects=True,
    ) as client:
        for source_key in sources:
            if source_key not in SOURCE_FETCHERS:
                print(f"Unknown source: {source_key}", file=sys.stderr)
                continue

            label, fetcher = SOURCE_FETCHERS[source_key]
            print(f"Fetching from {label}...")
            items = fetcher(client)
            print(f"  Found {len(items)} relevant items")

            for item in items:
                pid = _post_id(item["source"], item["url"], item["title"])

                if pid in seen:
                    skip_count += 1
                    continue

                date = _parse_rss_date(item.get("date", ""))
                slug = _slug(item["title"])
                filename = f"{date}-{slug}.md"
                draft_path = DRAFTS_DIR / filename

                if args.dry_run:
                    print(f"  [dry-run] Would create: {filename}")
                    print(f"    Title: {item['title']}")
                    print(f"    Keywords: {', '.join(item.get('keywords_matched', []))}")
                else:
                    content = generate_draft(item)
                    draft_path.write_text(content)
                    seen[pid] = {
                        "title": item["title"],
                        "source": item["source"],
                        "date": date,
                        "file": filename,
                    }
                    print(f"  Created: {filename}")

                new_count += 1

    if not args.dry_run:
        state["seen"] = seen
        state["last_fetch"] = datetime.now(timezone.utc).isoformat()
        save_state(state)

    print(f"\nDone: {new_count} new, {skip_count} already seen")
    return 0


def _extract_deadlines(content: str) -> dict[str, str]:
    """Extract deadline dates from post content into frontmatter fields."""
    deadlines: dict[str, str] = {}

    # Match patterns like "LOI Deadline: April 1, 2026" or "Closes: 03/06/2026"
    patterns = [
        (r"LOI\s+Deadline[:\s]*(\w+\s+\d{1,2},?\s+\d{4})", "deadline_loi"),
        (r"Application\s+Deadline[:\s]*(\w+\s+\d{1,2},?\s+\d{4})", "deadline_app"),
        (r"Closes[:\s]*(\d{2}/\d{2}/\d{4})", "deadline_close"),
        (r"Closes[:\s]*(\w+\s+\d{1,2},?\s+\d{4})", "deadline_close"),
    ]

    for pattern, key in patterns:
        m = re.search(pattern, content, re.IGNORECASE)
        if m and key not in deadlines:
            raw = m.group(1)
            # Try to parse into YYYY-MM-DD
            for fmt in ("%B %d, %Y", "%B %d %Y", "%m/%d/%Y"):
                try:
                    dt = datetime.strptime(raw.replace(",", "").strip(), fmt.replace(",", ""))
                    deadlines[key] = dt.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    continue
            else:
                deadlines[key] = raw  # Keep raw if parsing fails

    return deadlines


def _inject_frontmatter_fields(content: str, fields: dict[str, str]) -> str:
    """Add fields to YAML frontmatter block."""
    if not fields:
        return content

    # Find end of frontmatter
    m = re.match(r"(---\n)(.*?)(\n---)", content, re.DOTALL)
    if not m:
        return content

    fm_block = m.group(2)

    # Only add fields not already present
    additions = []
    for key, val in fields.items():
        if key not in fm_block:
            additions.append(f"{key}: {val}")

    if not additions:
        return content

    new_fm = fm_block + "\n" + "\n".join(additions)
    return m.group(1) + new_fm + m.group(3) + content[m.end():]


def cmd_publish(args: argparse.Namespace) -> int:
    """Move drafts to posts directory with deadline extraction."""
    if not DRAFTS_DIR.exists():
        print("No drafts directory found.", file=sys.stderr)
        return 1

    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        files = sorted(DRAFTS_DIR.glob("*.md"))
    elif args.files:
        files = [DRAFTS_DIR / f for f in args.files]
    else:
        print("Specify --all or specific filenames to publish.", file=sys.stderr)
        return 1

    published = 0
    for src in files:
        if not src.exists():
            print(f"  Not found: {src.name}", file=sys.stderr)
            continue

        content = src.read_text()

        # Strip draft: true
        content = re.sub(r"^draft:\s*true\n", "", content, flags=re.MULTILINE)

        # Extract deadline dates from content → frontmatter
        deadlines = _extract_deadlines(content)
        if deadlines:
            content = _inject_frontmatter_fields(content, deadlines)
            print(f"  Deadlines: {deadlines}")

        dest = POSTS_DIR / src.name
        dest.write_text(content)
        src.unlink()
        print(f"  Published: {src.name}")
        published += 1

    if published:
        print(f"\n{published} draft(s) published to posts/")
        # Regenerate blog index
        index_script = Path(__file__).resolve().parent / "update_blog_index.py"
        if index_script.exists():
            print("\nRegenerating blog index...")
            import subprocess
            subprocess.run([sys.executable, str(index_script)], check=True)
    else:
        print("\nNo drafts published.")

    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """List current drafts with category, date, and source."""
    if not DRAFTS_DIR.exists():
        print("No drafts directory.")
        return 0

    drafts = sorted(DRAFTS_DIR.glob("*.md"))
    if not drafts:
        print("No drafts pending.")
        return 0

    print(f"{len(drafts)} draft(s):\n")
    for d in drafts:
        content = d.read_text()
        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        title = title_match.group(1) if title_match else d.stem

        # Extract category
        cat_match = re.search(r"categories:\n\s+-\s+(.+)", content)
        cat = cat_match.group(1).strip() if cat_match else "?"

        # Extract date
        date_match = re.search(r"^date:\s+(.+)$", content, re.MULTILINE)
        date_str = date_match.group(1).strip() if date_match else "?"

        # Extract source
        source_match = re.search(r"\*\*Source\*\*:\s+\[(.+?)\]", content)
        source = source_match.group(1) if source_match else "?"

        print(f"  [{cat:<20}] {date_str}  {d.name}")
        print(f"    {title}")
        print(f"    Source: {source}")
        print()

    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch funding opportunities and OMOP news into blog drafts.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # fetch
    fetch_parser = subparsers.add_parser(
        "fetch",
        help="Fetch new opportunities from external sources",
    )
    fetch_parser.add_argument(
        "--source",
        action="append",
        choices=list(SOURCE_FETCHERS.keys()),
        help="Fetch from specific source(s) only",
    )
    fetch_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be fetched without creating files",
    )

    # publish
    pub_parser = subparsers.add_parser(
        "publish",
        help="Move reviewed drafts to blog posts",
    )
    pub_parser.add_argument(
        "--all",
        action="store_true",
        help="Publish all drafts",
    )
    pub_parser.add_argument(
        "files",
        nargs="*",
        help="Specific draft filenames to publish",
    )

    # list
    subparsers.add_parser(
        "list",
        help="List pending drafts",
    )

    args = parser.parse_args()

    if args.command == "fetch":
        return cmd_fetch(args)
    elif args.command == "publish":
        return cmd_publish(args)
    elif args.command == "list":
        return cmd_list(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
