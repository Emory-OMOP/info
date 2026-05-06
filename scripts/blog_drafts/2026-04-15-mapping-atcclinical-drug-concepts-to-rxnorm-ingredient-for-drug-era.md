---
date: 2026-04-15
draft: true
categories:
  - OHDSI
tags:
  - ohdsi
  - community
---

# Mapping ATC/Clinical Drug concepts to RxNorm Ingredient for drug_era

**Source**: [OHDSI Forums](https://forums.ohdsi.org/t/mapping-atc-clinical-drug-concepts-to-rxnorm-ingredient-for-drug-era/25230)
**Matched keywords**: OMOP, OHDSI

Hello OHDSI community,
We are building an ETL to transform medication administration records into OMOP drug_exposure.
In our source table, we have, among other things, ATC codes. OHDSI provides ATC to RxNorm ingredient mappings which can be used in the drug_exposure table.
Let’s assume the example of having concept abacavir – 300 mg – J05AF06 in the source.
In drug_exposure we do not have an “amount_value” field because this is derived from drug_strength. It does not work for RxNorm Ingredient c

<!-- more -->

[:octicons-link-external-24: Read full announcement](https://forums.ohdsi.org/t/mapping-atc-clinical-drug-concepts-to-rxnorm-ingredient-for-drug-era/25230){.md-button}
