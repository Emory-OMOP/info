---
search:
  exclude: false
title: Request ATLAS Access
---

# Request ATLAS Access

Get access to OHDSI ATLAS — Emory's web application for building cohorts, exploring vocabularies, and running standardized analyses on OMOP data.

## What You'll Get

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } __Cohort Building__

    ---

    Define study populations visually with inclusion/exclusion criteria, temporal logic, and demographic filters.

-   :material-book-search:{ .lg .middle } __Concept Exploration__

    ---

    Search and navigate 7M+ standardized clinical concepts across SNOMED, RxNorm, LOINC, ICD10, and more.

-   :material-chart-timeline-variant:{ .lg .middle } __Standardized Analyses__

    ---

    Run characterization, incidence rate, and care pathway analyses directly in the browser.

-   :material-share-variant:{ .lg .middle } __Reproducible Designs__

    ---

    Export cohort definitions as JSON to share with collaborators or deploy across OHDSI network studies.

</div>

!!! info "Need direct SQL access instead?"
    If you want to query OMOP tables with SQL, Python, or R, see [:octicons-arrow-right-24: Request Database Access](../Databases/index.md).

## Prerequisites

Before submitting your request, confirm the following:

- [x] **Emory VPN** — connected and working[^1]
- [x] **Biomedical CITI training** — completed within the last 3 years
- [x] **Emory HIPAA training** — completed

[^1]: Verify your VPN by navigating to the [Emory ATLAS Instance](https://ohdsi-atlas.emory.edu/atlas/#/){ target="_blank" }. If the page loads, you're connected.

## Request Access

All access requests are submitted through REDCap:

[:octicons-arrow-right-24: Open the Access Request Form](https://redcap.emory.edu/surveys/?s=KTPWCCDPEHFYLETP){ target="_blank" .md-button }

---

### Step 1: Select Resources and Systems

Fill in your name and Emory email, then make the following selections: (1)
{ .annotate }

1.  :material-information-outline: The form dynamically shows follow-up questions based on your selections. Choose them in order from top to bottom.

| Field | What to Select |
|-------|----------------|
| Which resources do you need access to? | **Databases, applications, and data lakes** |
| Which application, database, or data lake? | **OMOP - Atlas** |
| Which OMOP domain do you need? | **OMOP - EHC De-Identified** |

![REDCap form showing the correct selections for ATLAS access to de-identified OMOP data](../../../assets/images/atlas_access_request_1.png)

??? tip "Need access to identified data?"
    Start with de-identified access first. Identified data requires additional approvals — including IRB protocol documentation — and is handled through a separate process. Contact the Data Solutions team for guidance.

---

### Step 2: Provide a Justification

Describe your use case for the ATLAS tool. A brief statement is sufficient:

> *Exploring concept and cohort creation using the OMOP-CDM*

### Step 3: Upload Required Trainings

Confirm completion and upload certificates for both required trainings:

1. **Biomedical CITI training** — completed within the last 3 years. Select **Yes** and upload your certificate.
2. **Emory HIPAA training** — current. Select **Yes** and upload your certificate.

---

### Step 4: Review the OMOP Terms of Data Use

Read the **OMOP Terms of Data Use** agreement carefully, then provide your electronic signature.

??? example "What does the Terms of Data Use cover?"
    The agreement covers appropriate use of the OMOP database, including data security requirements, disclosure restrictions, and compliance with Emory's HIPAA security and technical controls.

---

### Step 5: Submit

Click **Submit**. The Data Solutions team will review your request and provision access.

## After You're Approved

Once approved, access ATLAS immediately via VPN:

[:octicons-arrow-right-24: Open Emory ATLAS](https://ohdsi-atlas.emory.edu/atlas/#/home){ target="_blank" .md-button }

New to ATLAS? Start here:

<div class="grid cards" markdown>

-   :material-school:{ .lg .middle } __Emory Training__

    ---

    Emory-specific tutorials covering our ATLAS instance and local conventions.

    [:octicons-arrow-right-24: Training Resources](../../../Training/Emory/ATLAS/index.md)

-   :material-github:{ .lg .middle } __OHDSI Documentation__

    ---

    Official ATLAS documentation from the OHDSI community.

    [:octicons-arrow-right-24: OHDSI ATLAS](https://github.com/OHDSI/Atlas){ target="_blank" }

</div>

## Questions?

Reach out via the support channels on the [:octicons-arrow-right-24: Contact Us](../../../Contact Us/index.md) page.
