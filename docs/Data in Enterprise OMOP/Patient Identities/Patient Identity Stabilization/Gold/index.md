---
hide:
  - footer
title: Gold
---

# Gold

*Released in v1.0.0 — snapshot 2026-03-31*

Gold (`emory_identity_gold`) is the analyst-facing surface of the identity pipeline. Everything upstream — Bronze, Silver, Clustering — exists to make these tables reliable. If you're looking up a patient, listing identifiers, or following a merge, this is the schema you want.

??? abstract "Quick reference — what's on this page"

    [**Core resolution**](#core-resolution) — `person_id_gold`, `person_identity_link_gold`

    [**Analyst-facing identifier views**](#analyst-facing-identifier-views) — `person_identifier_gold`, `person_identifier_gold_current`, `person_identifier_gold_history`

    [**Merge tracking**](#merge-tracking) — `person_merge_history_gold`

    [**Source status**](#source-status) — `person_ssid_source_status`

    [**Governance**](#governance) — `person_quarantine_gold`

## When to use which table

| If you want to... | Use |
|---|---|
| Find the canonical `person_id` from an MRN, EMPI, or other identifier | `person_identifier_gold_current` |
| List all currently-active identifiers for a known `person_id` | `person_identifier_gold_current` |
| See an identifier's full attachment history (including detachments) | `person_identifier_gold_history` |
| Get one row per resolved person with confidence and clustering metadata | `person_id_gold` |
| Map every identifier node to its person with role labels | `person_identity_link_gold` |
| Trace patient merges from Epic | `person_merge_history_gold` |
| See per-source status of each top-level patient identifier | `person_ssid_source_status` |
| Inspect components held back from `person_id` assignment | `person_quarantine_gold` |

## Tables

All gold models are materialized as denormalized tables and are joinable on `person_id`.

!!! warning "Quarantined components have no `person_id`"
    `person_quarantine_gold` is the exception — its rows are unresolved components by definition and do not appear in any of the other gold tables. Joining them in requires the upstream `component_id` from the clustering schema, not `person_id`.

### Core resolution

??? example "person_id_gold — one row per resolved person"

    The authoritative list of resolved persons. Rebuilt entirely on each clustering run; reflects current state only and excludes quarantined components.

    | Column | Description | Type |
    |---|---|---|
    | `person_id` | Canonical patient identifier. Stable across clustering runs whenever possible. | bigint |
    | `cluster_hash` | Stable component-identity hash; tracks the same person's cluster across runs. | varchar |
    | `created_datetime` | When this person's cluster was first observed. | timestamp |
    | `last_updated_datetime` | Most recent clustering run that touched this person. | timestamp |
    | `status` | Always `ACTIVE` for current persons. | varchar |
    | `confidence_score` | Heuristic confidence (0.70–0.95) based on resolution status and Epic-merge anchoring. | double |
    | `clustering_method` | Algorithm flavor used (e.g., `AUTO_CONNECTED_COMPONENTS`, `AUTO_CONNECTED_COMPONENTS_EPIC_MERGE`). | varchar |
    | `clustering_algorithm_version` | Version of the clustering algorithm that produced this row. | varchar |
    | `review_status` | Manual review state; defaults to `UNREVIEWED`. | varchar |
    | `reviewed_by` / `reviewed_datetime` / `review_notes` | Review provenance, populated when a person is manually reviewed. | varchar / timestamp / varchar |
    | `node_count` | Number of identifier nodes in this person's cluster. | bigint |
    | `identifier_count` | Distinct count of `canonical_id_value`s in this cluster. | bigint |

??? example "person_identity_link_gold — node ↔ person with role labels"

    Maps every identifier node to its resolved person, with a computed `node_role` indicating how the node participates in the person's identity. Heavy table — used as the join hub for the analyst views.

    | Column | Description | Type |
    |---|---|---|
    | `link_id` | Deterministic hash of `(person_id, node_id, assignment_timestamp)`. | varchar |
    | `person_id` | Resolved person this node belongs to. | bigint |
    | `node_id` | Identifier node (deterministic hash of `id_type :: id_value`). | varchar |
    | `node_role` | One of `PRIMARY_PAT_ID`, `MERGED_PAT_ID`, `IDENTIFIER_NODE`, `EXTERNAL_ID`, `PERSON_NODE`. | varchar |
    | `start_datetime` | When this node was first linked to this person. | timestamp |
    | `end_datetime` | Always NULL in current-state view. | timestamp |
    | `active_flag` | Always TRUE in current-state view. | boolean |
    | `link_version_id` / `superseded_by_link_id` | Versioning placeholders (1 / NULL in current state). | bigint / varchar |
    | `change_reason` | Always `CLUSTERING_UPDATE`. | varchar |
    | `created_by_run_id` | Identifier of the clustering run that produced this row. | varchar |
    | `is_merged_away` | TRUE if this node is a PAT that was merged into the primary. | boolean |

    !!! tip "Node role meanings"
        - **`PRIMARY_PAT_ID`** — the active Epic PAT for this person
        - **`MERGED_PAT_ID`** — a PAT that was merged into the primary (kept for historical traceability)
        - **`IDENTIFIER_NODE`** — a non-PAT identifier (MRN, EMPI, SSN, etc.) currently attached
        - **`EXTERNAL_ID`** — identifiers from external systems
        - **`PERSON_NODE`** — legacy OMOP `person_id` preserved for stability

### Analyst-facing identifier views

??? example "person_identifier_gold — flattened current-state identifiers"

    Joins `person_identity_link_gold` to node metadata for one-stop querying. One row per `(person_id, identifier)` currently attached.

    | Column | Description | Type |
    |---|---|---|
    | `person_id` | Resolved person. | bigint |
    | `node_id` | Identifier node hash. | varchar |
    | `id_type` | Identifier type, e.g., `EPIC::914`, `EPIC::PAT_ID[SSID]`, `CDW::EMPI`. | varchar |
    | `id_value` | Identifier value (the MRN, EMPI, etc.). | varchar |
    | `source_system` | System the identifier originated in (`EPIC`, `CDW`, ...). | varchar |
    | `node_role` | Same role taxonomy as `person_identity_link_gold`. | varchar |
    | `valid_start` | When this attachment was first observed. | timestamp |
    | `valid_end` | Always NULL — this view is current-state only. | timestamp |
    | `pii_level` / `phi_flag` / `restricted_flag` | PHI/PII handling flags carried from the node. | varchar / boolean / boolean |
    | `confidence_score` | Confidence score from `person_id_gold`. | double |

??? example "person_identifier_gold_current — slim convenience view"

    A trimmed selection of `person_identifier_gold` for day-to-day analyst queries.

    | Column | Description | Type |
    |---|---|---|
    | `person_id` | Resolved person. | bigint |
    | `id_type` | Identifier type. | varchar |
    | `id_value` | Identifier value. | varchar |
    | `source_system` | Originating source. | varchar |
    | `valid_start` | When this attachment was first observed. | timestamp |
    | `node_role` | Role of this identifier in the person's identity. | varchar |
    | `confidence_score` | Confidence from `person_id_gold`. | double |

??? example "person_identifier_gold_history — full attachment history"

    Every identifier ever attached to a person, with derived `is_current` flag. Use this when detached or merged-away identifiers matter.

    !!! warning "Column names differ from the current-state views"
        This table uses `identity_type_id` / `identity_id` rather than `id_type` / `id_value`. Don't try to UNION it against the `_current` views without aliasing.

    | Column | Description | Type |
    |---|---|---|
    | `person_id` | Resolved person. | bigint |
    | `pat_id` | The SSID node (Epic PAT or CDW PATIENT) the identifier was attached to. | varchar |
    | `identity_type_id` | Identifier type. | varchar |
    | `identity_id` | Identifier value. | varchar |
    | `first_attached_date` | First observed attachment. | date |
    | `last_event_date` | Most recent event date. | date |
    | `last_event_type` | `ATTACH` or `DETACH`. | varchar |
    | `is_current` | TRUE if `last_event_type = 'ATTACH'`. | boolean |
    | `source_system` | Originating source. | varchar |
    | `last_updated_at` | Detection timestamp of the most recent event. | timestamp |

### Merge tracking

??? example "person_merge_history_gold — Epic PAT-merge events at the person layer"

    One row per Epic PAT-merge event projected to the `person_id` layer.

    | Column | Description | Type |
    |---|---|---|
    | `merge_history_id` | Stable identifier for this merge event (from upstream `edge_id`). | varchar |
    | `superseded_person_id` | The `person_id` of the merged-away patient. | bigint |
    | `surviving_person_id` | The `person_id` of the post-merge surviving patient. | bigint |
    | `merge_reason` | Reason recorded with the merge event. | varchar |
    | `merged_at` | When the merge was detected by change-detection. | timestamp |
    | `snapshot_date` | Pipeline snapshot in which this merge first appeared. | date |

    !!! tip "Use OR across both ID columns when filtering by cohort"
        Filter as `WHERE surviving_person_id IN (...) OR superseded_person_id IN (...)` to capture merges where the cohort patient was the *source* of the merge, not just the survivor.

### Source status

??? example "person_ssid_source_status — per-source status of each SSID"

    Per-source-system status of each top-level patient identifier (SSID). Useful for tracing merge chains and diagnosing why a patient surfaces under multiple SSIDs.

    | Column | Description | Type |
    |---|---|---|
    | `node_id` | Identifier node hash. | varchar |
    | `person_id` | Resolved person (NULL if the node is quarantined). | bigint |
    | `node_role` | Role from `person_identity_link_gold`. | varchar |
    | `canonical_id_type` | `EPIC::PAT_ID[SSID]`, `CDW::PATIENT_ID[SSID]`, etc. | varchar |
    | `ssid_value` | The SSID value itself. | varchar |
    | `source_system` | `EPIC`, `CDW`, etc. | varchar |
    | `is_active_in_source` | TRUE if the SSID is still active in its origin system. | boolean |
    | `is_merged_away` | TRUE if this SSID was merged into another. | boolean |
    | `deactivation_reason` | Why the SSID is no longer active (when applicable). | varchar |
    | `survivor_ssid_value` | The surviving SSID at the end of the merge chain. | varchar |
    | `survivor_node_id` | Node hash of the surviving SSID. | varchar |
    | `merge_chain_depth` | Number of merge hops to reach the surviving SSID. 0 = this row IS the survivor. | integer |
    | `first_seen_datetime` | When this SSID was first observed. | timestamp |

### Governance

??? example "person_quarantine_gold — unresolved components"

    Components that could not be cleanly resolved to a single `person_id`, typically due to contradictory evidence in the graph (e.g., two Epic PATs that aren't linked by a merge but share a high-authority identifier).

    !!! danger "These rows have no `person_id`"
        Quarantined components are held back from `person_id` assignment and do not appear in any of the other gold tables. Use `component_id` to identify them.

    | Column | Description | Type |
    |---|---|---|
    | `component_id` | Identifier of the unresolved component. | varchar |
    | `quarantine_reason` | Why the component was quarantined. | varchar |
    | `competing_person_id_count` | How many candidate `person_id`s the algorithm could not pick between. | integer |
    | `competing_person_ids_json` | JSON array of the candidate `person_id`s. | varchar |
    | `has_epic_merge` | TRUE if at least one Epic merge edge appears in the component. | boolean |
    | `node_count` | Total nodes in the component. | bigint |
    | `ssid_count` | Number of top-level SSID nodes in the component. | bigint |
    | `first_quarantined_at` | First clustering run in which this component was quarantined. | timestamp |
    | `last_updated_at` | Most recent run that re-evaluated this component. | timestamp |
    | `snapshot_date` | Pipeline snapshot the row reflects. | date |

---

[:octicons-arrow-right-24: Query Patterns](Query%20Patterns.md){ .md-button .md-button--primary }

## Related Pages

- [:octicons-arrow-right-24: Query Patterns](Query%20Patterns.md) — example SQL for common identity lookups
- [:octicons-arrow-right-24: Pipeline Overview](../Pipeline%20Overview.md) — Bronze → Silver → Clustering → Gold
- [:octicons-arrow-right-24: Clustering](../Clustering/index.md) — how `person_id` is assigned
