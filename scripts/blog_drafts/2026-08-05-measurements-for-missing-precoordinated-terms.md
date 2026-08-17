---
date: 2026-08-05
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Measurements for missing precoordinated terms

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/measurements-for-missing-precoordinated-terms/25754)
**Matched keywords**: OMOP

What’s the usual way of representing measurements of substances that exist as ingredients in omop but do not exist as precoordinated terms?
Seems like a clean solution could be to use Measurement of substance and have a potential qualifier marking the substance to be measured, but as Measurement of substance is in measurement domain you cannot put it either as observation or have a qualifier field available
This seems a good use case for having qualifier in measurement table, which would also be

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/measurements-for-missing-precoordinated-terms/25754){.md-button}
