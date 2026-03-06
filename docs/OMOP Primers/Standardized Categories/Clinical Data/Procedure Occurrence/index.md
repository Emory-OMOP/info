---
hide:
  - footer
title: Procedure Occurrence
---

# Procedure Occurrence

**Epic equivalent**: Procedure orders / Surgical case records / Radiology orders / CPT-coded billing entries

The `procedure_occurrence` table captures **medical procedures performed on a patient** — surgeries, imaging studies, vaccinations, biopsies, and other interventions. In Epic, this data comes from procedure orders, surgical case records, radiology modules, and CPT/HCPCS-coded billing. In OMOP, procedures are standardized to SNOMED (mapped from CPT, HCPCS, ICD-10-PCS).

Each row is a single procedure event.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `procedure_occurrence_id` | Procedure record ID | Unique identifier |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `procedure_concept_id` | SNOMED standard concept | Standardized procedure (mapped from CPT/HCPCS). Use for analysis |
    | `procedure_date` | Date of procedure | When performed; `procedure_datetime` has time precision |
    | `procedure_type_concept_id` | Data provenance | Whether from EHR, billing, registry, etc. |
    | `modifier_concept_id` | CPT modifiers | Laterality, approach, or other refinements (often missing) |
    | `quantity` | Count performed | How many times in this instance |
    | `provider_id` | Performing provider | Who performed the procedure |
    | `visit_occurrence_id` | Linked encounter | Visit context |
    | `procedure_source_value` | CPT / HCPCS / ICD-10-PCS code | Original code from the source system |

## What to Watch For

!!! warning "Common pitfalls"

    **Domain overlap**
    :   Imaging (e.g., MRI) may appear in `procedure_occurrence`, `measurement`, or both depending on capture method. Verify context before analysis.

    **One row per event, not per visit**
    :   A patient with 3 procedures in one visit has 3 rows. Don't assume one procedure per encounter.

    **Modifiers are often missing**
    :   `modifier_concept_id` is sparsely populated in most EHR-derived OMOP instances.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Colonoscopy frequency in the past 5 years | `procedure_concept_id` (colonoscopy) + `procedure_date` |
| Mastectomy vs. lumpectomy rates in breast cancer | `procedure_occurrence` + `condition_occurrence` (breast cancer) |
| Cardiac catheterization followed by CABG | `procedure_occurrence` sequenced by `procedure_date` |
| Joint replacement volume by surgical center | `procedure_occurrence` + `care_site_id` |
| Time from prostate biopsy to definitive surgery | `procedure_occurrence` (biopsy + prostatectomy) + date diff |
