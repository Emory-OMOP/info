---
hide:
  - footer
title: Data Mapping
---

# Data Mapping

How source data flows from Epic and CDW into OMOP — the ELT pipeline, vocabulary mapping coverage, and custom concept extensions.

<div class="grid cards" markdown>

-   :material-pipe:{ .lg .middle } **Extract Load Transform (ELT)**

    ---

    The DBT-based pipeline that transforms raw clinical data from Epic and CDW into OMOP CDM tables, orchestrated by Apache Airflow on Amazon Redshift.

    [:octicons-arrow-right-24: ELT Pipeline](Extract%20Load%20Transform%20(ELT)/index.md)

-   :material-chart-bar:{ .lg .middle } **Vocabulary Mapping Coverage**

    ---

    Live dashboard showing mapping progress across all CVB vocabulary projects — coverage percentages, predicate distributions, and top unmapped items.

    [:octicons-arrow-right-24: Mapping Coverage](Vocabulary%20Mapping%20Coverage/index.md)

-   :material-puzzle:{ .lg .middle } **Custom Concepts**

    ---

    Emory-specific vocabulary extensions for data elements not covered by standard OHDSI ontologies. Request mappings or contribute vocabularies through the CVB pipeline.

    [:octicons-arrow-right-24: Custom Concepts](Custom%20Concepts/index.md)

</div>
