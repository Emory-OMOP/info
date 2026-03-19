---
hide:
  - footer
title: "TRIPOD-LLM Alignment"
---

# TRIPOD-LLM Alignment

!!! danger "DRAFT — Internal Review Only · Not for distribution in wide release"

    This document is a **working draft** intended for internal review by the Enterprise OMOP implementation team and our growing network of collaborators. It has not been finalized, peer-reviewed, or approved for external distribution.

    See [releases](../../Data%20in%20Enterprise%20OMOP/Releases/) and [roadmap](../../Project%20and%20Product%20Management/Product%20Roadmap/) for details.

!!! tip "Context"

    See [:octicons-arrow-left-24: Notes and NLP Design](./) for the problem overview and [:octicons-arrow-left-24: Architecture](architecture.md) for the full schema specification.

## Two halves of the same problem

In January 2025, **TRIPOD-LLM** was published in *Nature Medicine* as a consensus reporting guideline for studies using large language models in healthcare (Gallifant et al., 2025). It provides 19 main items and 50 subitems covering everything from title and abstract through methods, results, and discussion — a comprehensive checklist for *what to write in a paper*.

The Enterprise OMOP NLP infrastructure addresses the other half: *what to record in the database*. TRIPOD-LLM tells authors how to describe their NLP pipeline in a methods section. Our architecture makes that same metadata queryable, traceable, and attached to every row of extracted data.

**Neither replaces the other.** A TRIPOD-LLM–compliant paper without infrastructure metadata leaves downstream researchers unable to audit the data. Infrastructure metadata without publication-level reporting leaves the scientific community unable to evaluate the approach. Both are necessary.

---

## Mapping TRIPOD-LLM to the NLP infrastructure

The table below maps TRIPOD-LLM checklist items to the corresponding tables and fields in the Enterprise OMOP NLP architecture. Items are grouped by where the metadata lives: in the infrastructure (queryable), in the publication (prose), or requiring both.

### Model and pipeline identity

These items describe *what* system produced the NLP output.

| TRIPOD-LLM Item | Description | Infrastructure Table | Infrastructure Fields |
|:---|:---|:---|:---|
| **6a** | Report the LLM name, version, and last date of training | `nlp_system` | `name`, `version` |
| **6b** | Report architecture, training, fine-tuning, alignment strategy | `nlp_system`, `Component` | `name`, `version`, `data` |
| **6c** | Report prompt engineering, inference settings (seed, temperature, max tokens) | `pipeline`, `pipeline_component` | `pipeline_name`, `config` |

!!! success "Infrastructure advantage"

    When a researcher queries `measurement_DERIVED`, they can join through `note_span_execution` → `nlp_execution` → `nlp_system` to recover the exact system name, version, and pipeline configuration that produced every row — without consulting the original paper.

### Data and preprocessing

These items describe *what data* the NLP system processed.

| TRIPOD-LLM Item | Description | Infrastructure Table | Infrastructure Fields |
|:---|:---|:---|:---|
| **5a** | Sources of training, tuning, and evaluation data | `nlp_system`, `Component` | `data` (model artifact references) |
| **5b** | Quantitative and qualitative description of the dataset | Publication only | — |
| **5c** | Date of oldest and newest data used | `nlp_execution` | `nlp_date` |
| **5d** | Data preprocessing and quality checking | Publication + `pipeline_component` | `config` |
| **5e** | Missing and imbalanced data handling | Publication only | — |

### Execution and reproducibility

These items describe *when and how* the NLP system ran.

| TRIPOD-LLM Item | Description | Infrastructure Table | Infrastructure Fields |
|:---|:---|:---|:---|
| **12** | Compute, proxies, time, machines, inference time | `nlp_execution` | `nlp_date`, `worker_version` |
| **6d** | Initial and postprocessed output (probabilities, classification) | `note_span` | `probability` |
| **6e** | Classification rationale and thresholds | `note_span`, confidence tiers | `probability` thresholds |
| **14f** | Availability of code to reproduce results | Publication only | — |

!!! success "Infrastructure advantage"

    TRIPOD-LLM item 12 asks authors to report compute details in prose. The infrastructure captures `nlp_execution` records with execution dates and worker versions automatically — every run, not just the one described in the paper.

### Output quality and evaluation

These items describe *how well* the NLP system performed.

| TRIPOD-LLM Item | Description | Infrastructure Table | Infrastructure Fields |
|:---|:---|:---|:---|
| **7a** | Metrics: consistency, relevance, accuracy, errors vs gold standards | Publication + future `nlp_evaluation` | Planned extension |
| **7b** | Outcome metrics' relevance to deployment | Publication only | — |
| **7c** | How predictions were calculated (formula, code, API) | `pipeline`, `pipeline_component` | `config`, component chain |
| **7d** | Annotator qualifications, interassessor agreement | Publication only | — |
| **7e** | Comparison to other LLMs, humans, benchmarks | Publication only | — |

!!! info "Future direction: evaluation metadata"

    The current architecture does not include tables for model performance metrics (precision, recall, F1). This is identified as a [future direction](architecture.md#future-directions) — linking execution records to evaluation results from validation runs would close the gap between TRIPOD-LLM items 7a–7e and queryable infrastructure.

### Annotation and prompting

These items describe *how human oversight* was conducted.

| TRIPOD-LLM Item | Description | Infrastructure Table | Infrastructure Fields |
|:---|:---|:---|:---|
| **8a** | Annotation guidelines and labeling methodology | Publication only | — |
| **8b** | Number of annotators, interannotator agreement | Publication only | — |
| **8c** | Annotator background and experience | Publication only | — |
| **9a** | Prompt design, curation, and selection processes | `pipeline_component` | `config` (prompt stored as component config) |
| **9b** | Data used to develop prompts | Publication only | — |
| **10** | Preprocessing of data before summarization | `pipeline_component` | `config`, component chain |

### Provenance and separation

These items describe *how to distinguish* NLP-derived data from discrete clinical data — the core contribution of the Enterprise OMOP architecture that TRIPOD-LLM does not address.

| Concern | TRIPOD-LLM Coverage | Infrastructure Coverage |
|:---|:---|:---|
| Separating NLP data from discrete EHR data | Not addressed | `_DERIVED` suffix tables |
| Tracing an extracted fact back to the source note | Not addressed | Full provenance chain: `_DERIVED` → `note_nlp_modifier` → `note_span` → `note` |
| Filtering by pipeline version or confidence | Not addressed | `nlp_execution` join + `probability` field |
| Supporting multiple NLP systems on the same notes | Not addressed | `nlp_system` + `pipeline` + `nlp_execution` hierarchy |
| Downstream researcher audit capability | Not addressed | All metadata is queryable SQL, not prose |

!!! warning "The gap TRIPOD-LLM cannot fill"

    TRIPOD-LLM is a publication checklist — it standardizes what authors write in a methods section. But a downstream researcher who joins `condition_DERIVED` to their cohort two years later does not read the original paper. They need the metadata *in the database*, attached to the data, queryable with SQL.

    This is the fundamental gap the Enterprise OMOP NLP infrastructure addresses.

---

## Summary

| Dimension | TRIPOD-LLM | Enterprise OMOP NLP Infrastructure |
|:---|:---|:---|
| **Audience** | Paper authors, reviewers, editors | NLP engineers, researchers, downstream data consumers |
| **Format** | Prose in a manuscript | Structured, queryable database tables |
| **Scope** | One study, one publication | Every execution, every pipeline, every extracted fact |
| **Lifecycle** | Written once at publication time | Updated with every pipeline run |
| **Provenance depth** | Describes the pipeline in a methods section | Links every derived row to the exact execution, system, and source note |
| **Data separation** | Not addressed | `_DERIVED` tables structurally separate NLP data from discrete EHR data |
| **Reproducibility** | Enables reproduction from the paper | Enables audit from the data |

---

## References

- Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. *Nature Medicine*. 2025;31:60–69. [doi:10.1038/s41591-024-03425-5](https://doi.org/10.1038/s41591-024-03425-5)
- Fu S, Wang L, Moon S, et al. Recommended practices and ethical considerations for natural language processing–assisted observational research: A scoping review. *Clinical and Translational Science*. 2023;16(3):398–411. [doi:10.1111/cts.13463](https://doi.org/10.1111/cts.13463)
- TRIPOD-LLM interactive checklist: [tripod-llm.vercel.app](https://tripod-llm.vercel.app/)

---

## Related Pages

- [:octicons-arrow-left-24: Notes and NLP Design](./) — The problem and why NLP metadata matters
- [:octicons-arrow-left-24: Architecture](architecture.md) — The 4-layer, 13-table schema specification
- [:octicons-arrow-left-24: Entity Relationship Diagram](entity-relationship-diagram.md) — Visual schema reference
