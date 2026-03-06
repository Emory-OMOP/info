---
hide:
  - footer
title: Condition Era
---

# Condition Era

**Epic equivalent**: No direct equivalent — derived from diagnosis records

The `condition_era` table aggregates **periods of continuous presence of a condition** for a patient. It rolls up multiple `condition_occurrence` records (every time diabetes was documented across visits) into a single era representing "this patient had diabetes from X to Y."

Built during ETL using a **persistence window** — typically 30 days between diagnosis codes before ending an era.

## Field Reference

??? example "Field reference (click to expand)"

    | OMOP Field | What It Captures |
    |---|---|
    | `condition_era_id` | Unique identifier for the era |
    | `person_id` | Links to the patient |
    | `condition_concept_id` | Standardized condition (SNOMED) |
    | `condition_era_start_date` | First date the condition was recorded |
    | `condition_era_end_date` | Last date + persistence window |
    | `condition_occurrence_count` | Number of source records collapsed into this era |

## What to Watch For

!!! warning "Common pitfalls"

    **Gap logic is configurable**
    :   The default persistence window is typically 30 days, but this is set during ETL. Always verify your site's configuration before interpreting era durations.

    **Long eras for chronic conditions**
    :   A patient with diabetes may have a single era spanning years. That's expected.

    **Era is not episode of care**
    :   Condition era represents the *period of disease presence*, not active treatment. For curated clinical episodes, see `episode`.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Median duration of major depression | `condition_era` (depression) + end − start date |
| Gaps in hypertension diagnosis > 1 year | `condition_era` (hypertension) — multiple eras with gap analysis |
| Incident vs. prevalent asthma cases | `condition_era` start date relative to cohort entry |
| Condition recurrence after gap | `condition_era` — multiple eras per person/concept |
| Comorbidity burden at index date | `condition_era` overlapping on a target date |
