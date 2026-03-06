---
hide:
  - footer
title: Clinical Data
---

# Clinical Data

These are the tables you'll query most. Each captures a different domain of patient-level clinical data — the OMOP equivalent of what you'd find across Clarity's diagnosis, medication, lab, procedure, and encounter tables.

!!! tip "Start with these five"
    Most research projects use `person`, `visit_occurrence`, `condition_occurrence`, `drug_exposure`, and `measurement`. Everything else builds on that foundation.

## Core Tables

<div class="grid cards" markdown>

-   :material-account:{ .lg .middle } **Person**

    ---

    One row per patient. Demographics, birth date, race, ethnicity. The center of the OMOP universe.

    [:octicons-arrow-right-24: Person](Person/index.md){ .md-button }

-   :material-hospital-box:{ .lg .middle } **Visit Occurrence**

    ---

    Encounters — inpatient, outpatient, ER, telehealth. The OMOP equivalent of Epic's encounter table.

    [:octicons-arrow-right-24: Visit Occurrence](Visits/Visit%20Occurrence/index.md){ .md-button }

-   :material-hospital-box-outline:{ .lg .middle } **Visit Detail**

    ---

    Sub-encounter segments: ICU stays, department transfers, ADT events within a broader visit.

    [:octicons-arrow-right-24: Visit Detail](Visits/Visit%20Detail/index.md){ .md-button }

-   :material-stethoscope:{ .lg .middle } **Condition Occurrence**

    ---

    Diagnoses and problems. Maps to encounter diagnoses and problem list entries from Epic.

    [:octicons-arrow-right-24: Condition Occurrence](Conditions/Condition%20Occurrence/index.md){ .md-button }

-   :material-pill:{ .lg .middle } **Drug Exposure**

    ---

    Medication orders, administrations (MAR), prescriptions, and pharmacy data.

    [:octicons-arrow-right-24: Drug Exposure](Drugs/Drug%20Exposure/index.md){ .md-button }

-   :material-test-tube:{ .lg .middle } **Measurement**

    ---

    Lab results and vital signs — A1c, hemoglobin, blood pressure, creatinine, and more. All in one table.

    [:octicons-arrow-right-24: Measurement](Measurement/index.md){ .md-button }

-   :material-eye:{ .lg .middle } **Observation**

    ---

    The catch-all for clinical facts that don't fit elsewhere: smoking status, social determinants, screening responses, patient-reported outcomes.

    [:octicons-arrow-right-24: Observation](Observation/index.md){ .md-button }

-   :material-medical-bag:{ .lg .middle } **Procedure Occurrence**

    ---

    Surgeries, imaging orders, vaccinations, interventional procedures. Maps to Epic procedure orders and surgical case records.

    [:octicons-arrow-right-24: Procedure Occurrence](Procedure%20Occurrence/index.md){ .md-button }

</div>

## Additional Clinical Tables

<div class="grid cards" markdown>

-   :material-skull-crossbones:{ .lg .middle } **Death**

    ---

    Mortality data from EHR discharge records and state death indices.

    [:octicons-arrow-right-24: Death](Death/index.md){ .md-button }

-   :material-cellphone-link:{ .lg .middle } **Device Exposure**

    ---

    Medical devices: pacemakers, catheters, implants, glucose monitors. Often sparse in EHR-derived OMOP.

    [:octicons-arrow-right-24: Device Exposure](Device%20Exposure/index.md){ .md-button }

-   :material-file-document:{ .lg .middle } **Note / Note NLP**

    ---

    Unstructured clinical text (progress notes, discharge summaries, radiology reports) and NLP-extracted entities.

    [:octicons-arrow-right-24: Note](Notes/Note/index.md){ .md-button } [:octicons-arrow-right-24: Note NLP](Notes/Note%20NLP/index.md){ .md-button }

-   :material-flask:{ .lg .middle } **Specimen**

    ---

    Biological samples: blood, tissue, urine. Linked to Winship's OpenSpecimen biobank at Emory.

    [:octicons-arrow-right-24: Specimen](Specimen/index.md){ .md-button }

-   :material-link-variant:{ .lg .middle } **Fact Relationship**

    ---

    Cross-domain links: connecting a biopsy procedure to its pathology result, or a pregnancy diagnosis to a delivery.

    [:octicons-arrow-right-24: Fact Relationship](Fact%20Relationship/index.md){ .md-button }

</div>

## Derived Elements

These tables are computed from the raw clinical tables above — they aggregate events into clinically meaningful periods.

<div class="grid cards" markdown>

-   :material-chart-timeline:{ .lg .middle } **Condition Era**

    ---

    Continuous periods of a diagnosis, aggregated from `condition_occurrence` using gap logic (default 30-day window).

    [:octicons-arrow-right-24: Condition Era](Conditions/Derived%20-%20Condition%20Era/index.md){ .md-button }

-   :material-chart-timeline-variant:{ .lg .middle } **Drug Era / Dose Era**

    ---

    Continuous medication exposure periods and consistent-dose periods, derived from `drug_exposure`.

    [:octicons-arrow-right-24: Drug Era](Drugs/Derived/Drug%20Era/index.md){ .md-button } [:octicons-arrow-right-24: Dose Era](Drugs/Derived/Dose%20Era/index.md){ .md-button }

-   :material-calendar-range:{ .lg .middle } **Episode / Episode Event**

    ---

    Higher-level clinical constructs: treatment regimens, pregnancy episodes, disease courses. Explicitly curated during ETL or by researchers.

    [:octicons-arrow-right-24: Episode](Episodes/Episode/index.md){ .md-button } [:octicons-arrow-right-24: Episode Event](Episodes/Episode%20Event/index.md){ .md-button }

</div>
