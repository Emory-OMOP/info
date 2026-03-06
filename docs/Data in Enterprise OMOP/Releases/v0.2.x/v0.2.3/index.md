---
hide:
  - footer
title: "Release Notes — v0.2.3"
---

# v0.2.3 — July 2025

*Patch release | CDM v5.4*

### Summary

Data quality assessment and exploratory analysis across clinical tables, with initial subsample infrastructure for reproducible testing.

### Changes

- **Concept mapping assessment** — systematic review of concept mapping coverage across all tables, including top-10 concept analysis and non-zero mapping rates
- **Subsample creation** — created representative patient subsamples from Epic and CDW for unit testing and QA validation
- **Drug exposure EDA** — completed exploratory data analysis for ambulatory, anesthesia, and hospital drug exposure records
- **Procedure occurrence EDA rerun** — refreshed procedure analysis with updated data
- **Drug exposure final table EDA** — comprehensive review of the merged drug_exposure table
- **Deident_driver update** — updated de-identification driver with deduplicated patient set
- **QA documentation** — improved internal QA documentation structure
