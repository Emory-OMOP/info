---
hide:
  - footer
title: Data Quality Design
---

# Data Quality Design

Our data quality process is heavily influenced by the [DataOps framework](https://dataopsmanifesto.org/en/), which combines software engineering and manufacturing best practices to treat all aspects of the pipeline — software, data, and subsamples used in tests — as part of a CI/CD process.

## What is DataOps?

DataOps is not simply "DevOps for data." It extends DevOps principles with manufacturing-inspired process control, treating the analytic pipeline as a production system where quality is built in, not bolted on.

![Manufacturing process control as a foundation for DataOps](../../../assets/images/manufacturing.png)

![DevOps lifecycle — one component of the broader DataOps approach](../../../assets/images/devops.png)

## DataOps Manifesto

The [DataOps Manifesto](https://dataopsmanifesto.org/en/) defines 18 principles. The following table summarizes each and how we apply them at Emory.

| # | Principle | Summary |
|---|-----------|---------|
| 1 | Continually satisfy your customer | Deliver valuable analytic insights early and continuously |
| 2 | Value working analytics | Measure performance by delivery of accurate, insightful analytics |
| 3 | Embrace change | Welcome evolving requirements to maintain competitive advantage |
| 4 | It's a team sport | Encourage diverse roles and skills within analytic teams |
| 5 | Daily interactions | Ensure daily collaboration among researchers, engineers, and operations |
| 6 | Self-organize | Allow teams to self-organize for optimal results |
| 7 | Reduce heroism | Build sustainable processes; minimize reliance on individual effort |
| 8 | Reflect | Regularly self-reflect to improve operational performance |
| 9 | Analytics is code | Version all aspects of the analytics process |
| 10 | Orchestrate | Coordinate data, tools, code, environments, and team efforts |
| 11 | Make it reproducible | Ensure results are reproducible by versioning everything |
| 12 | Disposable environments | Provide easy-to-create, isolated environments for experimentation |
| 13 | Simplicity | Focus on simplicity to enhance agility and efficiency |
| 14 | Analytics is manufacturing | Apply process-thinking to achieve continuous efficiencies |
| 15 | Quality is paramount | Build pipelines capable of automated anomaly and security detection |
| 16 | Monitor quality and performance | Continuously monitor performance, security, and quality measures |
| 17 | Reuse | Avoid repetition by reusing previous work |
| 18 | Improve cycle times | Minimize the time from customer need to analytic insight |

## Implementation Steps

???+ example "Step 1 — Add Data and Logic Tests"

    Inspired by **Statistical Process Control (SPC)** from manufacturing: data must stay within an acceptable statistical range. Tests validate data values at the inputs and outputs of each processing stage in the pipeline.

    - Tests that fail trigger a notification-and-fix feedback loop
    - Failed records are "quarantined" until resolved
    - The loop continues until the agreed-upon measure of success is met

??? example "Step 2 — Use Version Control"

    Version code, documentation, tests, and meeting notes — all aligned within the context of releases. Understanding all aspects of version changes up and down the stack is critical.

??? example "Step 3 — Branch and Merge"

    Apply branching and merging not just to code, but across the entirety of the infrastructure — including data models, tests, and documentation.

??? example "Step 4 — Use Multiple Environments"

    Implement "test kitchens" where individual developers can experiment in isolated environments without affecting production data or pipelines.

??? example "Step 5 — Reuse and Containerize"

    Package reusable components so that engineers and analysts can utilize them without touching the internals — set up the container locally and use as needed.

??? example "Step 6 — Parameterize Processing"

    Design pipelines with flexibility for different run-time circumstances:

    - Which version of raw data should be used?
    - Is this a production or testing run?
    - Should specific processing steps be included or skipped?

    Atomizing code into discrete steps supports this naturally — each step can be independently included or excluded.

??? example "Step 7 — Work Without Fear"

    When tests, version control, and isolated environments are in place, team members can experiment and iterate without risking production data.

## Related Pages

- [:octicons-arrow-right-24: Data Quality Results](../Data%20Quality%20Results/index.md) — OHDSI DQD summary and failure analysis
- [:octicons-arrow-right-24: DBT Pipeline Tests](../DBT%20Tests/index.md) — column-level test definitions for every table
- [:octicons-arrow-right-24: Known Issues](../Known%20Issues/index.md) — table-by-table mapping gaps and workarounds
- [:octicons-arrow-right-24: DataOps Manifesto](https://dataopsmanifesto.org/en/) — the full 18 principles
