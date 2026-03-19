---
search:
  exclude: false
hide:
  - footer
title: Custom Concepts
---

# Custom Concepts

Custom concepts are additions to the standard OMOP vocabulary that capture Emory-specific data elements not covered by existing OHDSI ontologies. These allow Emory researchers to query local data elements using the same OMOP patterns used for standard concepts.

## How Custom Concepts Work

The Enterprise OMOP team maps source values from Epic and CDW to standard OMOP vocabulary concepts wherever possible. When no standard concept exists for a clinically important data element, a custom concept is created in Emory's local vocabulary extension.

Custom concepts:

- Follow OMOP naming conventions and are assigned concept IDs in a reserved range (2 billion+)
- Are queryable using the same `concept`, `concept_ancestor`, and `concept_relationship` tables as standard concepts
- Are documented and versioned alongside each product release
- Are built through the **Custom Vocabulary Builder (CVB)**, an automated pipeline that produces OMOP-compatible vocabulary deltas

## How to Get Involved

<div class="grid cards" markdown>

-   :material-message-question:{ .lg .middle } **Request a Mapping**

    ---

    Found unmapped source data in Epic or CDW? Submit a request and the vocabulary team will triage, prioritize, and build it into the next release.

    [:octicons-arrow-right-24: Requesting Mappings](requesting-mappings.md)

-   :material-source-branch:{ .lg .middle } **Contribute a Vocabulary**

    ---

    Have domain expertise and want to contribute mappings directly? Use the CVB pipeline to build OMOP-compatible vocabulary deltas and submit via pull request.

    [:octicons-arrow-right-24: Contributing Vocabularies](contributing-vocabularies.md)

-   :material-swap-horizontal:{ .lg .middle } **Network Study Bifurcation**

    ---

    How the ETL supports both local (CVB-enhanced) and OHDSI network study (Athena-only) concept resolution through compound targets and dual vocabulary schemas.

    [:octicons-arrow-right-24: Network Study Bifurcation](network-study-bifurcation.md)

</div>

## Current Coverage

The Enterprise OMOP team has prioritized mapping the most common source values across ingested domains. However, coverage is not exhaustive — particularly for:

- Uncommon clinical terms not tied to a standard medical ontology in Epic
- Data elements from specialized workflows or research-specific instruments
- Non-standard identifiers and local coding systems

If you believe important data is missing, [request a mapping](requesting-mappings.md) to start the process.
