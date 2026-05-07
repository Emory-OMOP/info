#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Apply a curation session to blog drafts.

Reads a YAML session file describing which drafts to publish (with editorial
intros), which to delete, and which featured-grid cards on the blog landing
page to refresh. Mechanical work only — the editorial decisions must be made
by the human, optionally with LLM assistance.

YAML schema:

    publish:
      - slug: 2026-05-04-health-systems-with-ehr-data-in-omop.md
        intro: |
          Editorial framing paragraph (1-2 sentences). No fabricated
          facts. Tie to known Emory work where relevant.

    delete:
      - 2026-04-13-weekly-ohdsi-digest---april-13-2026.md

    featured_grid:
      Funding:
        slug: 2026-05-06-broad-pragmatic-studies-pcori-funding-announcement----cycle-3-2026.md
      OHDSI:
        slug: 2026-04-09-release-of-phenelope---llm-concept-set-builder.md

All three sections are optional and can be applied independently. The script
processes them in order: publish → delete → featured_grid.

Run:

    uv run scripts/curate_blog_posts.py apply path/to/session.yml
    uv run scripts/curate_blog_posts.py apply path/to/session.yml --dry-run

For each `publish` entry the script:
  - Copies scripts/blog_drafts/<slug> → docs/blog/posts/<slug>
  - Removes `draft: true` from frontmatter
  - Adds `authors: - dsmith` if no `authors` block exists
  - Inserts the editorial intro after the H1, before the **Source** line
  - Adds `<!-- more -->` excerpt break
  - Removes the source draft from scripts/blog_drafts/

For each `delete` entry: removes scripts/blog_drafts/<slug>.

For each `featured_grid` entry:
  - Reads the target post's `date:` from frontmatter and H1 for the title
  - Replaces the `*<date>* — [<title>](posts/<slug>)` line under the matching
    category card on docs/blog/index.md
  - Other cards in the grid are left alone

The script does NOT modify `promoted: true` or `pin: true` flags — those are
explicit human decisions for each post.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent
DRAFTS = REPO / "scripts" / "blog_drafts"
POSTS = REPO / "docs" / "blog" / "posts"
BLOG_INDEX = REPO / "docs" / "blog" / "index.md"
DEFAULT_AUTHOR = "dsmith"


def transform(src_text: str, editorial_intro: str, author: str = DEFAULT_AUTHOR) -> str:
    """Transform a draft into a published post. Pure function — no I/O."""
    if not src_text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    parts = src_text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("malformed frontmatter")
    _, frontmatter, body = parts

    frontmatter = re.sub(r"^draft:\s*true\s*\n", "", frontmatter, flags=re.MULTILINE)

    if "authors:" not in frontmatter:
        frontmatter = frontmatter.rstrip() + f"\nauthors:\n  - {author}\n"

    intro = editorial_intro.strip()
    body_new = re.sub(
        r"^(# [^\n]+)\n\n(\*\*Source\*\*:)",
        rf"\1\n\n{intro}\n\n<!-- more -->\n\n\2",
        body,
        count=1,
        flags=re.MULTILINE,
    )
    if body_new == body:
        body_new = re.sub(
            r"^(# [^\n]+)\n\n",
            rf"\1\n\n{intro}\n\n<!-- more -->\n\n",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        if body_new == body:
            raise ValueError("could not find H1 to insert editorial intro after")

    return f"---\n{frontmatter.rstrip()}\n---\n{body_new}"


def extract_post_metadata(post_path: Path) -> tuple[str, str]:
    """Return (formatted_date, title) for a published post.

    Date format matches the existing grid style: 'Apr 1, 2026'.
    """
    text = post_path.read_text()
    date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    title_match = re.search(r"^# (.+?)\s*$", text, re.MULTILINE)
    if not date_match:
        raise ValueError(f"no `date:` in frontmatter")
    if not title_match:
        raise ValueError(f"no H1 title")
    dt = datetime.strptime(date_match.group(1), "%Y-%m-%d")
    # Strip leading zero from day: "Apr 01, 2026" -> "Apr 1, 2026"
    date_str = dt.strftime("%b %d, %Y").replace(" 0", " ", 1)
    return date_str, title_match.group(1).strip()


def update_grid(grid: dict, dry_run: bool = False) -> int:
    """Update the Browse by Category grid on docs/blog/index.md.

    Returns the number of cards updated.
    """
    if not BLOG_INDEX.exists():
        print(f"  ERROR: blog index not found: {BLOG_INDEX}", file=sys.stderr)
        return 0

    lines = BLOG_INDEX.read_text().splitlines(keepends=True)
    date_line_re = re.compile(r"^    \*[^*]+\* — \[[^\]]+\]\(posts/[^)]+\)")
    updated = 0

    for category, entry in grid.items():
        slug = entry.get("slug") if isinstance(entry, dict) else None
        if not slug:
            print(f"  ERROR: featured_grid['{category}'] missing `slug`", file=sys.stderr)
            continue

        post_path = POSTS / slug
        if not post_path.exists():
            print(f"  ERROR: post not found for {category}: {slug}", file=sys.stderr)
            continue

        try:
            date_str, title = extract_post_metadata(post_path)
        except ValueError as e:
            print(f"  ERROR ({slug}): {e}", file=sys.stderr)
            continue

        new_line = f"    *{date_str}* — [{title}](posts/{slug})\n"

        # Find the category card marker
        cat_marker = f"**{category}**"
        cat_idx = next((i for i, line in enumerate(lines) if cat_marker in line), None)
        if cat_idx is None:
            print(f"  ERROR: category '{category}' not found in {BLOG_INDEX.name}", file=sys.stderr)
            continue

        # Find the first matching date+link line after the category marker
        replaced = False
        for i in range(cat_idx + 1, len(lines)):
            if date_line_re.match(lines[i]):
                old_line = lines[i].rstrip("\n")
                if dry_run:
                    print(f"  WOULD UPDATE [{category}]:")
                    print(f"    -  {old_line}")
                    print(f"    +  {new_line.rstrip()}")
                else:
                    lines[i] = new_line
                    print(f"  UPDATED [{category}]: {slug}")
                replaced = True
                updated += 1
                break
            # Stop if we hit the next card (avoids drifting)
            if lines[i].lstrip().startswith("-   :material-"):
                break

        if not replaced:
            print(f"  ERROR: no date line found under category '{category}'", file=sys.stderr)

    if not dry_run and updated > 0:
        BLOG_INDEX.write_text("".join(lines))

    return updated


def validate_session(session: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(session, dict):
        return ["session must be a YAML mapping with `publish:`, `delete:`, and/or `featured_grid:` keys"]

    publish = session.get("publish")
    if publish is not None and not isinstance(publish, list):
        errors.append("`publish:` must be a list")
    else:
        for i, entry in enumerate(publish or []):
            if not isinstance(entry, dict):
                errors.append(f"publish[{i}] must be a mapping with `slug` and `intro`")
                continue
            if "slug" not in entry:
                errors.append(f"publish[{i}] missing `slug`")
            if "intro" not in entry or not str(entry.get("intro", "")).strip():
                errors.append(f"publish[{i}] ({entry.get('slug', '?')}) missing or empty `intro`")

    delete = session.get("delete")
    if delete is not None and not isinstance(delete, list):
        errors.append("`delete:` must be a list of slug strings")
    else:
        for i, slug in enumerate(delete or []):
            if not isinstance(slug, str):
                errors.append(f"delete[{i}] must be a string slug")

    grid = session.get("featured_grid")
    if grid is not None and not isinstance(grid, dict):
        errors.append("`featured_grid:` must be a mapping of `Category: {slug: ...}`")
    elif isinstance(grid, dict):
        for cat, entry in grid.items():
            if not isinstance(entry, dict) or "slug" not in entry:
                errors.append(f"featured_grid['{cat}'] must be a mapping with at least `slug`")

    return errors


def apply_session(session_path: Path, dry_run: bool = False) -> int:
    if not session_path.exists():
        print(f"ERROR: session file not found: {session_path}", file=sys.stderr)
        return 1
    if not DRAFTS.is_dir():
        print(f"ERROR: drafts dir not found: {DRAFTS}", file=sys.stderr)
        return 1
    if not POSTS.is_dir():
        print(f"ERROR: posts dir not found: {POSTS}", file=sys.stderr)
        return 1

    session = yaml.safe_load(session_path.read_text())
    errors = validate_session(session)
    if errors:
        print("Session YAML failed validation:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    publish = session.get("publish") or []
    delete = session.get("delete") or []
    grid = session.get("featured_grid") or {}

    mode = "DRY RUN — no changes will be made" if dry_run else "APPLYING"
    print(f"=== {mode} ===")
    print(f"Session : {session_path}")
    print(f"Drafts  : {DRAFTS}")
    print(f"Posts   : {POSTS}")
    print(f"Index   : {BLOG_INDEX}")
    print()

    print(f"=== publishing {len(publish)} posts ===")
    published = 0
    for entry in publish:
        slug = entry["slug"]
        intro = entry["intro"]
        src = DRAFTS / slug
        dst = POSTS / slug
        if not src.exists():
            print(f"  SKIP (not in drafts): {slug}", file=sys.stderr)
            continue
        if dst.exists():
            print(f"  SKIP (already published): {slug}", file=sys.stderr)
            continue
        try:
            transformed = transform(src.read_text(), intro)
        except ValueError as e:
            print(f"  ERROR ({slug}): {e}", file=sys.stderr)
            continue
        if dry_run:
            print(f"  WOULD PUBLISH: {slug}")
        else:
            dst.write_text(transformed)
            src.unlink()
            print(f"  PUBLISHED:     {slug}")
        published += 1
    print(f"Published: {published}/{len(publish)}")
    print()

    print(f"=== deleting {len(delete)} drafts ===")
    deleted = 0
    for slug in delete:
        path = DRAFTS / slug
        if not path.exists():
            print(f"  SKIP (not in drafts): {slug}")
            continue
        if dry_run:
            print(f"  WOULD DELETE: {slug}")
        else:
            path.unlink()
            print(f"  DELETED:      {slug}")
        deleted += 1
    print(f"Deleted: {deleted}/{len(delete)}")
    print()

    print(f"=== featured grid: {len(grid)} card(s) ===")
    update_grid(grid, dry_run=dry_run)
    print()

    remaining = sorted(p.name for p in DRAFTS.glob("*.md"))
    print(f"=== {len(remaining)} draft(s) still in scripts/blog_drafts/ ===")
    if remaining:
        for r in remaining[:20]:
            print(f"  {r}")
        if len(remaining) > 20:
            print(f"  ... and {len(remaining) - 20} more")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    apply_p = sub.add_parser("apply", help="Apply a curation session YAML.")
    apply_p.add_argument("session", type=Path, help="Path to the session YAML file.")
    apply_p.add_argument("--dry-run", action="store_true", help="Print what would happen, don't change files.")
    args = ap.parse_args()
    if args.cmd == "apply":
        return apply_session(args.session, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
