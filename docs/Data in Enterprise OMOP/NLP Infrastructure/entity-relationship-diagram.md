---
hide:
  - footer
title: "Entity Relationship Diagram"
---

# Entity Relationship Diagram

!!! danger "DRAFT — Internal Review Only · Not for distribution in wide release"

    This document is a **working draft** intended for internal review by the Enterprise OMOP implementation team and our growing network of collaborators. It has not been finalized, peer-reviewed, or approved for external distribution.

    See [releases](../../Data%20in%20Enterprise%20OMOP/Releases/) and [roadmap](../../Project%20and%20Product%20Management/Product%20Roadmap/) for details.

The entity relationship diagram visualizes the full NLP infrastructure schema across all four layers — from pipeline registration through `_DERIVED` CDM tables. It is the companion reference to the [Architecture](architecture.md) specification.

<div class="mdx-features__card" style="max-width: 36rem; margin: 2rem 0; padding: 1.5rem;">
  <h3 style="margin-top: 0;">
    :material-sitemap-outline: View the ERD
  </h3>
  <p>Interactive diagram on Lucidchart — zoom, pan, and comment directly on the schema design.</p>
  <p>
    <a href="https://lucid.app/lucidchart/a9c6fc6b-d23a-468e-bd22-b12432669d80/edit?invitationId=inv_f4d0c2b8-72c2-47ea-ab54-d24f89ada336" target="_blank" rel="noopener" class="md-button md-button--primary">
      Open in Lucidchart
    </a>
  </p>
</div>

!!! info "Emory login required"

    The Lucidchart ERD requires an Emory account. Comments and suggestions are welcome directly on the diagram.

The ERD covers:

- **Layer 1 — Process Metadata**: `nlp_system`, `pipeline`, `Component`, `pipeline_component`, `nlp_execution`, `note_span_execution`
- **Layer 2 — NLP Output**: `note_span`, `note_span_concept`, `nlp_date`, `nlp_quantity`, `note_span_assertion`
- **Layer 3 — Intermediate Translation**: `note_nlp_modifier`
- **Layer 4 — `_DERIVED` Tables**: `measurement_DERIVED`, `condition_DERIVED`, `drug_DERIVED`, `procedure_DERIVED`, `observation_DERIVED`, `death_DERIVED`

---

See [:octicons-arrow-left-24: Notes and NLP Design](./) for the problem overview and [:octicons-arrow-left-24: Architecture](architecture.md) for the full schema specification.
