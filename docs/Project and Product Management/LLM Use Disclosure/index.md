---
hide:
  - footer
title: LLM Use Disclosure
---

# LLM Use Disclosure

Transparency statement on the use of large language models in the Emory OMOP project.

!!! info "Last updated: March 2026"

## Current LLM usage

The Emory OMOP team uses **Claude Opus 4.6** (Anthropic) to support two categories of work:

- **Web design** — Layout, styling, and content drafting for this documentation site
- **Code development** — Software engineering assistance for pipeline code, dbt models, and tooling

## What is not involved

| Boundary | Detail |
|:---|:---|
| **No patient data** | No protected health information (PHI), de-identified data, or any patient-level records are ever provided to, processed by, or accessible to the LLM. |
| **No Emory infrastructure** | The LLM does not run on, connect to, or have access to any Emory-owned servers, networks, databases, or cloud environments. |
| **No on-premises models** | No LLM models are deployed on Emory infrastructure. There are no locally hosted models running on Emory equipment. |

## How the LLM is accessed

All LLM interaction occurs through **chat web interfaces** on Emory computers (e.g., Anthropic Claude, ChatGPT, Google Gemini). There is no programmatic integration between the LLM and any Emory system. The LLM operates as an external development aid — comparable to a reference tool — with no pathway to institutional data or infrastructure.

## Scope of AI-generated content

Content produced with LLM assistance includes:

- Documentation pages (including this one)
- Code suggestions, reviewed and committed by the developer
- Alignment analyses (e.g., TRIPOD-LLM and FUTURE-AI mappings)

All AI-assisted output is reviewed, edited, and approved by the development team before publication or deployment. LLMs may help draft commit messages, pull requests, and GitHub issues, but they are in no way able to submit them. Every change to the codebase is made by a human developer.

## Why disclose

The Emory OMOP team believes that transparency about AI tooling is a prerequisite for the trust we ask others to place in our data infrastructure. If we advocate for traceability and provenance in NLP pipelines, we should hold ourselves to the same standard in how we build them.
