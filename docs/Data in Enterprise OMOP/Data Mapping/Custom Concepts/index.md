---
search:
  exclude: false
title: Custom Concepts
---

# Custom Concepts

Custom concepts are additions to the standard OMOP vocabulary that capture Emory-specific data elements not covered by existing OHDSI ontologies. These allow Emory researchers to query local data elements using the same OMOP patterns used for standard concepts.

!!! info "Want to request a custom concept?"
    If you've identified source data in Epic or CDW that isn't currently mapped to an OMOP concept, follow the Community Contribution SOP to submit a request.

    [:octicons-arrow-right-24: Custom Concept SOP](../../../Emory%20OMOP%20Community/Community%20Contribution%20SOP/Custom%20Concept%20SOP/index.md)

## How Custom Concepts Work

The Enterprise OMOP team maps source values from Epic and CDW to standard OMOP vocabulary concepts wherever possible. When no standard concept exists for a clinically important data element, a custom concept is created in Emory's local vocabulary extension.

Custom concepts:

- Follow OMOP naming conventions and are assigned concept IDs in a reserved range (2 billion+)
- Are queryable using the same `concept`, `concept_ancestor`, and `concept_relationship` tables as standard concepts
- Are documented and versioned alongside each product release

## Current Coverage

The Enterprise OMOP team has prioritized mapping the most common source values across ingested domains. However, coverage is not exhaustive — particularly for:

- Uncommon clinical terms not tied to a standard medical ontology in Epic
- Data elements from specialized workflows or research-specific instruments
- Non-standard identifiers and local coding systems

If you believe important data is missing, the [Custom Concept SOP](../../../Emory%20OMOP%20Community/Community%20Contribution%20SOP/Custom%20Concept%20SOP/index.md) provides a structured process for requesting additions.
