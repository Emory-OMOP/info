---
hide:
  - footer
title: Known Issues
---

# Known Issues

!!! info "How issues are tracked"
    Each issue is tagged with the OMOP release where it was first observed and,
    if applicable, the release where it was resolved. Issues are automatically
    generated from DQD results history and supplemented with narrative context.

??? note "CDM Architecture Reference"

    ![CDM 5.4 Entity Relationship Diagram](../../../assets/images/cdm54.png)

<!-- KNOWN_ISSUES_START -->

## Open Issues

Issues that remain unresolved in the latest release (v1.0.0).

??? warning "VISIT_OCCURRENCE — 12 DQD failures"

    **First observed**: v0.1.0
    **Latest release**: v1.0.0
    **Category**: Completeness (4), Conformance (8)

    - `ADMITTED_FROM_CONCEPT_ID` — isForeignKey
    - `ADMITTED_FROM_CONCEPT_ID` — isStandardValidConcept
    - `ADMITTED_FROM_CONCEPT_ID` — standardConceptRecordCompleteness
    - `DISCHARGED_TO_CONCEPT_ID` — isForeignKey
    - `DISCHARGED_TO_CONCEPT_ID` — isStandardValidConcept
    - `DISCHARGED_TO_CONCEPT_ID` — standardConceptRecordCompleteness
    - `PRECEDING_VISIT_OCCURRENCE_ID` — isForeignKey
    - `VISIT_CONCEPT_ID` — isStandardValidConcept
    - `VISIT_CONCEPT_ID` — standardConceptRecordCompleteness
    - `VISIT_SOURCE_CONCEPT_ID` — isForeignKey
    - `VISIT_SOURCE_VALUE` — sourceValueCompleteness
    - `VISIT_TYPE_CONCEPT_ID` — isStandardValidConcept

??? warning "MEASUREMENT — 11 DQD failures"

    **First observed**: v0.1.0
    **Latest release**: v1.0.0
    **Category**: Completeness (1), Conformance (5), Plausibility (5)

    - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (5 concepts)
    - `MEASUREMENT_SOURCE_CONCEPT_ID` — isForeignKey
    - `MEASUREMENT_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `UNIT_CONCEPT_ID` — isStandardValidConcept
    - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
    - `VALUE_AS_CONCEPT_ID` — isForeignKey
    - `VISIT_DETAIL_ID` — isForeignKey

??? warning "OBSERVATION — 9 DQD failures"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Completeness (2), Conformance (7)

    - `OBSERVATION_CONCEPT_ID` — isStandardValidConcept
    - `OBSERVATION_SOURCE_CONCEPT_ID` — sourceConceptRecordCompleteness
    - `OBSERVATION_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `QUALIFIER_CONCEPT_ID` — isForeignKey
    - `UNIT_CONCEPT_ID` — isForeignKey
    - `UNIT_CONCEPT_ID` — isStandardValidConcept
    - `UNIT_CONCEPT_ID` — standardConceptRecordCompleteness
    - `VALUE_AS_CONCEPT_ID` — isForeignKey
    - `VISIT_DETAIL_ID` — isForeignKey

??? warning "CONDITION_OCCURRENCE — 8 DQD failures"

    **First observed**: v0.1.0
    **Latest release**: v1.0.0
    **Category**: Completeness (1), Conformance (2), Plausibility (5)

    - `CONDITION_CONCEPT_ID` — plausibleGender (4 concepts)
    - `CONDITION_START_DATE` — withinVisitDates
    - `CONDITION_STATUS_CONCEPT_ID` — standardConceptRecordCompleteness
    - `CONDITION_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `VISIT_DETAIL_ID` — isForeignKey

??? warning "DRUG_EXPOSURE — 6 DQD failures"

    **First observed**: v0.1.0
    **Latest release**: v1.0.0
    **Category**: Conformance (4), Plausibility (2)

    - `DAYS_SUPPLY` — plausibleValueLow
    - `DRUG_CONCEPT_ID` — isStandardValidConcept
    - `DRUG_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `QUANTITY` — plausibleValueLow
    - `ROUTE_CONCEPT_ID` — isStandardValidConcept
    - `VISIT_DETAIL_ID` — isForeignKey

??? warning "PROCEDURE_OCCURRENCE — 6 DQD failures"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Conformance (3), Plausibility (3)

    - `MODIFIER_CONCEPT_ID` — isForeignKey
    - `PROCEDURE_CONCEPT_ID` — plausibleGender
    - `PROCEDURE_CONCEPT_ID` — plausibleGenderUseDescendants
    - `PROCEDURE_DATE` — withinVisitDates
    - `PROCEDURE_TYPE_CONCEPT_ID` — isStandardValidConcept
    - `VISIT_DETAIL_ID` — isForeignKey

??? warning "OBSERVATION_PERIOD — 5 DQD failures"

    **First observed**: v0.1.0
    **Latest release**: v1.0.0
    **Category**: Completeness (1), Plausibility (4)

    - table-level — measurePersonCompleteness
    - `OBSERVATION_PERIOD_END_DATE` — plausibleBeforeDeath
    - `OBSERVATION_PERIOD_END_DATE` — plausibleDuringLife
    - `OBSERVATION_PERIOD_END_DATE` — plausibleValueHigh
    - `OBSERVATION_PERIOD_START_DATE` — plausibleStartBeforeEnd

??? warning "PERSON — 5 DQD failures"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Conformance (5)

    - `ETHNICITY_SOURCE_CONCEPT_ID` — isForeignKey
    - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
    - `RACE_CONCEPT_ID` — fkDomain
    - `RACE_CONCEPT_ID` — isStandardValidConcept
    - `RACE_SOURCE_CONCEPT_ID` — isForeignKey

??? warning "DEATH — 4 DQD failures"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Completeness (1), Conformance (1), Plausibility (2)

    - `CAUSE_CONCEPT_ID` — standardConceptRecordCompleteness
    - `DEATH_DATE` — plausibleValueHigh
    - `DEATH_DATETIME` — plausibleValueHigh
    - `DEATH_TYPE_CONCEPT_ID` — isStandardValidConcept

??? warning "PROVIDER — 4 DQD failures"

    **First observed**: v0.2.0
    **Latest release**: v1.0.0
    **Category**: Conformance (4)

    - `CARE_SITE_ID` — isForeignKey
    - `GENDER_CONCEPT_ID` — isForeignKey
    - `GENDER_SOURCE_CONCEPT_ID` — isForeignKey
    - `SPECIALTY_SOURCE_CONCEPT_ID` — isForeignKey

??? warning "CONDITION_ERA — 3 DQD failures"

    **First observed**: v0.1.0
    **Latest release**: v1.0.0
    **Category**: Plausibility (3)

    - `CONDITION_ERA_END_DATE` — plausibleBeforeDeath
    - `CONDITION_ERA_START_DATE` — plausibleBeforeDeath
    - `CONDITION_ERA_START_DATE` — plausibleDuringLife

??? warning "VISIT_DETAIL — 3 DQD failures"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Completeness (1), Conformance (2)

    - `DISCHARGED_TO_CONCEPT_ID` — isStandardValidConcept
    - `VISIT_DETAIL_CONCEPT_ID` — standardConceptRecordCompleteness
    - `VISIT_DETAIL_TYPE_CONCEPT_ID` — isStandardValidConcept

??? warning "DEVICE_EXPOSURE — 2 DQD failures"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Conformance (2)

    - `DEVICE_CONCEPT_ID` — isStandardValidConcept
    - `DEVICE_TYPE_CONCEPT_ID` — isStandardValidConcept

??? warning "CARE_SITE — 1 DQD failure"

    **First observed**: v0.1.1
    **Latest release**: v1.0.0
    **Category**: Conformance (1)

    - `PLACE_OF_SERVICE_CONCEPT_ID` — isStandardValidConcept

??? warning "LOCATION — 1 DQD failure"

    **First observed**: v1.0.0
    **Latest release**: v1.0.0
    **Category**: Conformance (1)

    - `COUNTRY_CONCEPT_ID` — isForeignKey

??? warning "DRUG_STRENGTH — 1 DQD failure"

    **First observed**: v1.0.0
    **Latest release**: v1.0.0
    **Category**: Conformance (1)

    - `INGREDIENT_CONCEPT_ID` — fkClass

## Resolved Issues

Issues that were observed in earlier releases but have been resolved.

??? success "CONDITION_OCCURRENCE — 179 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v0.2.2

    - `CONDITION_CONCEPT_ID` — isStandardValidConcept
    - `CONDITION_CONCEPT_ID` — plausibleGender (173 concepts)
    - `CONDITION_CONCEPT_ID` — plausibleGenderUseDescendants (2 concepts)
    - `CONDITION_START_DATE` — plausibleDuringLife
    - `CONDITION_START_DATETIME` — plausibleDuringLife
    - `CONDITION_STATUS_CONCEPT_ID` — isStandardValidConcept

??? success "MEASUREMENT — 133 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v1.0.0

    - `MEASUREMENT_CONCEPT_ID` — fkDomain
    - `MEASUREMENT_CONCEPT_ID` — isStandardValidConcept
    - `MEASUREMENT_CONCEPT_ID` — plausibleUnitConceptIds (130 concepts)
    - `OPERATOR_CONCEPT_ID` — isStandardValidConcept

??? success "PROCEDURE_OCCURRENCE — 64 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v0.2.2

    - `PROCEDURE_CONCEPT_ID` — isStandardValidConcept
    - `PROCEDURE_CONCEPT_ID` — plausibleGender (60 concepts)
    - `PROCEDURE_CONCEPT_ID` — plausibleGenderUseDescendants
    - `PROCEDURE_DATE` — plausibleDuringLife
    - `PROCEDURE_DATETIME` — plausibleDuringLife

??? success "VISIT_OCCURRENCE — 8 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v0.2.0

    - `VISIT_END_DATE` — plausibleDuringLife
    - `VISIT_END_DATE` — plausibleTemporalAfter
    - `VISIT_END_DATETIME` — plausibleDuringLife
    - `VISIT_END_DATETIME` — plausibleTemporalAfter
    - `VISIT_START_DATE` — plausibleDuringLife
    - `VISIT_START_DATE` — plausibleStartBeforeEnd
    - `VISIT_START_DATETIME` — plausibleDuringLife
    - `VISIT_START_DATETIME` — plausibleStartBeforeEnd

??? success "DRUG_EXPOSURE — 6 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v1.0.0

    - `DRUG_EXPOSURE_END_DATE` — plausibleDuringLife
    - `DRUG_EXPOSURE_END_DATETIME` — plausibleDuringLife
    - `DRUG_EXPOSURE_START_DATE` — plausibleDuringLife
    - `DRUG_EXPOSURE_START_DATETIME` — plausibleDuringLife
    - `QUANTITY` — plausibleValueHigh
    - `VERBATIM_END_DATE` — plausibleDuringLife

??? success "VISIT_DETAIL — 5 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v0.2.0

    - `VISIT_DETAIL_CONCEPT_ID` — isStandardValidConcept
    - `VISIT_DETAIL_END_DATE` — plausibleDuringLife
    - `VISIT_DETAIL_END_DATETIME` — plausibleDuringLife
    - `VISIT_DETAIL_START_DATE` — plausibleDuringLife
    - `VISIT_DETAIL_START_DATETIME` — plausibleDuringLife

??? success "PERSON — 3 issues resolved"

    **First observed**: v0.1.1
    **Resolved in**: v0.2.2

    - `ETHNICITY_CONCEPT_ID` — isStandardValidConcept
    - `GENDER_CONCEPT_ID` — isStandardValidConcept
    - `GENDER_CONCEPT_ID` — standardConceptRecordCompleteness

??? success "OBSERVATION_PERIOD — 2 issues resolved"

    **First observed**: v0.1.0
    **Resolved in**: v1.0.0

    - `OBSERVATION_PERIOD_START_DATE` — plausibleAfterBirth
    - `OBSERVATION_PERIOD_START_DATE` — plausibleDuringLife

??? success "DRUG_ERA — 1 issue resolved"

    **First observed**: v0.1.0
    **Resolved in**: v0.1.1

    - `DRUG_ERA_START_DATE` — plausibleDuringLife

??? success "CONDITION_ERA — 1 issue resolved"

    **First observed**: v0.1.1
    **Resolved in**: v0.2.0

    - table-level — measureConditionEraCompleteness

??? success "PROVIDER — 1 issue resolved"

    **First observed**: v0.1.1
    **Resolved in**: v0.2.0

    - `SPECIALTY_CONCEPT_ID` — isStandardValidConcept

??? success "OBSERVATION — 1 issue resolved"

    **First observed**: v0.2.0
    **Resolved in**: v0.2.4

    - `OBSERVATION_CONCEPT_ID` — standardConceptRecordCompleteness

??? success "CARE_SITE — 1 issue resolved"

    **First observed**: v0.2.2
    **Resolved in**: v0.2.4

    - `CARE_SITE_ID` — isPrimaryKey

<!-- KNOWN_ISSUES_END -->

## Not Mapped

Tables not yet populated in Emory's OMOP instance. These are on the roadmap for future releases.

??? info "Note"

    Not mapped. High priority given the medical information desired — will be a focus in the near future. Monitor the Product Roadmap for updates.

??? info "Note NLP"

    Not mapped. Unified enterprise-wide NLP ingestion is a challenge but is a worthwhile activity desired by researchers. Monitor the Product Roadmap for updates.

??? info "Payer Plan Period"

    Not mapped.

??? info "Cost"

    Not mapped.

??? info "Episode"

    Not mapped currently. Winship has a use case for chemotherapy regimens and is actively participating in a network study utilizing Episodes. Contact Daniel (daniel.g.smith@emory.edu) for details.

??? info "Episode Event"

    Not mapped.

??? info "Fact Relationship"

    Not utilized at present.

??? info "Metadata"

    Not populated. This will be a critical table long-term between loads, providing important information for downstream stakeholders. A feature request to populate this table is being considered during release planning.

!!! tip "Found an issue not listed here?"
    Report it through our [:octicons-arrow-right-24: bug report form](../../../Support/index.md) or reach out on [:octicons-arrow-right-24: Microsoft Teams](../../../Contact%20Us/index.md).
