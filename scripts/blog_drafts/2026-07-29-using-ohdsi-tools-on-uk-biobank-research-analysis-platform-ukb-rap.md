---
date: 2026-07-29
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Using OHDSI tools on UK Biobank Research Analysis Platform (UKB-RAP)

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/using-ohdsi-tools-on-uk-biobank-research-analysis-platform-ukb-rap/25733)
**Matched keywords**: OMOP, OHDSI

Hi,
Has anyone successfully run OHDSI tooling (e.g., Achilles, CohortMethod) against UK Biobank’s OMOP CDM data on the Research Analysis Platform (RAP)?
As far as I understand, the OMOP tables on RAP are exposed via a Spark-backed database (dxdata/sparklyr, dx xtract_dataset), not a standard RDBMS. DatabaseConnector lists Spark as a supported dbms via JDBC, but I haven’t found confirmation that RAP’s Spark layer exposes an endpoint that external tools can connect to.
So, has anyone gotten Databa

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/using-ohdsi-tools-on-uk-biobank-research-analysis-platform-ukb-rap/25733){.md-button}
