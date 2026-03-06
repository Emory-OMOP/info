---
hide:
  - footer
title: Convention Adherence
---

# Convention Adherence

This page tracks Emory's adherence to OHDSI's published conventions for the OMOP Common Data Model. Where gaps exist, they are documented with context and remediation status.

## General CDM Conventions

Emory follows the [General CDM Conventions](https://ohdsi.github.io/CommonDataModel/dataModelConventions.html) as of April 2025. The following known deviations have been identified:

???+ warning "Units not standardized within tables"

    **Convention**: For a given `{table}_concept_id`, the associated unit should be consistent across all observations (e.g., all hemoglobin measurements should use the same `unit_concept_id`).

    **Current state**: Units are not standardized within a table for a particular concept. For example, `measurement.unit_concept_id` for a hemoglobin measurement may differ across observations; `drug_exposure.unit_concept_id` for aspirin may differ across observations.

    **Impact**: Affects `measurement`, `drug_exposure`, and `dose_era` tables. See [:octicons-arrow-right-24: Known Issues](../../Data%20Quality/Known%20Issues/index.md) for table-specific guidance.

    **Remediation**: Under investigation for a future release.

## THEMIS Conventions

Emory follows the [THEMIS Convention Library](https://ohdsi.github.io/Themis/) to the extent known. A systematic audit of THEMIS convention adherence has not yet been completed.

!!! info "Work in progress"
    A full THEMIS adherence review is planned. This page will be updated as conventions are audited and gaps are documented.

## Related Pages

- [:octicons-arrow-right-24: OHDSI Conventions](../OHDSI%20Conventions/index.md) — community convention resources and references
- [:octicons-arrow-right-24: Emory Conventions](../Emory%20Conventions/index.md) — Emory-specific additions to the CDM
- [:octicons-arrow-right-24: Known Issues](../../Data%20Quality/Known%20Issues/index.md) — table-by-table quality issues and workarounds
