---
hide:
  - footer
title: Device Exposure
---

# Device Exposure

**Epic equivalent**: Surgical implant records / Anesthesia records / Supply chain / DME claims

The `device_exposure` table captures **medical devices used on or implanted in a patient** — pacemakers, catheters, orthopedic implants, glucose monitors, stents, and other equipment. In Epic, this data comes from procedural documentation, implant registries, anesthesia records, and supply tracking systems.

Each row is a single device exposure event.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `device_exposure_id` | Device record ID | Unique identifier |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `device_concept_id` | Device concept | Standardized device (e.g., "Total hip prosthesis", "Central venous catheter") |
    | `device_exposure_start_date` | Implant / insertion date | When the device was used or placed |
    | `device_exposure_end_date` | Removal / usage end | When removed or exposure ended (often null for implants) |
    | `device_type_concept_id` | Data provenance | EHR, registry, billing, etc. |
    | `unique_device_id` | UDI / barcode | Device identifier from supply chain or implant logs |
    | `quantity` | Count | Number of devices (e.g., 2 stents) |
    | `provider_id` | Performing provider | Who inserted or documented the device |
    | `visit_occurrence_id` | Linked encounter | Visit context |
    | `device_source_value` | Local device code | Original code from the source system |

## What to Watch For

!!! warning "Common pitfalls"

    **Often sparse at Emory**
    :   Device data requires robust supply chain or implant registry integration. Check our [Known Issues](../../../../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) page for current population status.

    **Null end dates for implants**
    :   Permanent implants (pacemakers, prostheses) typically have no `device_exposure_end_date` unless explanted.

    **Device naming is still maturing**
    :   OMOP device concepts are less mature than drug or condition concepts. Validate `device_concept_id` definitions carefully when building cohorts.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Orthopedic implant prevalence | `device_concept_id` filtered for joint prostheses |
| Pacemaker to first complication | `device_exposure` (pacemaker) + `condition_occurrence` (complication) |
| Catheter-associated infection rates | `device_exposure` (catheter) + `condition_occurrence` (UTI/CLABSI) |
| Central lines placed in ICU | `device_exposure` + `visit_detail` (ICU filter) |
| Devices removed within 30 days | `device_exposure_end_date` − `device_exposure_start_date` |
