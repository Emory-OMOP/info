---
hide:
  - toc
title: Code Heavy Applications
---


## Programming Languages and Tools

Users may develop against Emory's OMOP-CDM with any tool that can access our data lake(s) at Emory. However, the following are common languages used by the OHDSI community, and/or used locally to interact with our data.

<div class="grid cards grid-2" markdown>

-   :simple-r: __R and RStudio__

    ---

    R is a programming language and free software environment used for statistical computing and graphics. RStudio is an integrated development environment (IDE) for R. Together, they provide a powerful platform for data analysis and visualization. Historically, R has been the preferred language of OHDSI developers, and much of the ready-made tooling is available in R.

    [:octicons-arrow-right-24: Emory's R Repositories](https://ohdsi-atlas.emory.edu/atlas/#/home)

    [:octicons-arrow-right-24: Emory's R Training Resources](../../Training/Emory/R/index.md)

    ### Popular OHDSI Community Tools

    [:octicons-arrow-right-24: HADES](https://ohdsi.github.io/Hades/)

    
-   :simple-postgresql: __SQL__

    ---

    SQL (Structured Query Language) is a standard programming language specifically for managing and manipulating relational databases. It is widely used for querying and updating data in the OMOP-CDM.

    ### Query Libraries

    [:octicons-arrow-right-24: Emory](../../Training/Emory/SQL/Query%20Library/index.md)

    [:octicons-arrow-right-24: OHDSI](https://data.ohdsi.org/QueryLibrary/)

    ### Training

    [:octicons-arrow-right-24: Tips for Writing Queries Against OMOP](../../Training/Emory/SQL/index.md)

    [:octicons-arrow-right-24: General SQL Reference (w3schools)](https://www.w3schools.com/sql/)


</div>


<div class="grid cards grid-2" markdown>

-   :material-language-python: __Python__

    ---

    Python is a general-purpose programming language increasingly used in the OHDSI community for data analysis, machine learning, and ETL pipelines. Connect to Emory's OMOP data lake using `redshift_connector` or any Redshift-compatible driver.

    [:octicons-arrow-right-24: Database Connection Guide](../../Support/Access%20Requests/Databases/index.md#after-youre-approved)

</div>