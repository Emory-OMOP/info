---
hide:
  - footer
title: Specimen
---

# Specimen

**Epic equivalent**: Specimen collection records / Surgical pathology / LIMS / Biobank systems

The `specimen` table captures **biological samples** collected from a patient — blood, tissue, urine, swabs, and other materials sent for lab analysis, pathology review, or biobanking. At Emory, Winship populates cancer biospecimen data through OpenSpecimen integration.

Each row is a single specimen. Note: the actual lab *results* go in `measurement` — this table captures sample metadata.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `specimen_id` | Specimen accession ID | Unique identifier |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `specimen_concept_id` | Sample type | Standardized type (blood, urine, tissue, etc.) |
    | `specimen_type_concept_id` | Data provenance | How captured (EHR, biobank, etc.) |
    | `specimen_date` | Collection date | When the sample was collected; `specimen_datetime` has time |
    | `quantity` | Amount collected | Volume or size (if available) |
    | `unit_concept_id` | Unit | mL, grams, etc. |
    | `anatomic_site_concept_id` | Collection site | Body part (e.g., "left breast", "bone marrow") |
    | `disease_status_concept_id` | Disease context | Whether collected in disease state (e.g., tumor tissue) |
    | `specimen_source_id` | Local specimen ID | Original ID from the lab system |
    | `specimen_source_value` | Local name/code | Original description from EHR/LIMS |

## What to Watch For

!!! warning "Common pitfalls"

    **Specimens are not measurements**
    :   The lab values go in `measurement`. This table captures *what was collected*, not *what the result was*.

    **Often underused**
    :   Many OMOP implementations don't fully populate this table unless biospecimen workflows are in place.

    **Critical for omics**
    :   This table becomes essential when linking to sequencing, proteomics, or precision medicine data.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Tumor tissue samples from breast cancer patients | `specimen` (tissue + anatomic site) + `condition_occurrence` (breast cancer) |
| Blood collection timing relative to drug start | `specimen.specimen_date` + `drug_exposure.drug_exposure_start_date` |
| CSF samples for diagnostic testing | `specimen_concept_id` (CSF) |
| Archived FFPE samples for lung cancer cases | `specimen_type_concept_id` + `anatomic_site_concept_id` + `condition_occurrence` |
| Biopsy-to-pathology report turnaround time | `specimen.specimen_date` + `note.note_date` (pathology notes) |
