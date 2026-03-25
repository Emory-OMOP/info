---
hide:
  - footer
title: "Architecture"
---

# Architecture

!!! danger "DRAFT — Internal Review Only · Not for distribution in wide release"

    This document is a **working draft** intended for internal review by the Enterprise OMOP implementation team and our growing network of collaborators. It has not been finalized, peer-reviewed, or approved for external distribution. Schema details, table names, and implementation guidance are subject to change.

    See [releases](../../Data%20in%20Enterprise%20OMOP/Releases/) and [roadmap](../../Project%20and%20Product%20Management/Product%20Roadmap/) for details.

    **Authors**: Emory University — Enterprise OMOP Implementation Team

    **Version**: 0.1 | **Date**: March 17, 2026

!!! tip "New to NLP in OMOP?"

    Start with [:octicons-arrow-left-24: Notes and NLP Design](./) for a general overview of the problem this architecture is designed to solve.

## A Span-Based NLP Infrastructure for OMOP CDM

The OMOP CDM includes the `note_nlp` table for storing structured outputs from NLP applied to clinical notes. However, this flat, single-table design presents significant limitations for modern NLP workflows: it lacks pipeline provenance, cannot represent span-level annotations with relationships, and conflates NLP-derived data with discrete clinical observations.

We propose an extended schema architecture that addresses these gaps through four layers:

1. **NLP Process Metadata** for full pipeline provenance
2. **Span-based annotation model** for rich NLP output representation
3. **Modifier-based intermediate translation layer**
4. **`_DERIVED` suffix tables** that maintain clear separation between ETL-sourced and NLP-derived clinical data

This design draws on work by the **IOMED NLP** team, the **OHDSI NLP Working Group**, and includes **Emory-specific extensions** for operational deployment.

---

## The Problem

Clinical notes contain diagnoses, medications, temporal relationships, lab values, and social determinants that never reach the structured tables of the OMOP CDM. NLP can extract this information, but the current `note_nlp` table was designed as a minimal landing zone.

!!! warning "Limitations of `note_nlp`"

    **No pipeline provenance**
    :   When multiple NLP systems process the same notes, there is no standard way to record which system produced which result, at which version, on which date.

    **Flat annotation model**
    :   Modern NLP produces span-level annotations with probabilities, typed extractions (dates, quantities), and inter-span relationships. The `note_nlp` table cannot represent these structures.

    **Conflation of data provenance**
    :   If NLP-extracted lab values land in the same `measurement` table as discrete EHR data, researchers cannot distinguish high-confidence discrete values from probabilistic NLP extractions without complex filtering logic.

---

## Architecture Overview

The architecture flows through four layers, from the OMOP `note` table to `_DERIVED` CDM tables:

```
 OMOP note     NLP Model      Process Metadata    NLP Output +        _DERIVED
  table      (train/infer)      Creation          Intermediate       OMOP CDM Tables
─────────── ─────────────── ─────────────────── ─────────────────── ───────────────────
                              nlp_system          note_span           measurement_DERIVED
  note ───▶  Model ────────▶ pipeline            note_span_concept   death_DERIVED
             Train           Component            nlp_date            condition_DERIVED
                              pipeline_component  nlp_quantity        drug_DERIVED
                              nlp_execution       note_span_assert.    procedure_DERIVED
                              note_span_execution note_nlp_modifier   observation_DERIVED
```

!!! info "Key principle"

    Data is **not** forwarded from the NLP process metadata tables to the OMOP metadata tables. The process metadata layer is an operational concern; the output metadata layer produces the clinical data that lands in `_DERIVED` tables.

---

## Layer 1: NLP Process Metadata Creation

These tables describe the NLP infrastructure itself. They are **not forwarded to OMOP metadata tables** — they exist to support pipeline management, reproducibility, and auditability.

???+ example "`nlp_system` — NLP system registration"

    The top-level registration of an NLP system (e.g., "MedSpaCy v1.2", "Emory Clinical NER v3").

    | Column | Type | Description |
    |--------|------|-------------|
    | `nlp_system_id` | int (PK) | Unique identifier for the NLP system |
    | `name` | varchar | Human-readable name of the system |
    | `version` | int | Version number |
    | `source` | varchar | Source platform or registry (e.g., `github`, `huggingface`, `pypi`, `docker`, `s3`) |
    | `source_uri` | varchar | Full addressable location (e.g., `github.com/EmoryDataSolutions/emory_omop_internal_nlp`) |
    | `source_version` | varchar | Machine-verifiable version (git SHA, HF commit, Docker tag, PyPI version) |

???+ example "`pipeline` — Pipeline configuration"

    A specific pipeline configuration within an NLP system. A single system may expose multiple pipelines (e.g., "medication_extraction", "negation_detection").

    | Column | Type | Description |
    |--------|------|-------------|
    | `pipeline_id` | int (PK) | Unique identifier for the pipeline |
    | `pipeline_name` | varchar | Descriptive name |
    | `programming_language` | varchar | Implementation language (e.g., Python, Java) |
    | `active` | varchar | Whether the pipeline is currently active |
    | `source` | varchar | Source platform or registry (e.g., `github`, `huggingface`, `pypi`, `docker`, `s3`) |
    | `source_uri` | varchar | Full addressable location (e.g., `github.com/EmoryDataSolutions/emory_omop_internal_nlp`) |
    | `source_version` | varchar | Machine-verifiable version (git SHA, HF commit, Docker tag, PyPI version) |

???+ example "`Component` — Pipeline components"

    An individual processing step within a pipeline (e.g., a tokenizer, a named entity recognizer, a concept linker).

    | Column | Type | Description |
    |--------|------|-------------|
    | `component_id` | int (PK) | Unique identifier for the component |
    | `component_name` | varchar | Name of the component |
    | `version` | varchar | Component version string |
    | `data` | varchar | Reference to model artifacts or data dependencies |
    | `is_pipe` | varchar | Whether this component is itself a sub-pipeline |
    | `source` | varchar | Source platform or registry (e.g., `github`, `huggingface`, `pypi`, `docker`, `s3`) |
    | `source_uri` | varchar | Full addressable location (e.g., `github.com/EmoryDataSolutions/emory_omop_internal_nlp`) |
    | `source_version` | varchar | Machine-verifiable version (git SHA, HF commit, Docker tag, PyPI version) |

!!! info "Source provenance"

    Source provenance applies at all three levels because systems, pipelines, and components may originate from different repositories or registries. For example, an NLP system may live in a GitHub repo, while one of its components is a HuggingFace model and another is a PyPI package. The `source` / `source_uri` / `source_version` triple provides machine-verifiable provenance regardless of where the artifact lives.

    | Level | source | source_uri | source_version |
    |-------|--------|-----------|----------------|
    | nlp_system | github | github.com/EmoryDataSolutions/emory_omop_internal_nlp | 83b3464 |
    | component (medspacy) | pypi | medspacy | 1.2.0 |
    | component (BERT) | huggingface | emilyalsentzer/Bio_ClinicalBERT | a2ab630 |

??? example "`pipeline_component` — Pipeline-component linkage"

    Junction table linking pipelines to their constituent components, with per-pipeline configuration.

    | Column | Type | Description |
    |--------|------|-------------|
    | `pipeline_id` | int (FK) | Pipeline this component belongs to |
    | `component_id` | int (FK) | The component |
    | `config` | varchar | JSON or serialized configuration for this component within this pipeline |
    | `num_instances` | int | Number of parallel instances (for distributed execution) |

??? example "`nlp_execution` — Execution records"

    A record of a specific pipeline run — when it happened, which system and pipeline were used, and the worker version.

    | Column | Type | Description |
    |--------|------|-------------|
    | `nlp_execution_id` | int (PK) | Unique identifier for this execution |
    | `nlp_system_id` | int (FK) | The system that ran |
    | `pipeline_id` | int (FK) | The pipeline configuration used |
    | `worker_version` | int | Version of the execution worker/runtime |
    | `nlp_date` | date | Date the execution occurred |

??? example "`note_span_execution` — Span-to-execution linkage"

    Junction table linking individual note spans (outputs) back to the execution that produced them.

    | Column | Type | Description |
    |--------|------|-------------|
    | `note_span_id` | int (FK) | The output span |
    | `nlp_execution_id` | int (FK) | The execution that produced it |

---

## Layer 2: Note NLP Minimal Required Metadata

These tables store the actual NLP outputs. Some metadata from this layer is pushed to OMOP metadata tables for discoverability. This layer adopts the OHDSI NLP Working Group's span-based model.

???+ example "`note_span` — Core annotation table"

    Each row represents a contiguous span of text identified by the NLP system, with character-level offsets into the source note.

    | Column | Type | Description |
    |--------|------|-------------|
    | `note_span_id` | int (PK) | Unique identifier for the span |
    | `source_primary_key_source` | varchar | Fully qualified source path identifying the source system and column (e.g., `clarity.dbo.hno_notes.note_csn_id`) |
    | `source_primary_key` | varchar | The note identifier in that source system |
    | `span_start` | int | Character offset of span start (0-indexed) |
    | `span_end` | int | Character offset of span end (exclusive) |
    | `span_text` | varchar | The extracted text |
    | `probability` | double | Confidence score from the NLP model |

    NLP practitioners submit spans referencing notes by **source system identifiers**, not OMOP `note_id`. Resolution to OMOP IDs happens downstream via `note_mapping`, following the same `_source_primary_key_source` + `_source_primary_key` pattern used across the Enterprise OMOP pipeline (e.g., `visit_occurrence_mapping`, `care_site_mapping`).

    Character offsets enable precise text localization, which is critical for annotation review, model debugging, and adjudication workflows.

???+ example "`note_span_concept` — Concept mappings"

    Maps a span to one or more OMOP concepts. Supports both a standardized `concept_id` and a `source_concept_id` for the raw vocabulary mapping before standardization.

    | Column | Type | Description |
    |--------|------|-------------|
    | `note_span_id` | int (FK) | The annotated span |
    | `concept_id` | int (FK) | Standard OMOP concept |
    | `source_concept_id` | int (FK) | Source vocabulary concept before mapping |

??? example "`nlp_date` — Temporal extractions"

    Typed extraction for temporal expressions found in text (e.g., "last Tuesday", "March 2024").

    | Column | Type | Description |
    |--------|------|-------------|
    | `nlp_date_id` | int (PK) | Unique identifier |
    | `note_span_id` | int (FK) | The span containing the date expression |
    | `date_precision_concept_id` | int (FK) | Precision level (day, month, year) |
    | `nlp_date_time` | datetime | Resolved date/time value |

??? example "`nlp_quantity` — Numeric extractions"

    Typed extraction for numeric values with units (e.g., "BP 120/80 mmHg", "weight 72 kg").

    | Column | Type | Description |
    |--------|------|-------------|
    | `nlp_quantity_id` | int (PK) | Unique identifier |
    | `note_span_id` | int (FK) | The span containing the quantity |
    | `base_units_concept_id` | int (FK) | OMOP concept for the unit of measurement |
    | `magnitude_base_units` | double | The extracted numeric value |
    | `magnitude_base_units_range_low` | double | Lower bound (for range expressions) |
    | `magnitude_base_units_range_high` | double | Upper bound (for range expressions) |

??? example "`note_span_assertion` — Contextual assertions and inter-span relationships"

    Captures contextual assertions about spans — negation, experiencer, temporality, certainty — as well as binary inter-span relationships (e.g., a medication span "metformin" related to a dosage span "500mg").

    | Column | Type | Description |
    |--------|------|-------------|
    | `source_note_span_id` | int (FK) | The source span |
    | `target_note_span_id` | int (FK) | The target span; NULL for unary assertions (e.g., negation of a single span) |
    | `label_concept_id` | int (FK) | OMOP concept describing the assertion type (negation, experiencer, temporality, certainty) or relationship type |
    | `probability` | double | Confidence score for the assertion or relationship |

???+ example "`note_mapping` — Source-to-OMOP note resolution"

    Maps source system note identifiers to OMOP `note_id`. This is the bridge that allows `note_span` rows — which reference notes by source system keys — to be resolved to OMOP note table IDs downstream in dbt. Analogous to `visit_occurrence_mapping` and `care_site_mapping` in the existing Enterprise OMOP pipeline.

    | Column | Type | Description |
    |--------|------|-------------|
    | `note_id` | int (FK) | OMOP `note` table ID |
    | `source_primary_key_source` | varchar | Source system identifier (matches `note_span.source_primary_key_source`) |
    | `source_primary_key` | varchar | Note ID in source system (matches `note_span.source_primary_key`) |

    This table is populated by the ETL pipeline (not the NLP service) and is maintained as a reference for downstream dbt transformations.

### Terminology: Why `note_span_assertion`

The term **assertion** is the standard designation in clinical NLP for contextual attributes of extracted entity spans. It originates from the [i2b2/VA 2010 shared task](https://pmc.ncbi.nlm.nih.gov/articles/PMC3168320/) on "concepts, **assertions**, and relations in clinical text" (Uzuner et al., 2011), which established the canonical annotation categories: present/absent (negation), experiencer (patient vs. family), and hypothetical/conditional (certainty). This terminology was continued by the [n2c2](https://n2c2.dbmi.hms.harvard.edu/) Track 1 context classification tasks.

The [ConText algorithm](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757457/) (Harkema et al., 2009) is the foundational method for detecting these assertions automatically. Its successors — NegEx, pyConText, and medspaCy's `ConTextComponent` — remain the dominant approach in production clinical NLP systems.

The standard assertion categories are:

- **Negation** — whether a finding is present or absent (e.g., "denies chest pain")
- **Experiencer** — whether the finding pertains to the patient or someone else (e.g., "family history of diabetes")
- **Temporality** — whether the finding is current, historical, or hypothetical (e.g., "prior MI")
- **Certainty** — the confidence level: definite, possible, conditional (e.g., "possible pneumonia")

| Term | Used by | Scope |
|------|---------|-------|
| **Assertion** | i2b2, n2c2, academic publications | The annotation task and the concept itself |
| **Context** | ConText algorithm (Harkema et al.) | The algorithm that detects assertions |
| **Modifiers** | medspaCy, cTAKES, OMOP `term_modifiers` | Implementation-level term |

This table was previously named `note_span_relationship`. The rename to `note_span_assertion` reflects its primary role: capturing unary assertions about spans (negation, temporality, experiencer, certainty) via `label_concept_id`, with `target_note_span_id` = NULL for unary assertions. The table can also capture binary inter-span relationships when `target_note_span_id` is populated — but the dominant use case is assertion, and the name should reflect that.

---

## Layer 3: Intermediate Translation

### `note_nlp_modifier`

This table serves as the **bridge** between the span-based NLP output model and the OMOP CDM domain tables. Each row captures a single modifier attribute extracted from or derived for a span, in a format amenable to CDM mapping.

???+ example "Field reference (click to expand)"

    | Column | Type | Description |
    |--------|------|-------------|
    | `note_nlp_modifier_id` | int (PK) | Unique identifier |
    | `note_span_id` | int (FK) | The source span |
    | `note_nlp_modifier_field_concept_id` | int (FK) | The target CDM field this modifier populates (e.g., `condition_start_date`, `condition_concept_id`) |
    | `note_nlp_modifier_date` | date | Date value, if the modifier is temporal |
    | `note_nlp_modifier_string` | varchar | String value, if the modifier is textual |
    | `note_nlp_modifier_concept_id` | int (FK) | Concept value, if the modifier maps to a standard concept |
    | `note_nlp_modifier_number` | int | Numeric value, if the modifier is quantitative |
    | `nlp_execution_id` | int (FK) | Provenance link to the execution that produced this modifier |

!!! question "Why an intermediate step?"

    The span model (Layer 2) is optimized for **NLP output fidelity** — preserving exactly what the model found, where, and with what confidence. The CDM domain tables (Layer 4) are optimized for **clinical analytics** — person-level observations with dates and standard concepts.

    The `note_nlp_modifier` table provides the structured, typed attribute representation needed to map between these two paradigms. It decomposes complex span annotations into individual modifier fields that can be systematically transformed into CDM rows.

---

## Layer 4: OMOP CDM `_DERIVED` Tables

NLP-extracted observations land in tables suffixed with `_DERIVED`, which mirror the schema of their standard CDM counterparts:

| DERIVED Table | Standard CDM Counterpart | Example Use Case |
|---------------|--------------------------|------------------|
| `measurement_DERIVED` | `measurement` | Lab values extracted from notes (e.g., "A1c 7.2%") |
| `death_DERIVED` | `death` | Death dates extracted from discharge summaries |
| `condition_DERIVED` | `condition_occurrence` | Diagnoses mentioned in clinical notes |
| `drug_DERIVED` | `drug_exposure` | Medication mentions extracted from notes |
| `procedure_DERIVED` | `procedure_occurrence` | Procedures referenced in operative notes |
| `observation_DERIVED` | `observation` | Social determinants, symptoms, and other observations |

!!! tip "Design rationale"

    **Ensure clear separation between the clinical tables, and the derived elements from NLP for those tables.** Coupled with the upstream linkage to NLP metadata, researchers can choose which NLP-derived data is acceptable to join to the standard clinical table.

    - `measurement` holds discrete lab values from the EHR (high confidence, structured source)
    - `measurement_DERIVED` holds NLP-extracted lab values (variable confidence, unstructured source)

    By populating the upstream NLP metadata about the pipeline, researchers can **select specific runs, by specific NLP implementers**, filtering by execution date, system version, or confidence threshold before choosing to incorporate derived data into their analyses.

    *— Enterprise OMOP Implementation Team*

### Emory Extended Columns

Beyond the standard OMOP 5.4 columns, `_DERIVED` tables include Emory-specific columns for direct provenance linkage:

| Column | Type | Description |
|--------|------|-------------|
| `note_span_id` | int (FK) | Direct link to the source span in `note_span` |
| `execution_id` | int (FK) | Direct link to the NLP execution in `nlp_execution` |
| `_source_primary_key` | varchar | Caret-delimited `note_nlp_modifier_id` values that produced this row (e.g., `1000^1001`) |
| `_source_primary_key_source` | varchar | Fixed value: `note_nlp_modifier` |
| `condition_type_concept_id` | int (FK) | Set to the *NLP-Derived* concept to mark provenance (applies similarly as `*_type_concept_id` in other `_DERIVED` tables) |

### Backward Compatibility

The `_DERIVED` tables include all columns from their standard CDM counterparts, plus the Emory extended columns described above:

- Existing OHDSI tools (ATLAS, CohortDiagnostics, FeatureExtraction) can target `_DERIVED` tables with minimal configuration changes — OHDSI tools ignore unknown columns, so the extra provenance columns do not break compatibility
- A `UNION ALL` view can combine standard and derived tables when a researcher decides NLP-derived data meets their quality threshold
- The standard CDM tables remain untouched — no schema modifications required

---

## Full Provenance Chain

Every NLP-derived observation can be traced back through the full chain:

```
measurement_DERIVED row
  → note_nlp_modifier (what modifier attributes were applied)
    → note_span (exact text, character offsets, confidence)
      → note_mapping (resolves source_primary_key → OMOP note_id)
        → note (the original clinical text)
      → note_span_execution (which execution produced this span)
        → nlp_execution (when, which pipeline)
          → pipeline + pipeline_component (which components, what config)
            → nlp_system (which system, what version)
```

| Layer | Concern | Audience |
|-------|---------|----------|
| Process Metadata | What NLP infrastructure ran | NLP engineers, MLOps |
| Output Metadata | What was extracted from text | NLP researchers, annotators |
| Intermediate | How to map spans to CDM | ETL developers |
| `_DERIVED` Tables | Clinical analytics on NLP data | Researchers, clinicians |

---

## Comparison with Standard `note_nlp`

| Capability | Standard `note_nlp` | Proposed Architecture |
|------------|---------------------|----------------------|
| Pipeline provenance | Single `nlp_system` string field | Full normalized hierarchy (system, pipeline, component, execution) |
| Span representation | `offset` + `snippet` (substring) | `span_start` / `span_end` character offsets + `span_text` |
| Confidence scores | Not supported | `probability` on spans and assertions |
| Typed extractions | Not supported | Dedicated `nlp_date`, `nlp_quantity` tables |
| Contextual assertions and inter-span relationships | Not supported | `note_span_assertion` with typed labels |
| Separation from discrete data | NLP data lands in standard CDM tables | `_DERIVED` suffix tables with explicit provenance |
| Modifier representation | Free-text `term_modifiers` string | Structured `note_nlp_modifier` with typed fields |

---

## Implementation Guidance

### Pipeline Registration

Before any NLP processing occurs, register the infrastructure:

1. **Register the NLP system** in `nlp_system` with a unique name and version
2. **Register components** in `Component` — each tokenizer, model, post-processor gets an entry
3. **Define pipelines** in `pipeline` and link components via `pipeline_component`, including per-component configuration

This registration is a one-time setup per pipeline version. When a component is updated (e.g., a new model checkpoint), increment the component version and create a new pipeline entry.

### Execution and Annotation Flow

For each NLP run:

1. Create an `nlp_execution` record capturing the system, pipeline, worker version, and date
2. Process notes through the pipeline, producing span-level annotations
3. Write `note_span` rows with `source_primary_key_source` and `source_primary_key` identifying the source note, along with character offsets, extracted text, and confidence scores
4. Write typed extractions to `note_span_concept`, `nlp_date`, `nlp_quantity`, and `note_span_assertion` as appropriate
5. Link spans to executions via `note_span_execution`

!!! note "Source key pattern"

    The bronze ingestion layer (FastAPI service) accepts source system identifiers rather than OMOP `note_id` values. NLP practitioners reference notes using `source_primary_key_source` (the fully qualified source path, e.g., `clarity.dbo.hno_notes.note_csn_id`) and `source_primary_key` (the value in that source column). Resolution from source keys to OMOP `note_id` is handled downstream by dbt via the `note_mapping` table. This follows the existing Emory `_source_primary_key_source` + `_source_primary_key` pattern used for `visit_occurrence_mapping`, `care_site_mapping`, and other identity resolution tables in the Enterprise OMOP pipeline.

### Translation to `_DERIVED` Tables

The translation from span-based output to CDM-compatible rows is a distinct ETL step:

1. **Filter negated spans** — spans with a negation assertion in `note_span_assertion` do not produce modifier rows. They are retained in Layer 2 for auditability but excluded from downstream translation
2. **Generate `note_nlp_modifier` rows** from non-negated span annotations — decomposing each span into its modifier attributes (concept, date, string, number)
3. **Collapse modifiers to `_DERIVED` rows** — multiple modifiers for the same span + execution merge into a single `_DERIVED` row (e.g., a condition span with separate date and concept modifiers produces one `condition_DERIVED` row)
4. **Map modifiers to CDM domain tables** — for each span with a mapped concept, determine the target domain (measurement, condition, drug, etc.) based on the concept's `domain_id` in the OMOP vocabulary
5. **Write `_DERIVED` rows** with appropriate linkage back to `note_nlp_modifier` for provenance

### Confidence Thresholds

!!! info "Recommended thresholds (calibrate per system)"

    | Tier | Probability Range | Recommendation |
    |------|-------------------|----------------|
    | High confidence | &ge; 0.90 | Auto-populate `_DERIVED` tables |
    | Medium confidence | 0.70 – 0.89 | Populate with flag; available for research opt-in |
    | Low confidence | < 0.70 | Retain in `note_span` only; do not translate to `_DERIVED` |

### Schema Deployment

| Zone | Tables | Schema Recommendation |
|------|--------|-----------------------|
| NLP Operations | nlp_system, pipeline, Component, pipeline_component, nlp_execution, note_span_execution | Dedicated `nlp_ops` schema |
| NLP Output | note_span, note_span_concept, nlp_date, nlp_quantity, note_span_assertion, note_nlp_modifier | Dedicated `nlp_output` schema |
| CDM Extended | measurement_DERIVED, death_DERIVED, condition_DERIVED, drug_DERIVED, procedure_DERIVED, observation_DERIVED | Same schema as CDM (or `cdm_derived` schema) |

---

## Research Patterns

| Question | How to Query |
|----------|-------------|
| NLP-extracted A1c values from a specific pipeline | Join `measurement_DERIVED` through `note_nlp_modifier` → `note_span` → `note_span_execution` → `nlp_execution` → `nlp_system`, filter by system name and version |
| All medication mentions with confidence > 0.85 | Query `note_span` joined to `note_span_concept` where `probability >= 0.85` and concept is in Drug domain |
| Compare NLP-derived conditions to discrete diagnoses | `UNION ALL` of `condition_occurrence` and `condition_DERIVED`, with a source flag column |
| Audit which NLP pipeline produced a specific finding | Trace `note_span_execution` → `nlp_execution` → `pipeline` → `pipeline_component` → `Component` |

---

## Attribution

This architecture integrates work from three sources:

- **IOMED NLP** — NLP process metadata tables (`nlp_system`, `pipeline`, `Component`, `pipeline_component`, `nlp_execution`, `note_span_execution`)
- **OHDSI NLP Working Group** — Span-based annotation model and typed extraction tables (`note_span`, `note_span_concept`, `nlp_date`, `nlp_quantity`, `note_span_assertion`)
- **Emory Enterprise OMOP Team** — `_DERIVED` table pattern, `note_nlp_modifier` intermediate translation layer, operational deployment guidance, and column modifications

### References

- Uzuner Ö, South BR, Shen S, DuVall SL. 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text. *Journal of the American Medical Informatics Association*. 2011;18(5):552–556. [PMC3168320](https://pmc.ncbi.nlm.nih.gov/articles/PMC3168320/)
- Harkema H, Dowling JN, Thornblade T, Chapman WW. ConText: an algorithm for determining negation, experiencer, and temporal status from clinical reports. *Journal of Biomedical Informatics*. 2009;42(5):839–851. [PMC2757457](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757457/)
- n2c2 NLP Clinical Challenges — successor to i2b2, continuing shared tasks on clinical NLP including context classification. [n2c2.dbmi.hms.harvard.edu](https://n2c2.dbmi.hms.harvard.edu/)

---

## Future Directions

- **Annotation adjudication tables** — Schema support for multi-annotator review, inter-annotator agreement, and gold-standard corpus management
- **Model performance metadata** — Linking execution records to evaluation metrics (precision, recall, F1) from validation runs
- **OMOP CDM proposal** — Submitting the `_DERIVED` table pattern and span-based model as a formal OMOP CDM extension
- **Cross-site federation** — Validating the schema for federated NLP analyses across OHDSI network sites

---

## Related Pages

- [:octicons-arrow-right-24: NLP Glossary](glossary.md) — Terminology reference for clinical NLP concepts
- [:octicons-arrow-right-24: Note NLP (OMOP Primer)](../../OMOP%20Primers/Standardized%20Categories/Clinical%20Data/Notes/Note%20NLP/index.md) — Standard `note_nlp` table reference
- [:octicons-arrow-right-24: Data Mapping](../Data%20Mapping/index.md) — How source data flows into OMOP
- [:octicons-arrow-right-24: Data Quality Design](../Data%20Quality/Data%20Quality%20Design/index.md) — DataOps framework for pipeline quality
