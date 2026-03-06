---
hide:
  - footer
title: Data Quality Results
---

# Data Quality Results

## OHDSI Data Quality Dashboard — Release History

!!! info "How results are organized"
    Each release section shows the DQD pass rate, failure breakdown by table, and a diff from the previous release highlighting new failures, resolved issues, and persistent problems.

<!-- DQD_SUMMARY_START -->

???+ abstract "v1.0.0"

    **96.6%** pass rate — 2,374 checks, 81 failures

    #### Changes from v0.2.4

    **83 issues resolved**

    **25 new failures**

    - `CARE_SITE.PLACE_OF_SERVICE_CONCEPT_ID` — isStandardValidConcept
    - **CONDITION_OCCURRENCE** (2 checks)
        - `CONDITION_STATUS_CONCEPT_ID` — standardConceptRecordCompleteness
        - `CONDITION_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `DEATH.DEATH_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `DEVICE_EXPOSURE.DEVICE_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `DRUG_EXPOSURE.DRUG_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `DRUG_STRENGTH.INGREDIENT_CONCEPT_ID` — fkClass
    - `LOCATION.COUNTRY_CONCEPT_ID` — isForeignKey
    - `MEASUREMENT.MEASUREMENT_TYPE_CONCEPT_ID` — isStandardValidConcept
    - **OBSERVATION** (4 checks)
        - `OBSERVATION_CONCEPT_ID` — isStandardValidConcept
        - `OBSERVATION_TYPE_CONCEPT_ID` — isStandardValidConcept
        - `UNIT_CONCEPT_ID` — isStandardValidConcept
        - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
    - `PERSON.RACE_CONCEPT_ID` — isStandardValidConcept
    - `PROCEDURE_OCCURRENCE.PROCEDURE_TYPE_CONCEPT_ID` — isStandardValidConcept
    - **VISIT_DETAIL** (2 checks)
        - `DISCHARGED_TO_CONCEPT_ID` — isStandardValidConcept
        - `VISIT_DETAIL_TYPE_CONCEPT_ID` — isStandardValidConcept
    - **VISIT_OCCURRENCE** (8 checks)
        - `ADMITTED_FROM_CONCEPT_ID` — isForeignKey
        - `ADMITTED_FROM_CONCEPT_ID` — isStandardValidConcept
        - `ADMITTED_FROM_CONCEPT_ID` — standardConceptRecordCompleteness
        - `DISCHARGED_TO_CONCEPT_ID` — isForeignKey
        - `DISCHARGED_TO_CONCEPT_ID` — isStandardValidConcept
        - `DISCHARGED_TO_CONCEPT_ID` — standardConceptRecordCompleteness
        - `VISIT_CONCEPT_ID` — isStandardValidConcept
        - `VISIT_TYPE_CONCEPT_ID` — isStandardValidConcept

    ??? warning "Persistent failures (56)"

        - **CONDITION_ERA** (3 checks)
            - `CONDITION_ERA_END_DATE` — plausibleBeforeDeath
            - `CONDITION_ERA_START_DATE` — plausibleBeforeDeath
            - `CONDITION_ERA_START_DATE` — plausibleDuringLife
        - **CONDITION_OCCURRENCE** (6 checks)
            - `CONDITION_CONCEPT_ID` — plausibleGender (4 concepts)
            - `CONDITION_START_DATE` — withinVisitDates
            - `VISIT_DETAIL_ID` — isForeignKey
        - **DEATH** (3 checks)
            - `CAUSE_CONCEPT_ID` — standardConceptRecordCompleteness
            - `DEATH_DATE` — plausibleValueHigh
            - `DEATH_DATETIME` — plausibleValueHigh
        - `DEVICE_EXPOSURE.DEVICE_CONCEPT_ID` — isStandardValidConcept
        - **DRUG_EXPOSURE** (5 checks)
            - `DAYS_SUPPLY` — plausibleValueLow
            - `DRUG_CONCEPT_ID` — isStandardValidConcept
            - `QUANTITY` — plausibleValueLow
            - `ROUTE_CONCEPT_ID` — isStandardValidConcept
            - `VISIT_DETAIL_ID` — isForeignKey
        - **MEASUREMENT** (10 checks)
            - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (5 concepts)
            - `MEASUREMENT_SOURCE_CONCEPT_ID` — isForeignKey
            - `UNIT_CONCEPT_ID` — isStandardValidConcept
            - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VALUE_AS_CONCEPT_ID` — isForeignKey
            - `VISIT_DETAIL_ID` — isForeignKey
        - **OBSERVATION** (5 checks)
            - `OBSERVATION_SOURCE_CONCEPT_ID` — sourceConceptRecordCompleteness
            - `QUALIFIER_CONCEPT_ID` — isForeignKey
            - `UNIT_CONCEPT_ID` — isForeignKey
            - `VALUE_AS_CONCEPT_ID` — isForeignKey
            - `VISIT_DETAIL_ID` — isForeignKey
        - **OBSERVATION_PERIOD** (5 checks)
            - `table-level` — measurePersonCompleteness
            - `OBSERVATION_PERIOD_END_DATE` — plausibleBeforeDeath
            - `OBSERVATION_PERIOD_END_DATE` — plausibleDuringLife
            - `OBSERVATION_PERIOD_END_DATE` — plausibleValueHigh
            - `OBSERVATION_PERIOD_START_DATE` — plausibleStartBeforeEnd
        - **PERSON** (4 checks)
            - `ETHNICITY_SOURCE_CONCEPT_ID` — isForeignKey
            - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
            - `RACE_CONCEPT_ID` — fkDomain
            - `RACE_SOURCE_CONCEPT_ID` — isForeignKey
        - **PROCEDURE_OCCURRENCE** (5 checks)
            - `MODIFIER_CONCEPT_ID` — isForeignKey
            - `PROCEDURE_CONCEPT_ID` — plausibleGender
            - `PROCEDURE_CONCEPT_ID` — plausibleGenderUseDescendants
            - `PROCEDURE_DATE` — withinVisitDates
            - `VISIT_DETAIL_ID` — isForeignKey
        - **PROVIDER** (4 checks)
            - `CARE_SITE_ID` — isForeignKey
            - `GENDER_CONCEPT_ID` — isForeignKey
            - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
            - `SPECIALTY_SOURCE_CONCEPT_ID` — isForeignKey
        - `VISIT_DETAIL.VISIT_DETAIL_CONCEPT_ID` — standardConceptRecordCompleteness
        - **VISIT_OCCURRENCE** (4 checks)
            - `PRECEDING_VISIT_OCCURRENCE_ID` — isForeignKey
            - `VISIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VISIT_SOURCE_CONCEPT_ID` — isForeignKey
            - `VISIT_SOURCE_VALUE` — sourceValueCompleteness

    #### Failures by Table

    | Table | Failed | Total | Pass Rate |
    |-------|--------|-------|-----------|
    | OBSERVATION_PERIOD | 5 | 40 | 87.5% |
    | VISIT_OCCURRENCE | 12 | 103 | 88.3% |
    | DEATH | 4 | 41 | 90.2% |
    | OBSERVATION | 9 | 97 | 90.7% |
    | PROVIDER | 4 | 49 | 91.8% |
    | CONDITION_ERA | 3 | 43 | 93.0% |
    | PERSON | 5 | 85 | 94.1% |
    | DRUG_EXPOSURE | 6 | 124 | 95.2% |
    | CARE_SITE | 1 | 22 | 95.5% |
    | MEASUREMENT | 11 | 286 | 96.2% |
    | PROCEDURE_OCCURRENCE | 6 | 181 | 96.7% |
    | LOCATION | 1 | 33 | 97.0% |
    | VISIT_DETAIL | 3 | 112 | 97.3% |
    | CONDITION_OCCURRENCE | 8 | 303 | 97.4% |
    | DRUG_STRENGTH | 1 | 44 | 97.7% |
    | DEVICE_EXPOSURE | 2 | 107 | 98.1% |

    15 additional tables passed all checks with zero failures.


??? abstract "v0.2.4"

    **93.5%** pass rate — 2,201 checks, 144 failures

    #### Changes from v0.2.2

    **3 issues resolved**

    **3 new failures**

    - **MEASUREMENT** (3 checks)
        - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds
        - `MEASUREMENT_SOURCE_CONCEPT_ID` — isForeignKey
        - `VALUE_AS_CONCEPT_ID` — isForeignKey

    ??? warning "Persistent failures (136)"

        - **CONDITION_ERA** (3 checks)
            - `CONDITION_ERA_END_DATE` — plausibleBeforeDeath
            - `CONDITION_ERA_START_DATE` — plausibleBeforeDeath
            - `CONDITION_ERA_START_DATE` — plausibleDuringLife
        - **CONDITION_OCCURRENCE** (6 checks)
            - `CONDITION_CONCEPT_ID` — plausibleGender (4 concepts)
            - `CONDITION_START_DATE` — withinVisitDates
            - `VISIT_DETAIL_ID` — isForeignKey
        - **DEATH** (3 checks)
            - `CAUSE_CONCEPT_ID` — standardConceptRecordCompleteness
            - `DEATH_DATE` — plausibleValueHigh
            - `DEATH_DATETIME` — plausibleValueHigh
        - `DEVICE_EXPOSURE.DEVICE_CONCEPT_ID` — isStandardValidConcept
        - **DRUG_EXPOSURE** (6 checks)
            - `DAYS_SUPPLY` — plausibleValueLow
            - `DRUG_CONCEPT_ID` — isStandardValidConcept
            - `QUANTITY` — plausibleValueHigh
            - `QUANTITY` — plausibleValueLow
            - `ROUTE_CONCEPT_ID` — isStandardValidConcept
            - `VISIT_DETAIL_ID` — isForeignKey
        - **MEASUREMENT** (88 checks)
            - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (85 concepts)
            - `UNIT_CONCEPT_ID` — isStandardValidConcept
            - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VISIT_DETAIL_ID` — isForeignKey
        - **OBSERVATION** (5 checks)
            - `OBSERVATION_SOURCE_CONCEPT_ID` — sourceConceptRecordCompleteness
            - `QUALIFIER_CONCEPT_ID` — isForeignKey
            - `UNIT_CONCEPT_ID` — isForeignKey
            - `VALUE_AS_CONCEPT_ID` — isForeignKey
            - `VISIT_DETAIL_ID` — isForeignKey
        - **OBSERVATION_PERIOD** (6 checks)
            - `table-level` — measurePersonCompleteness
            - `OBSERVATION_PERIOD_END_DATE` — plausibleBeforeDeath
            - `OBSERVATION_PERIOD_END_DATE` — plausibleDuringLife
            - `OBSERVATION_PERIOD_END_DATE` — plausibleValueHigh
            - `OBSERVATION_PERIOD_START_DATE` — plausibleAfterBirth
            - `OBSERVATION_PERIOD_START_DATE` — plausibleStartBeforeEnd
        - **PERSON** (4 checks)
            - `ETHNICITY_SOURCE_CONCEPT_ID` — isForeignKey
            - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
            - `RACE_CONCEPT_ID` — fkDomain
            - `RACE_SOURCE_CONCEPT_ID` — isForeignKey
        - **PROCEDURE_OCCURRENCE** (5 checks)
            - `MODIFIER_CONCEPT_ID` — isForeignKey
            - `PROCEDURE_CONCEPT_ID` — plausibleGender
            - `PROCEDURE_CONCEPT_ID` — plausibleGenderUseDescendants
            - `PROCEDURE_DATE` — withinVisitDates
            - `VISIT_DETAIL_ID` — isForeignKey
        - **PROVIDER** (4 checks)
            - `CARE_SITE_ID` — isForeignKey
            - `GENDER_CONCEPT_ID` — isForeignKey
            - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
            - `SPECIALTY_SOURCE_CONCEPT_ID` — isForeignKey
        - `VISIT_DETAIL.VISIT_DETAIL_CONCEPT_ID` — standardConceptRecordCompleteness
        - **VISIT_OCCURRENCE** (4 checks)
            - `PRECEDING_VISIT_OCCURRENCE_ID` — isForeignKey
            - `VISIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VISIT_SOURCE_CONCEPT_ID` — isForeignKey
            - `VISIT_SOURCE_VALUE` — sourceValueCompleteness

    #### Failures by Table

    | Table | Failed | Total | Pass Rate |
    |-------|--------|-------|-----------|
    | MEASUREMENT | 91 | 271 | 66.4% |
    | OBSERVATION_PERIOD | 6 | 38 | 84.2% |
    | PROVIDER | 4 | 49 | 91.8% |
    | DEATH | 3 | 41 | 92.7% |
    | CONDITION_ERA | 3 | 43 | 93.0% |
    | OBSERVATION | 5 | 88 | 94.3% |
    | DRUG_EXPOSURE | 6 | 123 | 95.1% |
    | PERSON | 4 | 85 | 95.3% |
    | VISIT_OCCURRENCE | 8 | 206 | 96.1% |
    | PROCEDURE_OCCURRENCE | 5 | 163 | 96.9% |
    | CONDITION_OCCURRENCE | 6 | 300 | 98.0% |
    | DEVICE_EXPOSURE | 1 | 88 | 98.9% |
    | VISIT_DETAIL | 2 | 214 | 99.1% |

    10 additional tables passed all checks with zero failures.


??? abstract "v0.2.2"

    **93.5%** pass rate — 2,201 checks, 144 failures

    #### Changes from v0.2.0

    **228 issues resolved**

    **4 new failures**

    - `CARE_SITE.CARE_SITE_ID` — isPrimaryKey
    - `OBSERVATION_PERIOD.OBSERVATION_PERIOD_START_DATE` — plausibleAfterBirth
    - `PERSON.RACE_CONCEPT_ID` — fkDomain
    - `PROCEDURE_OCCURRENCE.PROCEDURE_DATE` — withinVisitDates

    ??? warning "Persistent failures (135)"

        - **CONDITION_ERA** (3 checks)
            - `CONDITION_ERA_END_DATE` — plausibleBeforeDeath
            - `CONDITION_ERA_START_DATE` — plausibleBeforeDeath
            - `CONDITION_ERA_START_DATE` — plausibleDuringLife
        - **CONDITION_OCCURRENCE** (6 checks)
            - `CONDITION_CONCEPT_ID` — plausibleGender (4 concepts)
            - `CONDITION_START_DATE` — withinVisitDates
            - `VISIT_DETAIL_ID` — isForeignKey
        - **DEATH** (3 checks)
            - `CAUSE_CONCEPT_ID` — standardConceptRecordCompleteness
            - `DEATH_DATE` — plausibleValueHigh
            - `DEATH_DATETIME` — plausibleValueHigh
        - `DEVICE_EXPOSURE.DEVICE_CONCEPT_ID` — isStandardValidConcept
        - **DRUG_EXPOSURE** (6 checks)
            - `DAYS_SUPPLY` — plausibleValueLow
            - `DRUG_CONCEPT_ID` — isStandardValidConcept
            - `QUANTITY` — plausibleValueHigh
            - `QUANTITY` — plausibleValueLow
            - `ROUTE_CONCEPT_ID` — isStandardValidConcept
            - `VISIT_DETAIL_ID` — isForeignKey
        - **MEASUREMENT** (89 checks)
            - `MEASUREMENT_CONCEPT_ID` — fkDomain
            - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (85 concepts)
            - `UNIT_CONCEPT_ID` — isStandardValidConcept
            - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VISIT_DETAIL_ID` — isForeignKey
        - **OBSERVATION** (6 checks)
            - `OBSERVATION_CONCEPT_ID` — standardConceptRecordCompleteness
            - `OBSERVATION_SOURCE_CONCEPT_ID` — sourceConceptRecordCompleteness
            - `QUALIFIER_CONCEPT_ID` — isForeignKey
            - `UNIT_CONCEPT_ID` — isForeignKey
            - `VALUE_AS_CONCEPT_ID` — isForeignKey
            - `VISIT_DETAIL_ID` — isForeignKey
        - **OBSERVATION_PERIOD** (5 checks)
            - `table-level` — measurePersonCompleteness
            - `OBSERVATION_PERIOD_END_DATE` — plausibleBeforeDeath
            - `OBSERVATION_PERIOD_END_DATE` — plausibleDuringLife
            - `OBSERVATION_PERIOD_END_DATE` — plausibleValueHigh
            - `OBSERVATION_PERIOD_START_DATE` — plausibleStartBeforeEnd
        - **PERSON** (3 checks)
            - `ETHNICITY_SOURCE_CONCEPT_ID` — isForeignKey
            - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
            - `RACE_SOURCE_CONCEPT_ID` — isForeignKey
        - **PROCEDURE_OCCURRENCE** (4 checks)
            - `MODIFIER_CONCEPT_ID` — isForeignKey
            - `PROCEDURE_CONCEPT_ID` — plausibleGender
            - `PROCEDURE_CONCEPT_ID` — plausibleGenderUseDescendants
            - `VISIT_DETAIL_ID` — isForeignKey
        - **PROVIDER** (4 checks)
            - `CARE_SITE_ID` — isForeignKey
            - `GENDER_CONCEPT_ID` — isForeignKey
            - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
            - `SPECIALTY_SOURCE_CONCEPT_ID` — isForeignKey
        - `VISIT_DETAIL.VISIT_DETAIL_CONCEPT_ID` — standardConceptRecordCompleteness
        - **VISIT_OCCURRENCE** (4 checks)
            - `PRECEDING_VISIT_OCCURRENCE_ID` — isForeignKey
            - `VISIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VISIT_SOURCE_CONCEPT_ID` — isForeignKey
            - `VISIT_SOURCE_VALUE` — sourceValueCompleteness

    #### Failures by Table

    | Table | Failed | Total | Pass Rate |
    |-------|--------|-------|-----------|
    | MEASUREMENT | 89 | 271 | 67.2% |
    | OBSERVATION_PERIOD | 6 | 38 | 84.2% |
    | PROVIDER | 4 | 49 | 91.8% |
    | DEATH | 3 | 41 | 92.7% |
    | CONDITION_ERA | 3 | 43 | 93.0% |
    | OBSERVATION | 6 | 88 | 93.2% |
    | DRUG_EXPOSURE | 6 | 123 | 95.1% |
    | PERSON | 4 | 85 | 95.3% |
    | CARE_SITE | 1 | 22 | 95.5% |
    | VISIT_OCCURRENCE | 8 | 206 | 96.1% |
    | PROCEDURE_OCCURRENCE | 5 | 163 | 96.9% |
    | CONDITION_OCCURRENCE | 6 | 300 | 98.0% |
    | DEVICE_EXPOSURE | 1 | 88 | 98.9% |
    | VISIT_DETAIL | 2 | 214 | 99.1% |

    9 additional tables passed all checks with zero failures.


??? abstract "v0.2.0"

    **83.3%** pass rate — 2,201 checks, 368 failures

    #### Changes from v0.1.1

    **29 issues resolved**

    **339 new failures**

    - **CONDITION_ERA** (3 checks)
        - `CONDITION_ERA_END_DATE` — plausibleBeforeDeath
        - `CONDITION_ERA_START_DATE` — plausibleBeforeDeath
        - `CONDITION_ERA_START_DATE` — plausibleDuringLife
    - **CONDITION_OCCURRENCE** (166 checks)
        - `CONDITION_CONCEPT_ID` — plausibleGender (163 concepts)
        - `CONDITION_CONCEPT_ID` — plausibleGenderUseDescendants (2 concepts)
        - `VISIT_DETAIL_ID` — isForeignKey
    - **DEATH** (3 checks)
        - `CAUSE_CONCEPT_ID` — standardConceptRecordCompleteness
        - `DEATH_DATE` — plausibleValueHigh
        - `DEATH_DATETIME` — plausibleValueHigh
    - **DRUG_EXPOSURE** (2 checks)
        - `DAYS_SUPPLY` — plausibleValueLow
        - `VISIT_DETAIL_ID` — isForeignKey
    - **MEASUREMENT** (79 checks)
        - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (77 concepts)
        - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
        - `VISIT_DETAIL_ID` — isForeignKey
    - **OBSERVATION** (6 checks)
        - `OBSERVATION_CONCEPT_ID` — standardConceptRecordCompleteness
        - `OBSERVATION_SOURCE_CONCEPT_ID` — sourceConceptRecordCompleteness
        - `QUALIFIER_CONCEPT_ID` — isForeignKey
        - `UNIT_CONCEPT_ID` — isForeignKey
        - `VALUE_AS_CONCEPT_ID` — isForeignKey
        - `VISIT_DETAIL_ID` — isForeignKey
    - **OBSERVATION_PERIOD** (5 checks)
        - `table-level` — measurePersonCompleteness
        - `OBSERVATION_PERIOD_END_DATE` — plausibleBeforeDeath
        - `OBSERVATION_PERIOD_END_DATE` — plausibleDuringLife
        - `OBSERVATION_PERIOD_END_DATE` — plausibleValueHigh
        - `OBSERVATION_PERIOD_START_DATE` — plausibleStartBeforeEnd
    - **PERSON** (4 checks)
        - `ETHNICITY_SOURCE_CONCEPT_ID` — isForeignKey
        - `GENDER_CONCEPT_ID` — standardConceptRecordCompleteness
        - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
        - `RACE_SOURCE_CONCEPT_ID` — isForeignKey
    - **PROCEDURE_OCCURRENCE** (63 checks)
        - `MODIFIER_CONCEPT_ID` — isForeignKey
        - `PROCEDURE_CONCEPT_ID` — plausibleGender (59 concepts)
        - `PROCEDURE_CONCEPT_ID` — plausibleGenderUseDescendants (2 concepts)
        - `VISIT_DETAIL_ID` — isForeignKey
    - **PROVIDER** (4 checks)
        - `CARE_SITE_ID` — isForeignKey
        - `GENDER_CONCEPT_ID` — isForeignKey
        - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
        - `SPECIALTY_SOURCE_CONCEPT_ID` — isForeignKey
    - `VISIT_DETAIL.VISIT_DETAIL_CONCEPT_ID` — standardConceptRecordCompleteness
    - **VISIT_OCCURRENCE** (3 checks)
        - `PRECEDING_VISIT_OCCURRENCE_ID` — isForeignKey
        - `VISIT_SOURCE_CONCEPT_ID` — isForeignKey
        - `VISIT_SOURCE_VALUE` — sourceValueCompleteness

    ??? warning "Persistent failures (24)"

        - **CONDITION_OCCURRENCE** (7 checks)
            - `CONDITION_CONCEPT_ID` — plausibleGender (6 concepts)
            - `CONDITION_START_DATE` — withinVisitDates
        - `DEVICE_EXPOSURE.DEVICE_CONCEPT_ID` — isStandardValidConcept
        - **DRUG_EXPOSURE** (4 checks)
            - `DRUG_CONCEPT_ID` — isStandardValidConcept
            - `QUANTITY` — plausibleValueHigh
            - `QUANTITY` — plausibleValueLow
            - `ROUTE_CONCEPT_ID` — isStandardValidConcept
        - **MEASUREMENT** (10 checks)
            - `MEASUREMENT_CONCEPT_ID` — fkDomain
            - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (8 concepts)
            - `UNIT_CONCEPT_ID` — isStandardValidConcept
        - `PROCEDURE_OCCURRENCE.PROCEDURE_CONCEPT_ID` — plausibleGender
        - `VISIT_OCCURRENCE.VISIT_CONCEPT_ID` — standardConceptRecordCompleteness

    #### Failures by Table

    | Table | Failed | Total | Pass Rate |
    |-------|--------|-------|-----------|
    | CONDITION_OCCURRENCE | 173 | 300 | 42.3% |
    | PROCEDURE_OCCURRENCE | 64 | 163 | 60.7% |
    | MEASUREMENT | 89 | 271 | 67.2% |
    | OBSERVATION_PERIOD | 5 | 38 | 86.8% |
    | PROVIDER | 4 | 49 | 91.8% |
    | DEATH | 3 | 41 | 92.7% |
    | CONDITION_ERA | 3 | 43 | 93.0% |
    | OBSERVATION | 6 | 88 | 93.2% |
    | DRUG_EXPOSURE | 6 | 123 | 95.1% |
    | PERSON | 4 | 85 | 95.3% |
    | VISIT_OCCURRENCE | 8 | 206 | 96.1% |
    | DEVICE_EXPOSURE | 1 | 88 | 98.9% |
    | VISIT_DETAIL | 2 | 214 | 99.1% |

    10 additional tables passed all checks with zero failures.


??? abstract "v0.1.1"

    **97.2%** pass rate — 2,201 checks, 62 failures

    #### Changes from v0.1.0

    **78 issues resolved**

    **45 new failures**

    - `CARE_SITE.PLACE_OF_SERVICE_CONCEPT_ID` — isStandardValidConcept
    - `CONDITION_ERA` — measureConditionEraCompleteness
    - **CONDITION_OCCURRENCE** (10 checks)
        - `CONDITION_CONCEPT_ID` — isStandardValidConcept
        - `CONDITION_CONCEPT_ID` — plausibleGender (7 concepts)
        - `CONDITION_STATUS_CONCEPT_ID` — isStandardValidConcept
        - `CONDITION_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `DEATH.DEATH_TYPE_CONCEPT_ID` — isStandardValidConcept
    - **DEVICE_EXPOSURE** (2 checks)
        - `DEVICE_CONCEPT_ID` — isStandardValidConcept
        - `DEVICE_TYPE_CONCEPT_ID` — isStandardValidConcept
    - **DRUG_EXPOSURE** (3 checks)
        - `DRUG_TYPE_CONCEPT_ID` — isStandardValidConcept
        - `QUANTITY` — plausibleValueLow
        - `ROUTE_CONCEPT_ID` — isStandardValidConcept
    - **MEASUREMENT** (11 checks)
        - `MEASUREMENT_CONCEPT_ID` — isStandardValidConcept
        - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (8 concepts)
        - `MEASUREMENT_TYPE_CONCEPT_ID` — isStandardValidConcept
        - `OPERATOR_CONCEPT_ID` — isStandardValidConcept
    - **OBSERVATION** (3 checks)
        - `OBSERVATION_CONCEPT_ID` — isStandardValidConcept
        - `OBSERVATION_TYPE_CONCEPT_ID` — isStandardValidConcept
        - `UNIT_CONCEPT_ID` — isStandardValidConcept
    - **PERSON** (3 checks)
        - `ETHNICITY_CONCEPT_ID` — isStandardValidConcept
        - `GENDER_CONCEPT_ID` — isStandardValidConcept
        - `RACE_CONCEPT_ID` — isStandardValidConcept
    - **PROCEDURE_OCCURRENCE** (3 checks)
        - `PROCEDURE_CONCEPT_ID` — isStandardValidConcept
        - `PROCEDURE_CONCEPT_ID` — plausibleGender
        - `PROCEDURE_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `PROVIDER.SPECIALTY_CONCEPT_ID` — isStandardValidConcept
    - **VISIT_DETAIL** (2 checks)
        - `VISIT_DETAIL_CONCEPT_ID` — isStandardValidConcept
        - `VISIT_DETAIL_TYPE_CONCEPT_ID` — isStandardValidConcept
    - **VISIT_OCCURRENCE** (4 checks)
        - `VISIT_CONCEPT_ID` — isStandardValidConcept
        - `VISIT_START_DATE` — plausibleStartBeforeEnd
        - `VISIT_START_DATETIME` — plausibleStartBeforeEnd
        - `VISIT_TYPE_CONCEPT_ID` — isStandardValidConcept

    ??? warning "Persistent failures (8)"

        - `CONDITION_OCCURRENCE.CONDITION_START_DATE` — withinVisitDates
        - **DRUG_EXPOSURE** (2 checks)
            - `DRUG_CONCEPT_ID` — isStandardValidConcept
            - `QUANTITY` — plausibleValueHigh
        - **MEASUREMENT** (2 checks)
            - `MEASUREMENT_CONCEPT_ID` — fkDomain
            - `UNIT_CONCEPT_ID` — isStandardValidConcept
        - **VISIT_OCCURRENCE** (3 checks)
            - `VISIT_CONCEPT_ID` — standardConceptRecordCompleteness
            - `VISIT_END_DATE` — plausibleTemporalAfter
            - `VISIT_END_DATETIME` — plausibleTemporalAfter

    #### Failures by Table

    | Table | Failed | Total | Pass Rate |
    |-------|--------|-------|-----------|
    | VISIT_OCCURRENCE | 14 | 206 | 93.2% |
    | MEASUREMENT | 13 | 271 | 95.2% |
    | CARE_SITE | 1 | 22 | 95.5% |
    | DRUG_EXPOSURE | 5 | 123 | 95.9% |
    | CONDITION_OCCURRENCE | 11 | 300 | 96.3% |
    | PERSON | 3 | 85 | 96.5% |
    | OBSERVATION | 3 | 88 | 96.6% |
    | DEATH | 1 | 41 | 97.6% |
    | CONDITION_ERA | 1 | 43 | 97.7% |
    | DEVICE_EXPOSURE | 2 | 88 | 97.7% |
    | PROVIDER | 1 | 49 | 98.0% |
    | VISIT_DETAIL | 4 | 214 | 98.1% |
    | PROCEDURE_OCCURRENCE | 3 | 163 | 98.2% |

    10 additional tables passed all checks with zero failures.


??? abstract "v0.1.0"

    **97.7%** pass rate — 3,705 checks, 86 failures

    #### Failures by Table

    | Table | Failed | Total | Pass Rate |
    |-------|--------|-------|-----------|
    | VISIT_OCCURRENCE | 7 | 93 | 92.5% |
    | DRUG_EXPOSURE | 7 | 111 | 93.7% |
    | OBSERVATION_PERIOD | 2 | 33 | 93.9% |
    | VISIT_DETAIL | 4 | 97 | 95.9% |
    | CONDITION_OCCURRENCE | 10 | 288 | 96.5% |
    | CONDITION_ERA | 1 | 38 | 97.4% |
    | MEASUREMENT | 51 | 2085 | 97.6% |
    | DRUG_ERA | 1 | 42 | 97.6% |
    | PROCEDURE_OCCURRENCE | 3 | 157 | 98.1% |

    14 additional tables passed all checks with zero failures.


<!-- DQD_SUMMARY_END -->

<div class="grid cards" markdown>

-   :material-diamond-outline:{ .lg .middle } **Interactive Dashboard**

    ---

    Drill into individual checks, filter by category, and explore failures across all tables.

    [:octicons-arrow-right-24: Emory's DQD Dashboard](https://emorydatasolutions.github.io/e_omop_dqd/){ .md-button .md-button--primary }

-   :material-test-tube:{ .lg .middle } **DBT Pipeline Tests**

    ---

    Column-level test definitions for every table in the ETL pipeline — nullability, uniqueness, referential integrity, and domain validation.

    [:octicons-arrow-right-24: DBT test definitions](../DBT%20Tests/index.md){ .md-button }

-   :material-alert-circle-outline:{ .lg .middle } **Known Issues**

    ---

    Narrative context on mapping gaps, data limitations, and recommended workarounds by table.

    [:octicons-arrow-right-24: Known Issues](../Known%20Issues/index.md){ .md-button }

</div>
