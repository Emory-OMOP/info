---
hide:
  - footer
title: "Release Notes — v0.2.1"
---

# v0.2.1 — May 2025

*Patch release | CDM v5.4*

### Summary

Focused on QA automation and resolving deduplication issues identified during the v0.2.0 community rollout.

### Changes

- **QA automation** — automated QA pipelines for person and visit_occurrence tables, replacing manual review workflows
- **Deduplication fixes** — resolved remaining person, measurement, care_site, and visit_occurrence duplicates surfaced by community users
- **Condition status mapping** — completed correction for `condition_status_concept_id` mapping (started in v0.2.0)
- **CDM v5.4 completion** — finalized remaining schema changes from the 5.3.1 → 5.4 migration
- **Patient data representation** — investigated and resolved inconsistencies in patient data across tables
- **Measurement source unit truncation** — investigated and addressed unit value truncation in source data
