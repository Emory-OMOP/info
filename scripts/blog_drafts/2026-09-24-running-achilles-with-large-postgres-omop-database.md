---
date: 2026-09-24
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Running ACHILLES with large postgres OMOP database

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/running-achilles-with-large-postgres-omop-database/26045)
**Matched keywords**: OMOP

I had asked this in the “General” forum, but that was likely not the best forum
Achilles on Postgres — analysis 117 extremely slow, Query drops silently, numThreads fails - #2 by schuemie
Issue:
For our large OMOP, Achilles run from the R code is failing for us - long queries in our postgres database
My question:
It is my understanding that we can do this:

Run Achilles with the “sqlonly” parameter that will generate all achilles.sql for our database type (postgres)
We can then simply run that e

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/running-achilles-with-large-postgres-omop-database/26045){.md-button}
