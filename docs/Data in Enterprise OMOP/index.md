---
hide:
  - footer
title: Data in Enterprise OMOP
---

# Data in Enterprise OMOP

Emory's OMOP Enterprise pipeline transforms clinical data from Epic and the Clinical Data Warehouse (CDW) into the OMOP Common Data Model. This section covers what's in the data, how it got there, and how we know it's right.

<div class="grid cards" markdown>

-   :material-database-arrow-right:{ .lg .middle } **Data Mapping**

    ---

    How source data flows from Epic and CDW into OMOP — the ELT pipeline, vocabulary mapping coverage, and custom concepts.

    [:octicons-arrow-right-24: Data Mapping](Data%20Mapping/index.md)

-   :material-check-decagram:{ .lg .middle } **Data Quality**

    ---

    Automated quality checks across 2,374 DQD tests (96.6% pass rate), 133 DBT tests, and a tracked list of known issues.

    [:octicons-arrow-right-24: Data Quality](Data%20Quality/index.md)

-   :material-book-check:{ .lg .middle } **Observed Conventions**

    ---

    OHDSI community conventions, Emory-specific conventions, and documented adherence to standards across the pipeline.

    [:octicons-arrow-right-24: Observed Conventions](Observed%20Conventions/index.md)

-   :material-brain:{ .lg .middle } **NLP Infrastructure** :material-progress-wrench:{ title="Draft" }

    ---

    Proposed span-based NLP schema extending the OMOP CDM — pipeline provenance, typed extractions, and `_DERIVED` tables for clean separation of NLP-derived data.

    [:octicons-arrow-right-24: NLP Infrastructure](NLP%20Infrastructure/index.md)

-   :material-tag-multiple:{ .lg .middle } **Releases**

    ---

    Version history from v0.2.0 through v1.0.0 — what changed, what was fixed, and what researchers should know.

    [:octicons-arrow-right-24: Releases](Releases/index.md)

</div>

## Data Mapping at a Glance

| Area | Pages |
|------|-------|
| **Pipeline** | [Extract Load Transform (ELT)](Data%20Mapping/Extract%20Load%20Transform%20(ELT)/index.md) · [Era Algorithms](Data%20Mapping/Extract%20Load%20Transform%20(ELT)/Era%20Algorithms/index.md) |
| **Coverage** | [Vocabulary Mapping Coverage](Data%20Mapping/Vocabulary%20Mapping%20Coverage/index.md) |
| **Extensions** | [Custom Concepts](Data%20Mapping/Custom%20Concepts/index.md) · [Requesting Mappings](Data%20Mapping/Custom%20Concepts/requesting-mappings.md) · [Contributing Vocabularies](Data%20Mapping/Custom%20Concepts/contributing-vocabularies.md) |
