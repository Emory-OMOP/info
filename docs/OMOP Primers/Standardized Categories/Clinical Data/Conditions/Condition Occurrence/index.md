---
hide:
  - footer
title: Condition Occurrence
---

# Condition Occurrence

**Epic equivalent**: Clarity diagnosis table / Encounter diagnoses / Problem list

The `condition_occurrence` table captures **diagnoses and problems** recorded for a patient — billing diagnoses, problem list entries, discharge diagnoses, and other structured condition data. Each row is a single recorded condition event, often tied to a visit.

In Epic, you'd query the diagnosis table or encounter diagnoses. In OMOP, all of these consolidate here with standardized SNOMED codes (mapped from ICD-10, ICD-9, etc.).

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `condition_occurrence_id` | Condition record ID | Unique identifier for the condition event |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `condition_concept_id` | ICD/SNOMED standard concept | Standardized condition (e.g., "Type 2 Diabetes Mellitus"). Always use this for analysis |
    | `condition_start_date` | Date of diagnosis | When the condition was recorded or began |
    | `condition_end_date` | Resolution / stop date | When the condition resolved (often null in EHRs) |
    | `condition_type_concept_id` | Source context | Origin: problem list, billing claim, EHR note, etc. |
    | `condition_source_value` | ICD-10 / ICD-9 / local code | The source code as it appeared in Epic |
    | `condition_source_concept_id` | Source code concept | Maps the source value to its OMOP concept ID |
    | `visit_occurrence_id` | Linked encounter | Visit during which the diagnosis was recorded (may be null for ongoing problems) |
    | `provider_id` | Recording provider | Who documented the diagnosis |

## What to Watch For

!!! warning "Common pitfalls"

    **Chronic conditions repeat**
    :   A patient with diabetes may have hundreds of `condition_occurrence` rows — one for every visit where it was recorded. Use `condition_era` if you want the continuous period.

    **Missing end dates**
    :   Most EHRs don't capture when a condition resolves. `NULL` in `condition_end_date` does **not** mean the condition is still active — it means we don't know.

    **Use `concept_id`, not `source_value`**
    :   `condition_source_value` contains raw ICD codes. For standardized cross-site analysis, always use `condition_concept_id` (SNOMED).

## Research Patterns

| Question | Tables Involved |
|---|---|
| Patients diagnosed with diabetes in the past year | `condition_concept_id` (diabetes descendants) + `condition_start_date` |
| Time from cancer diagnosis to first treatment | `condition_occurrence` (cancer) + `drug_exposure` or `procedure_occurrence` |
| COVID-19 diagnoses during inpatient stays | `condition_concept_id` + `visit_occurrence_id` filtered by inpatient |
| Diagnoses more common in ER visits | `condition_occurrence` + `visit_occurrence` with ER filter |
| ICU comorbidity burden | `condition_occurrence` + `visit_detail` filtered for ICU |
