---
search:
  exclude: false
title: Emory SQL Query Library
---

# Emory SQL Query Library

A collection of common SQL queries for working with Emory's OMOP data lake on Redshift. For the broader OHDSI community query library, see the [OHDSI Query Library](https://data.ohdsi.org/QueryLibrary/){ target="_blank" }.

## Patient Counts

### Total patients in the CDM

```sql
SELECT COUNT(*) AS total_persons
FROM cdm.person;
```

### Patients by gender

```sql
SELECT
    c.concept_name AS gender,
    COUNT(*) AS person_count
FROM cdm.person p
JOIN cdm.concept c ON p.gender_concept_id = c.concept_id
GROUP BY c.concept_name
ORDER BY person_count DESC;
```

### Patients by age group

```sql
SELECT
    CASE
        WHEN DATEDIFF(year, CAST(year_of_birth || '-01-01' AS DATE), CURRENT_DATE) < 18 THEN '0-17'
        WHEN DATEDIFF(year, CAST(year_of_birth || '-01-01' AS DATE), CURRENT_DATE) < 35 THEN '18-34'
        WHEN DATEDIFF(year, CAST(year_of_birth || '-01-01' AS DATE), CURRENT_DATE) < 50 THEN '35-49'
        WHEN DATEDIFF(year, CAST(year_of_birth || '-01-01' AS DATE), CURRENT_DATE) < 65 THEN '50-64'
        ELSE '65+'
    END AS age_group,
    COUNT(*) AS person_count
FROM cdm.person
GROUP BY 1
ORDER BY 1;
```

## Condition Queries

### Top 20 most common conditions

```sql
SELECT
    c.concept_name AS condition_name,
    COUNT(DISTINCT co.person_id) AS patient_count
FROM cdm.condition_occurrence co
JOIN cdm.concept c ON co.condition_concept_id = c.concept_id
WHERE c.standard_concept = 'S'
GROUP BY c.concept_name
ORDER BY patient_count DESC
LIMIT 20;
```

### Find patients with a specific condition

```sql
SELECT DISTINCT co.person_id
FROM cdm.condition_occurrence co
JOIN cdm.concept_ancestor ca
    ON co.condition_concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = 201826  -- Type 2 diabetes (includes all subtypes)
;
```

## Drug Queries

### Medications for a patient cohort

```sql
SELECT
    c.concept_name AS drug_name,
    COUNT(DISTINCT de.person_id) AS patient_count
FROM cdm.drug_exposure de
JOIN cdm.concept c ON de.drug_concept_id = c.concept_id
WHERE de.person_id IN (
    -- Your cohort here
    SELECT DISTINCT person_id
    FROM cdm.condition_occurrence
    WHERE condition_concept_id = 201826
)
AND c.standard_concept = 'S'
GROUP BY c.concept_name
ORDER BY patient_count DESC
LIMIT 20;
```

## Measurement Queries

### Most recent lab value for a patient

```sql
SELECT
    m.person_id,
    c.concept_name AS measurement_name,
    m.value_as_number,
    u.concept_name AS unit,
    m.measurement_date
FROM cdm.measurement m
JOIN cdm.concept c ON m.measurement_concept_id = c.concept_id
LEFT JOIN cdm.concept u ON m.unit_concept_id = u.concept_id
WHERE m.person_id = <person_id>
  AND c.concept_name ILIKE '%hemoglobin a1c%'
ORDER BY m.measurement_date DESC
LIMIT 1;
```

## Visit Queries

### Visit type distribution

```sql
SELECT
    c.concept_name AS visit_type,
    COUNT(*) AS visit_count,
    COUNT(DISTINCT vo.person_id) AS patient_count
FROM cdm.visit_occurrence vo
JOIN cdm.concept c ON vo.visit_concept_id = c.concept_id
GROUP BY c.concept_name
ORDER BY visit_count DESC;
```

## Vocabulary Queries

### Search for a concept by name

```sql
SELECT
    concept_id,
    concept_name,
    domain_id,
    vocabulary_id,
    concept_class_id,
    standard_concept
FROM cdm.concept
WHERE concept_name ILIKE '%search term%'
  AND standard_concept = 'S'
ORDER BY concept_name
LIMIT 50;
```

### Find source-to-standard concept mappings

```sql
SELECT
    source.concept_id AS source_concept_id,
    source.concept_name AS source_concept_name,
    source.vocabulary_id AS source_vocabulary,
    target.concept_id AS standard_concept_id,
    target.concept_name AS standard_concept_name,
    target.vocabulary_id AS standard_vocabulary
FROM cdm.concept_relationship cr
JOIN cdm.concept source ON cr.concept_id_1 = source.concept_id
JOIN cdm.concept target ON cr.concept_id_2 = target.concept_id
WHERE cr.relationship_id = 'Maps to'
  AND source.concept_name ILIKE '%search term%'
  AND target.standard_concept = 'S';
```
