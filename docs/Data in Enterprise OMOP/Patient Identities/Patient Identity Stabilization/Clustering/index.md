---
hide:
  - footer
title: Clustering
---

# Clustering

*Released in v1.0.0 — snapshot 2026-01-31*

Clustering (`emory_identity_clustering`) is where the graph is collapsed into people. The Python script `py/run_connected_components.py` reads Silver's edges, runs a connected-components analysis, and assigns each component a stable `person_id`.

Clustering is the only layer that runs Python rather than dbt SQL. The output is written to S3 as Parquet and registered in the `emory_identity_clustering` schema, where dbt picks it up to build the gold tables.

## Connected components

Two identifiers belong to the same human if there is *any* path between their nodes in the identity graph. The clustering job uses [NetworkX](https://networkx.org/) to compute connected components:

1. Read every active edge from `identity_edge_silver` (filtered through `identifier_attachment_current` so detached identifiers don't pull old anchors back into a component).
2. Build the undirected graph in memory.
3. Run `networkx.connected_components()` to partition nodes into components.
4. For each component, pick a canonical anchor node and assign a `person_id`.

The raw output is registered as `connected_components_raw` (external Parquet) and exposed as the `connected_components` view; downstream models in this schema build the resolved person tables on top.

## Component anchor selection

The canonical anchor for each component — the node that determines the component's "primary" representation — is chosen deterministically by the Python script:

1. Must be an SSID node (`canonical_id_type LIKE '%[SSID]%'`, i.e., a top-level patient identifier like `EPIC::PAT_ID[SSID]`).
2. Must NOT be merged away (no outgoing `EPIC_PAT_MERGED_TO` edge).
3. Highest-authority source system wins (lowest `authority_rank`).
4. Tiebreaker: `MIN(node_id)` — deterministic and repeatable across runs.

This deterministic anchor choice is the foundation of `person_id` stability: as long as a person's anchor node remains in the graph and isn't merged away, their `person_id` doesn't change between runs.

## Models in `emory_identity_clustering`

| Model | Role |
|---|---|
| `connected_components` | View on the external Python output: every node mapped to its component. |
| `identity_cluster_current` | Current-state mapping of node → component → `person_id`. |
| `identity_cluster_output_history` | Audit trail of cluster output across runs. |
| `cluster_person_resolution` | Per-component resolution metadata: status, competing-`person_id` counts, whether an Epic merge anchored the resolution. |
| `current_merge_state` | For each PAT-level node, whether it is merged away and to which surviving node. |
| `person_id_assignment` | The actual mapping of components to stable `person_id` values. |
| `person_merge_edges` | PAT-merge edges expressed at the `person_id` layer rather than the node layer. |
| `ssid_source_status` | Per-source-system status of each SSID node. |

A component carries a `RESOLVED` status when an authoritative SSID anchor is present; `GENERATED` when the algorithm had to synthesize a `person_id` for a component without a clean anchor.

!!! tip "Related: probabilistic match weights"
    Connected-components clustering is deterministic and treats every edge as equally weighted evidence. A separate methodology write-up — [Probabilistic Matching](../../Probabilistic%20Matching/index.md) — documents Emory's Fellegi-Sunter match-weight derivation for graded identifier evidence and the prior-estimation work behind it.

## Quarantine

A small fraction of components cannot be cleanly resolved — typically because the graph contains internal contradictions (e.g., two Epic PATs that aren't linked by a merge but share a high-authority identifier). These components are quarantined: they receive no `person_id` and surface in `person_quarantine_gold` for manual review. See [Gold](../Gold/index.md) for how quarantine appears to consumers.

---

[:octicons-arrow-left-24: Pipeline Overview](../Pipeline%20Overview.md) · [:octicons-arrow-right-24: Gold](../Gold/index.md)
