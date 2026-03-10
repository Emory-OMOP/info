# Extract, Load, Transform (ELT)

Emory's OMOP pipeline follows an **ELT** pattern — data is extracted from source systems (Epic, CDW), loaded into a staging area, and then transformed into the OMOP CDM using DBT (Data Build Tool).

## Architecture

| Component | Role |
|-----------|------|
| **Source systems** | Epic Clarity, CDW — the raw clinical data |
| **DBT** | Transforms raw data into OMOP CDM tables, generates documentation, and runs data quality tests |
| **Apache Airflow** | Orchestrates scheduled model runs and manages pipeline dependencies |
| **Amazon Redshift** | The final OMOP data lake where researchers query data |

## Documentation

ETL documentation is generated continuously from the DBT project itself — every model, column description, and test result is auto-documented as part of each pipeline run.

[:octicons-arrow-right-24: Emory Enterprise OMOP DBT Documentation](https://probable-chainsaw-6kvrj26.pages.github.io/projects/)

## Versioning

The pipeline implements a **DataOps versioning paradigm** (see [:octicons-arrow-right-24: Data Quality Design](../../Data%20Quality/Data%20Quality%20Design/index.md)) where code, data, and subsamples are each versioned and tracked within the documentation and test result tracking system. This ensures reproducibility and transparency across the ETL process.

## Related Pages

- [:octicons-arrow-right-24: Data Quality Design](../../Data%20Quality/Data%20Quality%20Design/index.md) — the DataOps framework behind our testing approach
- [:octicons-arrow-right-24: Data Quality Results](../../Data%20Quality/Data%20Quality%20Results/index.md) — current test pass/fail status per table
- [:octicons-arrow-right-24: Vocabulary Mapping Coverage](../Vocabulary%20Mapping%20Coverage/index.md) — mapping completeness across CVB vocabulary projects
