---
hide:
  - footer
title: Note NLP
---

# Note NLP

**Epic equivalent**: No direct equivalent — this is NLP pipeline output derived from clinical notes

The `note_nlp` table contains **structured outputs from NLP models applied to clinical notes**. Each row is a single extracted entity, concept, assertion, or relationship found in the free text stored in the `note` table. Think of it as the bridge between narrative documentation and structured analytics.

## Field Reference

??? example "Field reference (click to expand)"

    | OMOP Field | What It Captures |
    |---|---|
    | `note_nlp_id` | Unique identifier for the NLP output row |
    | `note_id` | Links back to the source note |
    | `section_concept_id` | Note section (e.g., HPI, Assessment) for context |
    | `snippet` | Short text window around the concept mention |
    | `offset` | Character position within the note |
    | `lexical_variant` | Actual words used (e.g., "SOB" or "shortness of breath") |
    | `note_nlp_concept_id` | Standard OMOP concept inferred from the text |
    | `note_nlp_source_concept_id` | Source vocabulary concept (UMLS, MedLEE, etc.) |
    | `nlp_system` | NLP engine used (cTAKES, MedLEE, BERT, etc.) |
    | `nlp_date` | When the NLP pipeline was run |
    | `term_exists` | Affirmed (1), negated (0), or uncertain |
    | `term_temporal` | Timing: current, history of, planned |
    | `term_modifiers` | Additional qualifiers (severity, etc.) |

## What to Watch For

!!! warning "Common pitfalls"

    **One concept per row**
    :   Multiple entities in one sentence produce multiple rows. Don't assume 1:1 with notes.

    **Tool-dependent structure**
    :   Different NLP pipelines populate different fields. Know what your pipeline supports.

    **Limited population at Emory**
    :   This table is project-specific at present. Check [Known Issues](../../../../../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) for current status.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Symptom mentions in COVID-era ER notes | `note_nlp.note_nlp_concept_id` + `note.note_type_concept_id` + date filter |
| Undocumented comorbidities found in text | `note_nlp` (`term_exists` = 1) cross-checked against `condition_occurrence` |
| Goals-of-care documentation frequency | `note_nlp.lexical_variant` or `note_nlp_concept_id` for palliative terms |
| NLP pain assessments vs. structured scores | `note_nlp` + `measurement` (pain scale) |
| Functional decline trends across progress notes | `note_nlp_concept_id` (functional status) + `nlp_date` |
