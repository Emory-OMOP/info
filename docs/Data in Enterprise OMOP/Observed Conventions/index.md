---
hide:
  - footer
title: Observed Conventions
---

# Observed Conventions

Emory's OMOP instance follows the OHDSI community's published conventions and adds Emory-specific extensions where needed. This section documents what we follow, what we've added, and where gaps remain.

<div class="grid cards" markdown>

-   :material-gavel:{ .lg .middle } **OHDSI Conventions**

    ---

    Community-published standards for the CDM — data types, vocabulary usage, domain routing, and THEMIS-ratified conventions that ensure cross-site compatibility.

    [:octicons-arrow-right-24: OHDSI conventions](OHDSI%20Conventions/index.md){ .md-button }

-   :material-hospital-building:{ .lg .middle } **Emory Conventions**

    ---

    Emory-specific additions to the CDM — mapping tables, PII tables, provenance fields, and ID generation strategies that support multi-source ETL.

    [:octicons-arrow-right-24: Emory conventions](Emory%20Conventions/index.md){ .md-button }

-   :material-clipboard-check-outline:{ .lg .middle } **Convention Adherence**

    ---

    Tracking Emory's adherence to OHDSI conventions — known deviations, their impact, and remediation status.

    [:octicons-arrow-right-24: Adherence status](Documented%20Adherence/index.md){ .md-button }

</div>

!!! tip "Why conventions matter"
    Conventions ensure that OHDSI tools (ATLAS, HADES, CohortDiagnostics) work consistently across sites and that Emory's data is compatible with federated network studies.
