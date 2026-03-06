---
hide:
  - footer
title: Note
---

# Note

**Epic equivalent**: Clinical documentation / Radiology reports / History & Physical / Discharge summaries

The `note` table captures **unstructured clinical text** — progress notes, discharge summaries, radiology reports, pathology interpretations, and other narrative documentation. In Epic, this maps to clinical documentation across all modules.

Each row is a single note or report. Downstream NLP pipelines can extract structured entities into the `note_nlp` table.

## Epic-to-OMOP Field Mapping

??? example "Field reference (click to expand)"

    | OMOP Field | Epic Equivalent | What It Captures |
    |---|---|---|
    | `note_id` | Note record ID | Unique identifier |
    | `person_id` | Patient ID / MRN | Links to the patient |
    | `note_date` | Note entry date | When authored; `note_datetime` has time precision |
    | `note_type_concept_id` | Note category | Type: discharge summary, pathology report, progress note, etc. |
    | `note_class_concept_id` | Note class | Format: dictation, transcription, structured note |
    | `note_title` | Note header | Original title (e.g., "Follow-Up", "Operative Report") |
    | `note_text` | Full note body | The unstructured text content |
    | `encoding_concept_id` | Character encoding | Usually UTF-8 (metadata) |
    | `language_concept_id` | Language | Typically English |
    | `provider_id` | Author | Who wrote or dictated the note |
    | `visit_occurrence_id` | Linked encounter | Visit context |
    | `note_source_value` | Local note type | Original source label (e.g., "IM Progress Note") |

## What to Watch For

!!! warning "Common pitfalls"

    **Large table — filter first**
    :   The note table can be massive. Always filter by date, note type, or visit before scanning. Check presence/absence of a note type for your patient sample before extracting full text.

    **Unstructured by nature**
    :   Notes require NLP to analyze at scale. The `note_nlp` table captures structured extractions.

    **Note titles vary by site and provider**
    :   Don't rely on `note_title` for classification — use `note_type_concept_id` instead.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Advance directive documentation in free-text notes | `note_text` keyword/NLP search + `note_type_concept_id` |
| Discharge summary analysis for palliative care | `note_text` + `condition_occurrence` (palliative) + NLP |
| ECOG performance status from oncology notes | `note_text` + NLP extraction + `condition_occurrence` (cancer) |
| Suicidal ideation in notes vs. coded diagnoses | `note_text` keyword search vs. `condition_occurrence` |
| Most common note types in the ER | `note_type_concept_id` + `visit_occurrence` (ER filter) |
