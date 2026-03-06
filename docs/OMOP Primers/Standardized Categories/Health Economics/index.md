---
hide:
  - footer
title: Health Economics
---

# Health Economics

Cost and insurance data in OMOP. These tables are heavily used in claims-derived OMOP databases but **sparse in EHR-derived instances like Emory's**. If your study requires detailed cost or payer data, check our [Known Issues](../../../Data%20in%20Enterprise%20OMOP/Data%20Quality/Known%20Issues/index.md) page for current coverage.

<div class="grid cards" markdown>

-   :material-currency-usd:{ .lg .middle } **Cost**

    ---

    Charges, allowed amounts, patient out-of-pocket, and payer payments linked to clinical events. Maps to billing and revenue cycle data.

    [:octicons-arrow-right-24: Cost](Cost/index.md){ .md-button }

-   :material-shield-account:{ .lg .middle } **Payer Plan Period**

    ---

    Spans of insurance coverage under specific plans and payers. Maps to registration and eligibility feeds. Enables continuous enrollment filters.

    [:octicons-arrow-right-24: Payer Plan Period](Payer%20Plan%20Period/index.md){ .md-button }

</div>

!!! warning "Limited at Emory"
    As a primarily EHR-derived OMOP instance, Emory's cost and payer data is limited. These tables become much richer when linked with claims data. See individual table pages for details on what's currently populated.
