---
hide:
  - footer
title: Observation
---

# Observation

**Epic equivalent**: Social history / Flowsheet entries / Questionnaires / Structured note templates

The `observation` table is the **catch-all for clinical facts** that don't fit into conditions, drugs, or measurements. Smoking status, social determinants of health, patient-reported outcomes, screening responses, advance directives, and reasons for medication non-use all land here.

In Epic, this data comes from social history tabs, flowsheet entries, questionnaires, and structured note templates. The OHDSI community's rule: if the data can go in a more specific table, it should. If not, it goes here.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `observation_id` | Observation record ID | Unique identifier |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `observation_concept_id` | Structured concept | Standardized concept (e.g., "Former smoker", "Lives alone") |
    | `observation_date` | Observation date | When recorded; `observation_datetime` has time precision |
    | `observation_type_concept_id` | Source type | Origin: EHR, survey, registry, etc. |
    | `value_as_number` | Numeric value | For scaled/scored responses (e.g., pack-years, pain score) |
    | `value_as_string` | Free-text value | Unstructured text response (not for standardized analysis) |
    | `value_as_concept_id` | Coded value | Categorical response as a concept (e.g., "Yes", "No", "Former") |
    | `qualifier_concept_id` | Modifier / context | Optional severity, status, or other qualifier |
    | `unit_concept_id` | Unit | Unit for numeric observations |
    | `provider_id` | Recording clinician | Who recorded the observation |
    | `visit_occurrence_id` | Linked encounter | Visit context |
    | `observation_source_value` | Local field name | Original EHR label (e.g., "TOB_STATUS") |

## What to Watch For

!!! warning "Common pitfalls"

    **Domain overlap**
    :   If it looks like a diagnosis, check `condition_occurrence` first. If it has a numeric result with units, check `measurement`. `observation` is the last resort.

    **Prefer `concept_id` over `string`**
    :   `value_as_string` is not analyzable at scale. Use `value_as_concept_id` for categorical responses.

    **High site-specific variation**
    :   Different institutions load very different things into observation. Always check what's actually in your dataset before assuming coverage.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Current smoking prevalence | `observation_concept_id` (smoking status) + `value_as_concept_id` |
| Food insecurity screening results | `observation_concept_id` (SDoH) + `value_as_concept_id` (positive) |
| Patient-reported pain scores > 6 | `observation_concept_id` (pain score) + `value_as_number` filter |
| Patients who declined statin therapy | `observation` (medication non-use) + `condition_occurrence` |
| Advance directive documentation in hospice patients | `observation_concept_id` (advance directive) + `visit_occurrence` |
