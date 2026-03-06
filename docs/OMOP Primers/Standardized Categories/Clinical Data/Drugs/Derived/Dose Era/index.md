---
hide:
  - footer
title: Dose Era
---

# Dose Era

**Epic equivalent**: No direct equivalent — derived from drug exposure with dose normalization

The `dose_era` table represents **periods of consistent daily dose** for a drug. Like `drug_era`, it's derived from `drug_exposure`, but with an additional layer of dose normalization. When the dose changes, a new era begins.

Useful for **dose-response studies**, **safety signal detection**, and tracking dose escalation/reduction patterns.

## Field Reference

??? example "Field reference (click to expand)"

    | OMOP Field | What It Captures |
    |---|---|
    | `dose_era_id` | Unique identifier |
    | `person_id` | Links to the patient |
    | `drug_concept_id` | RxNorm ingredient concept |
    | `unit_concept_id` | Dose unit (mg, mL, etc.) |
    | `dose_value` | Standardized daily dose during this era |
    | `dose_era_start_date` | First date of stable dosing |
    | `dose_era_end_date` | Last date of stable dosing |

## What to Watch For

!!! warning "Common pitfalls"

    **Dose changes create new eras**
    :   Unlike drug era (which tolerates gaps), dose era splits whenever the daily dose changes.

    **Less frequently populated**
    :   Many OMOP ETLs omit this table unless explicitly configured. Check availability before building analyses on it.

    **Dependent on accurate dose capture**
    :   Poor or missing dose data in `drug_exposure` limits this table's utility.

## Research Patterns

| Question | Tables Involved |
|---|---|
| High-dose corticosteroid duration in IBD | `dose_era` (prednisone + dose threshold) + `condition_occurrence` (IBD) |
| Dose-dependent statin safety signals | `dose_era` (statins) + `condition_occurrence` (rhabdomyolysis) |
| Antidepressant dose escalation patterns | `dose_era` sequenced by date + dose_value |
| Stable insulin dose for 90+ days | `dose_era` (insulin) filtered by duration |
| Lab changes after dose adjustment | `dose_era` + `measurement` before/after dose change |
