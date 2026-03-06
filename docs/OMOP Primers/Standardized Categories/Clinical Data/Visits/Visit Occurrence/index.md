---
hide:
  - footer
title: Visit Occurrence
---

# Visit Occurrence

**Epic equivalent**: Encounter table / ADT (Admit-Discharge-Transfer)

The `visit_occurrence` table captures **each encounter** a patient has with the healthcare system — outpatient visits, inpatient admissions, ER encounters, telehealth, and more. This is the closest thing to Epic's encounter table in OMOP.

Each row is a distinct episode of care. Other clinical tables (`condition_occurrence`, `drug_exposure`, `measurement`, etc.) can link to `visit_occurrence_id` to anchor events to a specific encounter.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `visit_occurrence_id` | Encounter ID (CSN) | Unique identifier for the visit |
    | `person_id` | Patient ID / MRN | Links the visit to the patient |
    | `visit_concept_id` | Encounter type | Standardized type: Inpatient, Outpatient, ER, etc. |
    | `visit_start_date`, `visit_end_date` | Admit/Discharge or Check-in/Check-out | Visit boundaries; `*_datetime` variants have time precision |
    | `visit_type_concept_id` | Data provenance | Whether from EHR, claims, etc. |
    | `provider_id` | Attending / Ordering provider | Provider associated with the encounter |
    | `care_site_id` | Hospital or clinic | Facility or department where the visit occurred |
    | `visit_source_value` | Raw encounter type | Original EHR value (e.g., "Office Visit", "Inpatient") |
    | `admitting_source_concept_id` | Admit source | Where the patient came from (home, SNF, ER) |
    | `discharge_to_concept_id` | Discharge disposition | Where the patient went after (home, rehab, expired) |

## What to Watch For

!!! warning "Common pitfalls"

    **Many rows per patient**
    :   Unlike `person` (one row), expect hundreds of rows per patient here — one for every encounter.

    **Same-day end dates**
    :   Outpatient visits often have `visit_end_date` = `visit_start_date`. Don't interpret this as zero-length visits — it's a data artifact.

    **Inconsistent provider/care_site**
    :   Not all source systems populate `provider_id` or `care_site_id` on every encounter. Cross-validate before running attribution analyses.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Average outpatient visits per patient per year | `visit_occurrence` filtered by `visit_concept_id` (outpatient) |
| 30-day hospital readmission rate | `visit_occurrence` with inpatient filter, self-join on `person_id` + date math |
| Discharge to skilled nursing facility rates | `discharge_to_concept_id` |
| Length of stay for cancer patients | `visit_occurrence` + `condition_occurrence` (cancer concepts) |
| ER visits preceding stroke hospitalizations | `visit_occurrence` (ER + inpatient) + `condition_occurrence` (stroke) + temporal ordering |
| Time between outpatient visits and hospitalizations | `visit_occurrence` self-join by `person_id` + `visit_concept_id` |
