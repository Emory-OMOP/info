---
hide:
  - footer
title: "Release Notes — v1.0.0"
---

# v1.0.0 — March 2026

*271 commits | 3 contributors | CDM v5.4 | Vocabulary v5.0 (Feb 2025)*

## What's New for Researchers

### Stable Patient Identities

Patient identifiers (`person_id`) are now **stable across data loads**. Previously, person IDs could shift between ETL runs as new data arrived. The new identity stabilization system uses graph-based clustering to resolve patients across CDW and Epic sources, ensuring that a `person_id` assigned today remains the same in future releases.

**What this means for you:**

- Longitudinal studies can safely reference `person_id` across data refreshes
- Patient cohorts built in ATLAS or SQL will not silently break between loads
- Cross-source patient matching (CDW + Epic) is now systematically resolved rather than heuristic

### HIPAA-Compliant De-identification

Location and care site data now follows Safe Harbor de-identification standards:

- **Patient addresses** are reduced to ZIP3 (first 3 digits only)
- **Care site names** and source values are masked
- **Facility addresses** are preserved at full granularity (publicly available information)
- **Latitude/longitude** values are removed for person-linked locations
- International addresses receive additional suppression

### Improved Data Quality Infrastructure

- **Cross-project subsampling** — a new testing paradigm lets the team validate ETL changes against representative patient subsets before full production runs
- **Safety guards** prevent accidental subsample execution against production data
- **Mock production mode** enables zero-row validation of pipeline logic across all dbt projects

### Vocabulary Updates

- Vocabulary tables reloaded with v5.0 (February 2025)
- CPT4 vocabulary jar processing completed
- `source_to_concept_map` table structure updated with additional fields
- Athena partitioning switched from date to year/month for improved query performance

### ETL Fixes

- Corrected Epic identity type mapping (14 → 914)
- Provider model refactored with COALESCE-based merging (Epic priority)
- Fixed race and gender concept ID test conditions across projects
- Resolved duplicate person records linked to location assignments
- Increased `address_1` field to 255 characters

---

## Technical Changelog

??? abstract "Patient Identity Stabilization (~80 commits)"

    **New dbt project**: `EmoryPatientIdentityStabilization`

    A ground-up identity resolution system built on graph-based clustering. Resolves patient identities across CDW and Epic sources using connected components analysis.

    **Architecture**:

    - **Bronze layer** — raw intake of identity evidence from CDW and Epic
    - **Silver layer** — change detection, edge construction, delta event tracking
    - **Gold layer** — resolved person identifiers, stable across loads
    - **Clustering layer** — Python connected components algorithm against Redshift/Athena

    **Key components**:

    - `identity_id_delta_events` — tracks identity changes over time
    - `epic_pat_merge_events` / `epic_pat_identity_events` — Epic-specific identity event models
    - `run_connected_components.py` — graph clustering pipeline
    - `identity_graph_clustering.py` — core clustering algorithm
    - Fellegi-Sunter match weight scoring for linkage quality assessment
    - SSID tracer diagnostic tool for step-by-step identity tracing
    - Evidence intake pipeline with QC, conflict detection, and clustering integration
    - Merge/unmerge tracking and cluster stability monitoring

    **Testing**:

    - Comprehensive seed-based unit testing with `get_source` macro for test vs. production routing
    - Test cases for AUTHORITY_WINS, re-attach events, merge evidence scenarios
    - `run_unit_test_pipeline.py` orchestrator

    **Documentation**: 20-section project documentation covering design principles, architecture, glossary, operational procedures, and known limitations.

    **Versioned internally**: v0.3.0 → v0.4.0 → v0.5.0 (no git tags)

??? abstract "Patient Ingest Pipeline (~15 commits)"

    **New dbt project**: `EmoryPatientIngest`

    Centralizes patient demographic ingestion, replacing the legacy `deident_driver` approach.

    - `identity_person_map` model backed by identity stabilization gold layer
    - `patient_exclusions` model filtering new Epic IDs that would reuse existing person_ids
    - Deterministic person_id assignment using `GREATEST(MAX(person_id))` for incremental runs
    - Deduplication and quarantine handling for duplicate identity_person_map rows
    - `lkp_master_patient_rebuilt` model in CDW, integrated across Epic, PatientIngest, Identity Stabilization, and Enterprise projects

??? abstract "HIPAA De-identification (~35 commits)"

    **Stored procedures** for location and care site de-identification.

    **Location de-identification** (`sp_location_jz.sql`):

    - ZIP3 suppression for patient (non-facility) addresses
    - PII field removal (address lines, city, county)
    - Facility-level vs. non-facility differentiation based on care_site match
    - Latitude/longitude set to -88 for person-linked locations where original values were not null
    - Non-USA zip suppression with special handling
    - Schema refactoring to `admin` schema with parameterized `cdmDatabaseSchema`

    **Care site masking** (`sp_care_site_jz.sql`):

    - `care_site_name`, `care_site_source_value`, `place_of_service_source_value` masked with `**Emory Masked**`

    **QC** (`jz_qc_explore.sql`):

    - 12-validation-query test suite covering zip suppression, facility matching, anomaly detection

??? abstract "Cross-Project Subsampling (~20 commits)"

    **New dbt project**: `EmoryOmopSubsampling`

    - `subsample_filter` macro added to all dbt projects for conditional data filtering
    - `assert_subsample_target` safety guard preventing accidental subsample execution against production
    - `generate_schema_name` macro for dynamic schema naming (subsample vs. production)
    - `mock_prod` validation mode added to all projects for zero-row production verification
    - `empty_artifacts` profile target added to CDW, Identity Stabilization, and PatientIngest
    - Cross-project subsample pipeline orchestrator script

??? abstract "CI/CD & Infrastructure (~20 commits)"

    - **dbt docs deployment** — GitHub Actions workflow for building and deploying dbt documentation to GitHub Pages (multi-project support)
    - **Airflow sync** — GitHub Actions workflow to sync dbt projects to the Airflow server
    - **Export-to-parquet pipeline** — cross-account S3 and Redshift transfer for data export
    - `prod_ec2_role` configuration added to dbt profiles for production deployment via EC2 IAM roles
    - Dependabot security fix upgrading transitive dependencies (11 vulnerabilities resolved)

??? abstract "Vocabulary Ingestion (~5 commits)"

    **New dbt project**: `EmoryOMOPVocabulariesIngest`

    - dbt project for vocabulary table loading from S3
    - Stored procedure for CSV → Redshift loading
    - `drug_strength.sql` — datatype conversion (BIGINT), amount/numerator/denominator handling
    - `source_to_concept_map` — updated table structure with additional fields
    - Partitioning changed from date to year/month for Athena scale

??? abstract "ETL Bug Fixes & Data Quality (~15 commits)"

    - Epic identity type corrected from 14 to 914; excluded CDW facility MRNs from clustering
    - Provider model refactored with COALESCE-based merging (Epic priority)
    - `race_concept_id` and `gender_concept_id` test conditions fixed across multiple projects
    - CDW stage model: added `DISTINCT` for `qualifier_new` in `array_agg`
    - Discrepancy/impact models: `WHERE EXISTS` instead of `INNER JOIN`, dedup with `DISTINCT`, scoped to rebuilt patient set
    - `location.address_1` increased to 255 characters; reordered state/zip assignments

??? abstract "Documentation & Project Management (~20 commits)"

    - DevOps philosophy documentation: hybrid DataOps framework, observability, SPC, team workflow guide
    - Identity Stabilization: 20-section project documentation
    - Glossary expansion with comprehensive internal terminology
    - LLM usage disclosure (Anthropic Claude transparency)
    - GitHub project board tooling: `set_pr_fields.sh`, `project_field_ids.csv`
    - Repository labels export (`repo_labels.csv`)

??? abstract "QA Investigation Scripts"

    - **Issue #320** — diagnostic queries for duplicate person_ids in Epic, filtering merged-away PAT records
    - **Issue #347** — Fellegi-Sunter scoring scripts, subsample validation, evidence pipeline match weights, identity_person_map CDW demographics join fix
    - **Issue #262** — lkp_master_patient model descriptions, duplicate patient_id fixes, discrepancy/impact model scoping
    - **Issue #264** — EmoryOmopCDW test infrastructure and pipeline configuration updates

---

## Contributors

| Contributor | Commits | Focus Areas |
|-------------|---------|-------------|
| Daniel Smith | 145 | Identity stabilization, infrastructure, subsampling, CI/CD |
| Jorge Marquez | 75 | ETL pipelines, stored procedures, vocabulary |
| Xueqiong Zhang | 51 | Location/care site de-identification, QC |
