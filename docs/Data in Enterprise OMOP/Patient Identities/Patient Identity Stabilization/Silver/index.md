---
hide:
  - footer
title: Silver
---

# Silver

*Released in v1.0.0 — snapshot 2026-03-31*

Silver (`emory_identity_silver`) is where the identity graph lives. It captures every identifier event ever observed as an append-only history, and on top of that builds current-state derivations that say *which identifiers belong to which patient anchor right now*.

Silver owns the truth about how identities have evolved over time. Bronze is ephemeral; Clustering and Gold are computed from Silver. If Silver is correct, the rest of the pipeline is correct.

## The graph: nodes and edges

Identity stabilization treats each identifier as a node and each piece of evidence connecting two identifiers as an edge.

| Model | Role |
|---|---|
| `identity_node_silver` | One row per known identifier — Epic PAT_IDs, MRNs, EMPIs, legacy CDW identifiers, EOMOP `person_id`s. Each node has a deterministic `node_id` derived from `MD5(UPPER(TRIM(id_type)) || '::' || UPPER(TRIM(id_value)))` so the same identifier always hashes to the same node. |
| `identity_edge_silver` | Append-only edge log. Each edge says "these two nodes belong to the same human" with a typed reason. |

Two relationship types are produced by ongoing change detection:

- **`EPIC_PAT_HAS_ID`** — Epic PAT carries this MRN / SSN / etc. (current attachment).
- **`EPIC_PAT_MERGED_TO`** — Two Epic PATs were merged in Clarity; this is permanent evidence linking the merged-away PAT to its survivor.

In addition, Silver loads **bootstrap seed edges** captured at project inception — one CDW snapshot (March 2025) and one Epic snapshot (August 2025) — that preserve the historical edge graph from before continuous change detection began. With the legacy Cerner CDW now taken offline, all new edges going forward originate from the Epic side.

Edges accumulate over time and are never deleted. A merge in Epic produces a permanent `EPIC_PAT_MERGED_TO` edge; even if a future event re-splits the data, that historical merge remains visible in the graph.

## Change detection

Silver is fed by the change-detection layer (`models/change_detection/`), which compares Bronze's current and previous snapshots to identify what changed:

- **`identity_id_delta_events`** — additions, removals, and modifications to identifier attachments since the last cycle.
- **`epic_pat_merge_events`** — newly observed PAT-level merges from `identity_id_hx`.

Each cycle, change-detection writes new event rows into the Silver edge log. The append-only contract means any historical query can reconstruct identifier state at any prior point in time.

## Current-state derivations

For consumers that don't want to time-travel, Silver also publishes current-state tables (`models/silver_current/`). The most important:

- **`identifier_attachment_current`** — for every identifier, which PAT (or PATs) currently carry it. Detached identifiers are filtered out of this view.

Current-state tables are how downstream Clustering avoids reprocessing the entire history every cycle: it works against the current attachments and merge state, not against the full event log.

---

[:octicons-arrow-left-24: Pipeline Overview](../Pipeline%20Overview.md) · [:octicons-arrow-right-24: Clustering](../Clustering/index.md)
