---
hide:
  - footer
title: Drug Exposure
---

# Drug Exposure

**Epic equivalent**: Medication orders / MAR (Medication Administration Record) / Prescription history / Pharmacy data

The `drug_exposure` table captures **every medication event** — inpatient administrations, outpatient prescriptions, pharmacy dispenses, and self-reported medications. In Epic, this data is scattered across medication orders, the MAR, prescription history, and pharmacy modules. In OMOP, it all lands here.

Each row is a single medication exposure event. Medications are coded in RxNorm (mapped from NDC, GPI, or local codes).

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `drug_exposure_id` | Medication record ID | Unique identifier for the exposure event |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `drug_concept_id` | RxNorm standard concept | Standardized drug (ingredient, clinical drug, or branded). Always use for analysis |
    | `drug_exposure_start_date` | Order/admin start date | When the medication exposure began |
    | `drug_exposure_end_date` | Order/admin end date | When it ended. Often null — may need to infer from `days_supply` |
    | `drug_type_concept_id` | Data provenance | Whether from prescription, dispensing, administration, etc. |
    | `stop_reason` | Discontinuation reason | Why the medication was stopped (if documented) |
    | `refills` | Number of refills | Refill count authorized |
    | `quantity` | Quantity dispensed | Amount dispensed or administered |
    | `days_supply` | Days supply | Intended duration of the supply |
    | `route_concept_id` | Route of administration | Oral, IV, subcutaneous, etc. |
    | `sig` | Prescription instructions | Free-text dosing instructions |
    | `visit_occurrence_id` | Linked encounter | Visit during which the drug was ordered/given |
    | `drug_source_value` | NDC / local code | Original code from the source system |

## What to Watch For

!!! warning "Common pitfalls"

    **Many rows per medication per patient**
    :   Each refill, each MAR administration, each separate prescription generates a row. Use `drug_era` to collapse into continuous exposure periods.

    **Null end dates are common**
    :   `drug_exposure_end_date` is often missing. You may need to calculate it as `start_date + days_supply`.

    **Route and sig are often sparse**
    :   Not all source systems capture `route_concept_id` or `sig` consistently.

    **Ingredient-level analysis**
    :   For drug class analyses (e.g., "all ACE inhibitors"), query at the RxNorm ingredient level using `concept_ancestor`.

## Research Patterns

| Question | Tables Involved |
|---|---|
| ACE inhibitor use among hypertension patients | `drug_exposure` (ACE ingredient descendants) + `condition_occurrence` (hypertension) |
| Duration of endocrine therapy in breast cancer | `drug_exposure` + `condition_occurrence` (breast cancer) |
| Statin prescribing equity across racial groups | `drug_exposure` + `person.race_concept_id` |
| Antibiotics given in the ER | `drug_exposure` + `visit_occurrence` filtered by ER |
| Chemotherapy cycle detection | `drug_exposure` (chemo drugs) grouped by `person_id` + date intervals |
