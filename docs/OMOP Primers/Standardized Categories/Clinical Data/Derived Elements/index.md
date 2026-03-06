---
hide:
  - footer
title: Derived Elements
---

# Derived Elements

Derived tables are **computed from raw clinical tables** — they aggregate individual events into clinically meaningful periods. You don't record data into these tables directly; the ETL pipeline builds them.

Think of it this way: `condition_occurrence` has one row every time a diabetes diagnosis is recorded. `condition_era` collapses those into a single continuous period of "this patient had diabetes from X to Y."

<div class="grid cards" markdown>

-   :material-chart-timeline:{ .lg .middle } **Condition Era**

    ---

    Continuous periods of a condition, aggregated from `condition_occurrence` using configurable gap logic (default: 30-day persistence window).

    [:octicons-arrow-right-24: Condition Era](../Conditions/Derived%20-%20Condition%20Era/index.md){ .md-button }

-   :material-chart-timeline-variant:{ .lg .middle } **Drug Era**

    ---

    Continuous medication exposure periods, aggregated from `drug_exposure` at the ingredient level.

    [:octicons-arrow-right-24: Drug Era](../Drugs/Derived/Drug%20Era/index.md){ .md-button }

-   :material-pill-multiple:{ .lg .middle } **Dose Era**

    ---

    Periods of consistent daily dose for a drug, derived from `drug_exposure` with dose normalization.

    [:octicons-arrow-right-24: Dose Era](../Drugs/Derived/Dose%20Era/index.md){ .md-button }

-   :material-calendar-range:{ .lg .middle } **Episode / Episode Event**

    ---

    Higher-level clinical constructs (treatment regimens, pregnancy episodes, disease courses) explicitly curated during ETL or by researchers.

    [:octicons-arrow-right-24: Episode](../Episodes/Episode/index.md){ .md-button } [:octicons-arrow-right-24: Episode Event](../Episodes/Episode%20Event/index.md){ .md-button }

</div>

!!! info "Gap logic matters"
    Era tables use a persistence window to decide when gaps between events create a new era vs. extend an existing one. The default is typically 30 days, but this is configurable in the ETL. Always verify the gap logic used at your site before interpreting era durations.
