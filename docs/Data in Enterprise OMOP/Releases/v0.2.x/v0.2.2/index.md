---
hide:
  - footer
title: "Release Notes — v0.2.2"
---

# v0.2.2 — June 2025

*Patch release | CDM v5.4 | Vocabulary v5.0*

### Summary

Vocabulary infrastructure updates and full Redshift reloads for both Epic and Enterprise datasets.

### Changes

- **Vocabulary CPT4 jar processing** — completed CPT4 vocabulary jar run for updated procedure mappings
- **Vocabulary reload** — refreshed vocabulary tables with latest OHDSI release
- **`source_to_concept_map` fix** — corrected table routing that was incorrectly pointing to `omop_etl_epic`
- **CDW vocabulary delta check** — reran CDW pipeline with new vocabularies to assess mapping changes
- **Enterprise Redshift reload** — full reload of the enterprise dataset incorporating all accumulated fixes
- **Epic Redshift reload** — full reload of Epic dataset with updated vocabulary mappings
- **DBT test review** — reviewed and resolved breaking tests introduced by new Epic and Enterprise loads
