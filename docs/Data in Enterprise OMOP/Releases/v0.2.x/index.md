---
hide:
  - footer
title: "Release Notes — v0.2.x"
---

# v0.2.x — April–August 2025

The v0.2.x series was the first community-facing release of Emory Enterprise OMOP. It introduced Epic ETL integration alongside the existing CDW pipeline, established the DBT test suite, and iterated through four monthly patches addressing data quality, vocabulary updates, and QA automation.

## Releases

| Version | Date | Summary |
|---------|------|---------|
| [v0.2.0](#v020-april-2025) | April 2025 | Initial community release |
| [v0.2.1](v0.2.1/index.md) | May 2025 | Deduplication fixes, QA automation |
| [v0.2.2](v0.2.2/index.md) | June 2025 | Vocabulary updates, Redshift reloads |
| [v0.2.3](v0.2.3/index.md) | July 2025 | Concept mapping assessment, EDA reviews |
| [v0.2.4](v0.2.4/index.md) | August 2025 | Repository migration, CI/CD setup |

---

## v0.2.0 — April 2025

*Initial community release | CDM v5.4 | Vocabulary v5.0*

The first release made available to the Emory research community, marking the transition from internal development to supported production use.

### Highlights

- **Epic ETL integration** — Epic EHR data brought into the OMOP pipeline alongside CDW, producing a unified Enterprise dataset
- **CDM v5.3.1 → v5.4 migration** — schema updates to align with the latest OHDSI Common Data Model specification
- **DBT test suite** — column-level tests (not_null, unique, FK referential integrity, domain validation) established across all clinical tables
- **Provider deduplication** — initial CDW/Epic provider matching using NPI where available
- **Vocabulary reload** — full vocabulary refresh including CPT4 jar processing
- **Oncology readiness patch** — schema preparation for Winship Cancer Institute use cases

### Bug Fixes

- Corrected `condition_status` mapping from type concept to status concept
- Fixed `source_to_concept_map` incorrectly routed to `omop_etl_epic`
- Resolved person duplicates associated with location assignments
- Fixed One Florida LOINC code errors
- Resolved empty `care_site` table for Epic source

### Data Quality

- DBT test failures resolved for condition_occurrence, drug_exposure, measurement, death, person, provider, and visit tables
- Person, visit_occurrence, care_site, and measurement deduplication across Epic source
- Exploratory data analysis (EDA) completed for condition_occurrence, procedure_occurrence, person, care_site, and drug_exposure
