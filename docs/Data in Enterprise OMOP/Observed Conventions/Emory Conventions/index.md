---
hide:
  - footer
---

# Emory Conventions

Emory-specific additions to the OMOP CDM. Standard OHDSI conventions are **not modified** — only additions are made to support Emory's research community (e.g., data provenance, PII for re-identification across sources). OHDSI tools ignore additional columns and tables, so these additions do not interfere with standard tooling.

??? abstract "Quick reference — what's on this page"
    **Tables** — Emory-added mapping and PII tables:

    - [CARE_SITE_MAPPING](#tables) — Care site ID generation and source tracking
    - [LOCATION_MAPPING](#tables) — Location ID generation and source tracking
    - [PROVIDER_MAPPING](#tables) — Provider deduplication across CDW/Epic
    - [VISIT_OCCURRENCE_MAPPING](#tables) — Visit occurrence linking across sources
    - [OMOP_PII.PATIENT](#hidden-tables) — Protected PII table (restricted access)

    **Fields** — Emory-added columns across CDM tables:

    - [`_source_primary_key`](#fields) — Granular source key for each record
    - [`_source_primary_key_source`](#fields) — Machine-readable provenance of the source key

## OMOP-CDM v5.4 Data Model Conventions

**Origin**: [OHDSI](https://ohdsi.github.io/CommonDataModel/dataModelConventions.html)

OHDSI's General, Vocabulary, and Mapping conventions are all observed by Emory, as of site access date, April 23, 2025. The following listed conventions are specific to Emory's implementation of the CDM and are not part of the standard OMOP CDM conventions.

## Tables

Several tables have been added to the CDM to support the needs of Emory's research community. These tables are not part of the standard OMOP CDM but have been created to enhance data management and analysis capabilities.

!!! warning "ID stability"
    IDs in these mapping tables (except `person_id` in `OMOP_PII.PATIENT`) are **not stable between loads**. Do not use them as durable identifiers across data refreshes.

??? example "CARE_SITE_MAPPING — CDW and Epic"

    Care site ID generation and source tracking. IDs are assigned first from CDW care sites, then by appending incremental IDs for Epic care sites.

    | CDM Field | Description | ETL Convention | Type | PK | FK |
    |---|---|---|---|---|---|
    | `care_site_id` | Unique identifier for the care site | Generated in this table for the final `care_site` OMOP table. **Not stable between loads.** | Integer | Yes | — |
    | `care_site_source_value` | Source value for the care site | Source value differs between CDW and Epic with regard to FK values | varchar | — | CDW: `lkp_location.location_key`; Epic: `clarity_pos.pos_id` |
    | `care_site_source` | Database source | Hardcoded for either Epic or CDW sources | varchar | — | — |

??? example "LOCATION_MAPPING — CDW and Epic"

    Location ID generation and source tracking. IDs are assigned first from CDW, then by appending incremental IDs for Epic.

    | CDM Field | Description | ETL Convention | Type | PK | FK |
    |---|---|---|---|---|---|
    | `location_id` | Unique identifier for the location | Generated in this table for the final `location` OMOP table. **Not stable between loads.** | Integer | Yes | — |
    | `location_source_value` | Source value for the location | Source value differs between CDW and Epic. Epic's source values are concatenated when present (or `''` if null): 1) `PATIENT.ADD_LINE_1`, 2) `PATIENT.ADD_LINE_2`, 3) `PATIENT.CITY`, 4) `ZC_STATE.ABBR`, 5) `PATIENT.ZIP`, 6) `ZC_COUNTY.COUNTY_C` | varchar | — | CDW: `lkp_facility.facility_key`; Epic: see concatenation |
    | `location_source` | Database source | Hardcoded for either Epic or CDW sources | varchar | — | — |

??? example "PROVIDER_MAPPING — CDW and Epic"

    Provider deduplication across CDW and Epic. Deduplication is based on NPI only, given sparse details elsewhere for trusted matching. This limitation is noted in [Known Issues](../../Data%20Quality/Known%20Issues/index.md).

    | CDM Field | Description | ETL Convention | Type | PK | FK |
    |---|---|---|---|---|---|
    | `provider_id` | Unique identifier for the provider | Generated in this table for the final `provider` OMOP table. **Not stable between loads.** | Integer | Yes | — |
    | `provider_source_value` | Source value for the provider | Source value differs between CDW and Epic. NPI-based deduplication across sources where possible | varchar | — | CDW: `lkp_personnel.personnel_id`; Epic: `clarity_ser.prov_id` |
    | `provider_source` | Database source | Hardcoded for either Epic or CDW sources | varchar | — | — |

??? example "VISIT_OCCURRENCE_MAPPING — CDW and Epic"

    Visit occurrence linking across sources. Deduplication is NPI-based where possible; limitations are noted in [Known Issues](../../Data%20Quality/Known%20Issues/index.md).

    | CDM Field | Description | ETL Convention | Type | PK | FK |
    |---|---|---|---|---|---|
    | `visit_occurrence_id` | Unique identifier for the visit occurrence | Generated in this table for the final `visit_occurrence` OMOP table. **Not stable between loads.** | Integer | Yes | — |
    | `visit_occurrence_source_value` | Source value for the encounter | Source value differs between CDW and Epic | varchar | — | CDW: `fact_encounter.encounter_key`; Epic: `PAT_ENC_HSP.PAT_ENC_CSN_ID` or `PAT_ENC.PAT_ENC_CSN_ID` |
    | `visit_occurrence_source` | Database source | Hardcoded for either Epic or CDW sources | varchar | — | — |

### Hidden Tables

The following tables are viewable by only certain members of a research team, given the sensitive nature of the data. They are protected from view so cannot be found in the OMOP schema. The `schema.table` convention is therefore used to identify the table in our production database.

??? example "OMOP_PII.PATIENT — CDW and Epic (restricted access)"

    !!! danger "Restricted"
        This table contains protected health information (PHI) and is only accessible to authorized team members.

    The `person_id` in this table **is stable** over time and across loads, unlike the mapping table IDs above.

    **Identity fields**

    | CDM Field | Description | Type | FK |
    |---|---|---|---|
    | `person_id` | Unique identifier for the person in the CDM | integer | CDW: `lkp_master_patient.person_id`; Epic: `deident_driver.person_id` |
    | `epic_pat_id` | Unique identifier in Epic | varchar | Epic: `patient.epic_pat_id` |
    | `pat_mrn_id` | Emory MRN from Epic. Often matches `empi_nbr` but not always due to CDW data collisions | varchar | Epic: `patient.pat_mrn_id` |
    | `empi_nbr` | CDW EMPI from Cerner | varchar | CDW: `lkp_patient.empi_nbr` |

    **Name fields**

    | CDM Field | Description | Type | FK |
    |---|---|---|---|
    | `epic_pat_last_nm` | Last name (Epic) | varchar | Epic: `patient.pat_last_name` |
    | `cdw_pat_last_nm` | Last name (CDW) | varchar | CDW: `lkp_patient.patient_last_nm` |
    | `epic_pat_first_nm` | First name (Epic) | varchar | Epic: `patient.pat_first_name` |
    | `cdw_pat_first_nm` | First name (CDW) | varchar | CDW: `lkp_patient.patient_first_nm` |
    | `epic_middle_name` | Middle name (Epic) | varchar | Epic: `patient.pat_middle_name` |
    | `cdw_middle_name` | Middle name (CDW) | varchar | CDW: `lkp_patient.patient_middle_nm` |
    | `epic_maiden_name` | Maiden name (Epic) | varchar | Epic: `patient_2.maiden_name` |
    | `cdw_maiden_name` | Maiden name (CDW) | varchar | CDW: `lkp_patient.patient_maiden_nm` |

    **Demographics and contact fields**

    | CDM Field | Description | Type | FK |
    |---|---|---|---|
    | `epic_birth_date` | Date of birth (Epic) | date | Epic: `patient.birth_date` |
    | `cdw_birth_date` | Date of birth (CDW) | date | CDW: `lkp_patient.birth_day_key` |
    | `epic_sex` | Sex/gender (Epic) | varchar | Epic: `zc_sex.name` |
    | `cdw_sex` | Sex/gender (CDW) | varchar | CDW: `lkp_patient.gender_desc` |
    | `epic_ssn` | SSN (Epic) | varchar | Epic: `patient.ssn` |
    | `cdw_ssn` | SSN (CDW) | varchar | CDW: `lkp_patient.patient_ssn_nbr` |
    | `epic_zip` | Zip code (Epic) | varchar | Epic: `patient.zip_code` |
    | `cdw_zip` | Zip code (CDW) | varchar | CDW: `lkp_patient.patient_address_zip_desc` |
    | `epic_email_address` | Email (Epic) | varchar | Epic: `patient.email_address` |
    | `cdw_email_address` | Email (CDW) | varchar | CDW: `lkp_patient.patient_email_address_nm` |
    | `epic_phone_cell` | Cell phone (Epic) — currently hardcoded to null | varchar | — |
    | `cdw_phone_cell` | Cell phone (CDW) | varchar | CDW: `lkp_patient.patient_phone_cell_nbr` |

## Fields

### General

These columns are added to standard OMOP CDM tables across the database to provide granular data provenance.

`_source_primary_key`
:   The primary key used to obtain the most granular data available to achieve distinct rows in the final OMOP table housing this column (e.g., `drug_exposure._source_primary_key`; `measurement._source_primary_key`).

    Aggregation across the primary key in a particular table may sometimes be required, as there are many changes to data in an EHR system that are not relevant to how data is represented in the OMOP CDM. For example, a patient's drug order may have been ordered by one clinician, modified by the pharmacist, cancelled by staff by mistake, and then re-added by the pharmacist. For research purposes, we are only interested in the final state of the drug order.

`_source_primary_key_source`
:   The exact location where the `_source_primary_key` was obtained. This should be nearly machine-readable, with the caveat being aggregations. For aggregations (such as taking a minimum table primary key where all other values are distinct for the row), the function used is appended to the `database.table.column` name following a caret `^`.

    For example, a drug administration from Epic data might be: `clarity_onprem_omop.order_med.order_med_id^MIN()`.

## Related Pages

- [:octicons-arrow-right-24: OHDSI Conventions](../OHDSI%20Conventions/index.md) — standard conventions Emory observes
- [:octicons-arrow-right-24: Documented Adherence](../Documented%20Adherence/index.md) — adherence tracking
- [:octicons-arrow-right-24: Known Issues](../../Data%20Quality/Known%20Issues/index.md) — known data quality limitations
