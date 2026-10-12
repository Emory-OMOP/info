---
date: 2026-09-18
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Is Synthea procedures.csv mapping to multiple OMOP tables  expected under domain-driven ETL?

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/is-synthea-procedures-csv-mapping-to-multiple-omop-tables-expected-under-domain-driven-etl/26001)
**Matched keywords**: OMOP

Hi everyone,
I’m building a domain-driven ETL from Synthea CSV to OMOP CDM and would like a sanity check on how procedure source rows should fan out across OMOP tables.
Context

Source: Synthea procedures.csv (15,884 rows in my run)
Approach: resolve each source CODE to standard concept via “Maps to”, then route each standard concept to the OMOP table matching its domain_id (Condition → condition_occurrence, Procedure → procedure_occurrence, Measurement → measurement, etc.)
This follows the guid

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/is-synthea-procedures-csv-mapping-to-multiple-omop-tables-expected-under-domain-driven-etl/26001){.md-button}
