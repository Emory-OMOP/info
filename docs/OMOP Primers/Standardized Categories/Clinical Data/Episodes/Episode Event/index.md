---
hide:
  - footer
title: Episode Event
---

# Episode Event

**Epic equivalent**: No direct equivalent — this is a cross-domain linking table

The `episode_event` table connects **individual clinical events** (a diagnosis, procedure, drug, measurement) to a broader **episode** defined in the `episode` table. It lets you reconstruct the full timeline and components of multi-domain clinical bundles like prenatal care, chemotherapy regimens, or stroke episodes.

Each row is a single link between an event and an episode.

## Field Reference

??? example "Field reference (click to expand)"

    | OMOP Field | What It Captures |
    |---|---|
    | `episode_event_id` | Unique identifier for this link |
    | `episode_id` | The parent episode |
    | `event_id` | The linked event (e.g., `condition_occurrence_id`, `drug_exposure_id`) |
    | `event_field_concept_id` | Tells you which table the `event_id` comes from |

    **Common `event_field_concept_id` values:**

    | Concept ID | Source Table |
    |---|---|
    | `1147127` | `condition_occurrence` |
    | `1147094` | `drug_exposure` |
    | `1147126` | `device_exposure` |

## What to Watch For

!!! warning "Common pitfalls"

    **Only useful if `episode` is populated**
    :   This table is meaningless without episode context.

    **Must resolve the event domain**
    :   `event_field_concept_id` tells you *which table* to join. You can't query events without knowing the domain.

    **Multiple events per episode**
    :   Expect many rows per episode — that's the point. Each linked fact gets its own row.

## Research Patterns

| Question | Tables Involved |
|---|---|
| Diagnoses and procedures in pregnancy episodes | `episode` (pregnancy) + `episode_event` + `condition_occurrence` + `procedure_occurrence` |
| Lab results contributing to cancer staging | `episode_event` linking `measurement` to `episode` (cancer) |
| Drug timing within chemotherapy cycles | `episode_event` + `drug_exposure` by episode ID |
| Care burden during stroke episodes | `episode_event` count of linked events per episode |
| Visit distribution within complex surgical episodes | `episode_event` + `visit_occurrence` |
