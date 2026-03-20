---
hide:
  - footer
title: Subsampling ("Canaries")
---

# Subsampling ("Canaries")

Subsampling selects a small, fixed set of patients — typically 40 — who are tracked longitudinally across every pipeline run. The same individuals appear in every snapshot, every reload, every environment test. This is not test data. It is a **variance detection mechanism**.

Like canaries in a coal mine, these patients serve as early-warning sentinels. When the pipeline transforms the same 40 patients and produces different output than the last run, something changed. That change must be found and explained. Subsampling turns invisible pipeline drift into a visible, auditable signal.

## Design principles

**Immutability.** A subsample is frozen at creation. The same 40 person_ids are used indefinitely. Regenerating a subsample breaks longitudinal comparability and is treated as a major event requiring documented justification.

**Representativeness.** Patients are selected for data richness, not randomness. Each subsample patient must have clinical records across multiple domains (conditions, medications, measurements, visits, procedures) in both CDW and Epic source systems. This ensures the subsample exercises the full pipeline — every join, every transformation, every mapping.

**Determinism.** Patient selection uses xxhash64 ordering on person_id for reproducibility. Given the same input cohort, the same 40 patients are always selected.

**Variance as signal.** If a subsample run produces output that differs from the prior run for the same date range, that variance is not noise — it is a defect signal. Possible causes include:

- Upstream source data changed (new records, corrections, deletes)
- Pipeline logic changed (new transforms, bug fixes, mapping updates)
- Vocabulary updates (concept mappings shifted between loads)
- Identity resolution changes (person_id reassignment, merges)

Each cause has different implications. The subsample makes these visible before they reach production.

## Architecture

The subsampling system spans two layers:

**EmoryOmopSubsampling** generates the frozen patient lists:

- `person_data_representation` — flags indicating which clinical domains each patient has data in, across CDW and Epic
- `person_subsample` — the core 40-patient set (≥3 domains in both CDW and Epic)
- Disease-specific subsamples: `brain_health_subsample`, `winship_subsample`, `nursing_cohort`

**Downstream projects** (CDW, Epic, Enterprise, Identity, Ingest, BrainHealth, Winship, Nursing) consume the subsample via `--target subsample --vars '{"subsample": "omop_subsampling.person_subsample"}'`. The `cohort_person_filter` or equivalent model filters all clinical data to just the 40 patients. Every table in the pipeline is rebuilt for only those individuals.

## Target-based routing

Each dbt project supports multiple targets that control where output lands:

| Target | Schema | Purpose |
|--------|--------|---------|
| `prod` | project-specific (e.g., `omop_etl_cdw`) | Production pipeline |
| `dev` | project-specific dev schema | Development |
| `subsample` | `omop_subsampling` | Longitudinal variance testing |
| `mock_prod` | `omop_subsampling` | Structure testing with empty tables |
| `unit_test` | `omop_subsampling` | Deterministic tests with seed data |
| `network_study` | `omop_network` | Athena-only vocab resolution |

The `subsample` target:

- Collapses all output into the `omop_subsampling` schema
- Applies an alias prefix (e.g., `dbt__cdw__subsample__20260320__`) to avoid collisions
- Materializes reference tables (vocab, provider, care_site, location) as views instead of tables
- Filters clinical data through the subsample patient list

## What NOT to do

- **Never regenerate a subsample** without explicit direction and documented reason
- **Never delete subsample tables** — they are permanent reference data
- **Never assume variance is acceptable** — every difference between subsample runs must be investigated
- **Never use subsamples as disposable test data** — they are longitudinal tracking cohorts

## Subsample tables in `omop_subsampling`

Permanent (never delete):

- `person_subsample` — core 40-patient OMOP subsample
- `person_data_representation` — data richness flags
- `brain_health_subsample` — BrainHealth 40-patient subsample
- `nursing_cohort` — frozen 1M nursing cohort
- Disease-specific `*_subsample` and `*_data_representation` tables

Temporary (clean up after runs):

- `dbt__<project>__subsample__<date>__<model>` — downstream build artifacts
- These are rebuilt on every run and can be safely dropped after verification
