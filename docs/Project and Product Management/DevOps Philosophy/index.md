---
hide:
  - footer
title: DevOps Philosophy
---

# DevOps Philosophy

Emory OMOP uses a hybrid framework designed for a small data engineering team shipping research infrastructure. It combines proven practices from several communities rather than adopting any single methodology wholesale.

## Why Not Scrum?

Traditional Scrum assumes cross-functional feature teams, predictable sprint capacity, and well-defined user stories. Data engineering work — ETL pipelines, identity resolution, vocabulary mapping, de-identification — doesn't fit these assumptions cleanly. Work is often exploratory, blocked by upstream data issues, and varies dramatically in scope.

We evaluated seven frameworks and adopted the best-fitting elements from each.

## The Hybrid Framework

<div class="grid cards" markdown>

-   :material-cog-sync-outline:{ .lg .middle } **DataOps**

    ---

    **Philosophy layer** — everything as code, automated quality gates, statistical process control. Borrowed from the [DataOps Manifesto](https://dataopsmanifesto.org/en/) and DataKitchen practices.

-   :material-package-variant-closed:{ .lg .middle } **Shape Up**

    ---

    **Cadence layer** — 6-week cycles with 2-week cooldowns. Borrowed from [Basecamp's Shape Up](https://basecamp.com/shapeup). Work is "bet on" at the start of a cycle, not groomed in a backlog indefinitely.

-   :material-chart-timeline-variant:{ .lg .middle } **Kanban**

    ---

    **Daily mechanics** — continuous flow with WIP limits. No sprints, no story points. Work moves through a 7-stage board: Inbox → Todo → Ready → In Progress → In Review → Validating → Done.

-   :material-database-cog:{ .lg .middle } **dbt Labs Practices**

    ---

    **Engineering layer** — analytics engineering workflows, modular SQL, test-driven development, documentation as code. Aligned with [dbt Labs' analytics engineering guide](https://www.getdbt.com/analytics-engineering/).

</div>

## How Work Flows

| Stage | What Happens |
|-------|-------------|
| **Inbox** | New requests land here — bug reports, feature ideas, research questions |
| **Todo** | Accepted work, scoped and ready to be picked up |
| **Ready** | Dependencies resolved, assignee can start immediately |
| **In Progress** | Actively being worked on |
| **In Review** | Code review, peer validation |
| **Validating** | Running against subsamples or production data to verify correctness |
| **Done** | Shipped and verified |

Work is prioritized using **hill charts** — each item is tracked as either "Figuring Out" (research/design phase) or "Making It Happen" (execution phase). This gives the team honest visibility into whether work is stuck in exploration or actively converging.

## Key Principles

- **Thin vertical slices** — deliver small, end-to-end increments rather than large horizontal layers. A single slice might add one new table mapping from source through ETL, tests, and documentation.
- **Bet, don't backlog** — at the start of each 6-week cycle, the team bets on a small number of high-value items. Work that isn't bet on stays in the shaping queue — it doesn't accumulate as groomed backlog debt.
- **Cooldown weeks** — the 2 weeks between cycles are for bug fixes, tooling improvements, documentation, and exploration. No new feature commitments.
- **Automated quality gates** — DBT tests, DQD checks, and subsample validation run automatically. Manual QA is reserved for judgment calls, not rote verification.

## Data Quality Infrastructure

Quality is built into the pipeline through a tiered testing approach:

| Tier | Description |
|------|-------------|
| **1. Unit Test Seeds** | 25 deterministic patients with known expected outputs |
| **2. Problem-Case Subsample** | High-churn patients selected for edge case coverage |
| **3. Disease-Group Subsamples** | Domain-specific cohorts (oncology, cardiology, etc.) |
| **4. Longitudinal Subsample** | 1-year archived snapshots for regression testing |

This is complemented by OHDSI community tools: [Achilles](https://ohdsi.github.io/Achilles/) for characterization, [DQD](https://emorydatasolutions.github.io/e_omop_dqd/) for automated quality checks, and [ARES](https://ohdsi-rstudio.emory.edu/ares/) for data source profiling.

## Detailed Documentation

!!! info "Core team and contributors only"
    The full framework source of truth, team workflow guide, and observability roadmap are maintained in the [`emory_omop_enterprise`](https://github.com/EmoryDataSolutions/emory_omop_enterprise/tree/main/docs/devops_philosophy) repository. Access is limited to core team members and approved contributors.

    Key documents available there:

    - **Framework Source of Truth** — authoritative reference for the hybrid framework, ceremony schedule, success metrics
    - **Team Workflow Guide** — practical how-to for working with the GitHub project board, creating issues, and navigating daily rhythms
    - **Observability Current State** — testing pyramid details, pipeline orchestration, and known gaps
    - **Observability Roadmap** — planned SPC monitoring, CI gates, and quality enhancements
