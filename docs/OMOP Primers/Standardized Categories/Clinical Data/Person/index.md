---
hide:
  - footer
title: Person
---

# Person

**Epic equivalent**: Patient header / registration demographics

The `person` table is the center of the OMOP universe — **one row per patient**. In Epic, demographic details can be split across registration modules, updated with each encounter, and duplicated across systems. In OMOP, all of that consolidates into a single record per individual.

Every other clinical table (`condition_occurrence`, `drug_exposure`, `measurement`, etc.) links back to `person_id`. This is always your starting point.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `person_id` | MRN / Enterprise ID | Unique patient identifier (re-keyed for privacy) |
    | `gender_concept_id` | Sex at birth / Gender | Standardized concept — "Male", "Female", etc. May differ from `gender_source_value` |
    | `year_of_birth`, `month_of_birth`, `day_of_birth` | Date of birth | Split fields to support date shifting for de-identification |
    | `race_concept_id` | Race (registration) | Standardized race value mapped from source |
    | `ethnicity_concept_id` | Ethnicity (registration) | Standardized ethnicity value mapped from source |
    | `location_id` | Home address / ZIP | Foreign key to `location` table (often de-identified) |
    | `provider_id` | PCP / Managing physician | Primary provider if available; may be null |
    | `care_site_id` | Primary facility / department | Main care site attribution |
    | `*_source_value` fields | Raw EHR text | Original values from the source system (e.g., "M", "Hispanic or Latino") |

## What to Watch For

!!! warning "Common pitfalls"

    **Snapshot, not history**
    :   This table captures the *current* state. If a patient's address, race, or gender was updated over time, only the latest value is here. For longitudinal demographics, check the `observation` table.

    **Birth dates may be shifted**
    :   De-identified datasets may truncate or shift dates of birth. Don't assume full precision.

    **Use `concept_id`, not `source_value`**
    :   Always use `gender_concept_id`, `race_concept_id`, etc. for analysis. The `*_source_value` fields contain raw EHR text that varies across source systems.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Proportion of female African American patients in the database | `person.race_concept_id` + `person.gender_concept_id` |
| Average age at death | `person.year_of_birth` + `death` |
| Statin prescribing disparities across racial groups | `person.race_concept_id` + `drug_exposure` |
| Pediatric patients seen for asthma in the past year | `person.year_of_birth` + `condition_occurrence` |
| Patient characteristics at a specific care site | `person.care_site_id` + `visit_occurrence` |
