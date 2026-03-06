---
hide:
  - footer
title: Fact Relationship
---

# Fact Relationship

**Epic equivalent**: No direct equivalent — implicit relationships made explicit

The `fact_relationship` table captures **relationships between records across different OMOP tables**. In EHR systems, these connections are usually implied through timing, proximity, or clinical context. OMOP makes them explicit — linking a biopsy procedure to its pathology finding, or a pregnancy diagnosis to a delivery event.

Think of it as the glue for non-obvious cross-domain connections.

## Field Reference

??? example "Field reference (click to expand)"

    | OMOP Field | What It Captures |
    |---|---|
    | `domain_concept_id_1` | Domain of the first record (condition, procedure, measurement, etc.) |
    | `fact_id_1` | The record ID in the first domain's table |
    | `domain_concept_id_2` | Domain of the second record |
    | `fact_id_2` | The record ID in the second domain's table |
    | `relationship_concept_id` | The nature of the link (e.g., "Has associated finding") |

    **Example relationship concept:**

    | Concept ID | Meaning |
    |---|---|
    | `44818770` | "Has associated finding" — links a procedure to a justifying diagnosis |

## What to Watch For

!!! warning "Common pitfalls"

    **Rarely populated**
    :   Most ETL pipelines don't fill this table by default. Emory does not currently populate it. See [Known Issues](../../../../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) for updates.

    **Soft joins — no foreign keys**
    :   Relationships are concept-driven, not enforced by referential integrity. Validate carefully.

    **Requires understanding the relationship vocabulary**
    :   You need to know the `relationship_concept_id` to interpret what the link means.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Link pathology results to biopsy procedures | `fact_relationship` between `measurement` and `procedure_occurrence` |
| Diagnoses that justified a specific surgery | `fact_relationship` linking `condition_occurrence` to `procedure_occurrence` |
| Composite blood pressure from systolic + diastolic | `measurement` + `fact_relationship` ("is component of") |
| Pregnancy episode from related diagnoses + procedures | `fact_relationship` with temporal link concepts |
| Conditions tied to device insertions | `fact_relationship` between `condition_occurrence` and `device_exposure` |
