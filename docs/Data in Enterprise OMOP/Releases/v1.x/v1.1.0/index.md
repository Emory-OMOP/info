---
hide:
  - footer
title: "Release Notes — v1.1.0"
---

# v1.1.0 — March 2026

*NLP Infrastructure | Brain Health Pilot | 2,488 notes | 9,411 spans | 850 patients*

## What's New for Researchers

### Clinical Notes in OMOP

For the first time, Emory Enterprise OMOP includes **structured NLP output from clinical notes**. The standard OMOP `note_nlp` table's flat design was insufficient for modern NLP workflows, so we developed a [4-layer span-based architecture](../../NLP%20Infrastructure/architecture.md) that captures full pipeline provenance, assertion context, and clear separation from discrete EHR data.

**What this means for you:**

- NLP-extracted conditions, observations, and drug mentions are available in `_derived` tables (`condition_occurrence_derived`, `observation_derived`, `drug_exposure_derived`, etc.)
- Every extracted finding traces back to the exact text span, source note, NLP pipeline version, and git commit that produced it
- Negated findings ("no evidence of hemorrhage") are filtered out — only affirmed, possible, and historical findings reach the `_derived` tables
- An `_assertion_value` column indicates whether a finding is affirmed (NULL), possible, or historical

### Brain Health Pilot

The first NLP pipeline processes **2,488 imaging notes** (CT Head, MR Brain) from **850 Brain Health (GINDR) patients**, extracting clinical findings across 79 entity categories including:

| Domain | Examples | Count |
|--------|----------|-------|
| Conditions | cerebral atrophy, hydrocephalus, small vessel disease, chronic infarct | 4,928 |
| Observations | mass effect, midline shift, focal slowing, calcification | 535 |
| Drugs | lecanemab, donanemab, donepezil, memantine | 31 |
| Measurements | MoCA | 1 |

### Assertion Detection

The pipeline classifies extracted entities by clinical context using the [ConText algorithm](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757457/) (Harkema et al., 2009), aligned with the [i2b2 2010 assertion categories](https://pmc.ncbi.nlm.nih.gov/articles/PMC3168320/):

| Assertion | Count | Meaning |
|-----------|-------|---------|
| Negated | 3,916 | Finding is absent — **excluded from `_derived` tables** |
| Affirmed | 3,648 | Finding is present — `_assertion_value = NULL` |
| Possible | 994 | Uncertain ("cannot exclude", "suggestive of") — `_assertion_value = 'possible'` |
| Historical | 853 | Past finding ("history of", "prior") — `_assertion_value = 'historical'` |
| Hypothetical | 68 | Future/conditional ("monitor for", "evaluate for") |
| Family | 6 | Attributed to family member — **excluded from `_derived` tables** |

### Context Snippets

The `note_span_snippet` table provides a **50-character context window** around each extracted entity, enabling rapid validation of NLP output without accessing full note text. This is the only NLP table containing PHI — all other NLP infrastructure tables are PHI-free.

### Annotation Review

The `nlp_annotation_review` table captures human judgments on NLP-extracted spans. Initial reviews identified **6 false positive familial assertions** where the ConText algorithm misclassified patient seizure activity during EEG monitoring in the presence of a family member as "family history."

---

## Architecture

### 4-Layer NLP Infrastructure

```
Layer 1: NLP Process Metadata (nlp_system, pipeline, component, nlp_execution)
Layer 2: NLP Output (note_span, note_span_concept, note_span_assertion, note_span_snippet)
Layer 3: Intermediate Translation (note_nlp_modifier)
Layer 4: _derived Tables (condition_occurrence_derived, observation_derived, etc.)
```

Full architecture specification: [:octicons-arrow-right-24: NLP Infrastructure](../../NLP%20Infrastructure/architecture.md)

### Key Design Decisions

- **`note_span_assertion`** replaces the original `note_span_relationship` — named after the [i2b2 assertion classification](https://pmc.ncbi.nlm.nih.gov/articles/PMC3168320/) standard. See [Glossary](../../NLP%20Infrastructure/glossary.md).
- **`concept_code` + `vocabulary_id`** on `note_span_concept` instead of `concept_id` — NLP implementers provide vocabulary codes they know (SNOMED, RxNorm, LOINC); dbt resolves to OMOP `concept_id` downstream via vocabulary join
- **`domain_hint`** for unmapped concepts — when no vocabulary mapping exists, NLP implementers provide a domain hint so findings still route to the correct `_derived` table
- **Source provenance** (`source`, `source_uri`, `source_version`) on `nlp_system`, `pipeline`, and `component` — supports GitHub, HuggingFace, PyPI, Docker, and S3 artifact references
- **`_derived` tables** use `_` prefix for non-standard columns (`_note_span_id`, `_execution_id`, `_source_primary_key`, `_assertion_value`) to distinguish from OMOP CDM standard columns
- **`condition_type_concept_id` = 32858 (NLP)** marks all derived rows as NLP-sourced

### FastAPI Ingestion Service

The NLP ingestion boundary is a [FastAPI service](https://github.com/EmoryDataSolutions/emory_omop_internal_nlp) (Docker, port 8006) that accepts NLP output from any tool (medspaCy, MedTagger, Claude API, custom models) and writes to a DuckDB bronze layer. This decouples "how you do NLP" from "how NLP results enter OMOP."

---

## Pipeline Details

### medspaCy Brain Health v1

| Field | Value |
|-------|-------|
| NLP System | medspacy v1 |
| Pipeline | brain_health_v1 |
| Git repo | `github.com/EmoryDataSolutions/emory_omop_internal_nlp` |
| Git commit | `3052d147910938b73bb5ed3b7f9a481ff359c42f` |
| medspaCy | 1.3.1 (PyPI) |
| spaCy | 3.8.13 (PyPI) |
| Rules spec | 180+ target rules, 117 context rules, 24 section rules |
| Literature references | 21 (ConText, i2b2, Fazekas, ARIA, RadLex, ACR/RSNA) |

### Note Extraction

- **Source**: Emory Healthcare EHAP (Clarity) via Athena federated query
- **Cohort**: 5,000 random patients from GINDR `cohort_person_filter`
- **Note types**: CT Head, MR Brain, PET Brain/Amyloid, EEG (via `V_IMG_STUDY`)
- **Result**: 2,488 notes from 850 patients (17% hit rate)
- **Extraction method**: Batched `IN (...)` clauses (50 per batch, 100 batches) due to SQL Server 2,100 parameter limit on federated queries

---

## Data Summary

| Table | Schema | Rows |
|-------|--------|------|
| note | omop_brain_health_ent | 2,473 |
| note_span | omop_brain_health_ent | 9,411 |
| note_span_concept | omop_brain_health_ent | 9,411 |
| note_span_assertion | omop_brain_health_ent | 5,837 |
| note_span_snippet | omop_brain_health_ent | 9,411 |
| note_nlp_modifier | omop_brain_health_ent | 5,495 |
| condition_occurrence_derived | omop_brain_health_ent | 4,928 |
| observation_derived | omop_brain_health_ent | 535 |
| drug_exposure_derived | omop_brain_health_ent | 31 |
| measurement_derived | omop_brain_health_ent | 1 |
| procedure_occurrence_derived | omop_brain_health_ent | 0 |
| nlp_annotation_review | omop_brain_health_ent | 6 |

---

## Known Limitations

1. **Pilot scope** — 5,000 random patients from GINDR cohort, not the full population
2. **Imaging notes only** — extraction uses `V_IMG_STUDY` join; primary care, EEG procedure notes, and lab notes not yet included
3. **58% of notes lack dates** — `V_IMG_STUDY.begin_exam_dttm` is sparse; `HNO_INFO` enrichment yielded only 3% additional coverage
4. **No visit/provider linkage** — `visit_occurrence_id` and `provider_id` are NULL; `HNO_INFO.pat_enc_csn_id` is 3% populated for imaging notes
5. **Rule-based NLP** — medspaCy uses literal string matching; no ML-based entity recognition
6. **Assertion concept_ids are placeholder (0)** — custom OMOP concepts for assertion types pending CVB work
7. **EHAP federated query constraints** — no predicate pushdown for JOINs, Lambda 900s timeout, SQL Server 2,100 parameter limit
8. **Duplicate note content** — some notes with different `note_csn_id` values contain identical text

---

## Repositories

| Repository | Purpose |
|------------|---------|
| [emory_omop_enterprise](https://github.com/EmoryDataSolutions/emory_omop_enterprise) | dbt projects: `EmoryOmopBrainHealthEnterprise` (NLP wrapper models), `EmoryOmopNoteIngestionPilot` (pilot transforms) |
| [emory_omop_internal_nlp](https://github.com/EmoryDataSolutions/emory_omop_internal_nlp) | FastAPI ingestion service, medspaCy pipeline, rules specification, provenance capture |
| [emory-omop](https://github.com/Emory-OMOP/emory-omop) | NLP architecture spec, glossary, validation framework, this documentation |

---

## Related Pages

- [:octicons-arrow-right-24: NLP Architecture](../../NLP%20Infrastructure/architecture.md) — 4-layer schema specification
- [:octicons-arrow-right-24: NLP Glossary](../../NLP%20Infrastructure/glossary.md) — Clinical NLP terminology reference
- [:octicons-arrow-right-24: Entity Relationship Diagram](../../NLP%20Infrastructure/entity-relationship-diagram.md) — Visual schema reference
