---
hide:
  - footer
search:
  exclude: false
title: Applications
---

# Applications

Emory's OMOP ecosystem supports two ways to work with the data — visual tools for point-and-click analysis, and direct code access for full flexibility. Many researchers use both.

=== ":material-mouse-variant: GUI Applications"

    Web-based tools for cohort building, data quality assessment, and standardized analyses — no coding required.

    <div class="grid cards" markdown>

    -   :material-globe-model:{ .lg .middle } **ATLAS**

        ---

        Define study populations, explore vocabularies, and run characterizations through a web-based interface.

        [:octicons-arrow-right-24: Emory's ATLAS (VPN required)](https://ohdsi-atlas.emory.edu/atlas/#/home){ .md-button }
        [:octicons-arrow-right-24: Training resources](../Training/Emory/ATLAS/index.md){ .md-button .md-button--primary }

    -   :material-diamond-outline:{ .lg .middle } **Data Quality Dashboard**

        ---

        Assess data completeness, conformance, and plausibility across Emory's OMOP instance.

        [:octicons-arrow-right-24: View dashboard](https://emorydatasolutions.github.io/e_omop_dqd/){ .md-button }

    -   :material-chart-box-outline:{ .lg .middle } **ARES**

        ---

        Explore data source characterization, quality metrics, and concept-level analysis across Emory's OMOP data.

        [:octicons-arrow-right-24: Emory's ARES (VPN required)](https://ohdsi-rstudio.emory.edu/ares/){ .md-button }

    -   :material-stethoscope:{ .lg .middle } **CohortDiagnostics**

        ---

        Evaluate cohort definitions with standardized analyses.

        *On Emory's roadmap — not yet available.*

        [:octicons-arrow-right-24: OHDSI documentation](https://ohdsi.github.io/CohortDiagnostics/){ .md-button }

    -   :simple-target:{ .lg .middle } **PhenotypeLibrary**

        ---

        Reusable phenotype repository for sharing and reusing cohort definitions across studies.

        *On Emory's roadmap — not yet available.*

        [:octicons-arrow-right-24: OHDSI library](https://data.ohdsi.org/PhenotypeLibrary/){ .md-button }

    </div>

    [:octicons-arrow-right-24: Full GUI application details](GUI/index.md)

=== ":material-code-braces: Code & Languages"

    Write SQL, R, or Python against Emory's OMOP data lake on Redshift. Full access to every table, every column.

    <div class="grid cards" markdown>

    -   :simple-r:{ .lg .middle } **R & RStudio**

        ---

        The HADES ecosystem, DatabaseConnector, CohortGenerator, and 100+ OHDSI packages — the most mature OHDSI toolchain.

        [:octicons-arrow-right-24: HADES packages](https://ohdsi.github.io/Hades/){ .md-button }
        [:octicons-arrow-right-24: R training](../Training/Emory/R/index.md){ .md-button .md-button--primary }

    -   :simple-postgresql:{ .lg .middle } **SQL**

        ---

        Direct Redshift queries using DBeaver, DataGrip, or any SQL client. Emory maintains a curated query library.

        [:octicons-arrow-right-24: Query library](../Training/Emory/SQL/Query%20Library/index.md){ .md-button }
        [:octicons-arrow-right-24: SQL tips](../Training/Emory/SQL/index.md){ .md-button .md-button--primary }

    -   :material-language-python:{ .lg .middle } **Python**

        ---

        Connect with `redshift_connector`, analyze with pandas, and build custom pipelines.

        [:octicons-arrow-right-24: Connection guide](../Support/Access%20Requests/Databases/index.md#after-youre-approved){ .md-button }

    </div>

    [:octicons-arrow-right-24: Full code tool details](Code/index.md)

!!! tip "Not sure where to start?"
    If you're new to OMOP, start with **ATLAS** to explore concepts and build your first cohort visually. When you need more flexibility, move to **SQL or R** for custom queries. See our [:octicons-arrow-right-24: Training](../Training/index.md) page for a recommended learning path.
