---
hide:
  - footer
title: Cost
---

# Cost

**Epic equivalent**: Professional/facility billing / Itemized charges / Revenue cycle exports

The `cost` table stores **financial data linked to clinical events** — billed charges, allowed amounts, patient out-of-pocket, and payer payments. Each row ties a cost to a specific procedure, drug, device, or visit.

Heavily used in claims-derived OMOP. In EHR-derived instances like Emory's, this table is **sparse**.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `cost_id` | Cost record ID | Unique identifier |
    | `cost_event_id` | Linked event ID | The clinical event this cost belongs to |
    | `cost_domain_id` | Event type | Which domain (procedure, drug, etc.) |
    | `cost_type_concept_id` | Cost type | Billed, paid, negotiated rate, etc. |
    | `currency_concept_id` | Currency | USD, etc. |
    | `total_charge` | Billed amount | List price from the provider |
    | `total_cost` | Allowed amount | Payer-approved amount |
    | `total_paid` | Paid amount | Sum from all sources |
    | `paid_by_payer` | Payer contribution | Amount covered by insurer |
    | `paid_by_patient` | Patient payment | Copay + deductible + coinsurance |
    | `paid_patient_copay`, `paid_patient_coinsurance`, `paid_patient_deductible` | Detailed patient responsibility | Granular patient cost breakdown |
    | `payer_plan_period_id` | Coverage link | Links to insurance enrollment period |
    | `drg_concept_id` | DRG | Inpatient billing classification |

## What to Watch For

!!! warning "Common pitfalls"

    **Sparse at Emory**
    :   Most EHR systems don't include detailed cost data unless merged with claims. See [Known Issues](../../../../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) for current status.

    **Charge vs. cost vs. paid**
    :   `total_charge` (list price) and `total_cost` (allowed amount) can differ enormously. Know which is appropriate for your analysis.

    **Multiple cost rows per event**
    :   Surgeries may have separate facility, professional, and anesthesia cost components.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Out-of-pocket cost for MRI by region | `procedure_occurrence` + `cost` + `location.zip` |
| Commercial vs. Medicaid payment structures | `cost` + `payer_plan_period.payer_concept_id` |
| Total hospitalization cost for COVID-19 | `condition_occurrence` + `visit_occurrence` + `cost` |
| Insulin therapy cost by plan type | `drug_exposure` + `cost` + `plan_concept_id` |
| Colonoscopy copays in high-deductible plans | `procedure_occurrence` + `cost.paid_patient_copay` |
