---
hide:
  - footer
title: Drug Era
---

# Drug Era

**Epic equivalent**: No direct equivalent — derived from medication records

The `drug_era` table represents **continuous periods of medication exposure**, aggregated from individual `drug_exposure` records using persistence window gap logic. It answers "how long was the patient on this medication?" rather than "how many prescriptions were written?"

Drug eras work at the **RxNorm ingredient level** (e.g., "metformin", not a specific brand or formulation).

## Field Reference

??? example "Field reference (click to expand)"

    | OMOP Field | What It Captures |
    |---|---|
    | `drug_era_id` | Unique identifier |
    | `person_id` | Links to the patient |
    | `drug_concept_id` | RxNorm ingredient concept |
    | `drug_era_start_date` | First day of continuous exposure |
    | `drug_era_end_date` | Last day + persistence window |
    | `drug_exposure_count` | Number of source records collapsed |
    | `gap_days` | Total gap days tolerated within the era |

## What to Watch For

!!! warning "Common pitfalls"

    **Derived, not raw**
    :   Eras are inferred from prescription/administration records. They may not align exactly with actual medication use.

    **Gap logic is configurable**
    :   Typically 30 days between fills. Check your site's ETL configuration.

    **Ingredient-level only**
    :   Eras are at the RxNorm ingredient level, not brand or formulation. Multiple brand-name prescriptions for the same ingredient collapse into one era.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Typical duration of statin therapy | `drug_era` (statin concepts) + era duration |
| Metformin discontinuation within first year | `drug_era` (metformin) filtered by duration |
| Treatment-free intervals in oncology | `drug_era` (chemo agents) + gaps between eras |
| Overlapping insulin and GLP-1 agonist use | `drug_era` with class-level concepts + overlap logic |
| Fragmented adherence patterns by drug class | `gap_days` + `drug_exposure_count` |
