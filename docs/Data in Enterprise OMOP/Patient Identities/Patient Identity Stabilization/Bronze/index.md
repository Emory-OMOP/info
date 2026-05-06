---
hide:
  - footer
title: Bronze
---

# Bronze

*Released in v1.0.0 — snapshot 2026-03-31*

Bronze is the operational intake layer. It has two responsibilities:

1. **Mirror upstream Epic Clarity identity tables** as rolling current/previous snapshot pairs in the `clarity_onprem_omop` schema (the Clarity raw mirror, owned by central ingestion).
2. **Hold project-curated bronze artifacts** like manually submitted merge evidence in the `emory_identity_bronze` schema (owned by this project).

Bronze itself is not a historical archive — only two snapshots per source are retained at any time. The full audit trail of identifier changes lives in Silver, which is rebuilt from bronze deltas each cycle.

## Source mirrors (`clarity_onprem_omop`)

Epic Clarity identity tables are staged here, each with a `_previous` companion:

| Table | Purpose |
|---|---|
| `identity_id` / `identity_id_previous` | Current and previous snapshots of patient identifier assignments (Epic PAT → identifier mapping). |
| `identity_id_hx` / `identity_id_hx_previous` | Current and previous snapshots of Epic's identity history / merge log. |

Each refresh cycle, the *current* snapshot becomes the *previous*, and the new snapshot is loaded as *current*. The change-detection layer compares the two to find new attachments, detachments, and PAT-level merges.

## Project-curated bronze (`emory_identity_bronze`)

The `emory_identity_bronze` schema is owned by this project and holds bronze artifacts that don't come from Clarity directly. The most important is:

- **`merge_evidence_submission`** — manually curated evidence linking pairs of `person_id`s that should be merged (e.g., a CDW person and an Epic person identified as the same human via EMPI). Each row carries an evidence category (`CLEAR_FIX`, `LIKELY_FIX`, `QUARANTINE_TYPE_1`, `QUARANTINE_TYPE_2`), a confidence score, and provenance. These submissions become input to the Silver edge graph.

## Why bronze isn't historical

Bronze is intentionally kept small. Two snapshots are sufficient to compute per-cycle deltas, and storing more would duplicate the historical record that already lives in Silver as an append-only event stream.

Older Epic Clarity snapshots are archived to **AWS S3 Glacier** for disaster recovery, with **August 2025** the earliest archived snapshot available — anything prior to August 2025 is not preserved. Routine queries against historical identifier state should always go through Silver or Gold; the Glacier archive is a recovery tool, not a query surface.

---

[:octicons-arrow-left-24: Pipeline Overview](../Pipeline%20Overview.md) · [:octicons-arrow-right-24: Silver](../Silver/index.md)
