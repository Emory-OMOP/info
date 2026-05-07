# Blog Curation Workflow

The Emory OMOP team runs a weekly **human + LLM-assisted** curation pass on blog drafts that the auto-fetch workflow surfaces every Monday morning. This document describes the workflow, the human checkpoints, and the tooling.

## Why this exists

The fetch workflow (`.github/workflows/fetch-opportunities.yml`, see `scripts/fetch_opportunities.py`) polls 6 sources every Monday — NIH Guide, Grants.gov, NIH Reporter, PCORI, OHDSI Forums, PubMed — and drops raw markdown drafts into `scripts/blog_drafts/`. It opens an auto-PR titled *"New funding opportunities — YYYY-MM-DD"*.

Those raw drafts are not yet ready for the public blog. They need a human curatorial pass: which ones are worth surfacing to the community, what editorial framing ties them to Emory's work, which (if any) deserve featured-grid placement.

This is the kind of high-judgment, low-effort task that benefits from LLM assistance — the LLM proposes selections and drafts editorial intros; the human reviews, edits, and approves.

## The cycle

```
Monday 8am ET  →  fetch workflow opens an auto-PR with raw drafts
        |
        v
Human + LLM    →  review drafts, draft a curation session YAML
                  (which to publish with intros, which to delete,
                  which featured-grid cards to refresh)
        |
        v
Human review   →  edit YAML, verify no fabricated facts in intros
        |
        v
Apply          →  uv run scripts/curate_blog_posts.py apply <session.yml>
        |
        v
Human review   →  mkdocs serve, eyeball the rendered posts + grid
        |
        v
Open PR        →  curation PR with the published posts + grid refresh
                  + draft cleanup
        |
        v
Merge          →  squash + delete branch; site rebuilds
```

## Step-by-step

### 1. The auto-PR opens

A scheduled workflow run drops new drafts into `scripts/blog_drafts/` and opens a PR. **Merge this auto-PR first** so the drafts land on `main` for curation. (The drafts won't render on the site until they're moved to `docs/blog/posts/`.)

### 2. Start an LLM-assisted curation session

Open a session with an LLM assistant of your choice (any tool-augmented LLM that can read the repo works; for chat-only LLMs, paste the relevant content into the conversation).

Paste the starter prompt from [`CURATION_PROMPT.md`](CURATION_PROMPT.md). It tells the LLM:

- The relevance criteria (what's worth publishing, what to skip)
- The editorial voice constraints (1–2 sentence intros, no fabricated facts, Emory-specific framing where it fits)
- The featured-grid review rule (after publish/delete decisions, propose grid refreshes for any category that received a new post)
- The output format (a YAML session file with `publish:`, `delete:`, and `featured_grid:` sections)
- Explicit "wait for human approval before applying" instructions

### 3. Human review of the proposal

This is the most important checkpoint. Review the LLM's proposed YAML:

- **Selections**: agree with which drafts are being published vs deleted? Add or remove items.
- **Editorial intros**: each one should be honest and substantive. Watch for fabricated facts (LLMs sometimes invent details). Strip or rewrite anything that overstates.
- **Voice**: 1–2 sentences each. Emory-specific framing where it actually fits — don't force a connection that isn't there.
- **Featured-grid picks**: for each category that received a new post, does the LLM's pick actually represent the category well? Don't refresh a card to a less-representative post just because something newer landed.

Save the reviewed YAML to a temp path (e.g., `/tmp/curation-2026-05-12.yml`).

### 4. Apply the session

```
uv run scripts/curate_blog_posts.py apply /tmp/curation-2026-05-12.yml --dry-run
```

The dry-run prints what would happen without changing files. If it looks right:

```
uv run scripts/curate_blog_posts.py apply /tmp/curation-2026-05-12.yml
```

The script:

- Copies each `publish` entry to `docs/blog/posts/`, removes `draft: true`, adds `authors: - dsmith`, inserts the editorial intro after the H1, and adds `<!-- more -->` excerpt break.
- Removes each published or deleted entry from `scripts/blog_drafts/`.
- For each `featured_grid:` entry, reads the target post's date and H1 and replaces the matching `*<date>* — [<title>](posts/<slug>)` line under the corresponding category card on `docs/blog/index.md`. Other cards are left alone.
- Leaves `promoted: true` and `pin: true` flags untouched — those are individual-post features, separate from the grid.

### 5. Pinned post (optional)

For one-off site-wide announcements (not regular weekly posts), add `pin: true` to the post's frontmatter and update the `!!! tip "Pinned — <date>"` block at the top of `docs/blog/index.md`. Keep no more than one pin at a time.

### 6. Local preview

```
uv run mkdocs serve
```

Eyeball each new post at `/blog/posts/<slug>/`. Confirm the editorial intro renders, the source link works, the excerpt cut is sensible, AND the Browse-by-Category grid on the blog landing reflects your refreshes.

### 7. Open the curation PR

Branch, commit (`git add docs/blog/ scripts/blog_drafts/`), push, open PR. Title format: `Curate <month> <year> blog posts (<N> published, <M> deleted)`.

### 8. Merge

Squash + delete branch on merge. Site rebuilds; new posts are live.

## Human checkpoints — where to push back on the LLM

| Step | What to verify |
|---|---|
| Selection list | Are these actually worth surfacing? Anything missed? |
| Editorial intros | Honest? Fact-checked? No fabricated deadlines, names, affiliations? |
| Tone | 1–2 sentences each. Emory framing where it fits, not forced. |
| Featured-grid picks | Does each refresh actually represent the category, or is it just newest-by-date? |
| Pinning | Is this announcement worth taking the single pin slot? |
| Final render | mkdocs serve looks right. No broken links. |

## Older draft backlog

`scripts/blog_drafts/` may contain older un-curated drafts from prior fetch attempts. Those are a separate triage backlog — clean them up periodically when convenient. The curator script's `delete:` list handles any drafts you point it at, so a backlog cleanup is just a YAML with a long `delete:` and an empty `publish:` (and no `featured_grid:`).

## See also

- [`CURATION_PROMPT.md`](CURATION_PROMPT.md) — the starter prompt to paste into your LLM session
- [`fetch_opportunities.py`](fetch_opportunities.py) — the fetcher that produces the raw drafts
- [`curate_blog_posts.py`](curate_blog_posts.py) — the curator script that applies a session YAML
- [`.github/workflows/fetch-opportunities.yml`](../.github/workflows/fetch-opportunities.yml) — the schedule + auto-PR workflow
