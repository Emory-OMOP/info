---
hide:
  - footer
title: Measurement
---

# Measurement

**Epic equivalent**: Clarity lab results / Flowsheet vitals / Observation results

The `measurement` table captures **structured numeric and categorical test results** — lab values, vital signs, imaging reads, and clinical assessments. In Epic, these live in separate places: lab results in one module, flowsheet vitals in another, some observations in yet another. In OMOP, they all land in this single table.

Each row is a single measurement event (one A1c result, one blood pressure reading, one creatinine value).

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `measurement_id` | Result ID | Unique identifier for the measurement |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `measurement_concept_id` | LOINC / test concept | Standardized test (e.g., "Hemoglobin A1c", "Systolic BP"). Use this for analysis |
    | `measurement_date` | Result date | When the measurement was taken; `measurement_datetime` has time precision |
    | `measurement_type_concept_id` | Data provenance | Whether from EHR, lab feed, patient-reported, etc. |
    | `value_as_number` | Numeric result | The test value (e.g., 6.2 for A1c, 120 for systolic BP) |
    | `value_as_concept_id` | Categorical result | For results like "Positive", "Negative", "Detected" |
    | `unit_concept_id` | Unit of measurement | Standardized unit (mg/dL, mmHg, etc.) |
    | `range_low`, `range_high` | Reference range | Normal range for the test |
    | `provider_id` | Ordering provider | Who ordered or recorded the result |
    | `visit_occurrence_id` | Linked encounter | Visit associated with the measurement |
    | `measurement_source_value` | Local test name | Original value from the source system |
    | `unit_source_value` | Local unit | Original unit as recorded in the EHR |

## What to Watch For

!!! warning "Common pitfalls"

    **Labs and vitals share the same table**
    :   Blood pressure and hemoglobin are neighbors. Always filter by `measurement_concept_id` — don't assume all rows are lab results.

    **Unit inconsistencies**
    :   Not all sites standardize units perfectly. Always check `unit_concept_id` and be cautious comparing values across different unit mappings.

    **Categorical vs. numeric results**
    :   Some tests (COVID PCR, pregnancy tests) use `value_as_concept_id` instead of `value_as_number`. Check both when querying.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Average A1c among diabetes patients | `measurement` (A1c concept) + `condition_occurrence` (diabetes) |
| Low hemoglobin prior to surgery | `measurement` (Hgb concept + value threshold) + `procedure_occurrence` |
| Creatinine trends over time in CKD patients | `measurement` (creatinine concept) + `condition_occurrence` (CKD) |
| Positive COVID-19 PCR tests in the ER | `measurement.value_as_concept_id` (Positive) + `visit_occurrence` (ER) |
| Uncontrolled systolic BP in hypertension | `measurement` (systolic BP concept + value > 140) + `condition_occurrence` (hypertension) |
