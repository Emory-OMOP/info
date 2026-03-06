---
hide:
  - footer
title: DBT Pipeline Tests
---

# DBT Pipeline Tests

Column-level test definitions for every table in Emory's OMOP ETL pipeline. All 13 tables currently pass.

!!! tip "How to read these tables"
    - **not_null** — column must not contain NULL values
    - **unique** — column values must be unique
    - **FK → table.column** — foreign key referential integrity check
    - **FK → concept** — concept FK check, excluding `0` and `-99` (Emory's "flavor of null")
    - **FK → concept (Domain)** — same as above, with domain validation
    - *Italic* entries are **commented out** — not yet active at this ETL stage, applicable to the final Redshift instance only

<!-- DBT_CURRENT_START -->

## Current (v1.0.0)

??? abstract "care_site — column-level tests"

    The CARE_SITE table contains uniquely identified institutional units where healthcare delivery is practiced (offices, wards, hospitals, clinics, etc.).

    | Column | Type | Tests |
    |--------|------|-------|
    | care_site_id | int | — |
    | care_site_name | varchar(255) | — |
    | place_of_service_concept_id | int | FK → concept |
    | location_id | int | FK → location.location_id |
    | care_site_source_value | varchar(50) | — |
    | place_of_service_source_value | varchar(50) | — |

??? abstract "condition_occurrence — column-level tests"

    Records of events suggesting the presence of a disease or medical condition — diagnoses, signs, or symptoms observed by a provider or reported by the patient.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | condition_concept_id | int | not_null, FK → concept (Condition) |
    | condition_start_date | date | not_null |
    | condition_start_datetime | timestamp | — |
    | condition_end_date | date | — |
    | condition_end_datetime | timestamp | — |
    | condition_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | condition_status_concept_id | int | FK → concept (Condition Status) |
    | stop_reason | varchar(20) | — |
    | provider_id | int | FK → provider.provider_id |
    | visit_occurrence_id | int | FK → visit_occurrence.visit_occurrence_id |
    | visit_detail_id | int | — |
    | condition_source_value | varchar(50) | — |
    | condition_source_concept_id | int | FK → concept |
    | condition_status_source_value | varchar(50) | — |
    | _source_primary_key | varchar(255) | — |
    | _source_primary_key_source | varchar(255) | — |

??? abstract "death — column-level tests"

    Contains the clinical event for how and when a person dies. A person can have up to one record if the source system contains evidence about the death.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | death_date | date | not_null |
    | death_datetime | timestamp | — |
    | death_type_concept_id | int | FK → concept (Type Concept) |
    | cause_concept_id | int | FK → concept |
    | cause_source_value | varchar(50) | — |
    | cause_source_concept_id | int | FK → concept |

??? abstract "device_exposure — column-level tests"

    Captures a person's exposure to a foreign physical object or instrument used for diagnostic or therapeutic purposes — implantable objects, medical equipment, supplies, and procedural instruments.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | device_concept_id | int | not_null, FK → concept (Device) |
    | device_exposure_start_date | date | not_null |
    | device_exposure_start_datetime | timestamp | — |
    | device_exposure_end_date | date | — |
    | device_exposure_end_datetime | timestamp | — |
    | device_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | unique_device_id | string | — |
    | production_id | string | — |
    | quantity | int | — |
    | provider_id | int | FK → provider.provider_id |
    | visit_occurrence_id | int | FK → visit_occurrence.visit_occurrence_id |
    | visit_detail_id | int | — |
    | device_source_value | string | — |
    | device_source_concept_id | int | FK → concept |
    | unit_concept_id | int | FK → concept (Unit) |
    | unit_source_value | string | — |
    | unit_source_concept_id | int | FK → concept |
    | _source_primary_key | string | — |
    | _source_primary_key_source | varchar(52) | — |

??? abstract "drug_exposure — column-level tests"

    Records about exposure to a drug ingested or otherwise introduced into the body — prescription and over-the-counter medicines, vaccines, and large-molecule biologic therapies.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | drug_concept_id | int | not_null, FK → concept (Drug) |
    | drug_exposure_start_date | date | not_null |
    | drug_exposure_start_datetime | timestamp | — |
    | drug_exposure_end_date | date | not_null |
    | drug_exposure_end_datetime | timestamp | — |
    | verbatim_end_date | date | — |
    | drug_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | stop_reason | varchar(20) | — |
    | refills | int | — |
    | quantity | double | — |
    | days_supply | int | — |
    | sig | string | — |
    | route_concept_id | int | FK → concept (Route) |
    | lot_number | varchar(50) | — |
    | provider_id | int | FK → provider.provider_id |
    | visit_occurrence_id | int | FK → visit_occurrence.visit_occurrence_id |
    | visit_detail_id | int | — |
    | drug_source_value | varchar(250) | — |
    | drug_source_concept_id | int | FK → concept |
    | route_source_value | varchar(50) | — |
    | dose_unit_source_value | varchar(50) | — |
    | _source_primary_key | string | — |
    | _source_primary_key_source | varchar(255) | — |

??? abstract "location — column-level tests"

    Represents a generic way to capture physical location or address information of persons and care sites.

    | Column | Type | Tests |
    |--------|------|-------|
    | location_id | int | not_null, unique |
    | address_1 | varchar(50) | — |
    | address_2 | varchar(50) | — |
    | city | varchar(50) | — |
    | state | varchar(2) | — |
    | zip | varchar(10) | — |
    | county | varchar(20) | — |
    | location_source_value | varchar(255) | — |
    | country_concept_id | int | FK → concept |
    | country_source_value | varchar(80) | — |
    | latitude | double | — |
    | longitude | double | — |

??? abstract "measurement — column-level tests"

    Records of structured values (numerical or categorical) obtained through systematic examination or testing — laboratory tests, vital signs, quantitative pathology findings, etc.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | measurement_concept_id | int | not_null, FK → concept (Measurement) |
    | measurement_date | date | not_null |
    | measurement_datetime | timestamp | — |
    | measurement_time | varchar(10) | — |
    | measurement_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | operator_concept_id | int | FK → concept |
    | value_as_number | double | — |
    | value_as_concept_id | int | FK → concept |
    | unit_concept_id | int | FK → concept (Unit) |
    | range_low | double | — |
    | range_high | double | — |
    | provider_id | int | FK → provider.provider_id |
    | visit_occurrence_id | int | FK → visit_occurrence.visit_occurrence_id |
    | visit_detail_id | int | — |
    | measurement_source_value | varchar(50) | — |
    | measurement_source_concept_id | int | FK → concept |
    | unit_source_value | varchar(50) | — |
    | unit_source_concept_id | int | FK → concept |
    | value_source_value | varchar(50) | — |
    | measurement_event_id | int | — |
    | meas_event_field_concept_id | int | FK → concept |
    | _source_primary_key | varchar(255) | — |
    | _source_primary_key_source | varchar(255) | — |

??? abstract "observation — column-level tests"

    Clinical facts about a person obtained in the context of examination, questioning, or a procedure. Captures data that cannot be represented by other domains.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | observation_concept_id | int | not_null, FK → concept |
    | observation_date | date | not_null |
    | observation_datetime | timestamp | — |
    | observation_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | value_as_number | double | — |
    | value_as_string | varchar(60) | — |
    | value_as_concept_id | int | FK → concept |
    | qualifier_concept_id | int | FK → concept |
    | unit_concept_id | int | FK → concept (Unit) |
    | provider_id | int | FK → provider.provider_id |
    | visit_occurrence_id | int | FK → visit_occurrence.visit_occurrence_id |
    | visit_detail_id | int | — |
    | observation_source_value | varchar(50) | — |
    | observation_source_concept_id | int | FK → concept |
    | unit_source_value | varchar(50) | — |
    | qualifier_source_value | varchar(50) | — |
    | value_source_value | varchar(50) | — |
    | observation_event_id | int | — |
    | obs_event_field_concept_id | int | FK → concept |
    | _source_primary_key | varchar(255) | — |
    | _source_primary_key_source | varchar(255) | — |

??? abstract "person — column-level tests"

    Central identity management for all persons in the database. Contains records that uniquely identify each person or patient, along with demographic information.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, unique |
    | gender_concept_id | int | not_null, FK → concept (Gender) |
    | year_of_birth | int | not_null |
    | month_of_birth | int | — |
    | day_of_birth | int | — |
    | birth_datetime | timestamp | — |
    | race_concept_id | int | not_null, FK → concept (Race) |
    | ethnicity_concept_id | int | not_null, FK → concept (Ethnicity) |
    | location_id | int | FK → location.location_id |
    | provider_id | int | FK → provider.provider_id |
    | care_site_id | int | FK → care_site.care_site_id |
    | person_source_value | varchar(50) | — |
    | gender_source_value | varchar(50) | — |
    | gender_source_concept_id | int | FK → concept |
    | race_source_value | varchar(50) | — |
    | race_source_concept_id | int | FK → concept |
    | ethnicity_source_value | varchar(50) | — |
    | ethnicity_source_concept_id | int | FK → concept |

??? abstract "procedure_occurrence — column-level tests"

    Records of activities or processes ordered by, or carried out by, a healthcare provider on the patient with a diagnostic or therapeutic purpose.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | procedure_concept_id | int | not_null, FK → concept (Procedure) |
    | procedure_date | date | not_null |
    | procedure_datetime | timestamp | — |
    | procedure_end_date | date | — |
    | procedure_end_datetime | timestamp | — |
    | procedure_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | modifier_concept_id | int | FK → concept |
    | quantity | int | — |
    | provider_id | int | FK → provider.provider_id |
    | visit_occurrence_id | int | FK → visit_occurrence.visit_occurrence_id |
    | visit_detail_id | int | — |
    | procedure_source_value | varchar(50) | — |
    | procedure_source_concept_id | int | FK → concept |
    | modifier_source_value | varchar(50) | — |
    | _source_primary_key | varchar(255) | — |
    | _source_primary_key_source | varchar(255) | — |

??? abstract "provider — column-level tests"

    Uniquely identified healthcare providers — individuals providing hands-on healthcare to patients (physicians, nurses, midwives, physical therapists, etc.).

    | Column | Type | Tests |
    |--------|------|-------|
    | provider_id | int | not_null, unique |
    | provider_name | string | — |
    | npi | string | — |
    | dea | string | — |
    | specialty_concept_id | int | FK → concept |
    | care_site_id | int | FK → care_site.care_site_id |
    | year_of_birth | int | — |
    | gender_concept_id | int | — |
    | provider_source_value | string | — |
    | specialty_source_value | string | — |
    | specialty_source_concept_id | int | FK → concept |
    | gender_source_value | string | — |
    | gender_source_concept_id | int | FK → concept |

??? abstract "visit_detail — column-level tests"

    Details of each record in the parent visit_occurrence table — movement between units during an inpatient stay, claim lines within an insurance claim, etc.

    | Column | Type | Tests |
    |--------|------|-------|
    | person_id | int | not_null, FK → person.person_id |
    | visit_detail_concept_id | int | not_null, FK → concept (Visit) |
    | visit_detail_start_date | date | not_null |
    | visit_detail_start_datetime | timestamp | — |
    | visit_detail_end_date | date | not_null |
    | visit_detail_end_datetime | timestamp | — |
    | visit_detail_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | provider_id | int | FK → provider.provider_id |
    | care_site_id | int | FK → care_site.care_site_id |
    | visit_detail_source_value | varchar(50) | — |
    | visit_detail_source_concept_id | int | FK → concept |
    | admitted_from_concept_id | int | FK → concept (Visit) |
    | admitted_from_source_value | varchar(50) | — |
    | discharged_to_concept_id | int | FK → concept (Visit) |
    | discharged_to_source_value | varchar(50) | — |
    | preceding_visit_detail_id | int | — |
    | parent_visit_detail_id | int | — |
    | visit_occurrence_id | int | — |
    | _source_primary_key | string | — |
    | _source_primary_key_source | varchar(255) | — |

??? abstract "visit_occurrence — column-level tests"

    Events where persons engage with the healthcare system for a duration of time. Defined by whether the patient comes to an institution or vice versa.

    | Column | Type | Tests |
    |--------|------|-------|
    | visit_occurrence_id | int | — |
    | person_id | int | not_null, FK → person.person_id |
    | visit_concept_id | int | not_null, FK → concept (Visit) |
    | visit_start_date | date | not_null |
    | visit_start_datetime | timestamp | — |
    | visit_end_date | date | not_null |
    | visit_end_datetime | timestamp | — |
    | visit_type_concept_id | int | not_null, FK → concept (Type Concept) |
    | provider_id | int | FK → provider.provider_id |
    | care_site_id | int | FK → care_site.care_site_id |
    | visit_source_value | varchar(50) | — |
    | visit_source_concept_id | int | FK → concept |
    | admitted_from_concept_id | int | FK → concept (Visit) |
    | admitted_from_source_value | varchar(50) | — |
    | discharged_to_concept_id | int | FK → concept (Visit) |
    | discharged_to_source_value | varchar(50) | — |
    | preceding_visit_occurrence_id | int | — |

<!-- DBT_CURRENT_END -->

## Changes by Release

<!-- DBT_RELEASE_LOG_START -->

???+ abstract "v1.0.0 — 133 tests (initial test suite)"

    133 tests across 13 tables — 133 pass, 0 fail


<!-- DBT_RELEASE_LOG_END -->
