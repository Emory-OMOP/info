---
hide:
  - footer
title: Location
---

# Location

**Epic equivalent**: Patient registration addresses / Facility address records / Provider contact info

The `location` table holds **geographic and address data** for patients, care sites, and providers. In Epic, this comes from patient registration addresses and facility records. In OMOP, other tables (`person`, `care_site`, `provider`) reference `location_id` to indicate where something or someone is located.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `location_id` | Address ID | Unique identifier |
    | `address_1`, `address_2` | Street address | Typically suppressed in de-identified datasets |
    | `city` | City | City name |
    | `state` | State | State/province code (e.g., "GA") |
    | `zip` | ZIP / postal code | 5- or 9-digit code |
    | `county` | County | May be derived from ZIP |
    | `location_source_value` | Original address ID | Local ID from the source system |
    | `country_concept_id` | Country | OMOP concept for country |
    | `latitude`, `longitude` | Geo-coordinates | For geospatial analysis (not always populated) |

## What to Watch For

!!! warning "Common pitfalls"

    **De-identification limits access**
    :   Address fields are often partially or fully removed under HIPAA. Only select Emory staff have full access to this table.

    **ZIP alone may not be enough**
    :   Many SDoH analyses require linking ZIP to census tract, ADI, or SVI indices — this must be done outside OMOP.

    **Location is not care site**
    :   `location` holds addresses. `care_site` and `provider` *reference* `location_id` for their physical location.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Patients in rural ZIP codes | `person.location_id` + `location.zip` + rural-urban crosswalk |
| Regional variation in hypertension treatment | `drug_exposure` + `person.location_id` + `location.state` |
| Medically underserved care site locations | `care_site.location_id` + `location.zip` |
| Outcomes by neighborhood deprivation index | `location.zip` + external ADI/SVI mapping |
| Distance from home to cancer center | `person.location_id` + `location.latitude/longitude` + geodistance |
