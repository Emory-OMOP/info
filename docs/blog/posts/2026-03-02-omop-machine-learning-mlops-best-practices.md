---
date: 2026-03-02
promoted: true
authors:
  - dsmith
categories:
  - Community
tags:
  - ohdsi
  - machine-learning
  - mlops
---

# Best Practices for Coupling OMOP with Machine Learning Metadata

An active OHDSI community discussion on how to store ML model predictions and versioning metadata alongside clinical data in OMOP. This is a frontier question for any team building predictive models on OMOP data.

<!-- more -->

## The challenge

As organizations "OMOPize" their data for ML pipelines, a practical question emerges: where do model outputs (predictions, confidence scores, model versions) live in the CDM? Standard OMOP tables weren't designed for ML metadata, but researchers need predictions linked back to patients and visits.

Current approaches being discussed include:

- Storing predictions in the **Observation** or **Measurement** tables with custom concepts
- Using **MLCroissant** for dataset-level metadata alongside OMOP for patient-level data
- Extending the CDM with custom tables for model provenance

## Why this matters

Emory researchers building predictive models on OMOP data will face this exact design decision. Following community consensus early avoids rework when OHDSI formalizes standards.

[:octicons-link-external-24: Join the discussion on OHDSI Forums](https://forums.ohdsi.org/t/best-practices-for-coupling-omop-with-machine-learning-metadata-for-mlops/25051){.md-button}
