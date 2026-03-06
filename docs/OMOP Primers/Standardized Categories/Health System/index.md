---
hide:
  - footer
title: Health System
---

# Health System

These tables describe **where** care happens and **who** provides it. In Epic, this information is spread across the provider master, facility/department records, and patient registration. In OMOP, it's consolidated into three tables that link to clinical events.

<div class="grid cards" markdown>

-   :material-map-marker:{ .lg .middle } **Location**

    ---

    Geographic/address data for patients and facilities. Maps to registration addresses and facility records in Epic. Often de-identified.

    [:octicons-arrow-right-24: Location](Location/index.md){ .md-button }

-   :material-hospital-building:{ .lg .middle } **Care Site**

    ---

    Hospitals, clinics, departments, and service lines. Maps to Epic facility and department IDs. Referenced by `visit_occurrence`, `person`, and `provider`.

    [:octicons-arrow-right-24: Care Site](Care%20Site/index.md){ .md-button }

-   :material-doctor:{ .lg .middle } **Provider**

    ---

    Individual clinicians: physicians, nurses, PAs, therapists. Maps to Epic's provider master. Supports attribution and practice pattern analysis.

    [:octicons-arrow-right-24: Provider](Provider/index.md){ .md-button }

</div>

!!! info "How these connect"
    `location` holds addresses. `care_site` references a `location_id` for its physical address. `provider` references a `care_site_id` for affiliation. Clinical tables like `visit_occurrence` reference both `provider_id` and `care_site_id` to attribute events.
