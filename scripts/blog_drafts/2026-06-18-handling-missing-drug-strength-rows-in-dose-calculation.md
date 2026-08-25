---
date: 2026-06-18
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Handling missing DRUG_STRENGTH rows in dose calculation

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/handling-missing-drug-strength-rows-in-dose-calculation/25527)
**Matched keywords**: OHDSI

Hi all,
I’m building a dose-calculation view (V_DRUG_DOSE_CALC) over DRUG_EXPOSURE joined to DRUG_STRENGTH, applying the six dose use cases at https://ohdsi.github.io/CommonDataModel/drug_dose.html. The arithmetic is straightforward; what I want a second opinion on is how to treat exposures where the join to DRUG_STRENGTH yields no row.

Non-calculable concept: the source mapped to a concept class that carries no strength by design (Ingredient, Clinical Drug Form, Branded Drug Form). Strength is

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/handling-missing-drug-strength-rows-in-dose-calculation/25527){.md-button}
