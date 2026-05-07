#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Apply a curation session to blog drafts.

Reads a YAML session file describing which drafts to publish (with editorial
intros) and which to delete. Mechanical work only — the editorial decisions
must be made by the human, optionally with LLM assistance.

YAML schema:

    publish:
      - slug: 2026-05-04-health-systems-with-ehr-data-in-omop.md
        intro: |
          Editorial framing paragraph (1-2 sentences). No fabricated
          facts. Tie to known Emory work where relevant.
      - slug: ...
        intro: |
          ...

    delete:
      - 2026-04-13-weekly-ohdsi-digest---april-13-2026.md
      - ...

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

The script does NOT modify `promoted: true`, `pin: true`, or the Featured
grid — those are explicit human decisions for each post.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# Resolve script-relative paths so this works regardless of where it's invoked
# from. Lives at <repo>/scripts/curate_blog_posts.py.
SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent
DRAFTS = REPO / "scripts" / "blog_drafts"
POSTS = REPO / "docs" / "blog" / "posts"
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


def validate_session(session: dict) -> list[str]:
    """Return a list of validation errors (empty if valid)."""
    errors: list[str] = []
    if not isinstance(session, dict):
        return ["session must be a YAML mapping with `publish:` and/or `delete:` keys"]

    publish = session.get("publish", [])
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

    delete = session.get("delete", [])
    if delete is not None and not isinstance(delete, list):
        errors.append("`delete:` must be a list of slug strings")
    else:
        for i, slug in enumerate(delete or []):
            if not isinstance(slug, str):
                errors.append(f"delete[{i}] must be a string slug")

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

    mode = "DRY RUN — no changes will be made" if dry_run else "APPLYING"
    print(f"=== {mode} ===")
    print(f"Session : {session_path}")
    print(f"Drafts  : {DRAFTS}")
    print(f"Posts   : {POSTS}")
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
