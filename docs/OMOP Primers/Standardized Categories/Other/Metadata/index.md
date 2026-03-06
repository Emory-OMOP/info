---
hide:
  - footer
title: Metadata
---

# Standardized Metadata

The OMOP CDM includes metadata tables (`cdm_source`, `metadata`) that describe the dataset itself — versioning, data refresh dates, vocabulary version, and ETL provenance.

At Emory, `cdm_source` captures the Enterprise OMOP release version, source data coverage dates, and the OMOP vocabulary version used. This is useful for documenting which data snapshot your study used.

!!! info "Check the release version"
    Always note the `cdm_source` version when publishing results. See our [Releases](../../../../Data%20in%20Enterprise%20OMOP/Releases/index.md) page for version history and changelogs.
