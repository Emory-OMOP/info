# OHDSI Conventions

The OMOP Common Data Model (CDM) is a standardized data model maintained by the OHDSI community. It provides a common structure for storing and analyzing healthcare data from diverse sources, enabling large-scale observational studies and federated research across institutions.

The OHDSI conventions are guidelines and best practices for implementing the CDM — covering data types, vocabulary usage, domain routing, and transformation processes. These conventions ensure that OHDSI tools (ATLAS, HADES, CohortDiagnostics) work consistently across all sites.

## Key Resources

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **CDM Documentation**

    ---

    The official specification for the OMOP CDM. Emory uses [version 5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html).

    [:octicons-arrow-right-24: CDM Documentation](https://ohdsi.github.io/CommonDataModel/)

-   :material-format-list-checks:{ .lg .middle } **General Conventions**

    ---

    Rules for data types, null handling, date formats, and standard field behaviors across all CDM tables.

    [:octicons-arrow-right-24: Data Model Conventions](https://ohdsi.github.io/CommonDataModel/dataModelConventions.html)

-   :material-gavel:{ .lg .middle } **THEMIS Convention Library**

    ---

    Community-ratified conventions for specific data scenarios — the authoritative source for "how should this be modeled?"

    [:octicons-arrow-right-24: THEMIS Conventions](https://ohdsi.github.io/Themis/)

-   :material-forum:{ .lg .middle } **OHDSI Forums**

    ---

    Active community discussions on CDM best practices, edge cases, and evolving conventions not yet codified in THEMIS.

    [:octicons-arrow-right-24: OHDSI Forums](https://forums.ohdsi.org/)

</div>

## Dataset-Specific Conventions

Conventions for specific data types or patient groups are developed by OHDSI [workgroups](https://ohdsi.org/workgroups/). Common examples include:

- **Healthcare Systems Interest Group** — conventions for healthcare system data
- **Oncology Workgroup** — conventions for patient oncology data

These workgroups publish conventions as white papers or technical reports, available on the OHDSI website or through academic publications.

## Emory's Adherence

Emory follows the General and THEMIS conventions to the extent known as of April 2025. There are known convention adherence gaps due to team workload — see [:octicons-arrow-right-24: Convention Adherence](../Documented%20Adherence/index.md) for details.
