---
hide:
  - footer
title: Payer Plan Period
---

# Payer Plan Period

**Epic equivalent**: Registration / ADT insurance data / Eligibility feeds

The `payer_plan_period` table captures **spans of insurance coverage** under specific plans and payers. In Epic, this comes from registration and insurance eligibility feeds. Each row is a continuous period of enrollment or coverage.

Essential for **eligibility criteria**, **payer stratification**, and **continuous enrollment filters**. Sparse in EHR-derived OMOP including Emory's.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `payer_plan_period_id` | Coverage segment ID | Unique identifier |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `payer_plan_period_start_date` | Coverage start | First day of active coverage |
    | `payer_plan_period_end_date` | Coverage end | Last day of coverage |
    | `payer_concept_id` | Payer organization | "Medicare", "Private payer", etc. |
    | `payer_source_value` | Raw payer name/code | Original payer ID from source |
    | `plan_concept_id` | Plan type | HMO, PPO, etc. |
    | `plan_source_value` | Local plan name | Original plan name (e.g., "BlueCross HMO Plan 2023") |
    | `sponsor_concept_id` | Employer/group | Sponsoring organization (rarely populated) |
    | `family_source_value` | Family group code | Household policy ID (for dependent analyses) |

## What to Watch For

!!! warning "Common pitfalls"

    **Often absent in EHR-derived OMOP**
    :   This table is primarily populated from claims or linked eligibility data. Emory's is limited. See [Known Issues](../../../../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) for updates.

    **Coverage, not claims**
    :   This table represents *insurance enrollment*, not service-level claim detail.

    **Validate continuity**
    :   Gaps between coverage periods are possible. Don't assume continuous enrollment without checking.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Continuous Medicaid coverage during pregnancy | `payer_plan_period` + `condition_occurrence` (pregnancy) |
| Cancer screening rates by insurance type | `payer_concept_id` + `procedure_occurrence` or `measurement` |
| Average commercial plan enrollment duration | `payer_plan_period` end − start date |
| 12-month continuous eligibility filter | `payer_plan_period` duration filtering |
| Access to high-cost therapies by payer type | `drug_exposure` + `payer_concept_id` |
