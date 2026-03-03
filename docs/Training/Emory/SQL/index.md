---
search:
  exclude: false
title: Tips for Writing Queries Against OMOP
---

# Tips for Writing Queries Against OMOP

Emory's OMOP data lake runs on Amazon Redshift. These tips will help you write efficient, correct queries against the OMOP Common Data Model.

## Schema Layout

All standard OMOP CDM tables live in the `cdm` schema. Common tables you'll query:

| Table | Contains |
|-------|----------|
| `cdm.person` | Demographics — one row per patient |
| `cdm.visit_occurrence` | Encounters (inpatient, outpatient, ER, etc.) |
| `cdm.condition_occurrence` | Diagnoses |
| `cdm.drug_exposure` | Medications |
| `cdm.procedure_occurrence` | Procedures |
| `cdm.measurement` | Labs, vitals, and other measurements |
| `cdm.observation` | Other clinical observations |
| `cdm.concept` | Vocabulary lookup — maps `concept_id` to human-readable names |

## Key Patterns

### Always Join to `concept` for Readable Output

Raw OMOP tables store integer `concept_id` values. Join to `cdm.concept` to get names:

```sql
SELECT
    p.person_id,
    c.concept_name AS condition_name,
    co.condition_start_date
FROM cdm.condition_occurrence co
JOIN cdm.person p ON co.person_id = p.person_id
JOIN cdm.concept c ON co.condition_concept_id = c.concept_id
WHERE c.concept_name ILIKE '%diabetes%'
LIMIT 100;
```

### Use Standard Concepts

Filter on `standard_concept = 'S'` when searching the vocabulary to get the canonical OMOP concept:

```sql
SELECT concept_id, concept_name, vocabulary_id
FROM cdm.concept
WHERE concept_name ILIKE '%hemoglobin a1c%'
  AND standard_concept = 'S'
  AND domain_id = 'Measurement';
```

### Concept Hierarchies with `concept_ancestor`

Find all descendants of a high-level concept to capture related conditions or drugs:

```sql
SELECT DISTINCT descendant_concept_id
FROM cdm.concept_ancestor
WHERE ancestor_concept_id = 201826  -- Type 2 diabetes
;
```

## Redshift-Specific Tips

- **Use `ILIKE`** for case-insensitive text searches (Redshift-specific, not standard SQL)
- **Avoid `SELECT *`** — Redshift is columnar; selecting only needed columns is significantly faster
- **Use `LIMIT`** during exploration to avoid pulling millions of rows
- **Date functions** — use `DATEDIFF(day, start_date, end_date)` for date arithmetic

## Additional Resources

- [:octicons-arrow-right-24: Emory SQL Query Library](Query%20Library/index.md)
- [:octicons-arrow-right-24: OHDSI Query Library](https://data.ohdsi.org/QueryLibrary/){ target="_blank" }
- [:octicons-arrow-right-24: The Book of OHDSI — SQL and R](https://ohdsi.github.io/TheBookOfOhdsi/SqlAndR.html){ target="_blank" }
- [:octicons-arrow-right-24: General SQL Reference (w3schools)](https://www.w3schools.com/sql/){ target="_blank" }
