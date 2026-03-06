---
hide:
  - footer
---

# Era Algorithms

Era tables in OMOP consolidate individual clinical events into continuous **periods of exposure or condition**. Emory's era algorithms are implemented as stored procedures at the database level in Amazon Redshift, running after the core ELT pipeline completes.

## What Are Eras?

| Era Table | Derived From | Purpose |
|-----------|-------------|---------|
| **drug_era** | `drug_exposure` | Groups sequential drug exposures into continuous periods of drug use, collapsing gaps shorter than a persistence window (default: 30 days) |
| **condition_era** | `condition_occurrence` | Groups sequential condition records into continuous periods, identifying the span of time a patient experienced a condition |
| **dose_era** | `drug_exposure` | Groups sequential drug exposures at the same dose into continuous periods (optional, not currently generated) |

## How They Work

Era algorithms follow the [OHDSI-standard logic](https://ohdsi.github.io/CommonDataModel/cdm54.html#ERA):

1. **Ingredient rollup** — Drug exposures are rolled up from specific drug concepts to their active ingredient (e.g., "Tylenol 500mg tablet" becomes "Acetaminophen")
2. **Chronological ordering** — Records are sorted by person and start date
3. **Gap detection** — If the gap between the end of one event and the start of the next exceeds the persistence window, a new era begins
4. **Aggregation** — Overlapping or adjacent events within the window are merged into a single era record

## Implementation

The stored procedures are maintained in the enterprise repository:

[:octicons-arrow-right-24: Era stored procedures](https://github.service.emory.edu/LITS/omop_emory_dbt/tree/main/redshift_omop_stored_procedures){ .md-button }

!!! info "Pipeline sequencing"
    Era procedures run **after** the main DBT transformation pipeline completes, since they depend on finalized `drug_exposure` and `condition_occurrence` tables. They are orchestrated as a downstream step in the Airflow DAG.

## Related Pages

- [:octicons-arrow-right-24: ELT Overview](../index.md) — the overall Extract, Load, Transform architecture
- [:octicons-arrow-right-24: Data Quality Results](../../../Data%20Quality/Data%20Quality%20Results/index.md) — test results including era table checks
- [:octicons-arrow-right-24: OHDSI Conventions](../../../Observed%20Conventions/OHDSI%20Conventions/index.md) — standard conventions Emory follows