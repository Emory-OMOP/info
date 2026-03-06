---
hide:
  - footer
title: Provider
---

# Provider

**Epic equivalent**: Provider master table / Attending, ordering, performing, authoring providers

The `provider` table represents **individual clinicians** — physicians, residents, nurses, PAs, therapists, and other care team members. In Epic, this maps to the provider master table referenced across encounters, procedures, prescriptions, and documentation.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `provider_id` | Provider ID | Unique identifier, referenced across OMOP tables |
    | `provider_name` | Clinician name | Often redacted in de-identified datasets |
    | `npi` | National Provider Identifier | Standard U.S. NPI (if available) |
    | `dea` | DEA number | For controlled substance research (rarely populated) |
    | `specialty_concept_id` | Provider specialty | Standardized concept (e.g., "Internal Medicine", "Medical Oncology") |
    | `care_site_id` | Affiliated facility | Where the provider primarily practices |
    | `year_of_birth` | Year of birth | Rarely populated |
    | `gender_concept_id` | Provider gender | From HR systems (workforce analytics) |
    | `provider_source_value` | Local provider ID | Original ID from Epic (e.g., PROVIDER_ID in Clarity) |
    | `specialty_source_value` | Raw specialty string | Source system's specialty label |

## What to Watch For

!!! warning "Common pitfalls"

    **Not linked on all events**
    :   Many OMOP ETLs omit `provider_id` from certain tables if the source doesn't track it. Don't assume universal coverage.

    **Names often redacted**
    :   Especially in de-identified datasets. Use `provider_id` for joins, not names.

    **Specialty mapping is limited at Emory**
    :   Specialty codes vary by EHR and Emory's mapping is a work in progress. Validate `specialty_concept_id` before using as a primary filter.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Providers with most uncontrolled diabetes patients | `measurement` + `condition_occurrence` + `provider_id` |
| Opioid prescribing by provider specialty | `drug_exposure` + `provider.specialty_concept_id` |
| Surgical procedure volume by surgeon | `procedure_occurrence` + `provider.specialty_concept_id` |
| Documentation patterns by provider type | `note` + `provider_id` + `note_type_concept_id` |
| Provider vs. care site attribution | Any clinical table + `provider_id` + `care_site_id` |
