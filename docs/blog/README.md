# News & Opportunities Blog

MkDocs Material blog for surfacing funding opportunities, OHDSI network updates, real-world evidence developments, and announcements to Emory's OMOP research community.

## Adding a post

Create a markdown file in `docs/blog/posts/` with this template:

```markdown
---
date: 2026-03-15
authors:
  - dsmith
categories:
  - Funding
tags:
  - nih
  - rwe
---

# Post Title

Brief description that appears in the blog listing.

<!-- more -->

Full post content below the fold. Supports all MkDocs Material
features — admonitions, tables, code blocks, links, etc.
```

### Required fields

| Field | Description |
|-------|-------------|
| `date` | Publication date (`YYYY-MM-DD`) |
| `categories` | One or more from the allowed list below |

### Optional fields

| Field | Description |
|-------|-------------|
| `authors` | Author key(s) from `.authors.yml` |
| `tags` | Free-form tags for filtering |
| `draft` | Set `true` to hide from production (visible in `mkdocs serve`) |

### The `<!-- more -->` separator

Everything above the separator shows in the blog listing as the post excerpt. Everything below only appears when a reader clicks through to the full post. If omitted, the entire post shows in the listing.

## Categories

Posts must use categories from this list (enforced in `mkdocs.yml`):

| Category | Use for |
|----------|---------|
| **Funding** | NIH RFAs, foundation grants, internal pilot funding, award announcements |
| **OHDSI** | Network studies, OHDSI symposium, community tools, workgroup updates |
| **Real-World Evidence** | RWE methods, regulatory developments, policy changes |
| **Vocabulary** | Vocabulary releases, mapping updates, concept coverage changes |
| **Data Quality** | DQD results, pipeline improvements, known issue resolutions |
| **Infrastructure** | Platform changes, new tooling, access updates, downtime notices |
| **Community** | Training sessions, onboarding, team updates, user spotlights |

To add a new category, update the `categories_allowed` list in `mkdocs.yml` under the `blog` plugin.

## Authors

Authors are defined in `docs/blog/.authors.yml`:

```yaml
authors:
  dsmith:
    name: Daniel Smith
    description: OMOP Program Lead
    avatar: https://github.com/identicons/dsmith.png
```

To add a new author, add an entry with a unique key, name, description, and avatar URL.

## File naming

No strict naming convention required — MkDocs sorts posts by the `date` field in frontmatter, not the filename. A recommended pattern for readability:

```
docs/blog/posts/YYYY-MM-DD-short-slug.md
```

## Automated funding opportunity fetcher

The script `scripts/fetch_opportunities.py` aggregates funding opportunities and research news from 6 sources into draft blog posts for review before publishing.

### Sources

| Source | Type | What it finds |
|--------|------|---------------|
| **NIH Guide** | RSS | NIH policy notices and funding announcements |
| **Grants.gov** | API | Federal FOAs from HHS, NIH, AHRQ, VA, NSF, DOD |
| **NIH Reporter** | API | Recently funded projects using OMOP/RWE methods |
| **PCORI** | Web scrape | Patient-centered outcomes research funding (Open/Upcoming) |
| **OHDSI Forums** | RSS | Community discussions, collaborations, network studies |
| **PubMed** | API | Recent OMOP/RWE methods publications |

### Automated workflow (CI/CD)

A GitHub Action (`.github/workflows/fetch-opportunities.yml`) runs **every Monday at 8am ET** and can also be triggered manually from the Actions tab.

1. **Fetch** — the Action runs the fetcher and creates draft files in `docs/blog/drafts/`
2. **PR** — if new drafts are found, a PR is opened automatically (branch: `auto/opportunities-YYYY-MM-DD`)
3. **Review** — you review the PR, delete posts you don't want, and keep the ones worth publishing
4. **Publish** — move approved drafts from `drafts/` to `posts/` (the `publish` command does this and strips `draft: true`), then merge the PR
5. **Deploy** — the site rebuilds with the new posts on merge

### Manual workflow (local)

```bash
# Fetch new opportunities into docs/blog/drafts/
uv run scripts/fetch_opportunities.py fetch

# Preview locally (drafts visible in serve mode)
uv run mkdocs serve

# List pending drafts
uv run scripts/fetch_opportunities.py list

# Publish reviewed drafts (moves to posts/, strips draft: true)
uv run scripts/fetch_opportunities.py publish --all
# Or publish specific files:
uv run scripts/fetch_opportunities.py publish file1.md file2.md

# Dry run (see what would be fetched without creating files)
uv run scripts/fetch_opportunities.py fetch --dry-run

# Fetch from a specific source only
uv run scripts/fetch_opportunities.py fetch --source pcori --source grants-gov
```

Available `--source` values: `nih-guide`, `ohdsi`, `grants-gov`, `nih-reporter`, `pcori`, `pubmed`

### Deduplication

The fetcher tracks previously seen posts in `scripts/feed_state.json` (gitignored). Running `fetch` multiple times won't create duplicate drafts. Delete this file to reset and re-fetch everything.

### Reviewing drafts

Each draft has `draft: true` in its frontmatter, so it won't appear on the published site. When reviewing:

- **Delete** drafts that aren't relevant
- **Edit** drafts to add context, fix formatting, or add author attribution
- **Publish** by running `uv run scripts/fetch_opportunities.py publish <filename>` or manually moving the file to `posts/` and removing the `draft: true` line

## Features

- **Pagination** — 10 posts per page
- **Categories** — browseable category pages auto-generated
- **Tags** — tag index page at `/blog/tags/`
- **Archive** — monthly archive auto-generated
- **Drafts** — set `draft: true` in frontmatter to preview locally without publishing

## See also

- [Repository README](../../README.md) — repo overview and quick start
- [Data Quality release pipeline](../../scripts/README.md) — DQD/DBT automation
- [Community overlap report](../../scripts/community_data/README.md) — stakeholder visualization
