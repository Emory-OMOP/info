---
hide:
  - footer
title: Releases
---

# Releases

Emory Enterprise OMOP uses [Semantic Versioning 2.0](https://semver.org/) — **MAJOR.MINOR.PATCH**.

- **Major** — structural changes to the data model, identity resolution, or ETL architecture
- **Minor** — new tables, concept mappings, or pipeline features
- **Patch** — bug fixes and corrections that don't change the data model

## Current Release

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **v1.1.0** — March 2026

    ---

    NLP infrastructure, Brain Health note pilot (2,488 notes, 9,411 spans, 850 patients), medspaCy pipeline with assertion detection, context snippets, and annotation review framework.

    [:octicons-arrow-right-24: Release notes](v1.x/v1.1.0/index.md){ .md-button .md-button--primary }

</div>

## Previous Releases

<div class="grid cards" markdown>

-   :material-package-variant:{ .lg .middle } **v1.x** — 2026

    ---

    Major release series — patient identity stabilization, NLP infrastructure, Brain Health note processing, and expanded data coverage.

    [:octicons-arrow-right-24: v1.x release notes](v1.x/index.md){ .md-button }

-   :material-package-variant:{ .lg .middle } **v0.2.x** — April–August 2025

    ---

    Initial community release series — Epic ETL integration, CDM v5.4 migration, DBT test suite, provider deduplication, vocabulary updates, and QA automation across 5 monthly releases.

    [:octicons-arrow-right-24: v0.2.x release notes](v0.2.x/index.md){ .md-button }

</div>

## Source Repositories

<div class="grid cards" markdown>

-   :octicons-repo-16:{ .lg .middle } **Development**

    ---

    Primary development repository with all dbt projects, stored procedures, and CI/CD workflows.

    [:octicons-arrow-right-24: emory_omop_enterprise](https://github.com/EmoryDataSolutions/emory_omop_enterprise){ .md-button }

-   :octicons-repo-16:{ .lg .middle } **Documentation**

    ---

    This documentation site — MkDocs Material, hosted on GitHub Pages.

    [:octicons-arrow-right-24: emory-omop](https://github.com/Emory-OMOP/emory-omop){ .md-button }

</div>
