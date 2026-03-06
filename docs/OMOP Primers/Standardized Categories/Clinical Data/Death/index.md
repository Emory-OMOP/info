---
hide:
  - footer
title: Death
---

# Death

**Epic equivalent**: Discharge records (deceased disposition) / State death index / Vital statistics

The `death` table captures **mortality information** — one row per deceased person. At Emory, sources include EHR discharge records and state death data supplements.

This table is critical for **survival analysis**, **mortality endpoints**, and **time-to-event** studies.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `person_id` | Patient ID / MRN | Identifies the deceased patient |
    | `death_date` | Date of death | As recorded from available sources |
    | `death_datetime` | Time of death | Rarely populated unless from inpatient EHR |
    | `death_type_concept_id` | Data provenance | EHR, claims, registry, state death data |
    | `cause_concept_id` | Primary cause of death | SNOMED concept for cause (if available) |
    | `cause_source_value` | ICD-10 cause code | Original value from death certificate or discharge diagnosis |

## What to Watch For

!!! warning "Common pitfalls"

    **Absence does not mean alive**
    :   If a patient is not in the `death` table, they may still be deceased — the death simply wasn't captured. This is a right-censoring issue in survival analysis.

    **Date precision varies**
    :   Deaths from external sources (claims, state indices) may have imprecise dates. Validate for time-to-event analyses.

    **Cause of death is often missing**
    :   Structured cause of death requires vital records data. Many EHR-only deaths have no `cause_concept_id`.

## Research Patterns

| Question | Tables Involved |
|---|---|
| All-cause mortality in the oncology cohort | `death` + `condition_occurrence` (cancer) |
| Median survival from Alzheimer's diagnosis | `condition_occurrence` (Alzheimer's) + `death.death_date` |
| 30-day post-surgical mortality | `procedure_occurrence` + `death` + date interval |
| Cause-of-death distribution in stroke patients | `condition_occurrence` (stroke) + `death.cause_concept_id` |
| Mortality and social risk factors | `observation` (SDoH) + `death` |
