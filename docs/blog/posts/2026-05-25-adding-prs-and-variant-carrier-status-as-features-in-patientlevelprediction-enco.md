---
date: 2026-05-25
categories:
  - OHDSI
tags:
  - ohdsi
  - community
authors:
  - dsmith
---

# Adding PRS and variant-carrier status as features in PatientLevelPrediction — encoding, leakage, and cross-ancestry calibration

An OHDSI PatientLevelPrediction thread on incorporating polygenic
risk scores and variant-carrier status as features — time-invariant,
off-platform covariates that break FeatureExtraction's assumptions.
Pertinent to genomics-informed prediction work.

<!-- more -->

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/adding-prs-and-variant-carrier-status-as-features-in-patientlevelprediction-encoding-leakage-and-cross-ancestry-calibration/25399)
**Matched keywords**: OMOP, OHDSI

With the PatientLevelPrediction workgroup picking back up, it seems worth opening a thread specifically on genetic covariates. PLP’s FeatureExtraction is built for time-varying clinical observations, but polygenic risk scores (PRS) and germline variant-carrier flags break several of those assumptions — they’re time-invariant, computed off-platform, and (in most networks) live outside the OMOP tables that FeatureExtraction reads from. A few questions where consensus would be useful:
1. Where do g

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/adding-prs-and-variant-carrier-status-as-features-in-patientlevelprediction-encoding-leakage-and-cross-ancestry-calibration/25399){.md-button}
