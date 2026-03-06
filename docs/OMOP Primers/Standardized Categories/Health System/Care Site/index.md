---
hide:
  - footer
title: Care Site
---

# Care Site

**Epic equivalent**: Facility / Department IDs / Clinic names / Cost center groupings

The `care_site` table represents **physical locations or organizational units** where care is delivered — hospitals, clinics, departments, specialty units, and service lines. In Epic, this maps to facility and department IDs used in scheduling and encounter metadata.

`care_site_id` is referenced by `visit_occurrence`, `person`, and `provider` to indicate *where* care was delivered.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `care_site_id` | Department / Facility ID | Unique identifier |
    | `care_site_name` | Clinic / facility name | Human-readable name (e.g., "Emory Winship Cancer Center") |
    | `place_of_service_concept_id` | Setting type | Standardized concept: inpatient hospital, outpatient clinic, etc. |
    | `location_id` | Physical address | Foreign key to `location` table |
    | `care_site_source_value` | Local care site code | Original ID (e.g., CLARITY_DEPARTMENT_ID) |
    | `place_of_service_source_value` | Raw POS string | Local text ("ED", "Ambulatory", etc.) |

## What to Watch For

!!! warning "Common pitfalls"

    **Granularity varies**
    :   Some data models use departments as care sites; others use whole facilities. Know what your data contains.

    **Not all visits link to a care site**
    :   Especially for billing or claims-derived data. Validate completeness before filtering on `care_site_id`.

    **Use `location` for geospatial work**
    :   `care_site` is the logical unit. `location` (via `location_id`) provides the physical address and coordinates.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Patients seen at the main cancer center | `visit_occurrence.care_site_id` + `care_site_name` |
| Hypertension control rates by primary care clinic | `measurement` + `visit_occurrence` + `care_site_id` |
| Procedure volume by surgical department | `procedure_occurrence` + `visit_occurrence.care_site_id` |
| Geocoding care delivery locations | `care_site.location_id` + `location.latitude/longitude` |
| Readmission rates by care site | `visit_occurrence.care_site_id` + readmission logic |
