---
hide:
  - footer
title: Detailed Product Roadmap
---

# Release Roadmap

*Last updated: March 2026* · *Monthly harvey ball updates*

**Data freshness**: Epic data refreshes quarterly. CDW last refreshed March 2025 (no longer receiving updates).

<div class="rm-legend">
  <span class="rm-legend__item"><span class="rm-chip rm-chip--shipped">SHIPPED</span> Production ready</span>
  <span class="rm-legend__item"><span class="rm-chip rm-chip--active">ACTIVE</span> In development</span>
  <span class="rm-legend__item"><span class="rm-chip rm-chip--planned">PLANNED</span> On roadmap</span>
</div>

<div class="hb-legend">
  <span class="hb-legend__item"><span class="hb-ball hb-ball--100"></span> Complete</span>
  <span class="hb-legend__item"><span class="hb-ball hb-ball--75"></span> Substantial</span>
  <span class="hb-legend__item"><span class="hb-ball hb-ball--50"></span> Partial</span>
  <span class="hb-legend__item"><span class="hb-ball hb-ball--25"></span> Early</span>
  <span class="hb-legend__item"><span class="hb-ball hb-ball--0"></span> Planned</span>
</div>

<div class="rm-legend" style="margin-top: .25rem;">
  <span class="rm-legend__item"><span class="rm-priority">H</span> High Priority &nbsp; <span class="rm-priority">M</span> Medium &nbsp; <span class="rm-priority">L</span> Low</span>
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
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">Patient Identity Stabilization</h3>
    </div>
    <p class="rm-card__desc">Foundational cross-source identity management across legacy Cerner and modern Epic EHR systems. Stable <code>person_id</code> across data loads via Medallion architecture (Bronze/Silver/Clustering/Gold) with graph-based clustering. Near-100% Epic PAT_ID coverage (742K/742K matched).</p>
    <span class="rm-tag">80+ commits</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">HIPAA De-identification</h3>
    </div>
    <p class="rm-card__desc">Production de-identification pipeline with <code>cohort_person_filter</code> and <code>deident_driver</code> for safe data exports.</p>
    <span class="rm-tag">35 commits</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">Drug &amp; Condition Eras</h3>
    </div>
    <p class="rm-card__desc">Longitudinal exposure and disease duration analysis via DRUG_ERA and CONDITION_ERA tables.</p>
    <span class="rm-tag">Core Clinical</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">Cross-Project Subsampling</h3>
    </div>
    <p class="rm-card__desc">40-patient reproducible sample with alias_prefix isolation. Supports multi-project dbt builds.</p>
    <span class="rm-tag">20 commits</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">CI/CD &amp; Test Framework</h3>
    </div>
    <p class="rm-card__desc">Automated dbt test pipeline, data quality checks, and deployment automation.</p>
    <span class="rm-tag">Infrastructure</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">OHDSI Agent MCP Servers</h3>
    </div>
    <p class="rm-card__desc">Three MCP servers in production: vocabulary search (7.4M+ concepts), CIRCE cohort compiler, and lineage sidecar. 82.1% tool-routing accuracy across 820 evaluation tasks.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">Custom Vocabulary Builder v0.3.0</h3>
    </div>
    <p class="rm-card__desc">Flowsheet mapping pipeline — 17,745 items mapped from unmappable pool. Clinical reasoning pass completed on review batches.</p>
    <span class="rm-tag">Vocabulary</span>
  </div>

  <div class="rm-card">
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--shipped">SHIPPED</span>
      <span class="hb-ball hb-ball--inline hb-ball--100"></span>
      <h3 class="rm-card__title">Documentation Site &amp; DQD</h3>
    </div>
    <p class="rm-card__desc">Public documentation site, Data Quality Dashboard with completeness, conformance, and plausibility metrics. ARES integration live.</p>
    <span class="rm-tag">Community</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- CQ1 2026 — IN PROGRESS                           -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">CQ1</div>
  <h2 class="rm-quarter__title">CQ1 2026 (Calendar Quarter 1)</h2>
  <p class="rm-quarter__subtitle">January &ndash; March &middot; Brain Health, FALCON-Bladder, CIRCLE, SON Prototype</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--active">ACTIVE</span>
      <span class="hb-ball hb-ball--inline hb-ball--75"></span>
      <h3 class="rm-card__title">Brain Health v1.0</h3>
    </div>
    <p class="rm-card__desc">First project-specific OMOP deployment for the Personalized Brain Health Initiative (Goizueta ADRC). BrainHealthEnterprise dbt models and subsample infrastructure. Serves 34 researchers across 12 departments (SOM, SON, RSPH).</p>
    <span class="rm-tag">Brain Health</span>
    <span class="rm-tag">~Mar 20–21</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--active">ACTIVE</span>
      <span class="hb-ball hb-ball--inline hb-ball--25"></span>
      <h3 class="rm-card__title">FALCON-Bladder Data Readiness</h3>
    </div>
    <p class="rm-card__desc">Data readiness assessment for FALCON-Bladder restart. Execute 3 SQL scripts (general concepts, genomic concepts, episode concepts) against Emory OMOP, generate CSV outputs, submit to study coordinators. First monthly meeting March 24.</p>
    <span class="rm-tag">OHDSI Oncology</span>
    <span class="rm-tag">Due Apr 15</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--active">ACTIVE</span>
      <span class="hb-ball hb-ball--inline hb-ball--25"></span>
      <h3 class="rm-card__title">ARPA-H CIRCLE AP1 Solution Summary</h3>
    </div>
    <p class="rm-card__desc">AP1 = single-award data platform role for ARPA-H critical illness digital twin program. Solution summary due March 30; full proposal May 28 if encouraged. Consumes the OMOP-on-FHIR Streaming MVP. ~$2M/3yr.</p>
    <span class="rm-tag">Grants</span>
    <span class="rm-tag">Due Mar 30</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--active">ACTIVE</span>
      <span class="hb-ball hb-ball--inline hb-ball--50"></span>
      <h3 class="rm-card__title">School of Nursing — Prototype</h3>
    </div>
    <p class="rm-card__desc">1M patient subsample created for SON experimentation against MVP — milestone achieved. Nursing cohort definitions in development.</p>
    <span class="rm-tag">Research Teams</span>
    <span class="rm-tag">Milestone ✓</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- CQ2 2026                                         -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">CQ2</div>
  <h2 class="rm-quarter__title">CQ2 2026 (Calendar Quarter 2)</h2>
  <p class="rm-quarter__subtitle">April &ndash; June &middot; v1.1 Notes &amp; NLP, CASSIDY, SON Export, Winship R01 Decision</p>
</div>

<div class="rm-items">
  <div class="rm-card rm-card--full">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">v1.1 — Notes, NLP &amp; Governance Infrastructure</h3>
    </div>
    <p class="rm-card__desc">Clinical notes access with governance, NLP extraction pipeline, and shared API platform enabling standard LLM/NLP pipelines across the institution. Brain Health is the first consumer. Includes CDW notes archival from Cerner sunsetting (BMI intermediate storage). BMI HPC cluster POC informs production requirements.</p>
    <div class="rm-card__features">
      <span class="hb-feature">Clinical Notes MVP</span>
      <span class="hb-feature">NLP Extraction Pipeline</span>
      <span class="hb-feature">Community Shared Governance Infrastructure</span>
      <span class="hb-feature">API Platform for LLM/NLP Pipelines</span>
    </div>
    <span class="rm-tag">NOTE / NOTE_NLP</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">CASSIDY Phenotype</h3>
    </div>
    <p class="rm-card__desc">Diabetes surveillance computable phenotype for the CASSIDY Network (CHOA + Emory). Multi-stage pipeline: identification, classification, complication staging (§4.1–4.4), multi-year index 2018–2025.</p>
    <span class="rm-tag">Pediatrics</span>
    <span class="rm-tag">Beginning CQ2</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">School of Nursing — Export</h3>
    </div>
    <p class="rm-card__desc">Deliver data export to School of Nursing for independent research use. Prototype and 1M patient subsample already created (CQ1 milestone).</p>
    <span class="rm-tag">Research Teams</span>
    <span class="rm-tag">Early CQ2</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">OMOP-on-FHIR Streaming MVP</h3>
    </div>
    <p class="rm-card__desc">Prototype to experimentally validate OMOP as a real-time streaming storage target. FHIR-to-OMOP architecture (Kafka + DuckDB vocabulary resolution + hot/cold OMOP stores). Feeds ARPA-H CIRCLE AP1 if funded.</p>
    <span class="rm-tag">Streaming</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">CVB Flowsheet Expansion</h3>
    </div>
    <p class="rm-card__desc">~38K remaining unmappable flowsheet items routing through CVB pipeline for expanded measurement coverage.</p>
    <span class="rm-tag">Vocabulary</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Winship Oncology R01</h3>
    </div>
    <p class="rm-card__desc">Clinical trial matching LLM incorporating OMOP. R01 submitted — decision expected May 2026.</p>
    <span class="rm-tag">Grants</span>
    <span class="rm-tag">Decision May '26</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════ -->
<!-- CH2 2026                                         -->
<!-- ════════════════════════════════════════════════ -->

<div class="rm-quarter">
  <div class="rm-quarter__badge">CH2</div>
  <h2 class="rm-quarter__title">CH2 2026 (Calendar Half 2)</h2>
  <p class="rm-quarter__subtitle">July &ndash; December &middot; NLP Production, SDOH, OHDSI Agent GA</p>
</div>

<div class="rm-items">
  <div class="rm-card">
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">NLP Pipeline — Production</h3>
    </div>
    <p class="rm-card__desc">Production entity extraction with quality metrics. Researcher-queryable NLP outputs in NOTE_NLP table.</p>
    <span class="rm-tag">NOTE_NLP</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">OHDSI Agent GA</h3>
    </div>
    <p class="rm-card__desc">General availability release of the MCP-native OHDSI agent with production-grade tool routing and evaluation framework.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">SDOH &amp; Geocoding Enhancement</h3>
    </div>
    <p class="rm-card__desc">Expanded social determinants of health data. GaCTSA geocoding of patient and care site addresses planned for contribution back to Enterprise OMOP.</p>
    <span class="rm-tag">OBSERVATION</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">L</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Provider Specialty Mapping</h3>
    </div>
    <p class="rm-card__desc">Improved provider specialty concept mapping for more accurate attribution and network analysis.</p>
    <span class="rm-tag">PROVIDER</span>
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
    <span class="rm-priority">H</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">OMOP on UDP / Azure Cloud Transition</h3>
    </div>
    <p class="rm-card__desc">Migrate OMOP into the Unified Data Platform on Azure. Enables ATLAS-based cohort discovery at speed, de-identified research data for cross-institutional collaboration.</p>
    <span class="rm-tag">Infrastructure</span>
    <span class="rm-tag">CQ1 2027</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">M</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Imaging &amp; DICOM Linkage</h3>
    </div>
    <p class="rm-card__desc">Radiology report integration and DICOM metadata linkage to OMOP clinical events. Gates Foundation grant submitted.</p>
    <span class="rm-tag">Extension</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">L</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Waveform Data</h3>
    </div>
    <p class="rm-card__desc">ECG waveforms and bedside monitor data integration for high-frequency clinical signal research.</p>
    <span class="rm-tag">Extension</span>
  </div>

  <div class="rm-card">
    <span class="rm-priority">L</span>
    <div class="rm-card__header">
      <span class="rm-chip rm-chip--planned">PLANNED</span>
      <h3 class="rm-card__title">Advanced NLP Products</h3>
    </div>
    <p class="rm-card__desc">LLM-assisted clinical note summarization, phenotyping from unstructured text, and multi-modal data integration.</p>
    <span class="rm-tag">AI Tooling</span>
  </div>
</div>

</div><!-- /rm-timeline -->

---

## Data Product Maturity

<div class="rm-maturity">
<table>
  <thead>
    <tr>
      <th>Domain</th>
      <th>Table</th>
      <th style="text-align:center">CDW</th>
      <th style="text-align:center">Epic</th>
      <th style="text-align:center">Combined</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Demographics</td><td>PERSON</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>Stable person_id shipped</td></tr>
    <tr><td>Encounters</td><td>VISIT_OCCURRENCE</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>~12M unmapped visits/yr</td></tr>
    <tr><td>Visit Detail</td><td>VISIT_DETAIL</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>ICU/OR segments</td></tr>
    <tr><td>Conditions</td><td>CONDITION_OCCURRENCE</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td></td></tr>
    <tr><td>Condition Eras</td><td>CONDITION_ERA</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>Shipped v1.0.0</td></tr>
    <tr><td>Medications</td><td>DRUG_EXPOSURE</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td></td></tr>
    <tr><td>Drug Eras</td><td>DRUG_ERA</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>Shipped v1.0.0</td></tr>
    <tr><td>Labs</td><td>MEASUREMENT</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>LOINC mapped</td></tr>
    <tr><td>Vitals/Flowsheets</td><td>MEASUREMENT</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>CVB expanding (17K mapped, ~38K remaining)</td></tr>
    <tr><td>Procedures</td><td>PROCEDURE_OCCURRENCE</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td></td></tr>
    <tr><td>Providers</td><td>PROVIDER</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td>Specialty mapping improving</td></tr>
    <tr><td>Social Hx</td><td>OBSERVATION</td><td style="text-align:center"><span class="hb-ball hb-ball--75"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--75"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--75"></span></td><td>Smoking, alcohol; SDOH expansion planned</td></tr>
    <tr><td>Notes</td><td>NOTE</td><td style="text-align:center"><span class="hb-ball hb-ball--25"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--25"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--25"></span></td><td>v1.1 target</td></tr>
    <tr><td>NLP</td><td>NOTE_NLP</td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td>CQ2 2026</td></tr>
    <tr><td>Device</td><td>DEVICE_EXPOSURE</td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--100"></span></td><td></td></tr>
    <tr><td>Imaging</td><td>—</td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td>CQ4 2026</td></tr>
    <tr><td>Waveforms</td><td>—</td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td style="text-align:center"><span class="hb-ball hb-ball--0"></span></td><td>CQ4 2026</td></tr>
  </tbody>
</table>
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
