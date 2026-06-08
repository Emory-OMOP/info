---
date: 2026-05-12
categories:
  - OHDSI
tags:
  - ohdsi
  - community
authors:
  - dsmith
---

# Introducing Alathea - a tool that tracks changes in cohorts due to vocabulary update

An R package that flags how a cohort's resolved membership shifts
across OMOP vocabulary versions — the same source codes can map
differently as the hierarchy and standard-concept status change.
Directly relevant as we refresh vocabularies and need cohort
definitions to stay stable across releases.

<!-- more -->

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/introducing-alathea-a-tool-that-tracks-changes-in-cohorts-due-to-vocabulary-update/25360)
**Matched keywords**: OHDSI

Alathea is an R package that tracks changes to the Cohort definition resolution depending on the vocabulary version it’s run on (assuming the CDM is made on the same vocabulary version).
Same medical events (source codes) can be mapped differently in different vocabulary versions,
Concept hierarchy can be changed
Concept Domain can be changed as well as the standard status.
Due to these changes different medical events might define your cohort in different vocabularu versions.
Usually changes ar

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/introducing-alathea-a-tool-that-tracks-changes-in-cohorts-due-to-vocabulary-update/25360){.md-button}
