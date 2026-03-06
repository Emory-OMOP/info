---
hide:
  - footer
title: Data Quality
---

# Data Quality

Emory's data quality program combines OHDSI community standards with DataOps-inspired pipeline testing to ensure OMOP data is accurate, complete, and fit for research.

## At a Glance

<div class="grid cards" markdown>

-   :material-check-decagram:{ .lg .middle } **<!-- DQD_PASS_RATE_START -->96.6% (v1.0.0)<!-- DQD_PASS_RATE_END --> Pass Rate**

    ---

    Overall OHDSI Data Quality Dashboard pass rate across all checks. Drill into failures and category breakdowns.

    [:octicons-arrow-right-24: DQD results](Data%20Quality%20Results/index.md){ .md-button }
    [:octicons-arrow-right-24: Interactive dashboard](https://emorydatasolutions.github.io/e_omop_dqd/){ .md-button .md-button--primary }

-   :material-test-tube:{ .lg .middle } **DBT Test Suites**

    ---

    Column-level test definitions for every table in the ETL pipeline — referential integrity, nullability, uniqueness, and domain validation.

    [:octicons-arrow-right-24: DBT test definitions](DBT%20Tests/index.md){ .md-button }

-   :material-alert-circle-outline:{ .lg .middle } **Known Issues**

    ---

    Table-by-table documentation of mapping gaps, data limitations, and recommended workarounds.

    [:octicons-arrow-right-24: Known issues](Known%20Issues/index.md){ .md-button }

</div>

## Our Approach

<div class="grid cards" markdown>

-   :material-cog-sync-outline:{ .lg .middle } **DataOps Design Philosophy**

    ---

    Our quality process is built on the DataOps framework — combining DevOps practices with manufacturing-inspired process control to build quality into the pipeline, not bolt it on after.

    [:octicons-arrow-right-24: Design philosophy](Data%20Quality%20Design/index.md){ .md-button }

-   :material-diamond-outline:{ .lg .middle } **OHDSI Data Quality Dashboard**

    ---

    The community-standard DQD runs 2,000+ automated checks across completeness, conformance, and plausibility — providing a standardized quality assessment comparable across OHDSI sites.

    [:octicons-arrow-right-24: Explore the dashboard](https://emorydatasolutions.github.io/e_omop_dqd/){ .md-button }

</div>

!!! question "Found a data quality issue?"
    Report it through our [:octicons-arrow-right-24: bug report form](../../Support/index.md) or reach out on [:octicons-arrow-right-24: Microsoft Teams](../../Contact%20Us/index.md).
