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
| [v0.2.1](#v021-may-2025) | May 2025 | Deduplication fixes, QA automation |
| [v0.2.2](#v022-june-2025) | June 2025 | Vocabulary updates, Redshift reloads |
| [v0.2.3](#v023-july-2025) | July 2025 | Concept mapping assessment, EDA reviews |
| [v0.2.4](#v024-august-2025) | August 2025 | Repository migration, CI/CD setup |

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

---

## v0.2.1 — May 2025

*Patch release | CDM v5.4*

Focused on QA automation and resolving deduplication issues identified during the v0.2.0 community rollout.

### Changes

- **QA automation** — automated QA pipelines for person and visit_occurrence tables, replacing manual review workflows
- **Deduplication fixes** — resolved remaining person, measurement, care_site, and visit_occurrence duplicates surfaced by community users
- **Condition status mapping** — completed correction for `condition_status_concept_id` mapping (started in v0.2.0)
- **CDM v5.4 completion** — finalized remaining schema changes from the 5.3.1 → 5.4 migration
- **Patient data representation** — investigated and resolved inconsistencies in patient data across tables
- **Measurement source unit truncation** — investigated and addressed unit value truncation in source data

---

## v0.2.2 — June 2025

*Patch release | CDM v5.4 | Vocabulary v5.0*

Vocabulary infrastructure updates and full Redshift reloads for both Epic and Enterprise datasets.

### Changes

- **Vocabulary CPT4 jar processing** — completed CPT4 vocabulary jar run for updated procedure mappings
- **Vocabulary reload** — refreshed vocabulary tables with latest OHDSI release
- **`source_to_concept_map` fix** — corrected table routing that was incorrectly pointing to `omop_etl_epic`
- **CDW vocabulary delta check** — reran CDW pipeline with new vocabularies to assess mapping changes
- **Enterprise Redshift reload** — full reload of the enterprise dataset incorporating all accumulated fixes
- **Epic Redshift reload** — full reload of Epic dataset with updated vocabulary mappings
- **DBT test review** — reviewed and resolved breaking tests introduced by new Epic and Enterprise loads

---

## v0.2.3 — July 2025

*Patch release | CDM v5.4*

Data quality assessment and exploratory analysis across clinical tables, with initial subsample infrastructure for reproducible testing.

### Changes

- **Concept mapping assessment** — systematic review of concept mapping coverage across all tables, including top-10 concept analysis and non-zero mapping rates
- **Subsample creation** — created representative patient subsamples from Epic and CDW for unit testing and QA validation
- **Drug exposure EDA** — completed exploratory data analysis for ambulatory, anesthesia, and hospital drug exposure records
- **Procedure occurrence EDA rerun** — refreshed procedure analysis with updated data
- **Drug exposure final table EDA** — comprehensive review of the merged drug_exposure table
- **Deident_driver update** — updated de-identification driver with deduplicated patient set
- **QA documentation** — improved internal QA documentation structure

---

## v0.2.4 — August 2025

*Patch release | CDM v5.4*

Final v0.2.x patch — migrated development to the `emory_omop_enterprise` repository and established CI/CD infrastructure for production deployment.

### Changes

- **Repository migration** — consolidated all dbt projects, stored procedures, and pipeline code into the new `emory_omop_enterprise` monorepo
- **CI/CD pipeline** — GitHub Actions workflows for dbt docs deployment to GitHub Pages and Airflow server synchronization
- **Production profiles** — `prod_ec2_role` configuration added to dbt profiles for IAM-based production deployment
- **Stored procedure parameterization** — refactored stored procedures to accept schema parameters, enabling multi-environment execution
- **Redshift optimization** — added SORTKEY directives to stored procedures for improved query performance
- **Vocabulary ingestion project** — initial `EmoryOMOPVocabulariesIngest` dbt project for loading vocabulary tables from S3
- **Patient ingest project** — initial `EmoryPatientIngest` dbt project structure for centralized patient demographic ingestion
