---
date: 2026-07-22
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# PoC: compiling ClinicalTrials.gov eligibility prose into a gate-verified Circe cohort, with refusal as a first-class output

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/poc-compiling-clinicaltrials-gov-eligibility-prose-into-a-gate-verified-circe-cohort-with-refusal-as-a-first-class-output/25695)
**Matched keywords**: OHDSI

I built a proof of concept for the eligibility-to-cohort authoring step: an LLM reads the verbatim registered criteria of a trial at build time and emits a standard Circe cohort definition, committed only after passing four automated gates. The runtime is unmodified OHDSI tooling (CirceR, SqlRender, DatabaseConnector), no model in the execution path. Where the prose admits no single determinate encoding over the CDM, the criterion compiles to AMBIGUOUS with a rationale, never to a guess.
NCT0366

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/poc-compiling-clinicaltrials-gov-eligibility-prose-into-a-gate-verified-circe-cohort-with-refusal-as-a-first-class-output/25695){.md-button}
