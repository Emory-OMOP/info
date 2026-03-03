---
search:
  exclude: false
title: R Training Resources
---

# R Training Resources

R is the historically preferred language of the OHDSI community, and much of the ecosystem's ready-made tooling is built in R.

## HADES — OHDSI's R Package Ecosystem

[HADES](https://ohdsi.github.io/Hades/) (Health Analytics Data-to-Evidence Suite) is a collection of open-source R packages for large-scale analytics against the OMOP CDM. Key packages include:

| Package | Purpose |
|---------|---------|
| [DatabaseConnector](https://ohdsi.github.io/DatabaseConnector/) | Connect to OMOP databases (Redshift, PostgreSQL, etc.) |
| [SqlRender](https://ohdsi.github.io/SqlRender/) | Write SQL once, translate to any dialect |
| [CohortGenerator](https://ohdsi.github.io/CohortGenerator/) | Generate cohorts from ATLAS definitions |
| [FeatureExtraction](https://ohdsi.github.io/FeatureExtraction/) | Extract patient-level features for modeling |
| [PatientLevelPrediction](https://ohdsi.github.io/PatientLevelPrediction/) | Build and evaluate predictive models |
| [CohortDiagnostics](https://ohdsi.github.io/CohortDiagnostics/) | Evaluate cohort definitions across databases |

## Connecting to Emory's OMOP Data Lake from R

```r
library(DatabaseConnector)

connectionDetails <- createConnectionDetails(
  dbms = "redshift",
  server = "<host from email>/<database from email>",
  port = 5439,
  user = "<your username>",
  password = "<your password>"
)

conn <- connect(connectionDetails)

# Query the person table
querySql(conn, "SELECT COUNT(*) AS person_count FROM cdm.person")

disconnect(conn)
```

!!! tip "Use `DatabaseConnector` over `RPostgres`"
    While you can connect with `RPostgres` or `DBI` directly, `DatabaseConnector` is recommended for OHDSI workflows because HADES packages expect a `DatabaseConnector` connection object.

## Additional Resources

- [:octicons-arrow-right-24: The Book of OHDSI — R Chapter](https://ohdsi.github.io/TheBookOfOhdsi/SqlAndR.html){ target="_blank" }
- [:octicons-arrow-right-24: HADES Installation Guide](https://ohdsi.github.io/Hades/rSetup.html){ target="_blank" }
- [:octicons-arrow-right-24: OHDSI R Package Index](https://ohdsi.github.io/Hades/packages.html){ target="_blank" }
