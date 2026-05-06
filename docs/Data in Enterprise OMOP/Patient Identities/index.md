---
hide:
  - footer
title: Patient Identities
---

# Patient Identities

How Emory's OMOP pipeline reconciles patient identifiers across Epic and the legacy Cerner Clinical Data Warehouse into a single canonical `person_id`, the methodology behind probabilistic patient matching, and how identity data is treated when it leaves the warehouse.

<div class="grid cards" markdown>

-   :material-account-network:{ .lg .middle } **Patient Identity Stabilization**

    ---

    The infrastructure that turns scattered identifiers — multiple MRNs, Epic patient IDs, legacy Cerner identifiers — into one stable `person_id` per human. Includes the medallion pipeline, the clustering algorithm, and the gold tables researchers query.

    [:octicons-arrow-right-24: Patient Identity Stabilization](Patient%20Identity%20Stabilization/index.md)

-   :material-function-variant:{ .lg .middle } **Probabilistic Matching** :material-progress-wrench:{ title="Draft" }

    ---

    Fellegi-Sunter match-weight derivation and priors calibrated against Emory's identifier landscape — published for use by other identity-resolution practitioners.

    [:octicons-arrow-right-24: Probabilistic Matching](Probabilistic%20Matching/index.md)

-   :material-incognito:{ .lg .middle } **De-identification** :material-progress-wrench:{ title="Draft" }

    ---

    How identity data is removed or transformed before clinical data leaves Emory's warehouse for external collaborators. Currently a placeholder; full content forthcoming.

    [:octicons-arrow-right-24: De-identification](De-identification/index.md)

</div>
