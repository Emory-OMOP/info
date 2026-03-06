---
hide:
  - footer
title: "Release Notes — v0.2.4"
---

# v0.2.4 — August 2025

*Patch release | CDM v5.4*

### Summary

Final v0.2.x patch — migrated development to the `emory_omop_enterprise` repository and established CI/CD infrastructure for production deployment.

### Changes

- **Repository migration** — consolidated all dbt projects, stored procedures, and pipeline code into the new `emory_omop_enterprise` monorepo
- **CI/CD pipeline** — GitHub Actions workflows for dbt docs deployment to GitHub Pages and Airflow server synchronization
- **Production profiles** — `prod_ec2_role` configuration added to dbt profiles for IAM-based production deployment
- **Stored procedure parameterization** — refactored stored procedures to accept schema parameters, enabling multi-environment execution
- **Redshift optimization** — added SORTKEY directives to stored procedures for improved query performance
- **Vocabulary ingestion project** — initial `EmoryOMOPVocabulariesIngest` dbt project for loading vocabulary tables from S3
- **Patient ingest project** — initial `EmoryPatientIngest` dbt project structure for centralized patient demographic ingestion
