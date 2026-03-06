---
hide:
  - footer
title: Vocabularies
---

# Vocabularies

The **OMOP Standardized Vocabularies** are the mapping layer that makes everything else work. They translate the source codes you're used to (ICD-10, CPT, NDC, local Epic codes) into a shared standard language (SNOMED, RxNorm, LOINC) so researchers can define cohorts and variables consistently — regardless of whether the data came from Epic, Cerner, or a claims feed.

!!! warning "If you learn one thing beyond the clinical tables, learn this"
    The vocabularies are what make OMOP powerful. Without them, you're just writing SQL against a different schema. With them, you can say "give me all patients with any type of diabetes" and get every ICD-9, ICD-10, and SNOMED code automatically. See [Training](../../../Training/index.md) for vocabulary-specific courses.

## Why Vocabularies Matter for Epic Users

In Epic, you work with **source codes** — ICD-10 for diagnoses, CPT/HCPCS for procedures, NDC for medications. To build a comprehensive cohort, you'd need to manually assemble code lists.

In OMOP, the vocabulary does this for you:

| Epic Workflow | OMOP Equivalent |
|---|---|
| Manually list every ICD-10 code for diabetes | Query `concept_ancestor` for all descendants of the "Diabetes mellitus" SNOMED concept |
| Cross-reference ICD-9 and ICD-10 for historical data | Both are already mapped to the same SNOMED standard concepts |
| Look up NDC codes for a drug class | Query RxNorm ingredient + `concept_ancestor` to get all formulations |
| Build a local code-to-meaning lookup | `source_to_concept_map` + `concept` already provides this |

## Key Vocabulary Tables

<div class="grid cards" markdown>

-   :material-book-alphabet:{ .lg .middle } **Concept**

    ---

    The dictionary of all medical terms OMOP understands. Every diagnosis, drug, lab, procedure, unit, and domain has a row here. This is one of the primary tables you'll use when building study definitions.

-   :material-link-variant:{ .lg .middle } **Concept Relationship**

    ---

    Defines how concepts relate to each other. Use this to **map source codes to standard codes** (via "Maps to" relationships) or to navigate between related concepts (e.g., a lung cancer subtype's anatomic site).

-   :material-file-tree:{ .lg .middle } **Concept Ancestor**

    ---

    The hierarchy navigator. Find all specific codes under a broader category without manually listing them. "Give me all descendants of diabetes" returns type 1, type 2, gestational, diabetes with nephropathy — everything in the hierarchy.

-   :material-map-marker-path:{ .lg .middle } **Source to Concept Map**

    ---

    Maps **local codes** (internal Epic codes, custom lab identifiers) to standard OMOP concepts. Critical for Emory — this is where non-standard source values get their OMOP meaning. We encourage community collaboration on improving these mappings via the [Custom Concept SOP](../../../Emory%20OMOP%20Community/Community%20Contribution%20SOP/Custom%20Concept%20SOP/index.md).

</div>

## What "Standard" Means in OMOP

In OMOP, "standard" doesn't mean arbitrary. The OHDSI community's [Vocabulary Working Group](https://github.com/OHDSI/Vocabulary-v5.0/wiki) decides which vocabulary serves as the standard for each domain:

| Domain | Standard Vocabulary | Source Vocabularies (mapped) |
|---|---|---|
| Conditions | SNOMED | ICD-9-CM, ICD-10-CM, Read, MedDRA |
| Drugs | RxNorm / RxNorm Extension | NDC, GPI, ATC |
| Measurements | LOINC | Local lab codes, CPT (some) |
| Procedures | SNOMED | CPT4, HCPCS, ICD-10-PCS |

These mappings are maintained by domain experts — ontologists use existing cross-walks (like NLM's ICD-to-SNOMED maps) supplemented by expert consensus. When issues are found by the global OMOP community, they're logged as GitHub issues and resolved through workgroup remapping efforts.

## Clinical Use Case Examples

??? example "Common vocabulary queries"

    | Question | How to use the vocabulary |
    |---|---|
    | Find all patients with any type of heart failure | Use `concept_ancestor` + `concept` to get all SNOMED descendants of "Heart failure" |
    | Include both ICD-9 and ICD-10 codes in a phenotype | Use `concept_relationship` to map source codes to their shared SNOMED standard |
    | Build a cohort of patients on ACE inhibitors | Use `concept` for the RxNorm ingredient + `concept_ancestor` for all ACE inhibitor drugs |
    | Understand if a procedure is surgical vs. diagnostic | Check `concept_class_id` in `concept` or navigate `concept_relationship` |
    | Map a local lab code to a standard concept | Check `source_to_concept_map`; if unmapped, submit via the Custom Concept SOP |
