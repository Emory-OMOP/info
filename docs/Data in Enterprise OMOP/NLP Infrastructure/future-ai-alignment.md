---
hide:
  - footer
title: "FUTURE-AI Alignment"
---

# FUTURE-AI Alignment

!!! danger "DRAFT — Internal Review Only · Not for distribution in wide release"

    This document is a **working draft** intended for internal review by the Enterprise OMOP implementation team and our growing network of collaborators. It has not been finalized, peer-reviewed, or approved for external distribution.

    See [releases](../../Data%20in%20Enterprise%20OMOP/Releases/) and [roadmap](../../Project%20and%20Product%20Management/Product%20Roadmap/) for details.

!!! tip "Context"

    See [:octicons-arrow-left-24: Notes and NLP Design](./) for the problem overview, [:octicons-arrow-left-24: Architecture](architecture.md) for the full schema specification, and [:octicons-arrow-left-24: TRIPOD-LLM Alignment](tripod-llm-alignment.md) for the companion reporting guideline mapping.

## From reporting to deployment

Where [TRIPOD-LLM](tripod-llm-alignment.md) standardizes what researchers write in a paper, **FUTURE-AI** addresses a broader question: *how should healthcare AI tools be designed, developed, validated, deployed, and monitored to be trustworthy?*

Published in *The BMJ* in February 2025, the FUTURE-AI framework was developed by 117 interdisciplinary experts from 50 countries over a two-year modified Delphi process (Lekadir et al., 2025). It provides **30 best practices** organized under six guiding principles — **F**airness, **U**niversality, **T**raceability, **U**sability, **R**obustness, **E**xplainability — plus 7 cross-cutting General recommendations.

FUTURE-AI is not a publication checklist. It is a **lifecycle framework** that spans from initial design through post-deployment monitoring. This makes it directly relevant to how NLP infrastructure should be built — not just documented.

---

## The six FUTURE-AI principles

| Principle | Core concern | # of recommendations |
|:---|:---|:---|
| **Fairness** | Equal performance across patient groups; bias identification and mitigation | 3 |
| **Universality** | Generalizability across settings, populations, and clinical workflows | 4 |
| **Traceability** | Documentation, auditing, logging, and governance throughout the AI lifecycle | 6 |
| **Usability** | User-centered design, human-AI interaction, oversight, training, and clinical utility evaluation | 5 |
| **Robustness** | Resilience to real-world data variations, adversarial inputs, and distribution shifts | 3 |
| **Explainability** | Clinically meaningful information about the logic behind AI decisions | 2 |

---

## Mapping FUTURE-AI to the NLP infrastructure

### Fairness

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **Fairness 1**: Define sources of bias | Identify potential bias types and sources at design phase | Publication/governance concern. Infrastructure supports post-hoc bias analysis by enabling stratified queries on `_DERIVED` tables joined to `person` demographics. |
| **Fairness 2**: Collect information on data attributes | Collect demographic and data attributes to enable bias detection | OMOP `person` table provides demographics. `note_span` linked to `note` linked to `person` enables demographic stratification of NLP outputs. |
| **Fairness 3**: Evaluate fairness | Apply bias detection methods (statistical parity, group fairness, equalized odds) | Future direction: evaluation metadata tables linking execution records to stratified performance metrics would close this gap. |

### Universality

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **Universality 1**: Define intended clinical settings | Specify populations, settings, and potential obstacles to universality | Publication/governance concern. |
| **Universality 2**: Use existing standards | Build on community standards (SNOMED CT, OMOP, FHIR, etc.) | **Core alignment.** The entire architecture is built on OMOP CDM. `note_span_concept` maps to OMOP standard concepts. `_DERIVED` tables follow CDM schema. OHDSI tools work natively. |
| **Universality 3**: Evaluate using external data | Validate with external datasets from multiple sites | `nlp_execution` records from different sites can be compared. The schema is designed for cross-site federation (identified as a [future direction](architecture.md#future-directions)). |
| **Universality 4**: Evaluate local clinical validity | Assess performance in local clinical workflows and populations | `_DERIVED` tables enable local validation by comparing NLP extractions against discrete EHR data at the same institution. |

!!! success "Infrastructure advantage"

    FUTURE-AI Universality 2 explicitly recommends building on OMOP. The Enterprise OMOP NLP architecture is a native OMOP extension — concept mappings, CDM-compatible `_DERIVED` tables, and vocabulary-driven typed extractions. This is not retrofitted alignment; the infrastructure was designed from the ground up on the standard FUTURE-AI recommends.

### Traceability

The Traceability principle is the most directly aligned with the Enterprise OMOP NLP architecture. FUTURE-AI defines traceability as *"mechanisms for documenting and monitoring the complete trajectory of the AI tool, from development and validation to deployment and usage."*

All six Traceability recommendations map to infrastructure tables:

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **Traceability 1**: Implement risk management | Analyse risks throughout the AI lifecycle; maintain a risk management file | `nlp_system` + `pipeline` registration provides the system-of-record for what is deployed. Risk documentation is a publication/governance concern, but the infrastructure ensures the *identity* of each system is unambiguous. |
| **Traceability 2**: Provide documentation | Create technical documentation (model properties, hyperparameters, training data, evaluation criteria, audits) | `nlp_system` (name, version), `Component` (version, data artifacts), `pipeline_component` (config including hyperparameters). The infrastructure *is* the structured documentation. |
| **Traceability 3**: Implement continuous quality control | Monitor AI inputs and outputs; provide uncertainty estimates | `note_span.probability` captures per-extraction confidence. `nlp_execution` records enable temporal monitoring. `_DERIVED` table separation enables quality comparison against discrete EHR data. |
| **Traceability 4**: Implement periodic auditing and updating | Configurable system for periodic evaluation; detect data drift, concept drift, performance degradation | `nlp_execution` records with dates enable audit trails. Multiple executions of different pipeline versions against the same notes enable before/after comparison. |
| **Traceability 5**: Implement AI logging | Log data accessed, AI predictions, clinical decisions, and issues encountered | `note_span_execution` links every output to its execution. `nlp_execution` captures when, which pipeline, which worker version. The full provenance chain from `_DERIVED` row back to `note` serves as the audit log. |
| **Traceability 6**: Implement AI governance | Specify roles for risk management, auditing, maintenance, and supervision; assign accountability | Governance is an organizational concern, but the infrastructure provides the *substrate* — you cannot govern what you cannot trace. The normalized hierarchy (`nlp_system` → `pipeline` → `Component`) makes it possible to assign ownership per system and pipeline. |

!!! success "Infrastructure advantage"

    FUTURE-AI Traceability asks teams to *implement* logging, auditing, documentation, and quality control. The Enterprise OMOP NLP architecture provides the **schema** where all of this lives — queryable, structured, and attached to every extracted fact. Without this schema, traceability recommendations become aspirational prose in a governance document.

### Usability

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **Usability 1**: Define user requirements | Involve clinical experts and end users from early stages to gather intended use and user requirements | Organizational/process concern. Infrastructure supports usability by producing outputs in standard OMOP CDM format — familiar to OHDSI researchers and compatible with existing analytic tools. |
| **Usability 2**: Establish human-AI interactions and oversight | Create interfaces for effective operation and implement human-in-the-loop mechanisms for quality checks and overrides | `note_span.probability` enables confidence-based review workflows. `_DERIVED` table separation from discrete EHR data supports human comparison and override. The span-level model (offsets, source text) gives reviewers the context needed to evaluate and correct extractions. |
| **Usability 3**: Provide training materials | Supply tutorials, manuals, examples, and hands-on sessions | Publication/documentation concern. The schema's self-describing hierarchy (`nlp_system` → `pipeline` → `Component`) reduces the documentation burden — the structure is the explanation. |
| **Usability 4**: Evaluate user experience | Test usability in real-world clinical settings with diverse end users | Organizational concern. Infrastructure supports evaluation by providing queryable execution records and outputs that can be assessed against clinical workflows. |
| **Usability 5**: Evaluate clinical utility | Demonstrate benefits compared to standard care; document safety | `_DERIVED` tables enable direct comparison of NLP-extracted data against discrete EHR data at the same institution, providing the substrate for clinical utility evaluation. |

!!! success "Infrastructure advantage"

    FUTURE-AI Usability emphasizes human-in-the-loop oversight and clinical validation. The Enterprise OMOP NLP architecture supports this through confidence scores (`note_span.probability`), span-level provenance for human review, and `_DERIVED` table separation that enables side-by-side comparison with discrete clinical data.

### Robustness

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **Robustness 1**: Define sources of data variation | Inventory real-world variations that may affect performance | Publication/governance concern. Infrastructure enables detection through temporal analysis of `nlp_execution` records and confidence distributions in `note_span`. |
| **Robustness 2**: Train with representative data | Use training data that reflects real-world variation | Model training concern, outside infrastructure scope. |
| **Robustness 3**: Evaluate robustness | Stress tests, repeatability tests under real-world conditions | Multiple `nlp_execution` records against the same notes with different pipeline versions enable repeatability analysis. `note_span.probability` distributions can be compared across executions. |

### Explainability

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **Explainability 1**: Define explainability needs | Establish whether and what type of explainability is required | Publication/governance concern. |
| **Explainability 2**: Evaluate explainability | Assess whether explanations are meaningful, correct, and beneficial | `note_span` with character offsets (`span_start`, `span_end`) and `span_text` provides intrinsic explainability — every extraction is grounded in the exact source text. `note_span_relationship` captures inter-span reasoning (e.g., negation, temporal links). |

!!! success "Infrastructure advantage"

    The span-based model provides **built-in explainability** at the extraction level. Every NLP-derived fact in a `_DERIVED` table can be traced back to the exact text span, character offsets, and source note. This is not a post-hoc explanation — it is the provenance chain itself.

### General

| FUTURE-AI Recommendation | Description | Infrastructure Coverage |
|:---|:---|:---|
| **General 1**: Engage stakeholders continuously | Multidisciplinary engagement throughout the AI lifecycle | Organizational concern. |
| **General 2**: Ensure data protection | Privacy-enhancing techniques, data governance, access logging | OMOP's de-identification model applies. `nlp_execution` logging supports data governance audits. |
| **General 3**: Implement measures to address AI risks | Define mitigation plan aligned with application-specific requirements | Risk management file is a governance artifact. Infrastructure provides the audit substrate. |
| **General 4**: Define adequate evaluation plan | Test data, metrics, reference methods, benchmarking | Future direction: evaluation metadata tables. |
| **General 5**: Comply with AI regulations | Identify applicable regulations (EU AI Act, FDA, etc.) | The infrastructure supports compliance by providing the traceability and documentation that regulations require. |
| **General 6**: Investigate ethical issues | Address application-specific ethical, social, legal concerns | Organizational/publication concern. |
| **General 7**: Investigate social and environmental issues | Assess impact on working conditions, sustainability, societal effects | Organizational/publication concern. |

---

## Summary: where infrastructure meets guidance

| FUTURE-AI Principle | Recommendations addressed by infrastructure | Recommendations requiring governance/publication |
|:---|:---|:---|
| **Fairness** (3) | 1 of 3 — demographic stratification via OMOP `person` joins | Bias source definition, fairness evaluation |
| **Universality** (4) | 3 of 4 — OMOP standards, cross-site federation, local validation | Clinical setting definition |
| **Traceability** (6) | All 6 — the infrastructure *is* the traceability layer | Risk documentation, governance roles |
| **Usability** (5) | 2 of 5 — confidence-based review, span provenance for oversight, clinical utility comparison via `_DERIVED` tables | User requirements, training materials, UX evaluation |
| **Robustness** (3) | 2 of 3 — repeatability analysis, variation detection | Training data representativeness |
| **Explainability** (2) | 1 of 2 — span-based provenance provides intrinsic explainability | Explainability needs assessment |

**15 of 23 principle-level recommendations** (plus 2 of 7 general recommendations) are directly supported or enabled by the Enterprise OMOP NLP infrastructure. The remaining recommendations are governance, organizational, or publication concerns that require human processes — but the infrastructure provides the *substrate* that makes those processes auditable rather than aspirational.

---

## FUTURE-AI and TRIPOD-LLM: complementary layers

| Dimension | TRIPOD-LLM | FUTURE-AI | Enterprise OMOP NLP Infrastructure |
|:---|:---|:---|:---|
| **Scope** | Publication reporting | Full AI lifecycle | Production data infrastructure |
| **Format** | Checklist for manuscripts | Best practices framework | Queryable database schema |
| **Primary audience** | Authors and reviewers | Development teams and regulators | NLP engineers and data consumers |
| **Traceability** | Report what was done | Implement logging and auditing | Store provenance at the row level |
| **Standards** | — | Recommends OMOP, SNOMED CT, FHIR | Built natively on OMOP CDM |
| **Lifecycle coverage** | Publication time | Design → deployment → monitoring | Every pipeline execution |

All three layers are necessary. TRIPOD-LLM ensures the scientific community can evaluate the approach. FUTURE-AI ensures the development team builds responsibly. The Enterprise OMOP NLP infrastructure ensures the data itself carries the metadata that both frameworks require.

---

## References

- Lekadir K, Frangi AF, Porras AR, et al. FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare. *BMJ*. 2025;388:e081554. [doi:10.1136/bmj-2024-081554](https://doi.org/10.1136/bmj-2024-081554)
- Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. *Nature Medicine*. 2025;31:60–69. [doi:10.1038/s41591-024-03425-5](https://doi.org/10.1038/s41591-024-03425-5)
- Fu S, Wang L, Moon S, et al. Recommended practices and ethical considerations for natural language processing–assisted observational research: A scoping review. *Clinical and Translational Science*. 2023;16(3):398–411. [doi:10.1111/cts.13463](https://doi.org/10.1111/cts.13463)

---

## Related Pages

- [:octicons-arrow-left-24: Notes and NLP Design](./) — The problem and why NLP metadata matters
- [:octicons-arrow-left-24: TRIPOD-LLM Alignment](tripod-llm-alignment.md) — Mapping the reporting guideline
- [:octicons-arrow-left-24: Architecture](architecture.md) — The 4-layer, 13-table schema specification
- [:octicons-arrow-left-24: Entity Relationship Diagram](entity-relationship-diagram.md) — Visual schema reference
