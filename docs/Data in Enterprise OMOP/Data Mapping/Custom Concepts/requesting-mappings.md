---
hide:
  - footer
title: Requesting Mappings
---

# Requesting Mappings

If you've found source data in Epic or CDW that isn't mapped to an OMOP concept, you can request a mapping. The Enterprise OMOP team triages requests and routes them into the vocabulary build pipeline.

!!! tip "Check coverage first"
    Before submitting a request, check the [Vocabulary Mapping Coverage](../Vocabulary%20Mapping%20Coverage/index.md) dashboard. Your source values may already be mapped in the latest release.

## What to Include

A good mapping request helps the team prioritize and act quickly. Include:

| Field | Example |
|-------|---------|
| **Source system** | Epic Flowsheets, CDW Labs, Epic Orders |
| **Source field / table** | `flowsheet_name`, `order_type` |
| **Example values** | "BRADEN SCORE", "FALL RISK ASSESSMENT" |
| **Clinical context** | Why these values matter for your research question |
| **Approximate volume** | ~50K rows, affects 12K patients |

!!! info "You don't need to know OMOP to submit"
    You don't need to identify target concepts or vocabulary codes. The mapping team handles the OMOP side — just describe the source data and why it matters.

## How to Submit

<div class="grid cards" markdown>

-   :material-jira:{ .lg .middle } **Jira Feature Request**

    ---

    Open a feature request in the OMOP Enterprise Jira project. Use the "Vocabulary Mapping" request type and include the details above.

-   :material-microsoft-teams:{ .lg .middle } **Teams Channel**

    ---

    Post in the **OMOP Enterprise** Teams channel. Tag the vocabulary team and include example source values. Good for quick questions before filing a formal request.

</div>

## What Happens Next

1. **Triage** — The team reviews your request and confirms the source data is identifiable in the pipeline
2. **Prioritization** — Requests are prioritized based on clinical impact, researcher demand, and mapping complexity
3. **CVB pipeline** — Accepted mappings are built through the Custom Vocabulary Builder, an automated pipeline that produces OMOP-compatible vocabulary deltas
4. **Next release** — New mappings ship with the next Enterprise OMOP product release and appear in the Vocabulary Mapping Coverage dashboard
