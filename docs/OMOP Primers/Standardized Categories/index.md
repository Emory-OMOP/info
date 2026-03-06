---
hide:
  - footer
title: Standardized Categories
---

# Standardized Categories

The OMOP CDM organizes tables into categories that match the color-coded regions on the CDM diagram. If you're coming from Epic, think of this as a re-organization of the same clinical data you already know — just structured around patients instead of encounters.

!!! note "Person-centric, not encounter-centric"
    In Epic, you navigate from encounters to data. In OMOP, you navigate from patients to data. Encounters (`visit_occurrence`) are one of many tables linked to `person` — not the organizing spine.

<div class="grid cards" markdown>

-   :material-heart-pulse:{ .lg .middle } **Clinical Data**

    ---

    The core research tables. Conditions, drugs, measurements, procedures, visits, observations, notes, devices, specimens, and derived elements (eras, episodes).

    [:octicons-arrow-right-24: Clinical Data](Clinical%20Data/index.md){ .md-button }

-   :material-hospital-building:{ .lg .middle } **Health System**

    ---

    Where care happens and who delivers it: providers, care sites, and geographic locations.

    [:octicons-arrow-right-24: Health System](Health%20System/index.md){ .md-button }

-   :material-book-open-variant:{ .lg .middle } **Vocabularies**

    ---

    The mapping layer under everything — how ICD, CPT, NDC, and local codes translate to standard OMOP concepts. If you only learn one thing beyond the clinical tables, learn this.

    [:octicons-arrow-right-24: Vocabularies](Vocabularies/index.md){ .md-button }

-   :material-cash-multiple:{ .lg .middle } **Health Economics**

    ---

    Cost and insurance coverage data. Sparse in EHR-derived OMOP (including Emory), but important for claims-linked analyses.

    [:octicons-arrow-right-24: Health Economics](Health%20Economics/index.md){ .md-button }

</div>

![OMOP CDM v5.4 entity relationship diagram showing standardized table categories](../../assets/images/cdm54.png)
