---
hide:
  - footer
title: Metadata & Results
---

# Metadata & Results

Beyond the clinical and reference categories, the OMOP CDM includes two small housekeeping groups: **metadata** tables that describe the dataset itself, and **results** tables that store analysis output alongside the clinical data.

## Standardized Metadata

The OMOP CDM includes metadata tables (`cdm_source`, `metadata`) that describe the dataset itself — versioning, data refresh dates, vocabulary version, and ETL provenance.

At Emory, `cdm_source` captures the Enterprise OMOP release version, source data coverage dates, and the OMOP vocabulary version used. This is useful for documenting which data snapshot your study used.

!!! info "Check the release version"
    Always note the `cdm_source` version when publishing results. See our [Releases](../../../Data%20in%20Enterprise%20OMOP/Releases/index.md) page for version history and changelogs.

## Standardized Results

The OMOP CDM includes tables for storing **analysis results** alongside the clinical data — primarily `cohort` and `cohort_definition`. These tables hold the output of phenotyping algorithms, cohort definitions built in ATLAS, and other derived patient sets.

At Emory, cohort results from ATLAS are stored in the results schema. If you're building cohorts via SQL or ATLAS, the output lands here.

!!! tip "Working with cohorts?"
    See our [ATLAS Training](../../../Training/Emory/ATLAS/index.md) for how to build and export cohort definitions at Emory.
