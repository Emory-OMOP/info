---
date: 2026-05-12
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Introducing the LLM mapping classificator

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/introducing-the-llm-mapping-classificator/25362)
**Matched keywords**: OHDSI

This tool classifies the OHDSI vocabulary mappings into uphil or, downhil, equal or incorrect.
The current work is focused on ICD10CM conditions mapping assesment, but it can be relatively easily adopted to the classification of other domains or vocabularies mappings, by changing the classification prompt
and the concept normalization prompt
So it can support the curation of mappings you have with a bit of fine tuning.
The overall idea, prerequisites and how to run are described in the readme.md

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/introducing-the-llm-mapping-classificator/25362){.md-button}
