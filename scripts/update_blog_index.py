#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Regenerate docs/blog/index.md from published post frontmatter.

Scans all posts in docs/blog/posts/, finds the most recent post per category,
and writes the blog landing page with category cards, dates, and deadline info.

Usage:
    uv run scripts/update_blog_index.py
    uv run scripts/update_blog_index.py --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "docs" / "blog" / "posts"
INDEX_FILE = REPO_ROOT / "docs" / "blog" / "index.md"

# Category display config: slug -> (icon, description)
CATEGORIES = {
    "Funding": (
        ":material-cash-multiple:",
        "NIH RFAs, PCORI, foundation grants, and award announcements.",
    ),
    "Vocabulary": (
        ":material-book-open-variant:",
        "Vocabulary releases, mapping updates, and concept coverage changes.",
    ),
    "Data Quality": (
        ":material-check-decagram:",
        "DQD results, pipeline improvements, and known issue resolutions.",
    ),
    "Infrastructure": (
        ":material-server-network:",
        "Platform changes, new tooling, access updates, and downtime notices.",
    ),
    "Community": (
        ":material-human-greeting-proximity:",
        "Training sessions, onboarding, team updates, and research discussions.",
    ),
    "OHDSI": (
        ":material-account-group:",
        "Network studies, symposium news, community tools, and workgroup updates.",
    ),
    "Real-World Evidence": (
        ":material-flask:",
        "RWE methods, regulatory developments, and policy changes.",
    ),
}

# Category slug for URL (Material auto-generates these)
CATEGORY_SLUGS = {
    "Funding": "funding",
    "Vocabulary": "vocabulary",
    "Data Quality": "data-quality",
    "Infrastructure": "infrastructure",
    "Community": "community",
    "OHDSI": "ohdsi",
    "Real-World Evidence": "real-world-evidence",
}


def parse_frontmatter(path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None

    fm: dict = {
        "path": path,
        "filename": path.name,
        "categories": [],
    }

    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("date:"):
            fm["date"] = line.split(":", 1)[1].strip()
        elif line.startswith("- ") and "categories" not in line:
            # Collect list items (categories or tags)
            val = line[2:].strip()
            if val in CATEGORIES:
                fm["categories"].append(val)
        elif line.startswith("pin:"):
            fm["pin"] = line.split(":", 1)[1].strip().lower() == "true"
        elif line.startswith("deadline_loi:"):
            fm["deadline_loi"] = line.split(":", 1)[1].strip()
        elif line.startswith("deadline_app:"):
            fm["deadline_app"] = line.split(":", 1)[1].strip()
        elif line.startswith("deadline_close:"):
            fm["deadline_close"] = line.split(":", 1)[1].strip()

    # Extract title from first # heading
    title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    if title_match:
        fm["title"] = title_match.group(1).strip()

    return fm


def format_date(d: str, short: bool = False) -> str:
    """Format YYYY-MM-DD as 'Mon D, YYYY' or 'Mon D' if short and same year."""
    try:
        dt = datetime.strptime(d, "%Y-%m-%d")
        if short and dt.year == date.today().year:
            return dt.strftime("%b %-d")
        return dt.strftime("%b %-d, %Y")
    except (ValueError, AttributeError):
        return d


def format_deadline_suffix(post: dict) -> str:
    """Build deadline string for funding posts."""
    parts = []
    if "deadline_loi" in post:
        parts.append(f"LOI {format_date(post['deadline_loi'], short=True)}")
    if "deadline_app" in post:
        parts.append(f"App {format_date(post['deadline_app'], short=True)}")
    if "deadline_close" in post:
        parts.append(f"Closes {format_date(post['deadline_close'], short=True)}")
    if parts:
        return " · " + ", ".join(parts)
    return ""


def find_pinned_post(posts: list[dict]) -> dict | None:
    """Find the most recent pinned post (for the top banner)."""
    pinned = [p for p in posts if p.get("pin")]
    if not pinned:
        return None
    return max(pinned, key=lambda p: p.get("date", ""))


def find_latest_per_category(posts: list[dict]) -> dict[str, dict]:
    """Find the most recent post for each category."""
    latest: dict[str, dict] = {}
    for post in posts:
        for cat in post.get("categories", []):
            if cat not in latest or post.get("date", "") > latest[cat].get("date", ""):
                latest[cat] = post
    return latest


def relative_post_path(post: dict) -> str:
    """Get the relative path from blog/index.md to the post."""
    return f"posts/{post['filename']}"


def generate_index(posts: list[dict]) -> str:
    """Generate the full blog index.md content."""
    pinned = find_pinned_post(posts)
    latest = find_latest_per_category(posts)

    lines = [
        "---",
        "hide:",
        "  - footer",
        "title: News & Opportunities",
        "---",
        "",
        "# News & Opportunities",
        "",
        "Funding opportunities, OHDSI network updates, real-world evidence developments, and announcements relevant to Emory's OMOP community.",
        "",
    ]

    # Pinned post banner
    if pinned:
        pinned_date = format_date(pinned.get("date", ""))
        pinned_title = pinned.get("title", "Untitled")
        pinned_path = relative_post_path(pinned)
        lines.extend([
            f'!!! tip "Pinned — {pinned_date}"',
            f"    **{pinned_title}** [:octicons-arrow-right-24: Read more]({pinned_path})",
            "",
        ])

    # Category cards
    lines.extend([
        "## Browse by Category",
        "",
        '<div class="grid cards" markdown>',
        "",
    ])

    for cat_name, (icon, description) in CATEGORIES.items():
        slug = CATEGORY_SLUGS[cat_name]
        post = latest.get(cat_name)

        lines.append(f"-   {icon}{{ .lg .middle }} **{cat_name}**")
        lines.append("")
        lines.append("    ---")
        lines.append("")
        lines.append(f"    {description}")
        lines.append("")

        if post:
            post_date = format_date(post.get("date", ""))
            post_title = post.get("title", "Untitled")
            post_path = relative_post_path(post)
            deadline = ""
            if cat_name == "Funding":
                deadline = format_deadline_suffix(post)
            lines.append(f"    *{post_date}* — [{post_title}]({post_path}){deadline}")
            lines.append("")

        lines.append(f"    [:octicons-arrow-right-24: All {cat_name} posts](category/{slug}/)")
        lines.append("")

    lines.extend([
        "</div>",
        "",
        "---",
        "",
        "## Recent Posts",
        "",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Regenerate blog index.md")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    args = parser.parse_args()

    if not POSTS_DIR.exists():
        print(f"Posts directory not found: {POSTS_DIR}", file=sys.stderr)
        sys.exit(1)

    posts = []
    for md in sorted(POSTS_DIR.glob("*.md")):
        fm = parse_frontmatter(md)
        if fm:
            posts.append(fm)

    print(f"Found {len(posts)} posts")

    content = generate_index(posts)

    if args.dry_run:
        print("\n--- Generated index.md ---\n")
        print(content)
    else:
        INDEX_FILE.write_text(content)
        print(f"Wrote {INDEX_FILE}")


if __name__ == "__main__":
    main()
