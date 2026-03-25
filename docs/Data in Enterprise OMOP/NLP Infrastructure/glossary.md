---
hide:
  - footer
title: "Glossary"
---

# NLP Terminology Glossary

!!! danger "DRAFT — Internal Review Only · Not for distribution in wide release"

    This document is a **working draft** intended for internal review by the Enterprise OMOP implementation team and our growing network of collaborators. It has not been finalized, peer-reviewed, or approved for external distribution.

    See [releases](../../Data%20in%20Enterprise%20OMOP/Releases/) and [roadmap](../../Project%20and%20Product%20Management/Product%20Roadmap/) for details.

!!! tip "Context"

    See [:octicons-arrow-left-24: Notes and NLP Design](./) for the problem overview and [:octicons-arrow-left-24: Architecture](architecture.md) for the full schema specification.

## Terms

| Term | Definition | Source |
|------|-----------|--------|
| **Assertion** | A contextual attribute of an extracted entity span — negation, experiencer, temporality, certainty. The standard annotation task in clinical NLP. | i2b2 2010, n2c2 |
| **Context** | The algorithm and process for detecting assertions. Named after the ConText algorithm. | Harkema et al. (2009) |
| **Modifier** | Implementation-level term for assertion attributes in NLP frameworks. | medspaCy, cTAKES, OMOP |
| **Span** | A contiguous segment of text identified by an NLP system, with character-level offsets. | OHDSI NLP WG |
| **Entity** | A clinically meaningful concept identified within a span (e.g., a condition, drug, measurement). | General NLP |
| **Negation** | An assertion that a clinical finding is absent. e.g., "denies chest pain" — chest pain is negated. | i2b2 assertion categories |
| **Experiencer** | An assertion about who has the finding — patient or someone else (e.g., family member). | ConText (Harkema et al.) |
| **Temporality** | An assertion about when a finding occurred — current, historical, or hypothetical. | ConText (Harkema et al.) |
| **Certainty** | An assertion about the confidence level — definite, possible, conditional, hypothetical. | i2b2 assertion categories |
| **Source Provenance** | The `source` / `source_uri` / `source_version` triple that records where an NLP system, pipeline, or component originates — platform (e.g., GitHub, PyPI, HuggingFace), addressable location, and machine-verifiable version (git SHA, package version, Docker tag). | Emory Enterprise OMOP |
| **`_DERIVED` table** | An OMOP CDM table suffixed with `_DERIVED` that contains NLP-extracted data, structurally separated from discrete EHR data. | Emory Enterprise OMOP |

---

## References

- Uzuner Ö, South BR, Shen S, DuVall SL. 2010 i2b2/VA challenge on concepts, assertions, and relations in clinical text. *Journal of the American Medical Informatics Association*. 2011;18(5):552–556. [PMC3168320](https://pmc.ncbi.nlm.nih.gov/articles/PMC3168320/)
- Harkema H, Dowling JN, Thornblade T, Chapman WW. ConText: an algorithm for determining negation, experiencer, and temporal status from clinical reports. *Journal of Biomedical Informatics*. 2009;42(5):839–851. [PMC2757457](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757457/)
- n2c2 NLP Clinical Challenges — successor to i2b2, continuing shared tasks on clinical NLP including context classification. [n2c2.dbmi.hms.harvard.edu](https://n2c2.dbmi.hms.harvard.edu/)
- OHDSI NLP Working Group — community-driven standards for NLP output representation in the OMOP CDM. [ohdsi.org](https://www.ohdsi.org/)

---

## Related Pages

- [:octicons-arrow-left-24: Notes and NLP Design](./) — The problem and why NLP metadata matters
- [:octicons-arrow-left-24: Architecture](architecture.md) — The 4-layer schema specification
- [:octicons-arrow-left-24: Entity Relationship Diagram](entity-relationship-diagram.md) — Visual schema reference
