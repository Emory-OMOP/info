---
hide:
  - footer
title: Query Patterns
---

# Query Patterns

*Released in v1.0.0 — snapshot 2026-03-31*

Common patterns for querying `emory_identity_gold`. All examples target Athena / Trino SQL.

## Find a person from a known identifier

You have an MRN, EMPI, or other identifier value, and you want the canonical `person_id`:

```sql
SELECT person_id, id_type, id_value, source_system
FROM emory_identity_gold.person_identifier_gold_current
WHERE id_value = '<the value>'
  AND id_type = '<EPIC::914 or CDW::EMPI or whichever>';
```

!!! tip "Always filter on `id_type` as well as `id_value`"
    Different identifier types may share values across systems. The `id_type` strings follow `<SOURCE>::<TYPE>` — e.g., `EPIC::PAT_ID[SSID]`, `EPIC::914` (EMPI), `CDW::EMPI`. To discover what types exist in your data, run `SELECT DISTINCT id_type FROM person_identifier_gold_current` first.

## List all current identifiers for a person

You have a `person_id` and want every currently-attached identifier:

```sql
SELECT id_type, id_value, source_system, node_role, valid_start
FROM emory_identity_gold.person_identifier_gold_current
WHERE person_id = <X>
ORDER BY source_system, id_type;
```

The `node_role` column tells you how each identifier participates in the person's identity: `PRIMARY_PAT_ID` is the active Epic PAT; `MERGED_PAT_ID` rows indicate PATs that were merged into the primary; `IDENTIFIER_NODE` is everything else.

## Show the full identifier history (including detached)

Same intent as above, but you also want identifiers that were once attached and have since been detached or merged away:

```sql
SELECT identity_type_id, identity_id, source_system,
       first_attached_date, last_event_date, last_event_type, is_current
FROM emory_identity_gold.person_identifier_gold_history
WHERE person_id = <X>
ORDER BY first_attached_date;
```

`is_current = TRUE` when the most recent event for that identifier was an `ATTACH`. Note the column rename from the current-state view: `identity_type_id` / `identity_id` here, vs. `id_type` / `id_value` in `person_identifier_gold_current`.

## Trace a merge in Epic

Find every Epic PAT-merge event that touches a patient cohort:

```sql
SELECT superseded_person_id, surviving_person_id,
       merge_reason, merged_at, snapshot_date
FROM emory_identity_gold.person_merge_history_gold
WHERE surviving_person_id IN (<your cohort>)
   OR superseded_person_id IN (<your cohort>);
```

The `OR` matters — without it you would miss merges where the cohort patient was the *source* of the merge rather than the survivor.

## Resolve an Epic PAT_ID with merge handling

You have an Epic PAT_ID and want the resolved `person_id`, plus the surviving PAT_ID at the end of any merge chain:

```sql
SELECT ssid_value AS pat_id,
       person_id AS resolved_person_id,
       is_merged_away,
       survivor_ssid_value AS surviving_pat_id,
       merge_chain_depth
FROM emory_identity_gold.person_ssid_source_status
WHERE ssid_value = '<the PAT_ID>'
  AND canonical_id_type = 'EPIC::PAT_ID[SSID]';
```

`merge_chain_depth` tells you how many merge hops were traversed to reach the surviving PAT. A depth of 0 means this PAT is itself the survivor; depth ≥ 1 means it was merged away at some point.

## Inspect quarantined components

Quarantined components don't appear in `person_id_gold` or any of the analyst views — they have no `person_id`. To audit them:

```sql
SELECT component_id, quarantine_reason,
       competing_person_id_count, competing_person_ids_json,
       has_epic_merge, node_count, ssid_count, snapshot_date
FROM emory_identity_gold.person_quarantine_gold
ORDER BY competing_person_id_count DESC
LIMIT 50;
```

`competing_person_ids_json` is a JSON array of the candidate `person_id`s the clustering algorithm could not pick between. High-`competing_person_id_count` rows are the most useful starting points for a manual identity review.

---

[:octicons-arrow-left-24: Gold tables](index.md) · [:octicons-arrow-up-24: Pipeline Overview](../Pipeline%20Overview.md)
