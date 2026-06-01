---
date: 2026-05-07
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# How best should I map values that are the result of composite scores for a particular condition?

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/how-best-should-i-map-values-that-are-the-result-of-composite-scores-for-a-particular-condition/25333)
**Matched keywords**: OMOP

In my OMOP ETL, I have run into a bit of a conundrum. I currently have a few columns whose values reflect a composite score (e.g. for scoring a patient’s alcohol risk or calculating the atrial fibrillation stroke risk, a.k.a. CHAD score) but I’m not sure how best to map these values to concepts in the OMOP vocabularies.
For example, in the case of the CHAD score, the values in this column are integers that range from 0 to 9, where higher values indicate a greater stroke risk. These integers, in 

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/how-best-should-i-map-values-that-are-the-result-of-composite-scores-for-a-particular-condition/25333){.md-button}
