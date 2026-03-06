---
hide:
  - footer
title: When to Use OMOP
---

# When to Use OMOP

Emory has multiple data platforms. Choosing the right one saves weeks of work. This guide helps you decide when Enterprise OMOP is the right fit — and when you should use Epic Clarity, Caboodle, or the Reporting Workbench instead.

## OMOP vs. Epic Resources at a Glance

| | **Enterprise OMOP** | **Epic Clarity / Caboodle** | **Reporting Workbench** |
|---|---|---|---|
| **Best for** | Multi-source research, standardized analytics, federated studies | Operational reporting, real-time data, full encounter detail | Quick ad-hoc operational reports |
| **Data sources** | Epic Clarity + Legacy CDW (Cerner) + Tumor Registry + OpenSpecimen | Epic only | Epic only |
| **Coding** | Standardized (SNOMED, RxNorm, LOINC) | Source codes (ICD-10, CPT, NDC) | Source codes |
| **Structure** | Patient-centric, cleaned, de-duplicated | Encounter-centric, raw | Pre-built report templates |
| **Timeliness** | Periodic refresh (lags real-time) | Near real-time | Near real-time |
| **Cross-site** | Yes — OHDSI network-compatible | No | No |
| **Vocabularies** | Hierarchies + mappings built in | Manual code lists | Manual code lists |

## Use OMOP When...

<div class="grid cards" markdown>

-   :material-check-circle:{ .lg .middle } **Comparative effectiveness research**

    ---

    Comparing treatments, outcomes, or utilization patterns across patient populations using standardized codes and clean data.

-   :material-check-circle:{ .lg .middle } **Federated or multi-site studies**

    ---

    Running analyses that need to be portable across OHDSI network sites. OMOP's standard structure means your query works everywhere.

-   :material-check-circle:{ .lg .middle } **Linking across data sources**

    ---

    Combining EHR data with tumor registry (Winship) or biospecimen data (OpenSpecimen) in a single, patient-centric model.

-   :material-check-circle:{ .lg .middle } **Cohort definitions using standard vocabularies**

    ---

    Using SNOMED hierarchies to capture "all diabetes" without manually listing every ICD-10 code. The vocabulary does the work.

-   :material-check-circle:{ .lg .middle } **Health equity and SDoH analyses**

    ---

    Standardized demographics, geographic data, and observation-domain social determinants in a research-ready format.

-   :material-check-circle:{ .lg .middle } **You need cleaned data**

    ---

    Non-events (cancelled encounters, missed medications, future procedures) are excluded. What's in OMOP is what actually happened.

</div>

## Don't Use OMOP When...

<div class="grid cards" markdown>

-   :material-close-circle:{ .lg .middle } **You need real-time or near-real-time data**

    ---

    OMOP refreshes on a periodic cadence. If your study depends on today's data, start with an Epic resource.

-   :material-close-circle:{ .lg .middle } **You need the full encounter narrative**

    ---

    OMOP captures what happened to the patient, not everything the provider intended. Cancelled orders, missed medications, and charge-only entries are excluded. Use Clarity for the complete picture.

-   :material-close-circle:{ .lg .middle } **Intent-to-treat analysis**

    ---

    If your study is about what care the provider *tried* to deliver (not what the patient received), Clarity or the CDW is the better source.

-   :material-close-circle:{ .lg .middle } **Historical demographic tracking**

    ---

    OMOP's `person` table is a snapshot — it doesn't track address changes, insurance transitions, or prior name/gender over time.

-   :material-close-circle:{ .lg .middle } **Operational or billing reports**

    ---

    Charge data, scheduling workflows, and real-time census are Epic's domain. OMOP is built for research, not operations.

</div>

## What OMOP Actually Is (Under the Hood)

Enterprise OMOP is a **structural standardization** and **semantic harmonization** of the data in Epic Clarity and the legacy Clinical Data Warehouse (primarily Cerner). In practice, that means:

Structural standardization
:   All medications land in `drug_exposure`, all diagnoses in `condition_occurrence`, all labs in `measurement` — regardless of which source system they came from.

Semantic harmonization
:   NDC codes map to RxNorm. ICD-10 maps to SNOMED. Local lab codes map to LOINC. The vocabulary layer translates source codes into a shared language.

Cleaning
:   Non-events are removed. Records are de-duplicated where applicable. The result is a curated research dataset, not a raw operational dump.

!!! warning "OMOP is not a replacement for Clarity"
    It's a research-optimized view of the same underlying data. If something looks unexpected in OMOP, the source of truth is always the Epic infrastructure. See our [Known Issues](../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) page for documented limitations.

## Next Steps

Ready to explore the data model? Head to the [OMOP Primers](../OMOP%20Primers/index.md) landing page for table-by-table guides, or jump straight to the tables you'll use most:

- [Person](../OMOP%20Primers/Standardized%20Categories/Clinical%20Data/Person/index.md) — start here, it's the center of everything
- [Visit Occurrence](../OMOP%20Primers/Standardized%20Categories/Clinical%20Data/Visits/Visit%20Occurrence/index.md) — the encounter equivalent
- [Condition Occurrence](../OMOP%20Primers/Standardized%20Categories/Clinical%20Data/Conditions/Condition%20Occurrence/index.md) — diagnoses and problems
- [Drug Exposure](../OMOP%20Primers/Standardized%20Categories/Clinical%20Data/Drugs/Drug%20Exposure/index.md) — medications
- [Measurement](../OMOP%20Primers/Standardized%20Categories/Clinical%20Data/Measurement/index.md) — labs and vitals
