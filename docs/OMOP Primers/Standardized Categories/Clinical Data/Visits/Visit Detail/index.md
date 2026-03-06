---
hide:
  - footer
title: Visit Detail
---

# Visit Detail

**Epic equivalent**: ADT segments / Department transfers / Hospital accounts

The `visit_detail` table captures **sub-components of a broader visit**. If `visit_occurrence` is the full hospital stay, `visit_detail` is each department transfer within it — ICU to step-down, ER holding to admission, surgery to recovery.

In Epic, this maps to ADT segments, hospital account splits, and department-level stay records. When populated, it enables fine-grained, time-aware analyses of inpatient workflows.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `visit_detail_id` | Sub-encounter ID | Unique identifier for the detail segment |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `visit_occurrence_id` | Parent encounter ID | Links to the parent `visit_occurrence` record |
    | `visit_detail_concept_id` | Level of care / room type | Standardized type: ICU, Med/Surg, ER holding, etc. |
    | `visit_detail_start_date`, `visit_detail_end_date` | Unit stay start/end | Time boundaries for this segment |
    | `provider_id` | Unit attending / team | Provider for this department segment |
    | `care_site_id` | Department / physical location | Where this segment took place |
    | `admitting_source_concept_id` | Transfer source | Where the patient came from before this segment |
    | `discharge_to_concept_id` | Transfer destination | Where the patient went after this segment |
    | `preceding_visit_detail_id` | Prior segment | Links to the previous detail record for flow reconstruction |

## What to Watch For

!!! warning "Common pitfalls"

    **Often sparse or empty**
    :   Only systems with robust ADT or departmental transfer logs populate this table. Check row counts before building analyses on it.

    **Don't confuse with `visit_occurrence`**
    :   `visit_occurrence` is the full encounter. `visit_detail` is movements *within* that encounter. They answer different questions.

    **Clock artifacts at transfers**
    :   Midnight splits or overlapping timestamps between segments are common. Validate for continuous flow before computing LOS by unit.

## Research Patterns

| Question | Tables Involved |
|---|---|
| ICU stays within cancer-related hospitalizations | `visit_detail` (ICU concept) + `visit_occurrence` + `condition_occurrence` (cancer) |
| ER-to-admission time | `visit_detail` (ER segment end) → `visit_detail` (inpatient segment start) |
| Department-level readmission rates | `visit_detail.care_site_id` + readmission logic |
| Inpatient journey mapping for a cohort | `visit_detail` ordered by `start_date` + `preceding_visit_detail_id` |
| Post-surgical step-down transfers | `visit_detail` + `procedure_occurrence` (surgery) + concept filters |
