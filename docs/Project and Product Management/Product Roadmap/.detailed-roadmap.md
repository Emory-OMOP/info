---
hide:
  - footer
title: Detailed Product Roadmap
---

# Detailed Product Roadmap

*Last updated: March 13, 2026* | *v1.0.0 shipped March 2026*

**Data freshness**: Epic refreshes quarterly. CDW last refreshed March 2025 (no longer receiving updates).

<div class="rm-legend">
  <span class="rm-legend__item"><span class="rm-chip rm-chip--shipped">SHIPPED</span> Production ready</span>
  <span class="rm-legend__item"><span class="rm-chip rm-chip--active">ACTIVE</span> In development</span>
  <span class="rm-legend__item"><span class="rm-chip rm-chip--high">HIGH PRIORITY</span> Top priority</span>
  <span class="rm-legend__item"><span class="rm-chip rm-chip--planned">PLANNED</span> On roadmap</span>
</div>

---

<!-- ════════════════════════════════════════════════ -->
<!-- SHIPPED                                          -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-timeline">

<div class="rm-quarter">
  <div class="rm-quarter__badge">v1.0</div>
  <h2 class="rm-quarter__title">Shipped — v1.0.0</h2>
  <p class="rm-quarter__subtitle">March 2026 &middot; 271 commits &middot; 3 contributors &middot; CDM v5.4 &middot; Vocabulary v5.0</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">Patient Identity Stabilization</h3>
    </div>
    <p class="rm-card__desc">Stable <code>person_id</code> across data loads. Medallion architecture (Bronze/Silver/Clustering/Gold) with graph-based clustering. Near-100% Epic PAT_ID coverage (742K/742K matched).</p>
    <span class="rm-tag">80+ commits</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">HIPAA De-identification</h3>
    </div>
    <p class="rm-card__desc">Production de-identification pipeline with <code>cohort_person_filter</code> and <code>deident_driver</code> for safe data exports.</p>
    <span class="rm-tag">35 commits</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">Drug &amp; Condition Eras</h3>
    </div>
    <p class="rm-card__desc">Longitudinal exposure and disease duration analysis via DRUG_ERA and CONDITION_ERA tables.</p>
    <span class="rm-tag">Core Clinical</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">Cross-Project Subsampling</h3>
    </div>
    <p class="rm-card__desc">40-patient reproducible sample with alias_prefix isolation. Supports multi-project dbt builds.</p>
    <span class="rm-tag">20 commits</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">CI/CD &amp; Test Framework</h3>
    </div>
    <p class="rm-card__desc">Automated dbt test pipeline, data quality checks, and deployment automation.</p>
    <span class="rm-tag">Infrastructure</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">OHDSI Agent MCP Servers</h3>
    </div>
    <p class="rm-card__desc">Three MCP servers in production: vocabulary search (7.4M+ concepts), CIRCE cohort compiler, and lineage sidecar. 82.1% tool-routing accuracy across 820 evaluation tasks.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">Custom Vocabulary Builder v0.3.0</h3>
    </div>
    <p class="rm-card__desc">Flowsheet mapping pipeline — 17,745 items mapped from unmappable pool. Clinical reasoning pass completed on review batches.</p>
    <span class="rm-tag">Vocabulary</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <h3 class="rm-card__title">Documentation Site &amp; DQD</h3>
    </div>
    <p class="rm-card__desc">Public documentation site, Data Quality Dashboard with completeness, conformance, and plausibility metrics. ARES integration live.</p>
    <span class="rm-tag">Community</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- Q2 2026                                          -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">Q2</div>
  <h2 class="rm-quarter__title">Q2 2026</h2>
  <p class="rm-quarter__subtitle">April &ndash; June &middot; Notes, NLP, Nursing, LLM Rollout</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--high">HIGH PRIORITY</span>
      <h3 class="rm-card__title">Clinical Notes MVP</h3>
    </div>
    <p class="rm-card__desc">Full note text access with governance framework. IRB-aligned access controls, note type classification, and researcher-facing query interface.</p>
    <span class="rm-tag">NOTE / NOTE_NLP</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--high">HIGH PRIORITY</span>
      <h3 class="rm-card__title">NLP Pipeline Alpha</h3>
    </div>
    <p class="rm-card__desc">Entity extraction from clinical notes — conditions, medications, procedures. Foundation for downstream NLP products and LLM-assisted annotation.</p>
    <span class="rm-tag">NOTE_NLP</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--high">HIGH PRIORITY</span>
      <h3 class="rm-card__title">LLM Rollout — Tools &amp; Approvals</h3>
    </div>
    <p class="rm-card__desc">Institutional LLM tools inventory, approval process design, and governance framework for AI-assisted clinical data workflows.</p>
    <span class="rm-tag">AI Governance</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--high">HIGH PRIORITY</span>
      <h3 class="rm-card__title">School of Nursing Support</h3>
    </div>
    <p class="rm-card__desc">SON team onboarding, nursing cohort definitions, subsampled nursing data, and dedicated documentation. Standing up research support for nursing faculty.</p>
    <span class="rm-tag">Research Teams</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--active">ACTIVE</span>
      <h3 class="rm-card__title">CVB Flowsheet Expansion</h3>
    </div>
    <p class="rm-card__desc">~38K remaining unmappable flowsheet items routing through CVB pipeline for expanded measurement coverage.</p>
    <span class="rm-tag">Vocabulary</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--active">ACTIVE</span>
      <h3 class="rm-card__title">OMOP Sidecar Structural Mapping</h3>
    </div>
    <p class="rm-card__desc">Lineage-based integration path recommendations for new Clarity tables based on patterns from already-integrated tables.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- Q3 2026                                          -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">Q3</div>
  <h2 class="rm-quarter__title">Q3 2026</h2>
  <p class="rm-quarter__subtitle">July &ndash; September &middot; NLP Production, LLM Deployment, Operations</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">NLP Pipeline Beta</h3>
    </div>
    <p class="rm-card__desc">Production entity extraction with quality metrics. Researcher-queryable NLP outputs in NOTE_NLP table.</p>
    <span class="rm-tag">NOTE_NLP</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">LLM Tool Deployment</h3>
    </div>
    <p class="rm-card__desc">Institutional rollout of approved LLM-assisted data tools. Audit trail integration and monitoring dashboards.</p>
    <span class="rm-tag">AI Governance</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">OHDSI Agent GA</h3>
    </div>
    <p class="rm-card__desc">General availability release of the MCP-native OHDSI agent with production-grade tool routing and evaluation framework.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">SDOH Enhancement</h3>
    </div>
    <p class="rm-card__desc">Enhanced social determinants of health data — expanded structured social history and survey integration.</p>
    <span class="rm-tag">OBSERVATION</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Provider Specialty Mapping</h3>
    </div>
    <p class="rm-card__desc">Improved provider specialty concept mapping for more accurate attribution and network analysis.</p>
    <span class="rm-tag">PROVIDER</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Operations Extension Design</h3>
    </div>
    <p class="rm-card__desc">FHIR-first design for OMOP operations tables — Schedule, Slot, Appointment, Claim, Coverage. Prioritizing bidirectional interoperability.</p>
    <span class="rm-tag">Extension</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- Q4 2026                                          -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">Q4</div>
  <h2 class="rm-quarter__title">Q4 2026</h2>
  <p class="rm-quarter__subtitle">October &ndash; December &middot; Governance, Operations, Health Economics</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">LLM Governance Framework</h3>
    </div>
    <p class="rm-card__desc">Audit trails, approval workflows, and compliance documentation for institutional LLM tool usage in clinical data contexts.</p>
    <span class="rm-tag">AI Governance</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Operations Extension Alpha</h3>
    </div>
    <p class="rm-card__desc">Initial implementation of OMOP operations tables. Health economics data (Claim, Coverage) as first deliverable.</p>
    <span class="rm-tag">Extension</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Survey &amp; Questionnaire Integration</h3>
    </div>
    <p class="rm-card__desc">Structured survey response capture and mapping for patient-reported outcomes and research instruments.</p>
    <span class="rm-tag">OBSERVATION</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- 2027 HORIZON                                     -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">2027</div>
  <h2 class="rm-quarter__title">2027 Horizon</h2>
  <p class="rm-quarter__subtitle">Long-range initiatives</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Imaging &amp; DICOM Linkage</h3>
    </div>
    <p class="rm-card__desc">Radiology report integration and DICOM metadata linkage to OMOP clinical events.</p>
    <span class="rm-tag">Extension</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Waveform Data</h3>
    </div>
    <p class="rm-card__desc">ECG waveforms and bedside monitor data integration for high-frequency clinical signal research.</p>
    <span class="rm-tag">Extension</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Advanced NLP Products</h3>
    </div>
    <p class="rm-card__desc">LLM-assisted clinical note summarization, phenotyping from unstructured text, and multi-modal data integration.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Operations Extension GA</h3>
    </div>
    <p class="rm-card__desc">Full operations table suite — scheduling, appointments, claims, coverage — with FHIR bidirectional interoperability.</p>
    <span class="rm-tag">Extension</span>
  </div>
</div>

</div><!-- /rm-timeline -->

---

## Data Product Maturity

<div class="rm-maturity" markdown>

| Domain | Table | Epic | CDW | Status |
|--------|-------|:----:|:---:|--------|
| Demographics | PERSON | :white_check_mark: GA | :white_check_mark: GA | Stable person_id shipped |
| Encounters | VISIT_OCCURRENCE | :white_check_mark: GA | :large_orange_diamond: Beta | ~12M unmapped visits/yr |
| Visit Detail | VISIT_DETAIL | :large_orange_diamond: Beta | :black_circle: Planned | ICU/OR segments |
| Conditions | CONDITION_OCCURRENCE | :white_check_mark: GA | :white_check_mark: GA | |
| Condition Eras | CONDITION_ERA | :white_check_mark: GA | :white_check_mark: GA | Shipped v1.0.0 |
| Medications | DRUG_EXPOSURE | :white_check_mark: GA | :large_orange_diamond: Beta | |
| Drug Eras | DRUG_ERA | :white_check_mark: GA | :white_check_mark: GA | Shipped v1.0.0 |
| Labs | MEASUREMENT | :white_check_mark: GA | :large_orange_diamond: Beta | LOINC mapped |
| Vitals/Flowsheets | MEASUREMENT | :large_orange_diamond: Beta | :black_circle: Planned | CVB expanding coverage |
| Procedures | PROCEDURE_OCCURRENCE | :white_check_mark: GA | :white_check_mark: GA | |
| Providers | PROVIDER | :white_check_mark: GA | :large_orange_diamond: Beta | Specialty mapping improving |
| Social Hx | OBSERVATION | :large_orange_diamond: Beta | :small_orange_diamond: Preview | Smoking, alcohol |
| Notes | NOTE | :small_orange_diamond: Preview | :black_circle: Planned | High priority Q2 2026 |
| NLP | NOTE_NLP | :black_circle: Planned | :black_circle: Planned | High priority Q2-Q3 2026 |
| Imaging | — | :black_circle: Planned | :black_circle: Planned | 2027 horizon |
| Waveforms | — | :black_circle: Planned | :black_circle: Planned | 2027 horizon |

</div>

---

<div class="grid cards" markdown>

-   :material-arrow-left:{ .lg .middle } **Back to Roadmap Overview**

    ---

    Lucidchart interactive diagram and GitHub project board links.

    [:octicons-arrow-right-24: Roadmap Overview](./)

-   :material-github:{ .lg .middle } **GitHub Project Board**

    ---

    Real-time status on individual work items (core team access).

    [:octicons-arrow-right-24: Open Project Board](https://github.com/orgs/EmoryDataSolutions/projects)

</div>
