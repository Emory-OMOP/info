---
title: "Non-Human Subjects Research Determination (NHSRD)"
hide:
  - footer
---

# Non-Human Subjects Research Determination (NHSRD)

!!! danger "DRAFT — Internal Review Only · Not for distribution in wide release"

    This page is a **working process guide** for the Enterprise OMOP implementation team and our network of collaborators. It explains how Emory investigators document that a project does **not** require IRB review. It is not legal advice and does not replace the Emory IRB's own guidance — when in doubt, contact the IRB office. Wording and links are subject to change.

    See [releases](../../../../Data%20in%20Enterprise%20OMOP/Releases/) and [roadmap](../../../Product%20Roadmap/) for details.

    **Authors**: Emory University — Enterprise OMOP Implementation Team

    **Version**: 0.1 | **Date**: June 18, 2026

!!! note "Scope"

    This is a **how-to guide** for completing and filing an Emory **Non-Human Subjects Research Determination (NHSRD)** when a project works only with de-identified, pre-existing data and therefore is not human-subjects research. It walks through the federal definitions that drive the outcome, the step-by-step workflow, the form's decision logic, a worked example, and the record-keeping you must keep on file. It is a reusable procedure — **every new project needs its own determination**, even if it looks like an earlier one. It does **not** cover protocols that *do* require IRB review (identifiable data, prospective collection, interaction with participants, FDA-regulated test articles); those go through eIRB.

??? abstract "Quick reference — what's on this page"

    - [When to use this](#when-to-use-this) — and when you must use eIRB instead
    - [Why de-identified secondary analysis is "not human subjects"](#the-definitions-that-drive-the-outcome) — the federal definitions
    - [The workflow](#the-workflow-step-by-step) — six steps from guidance page to filed record
    - [How the form decides](#how-the-form-decides) — the branching logic
    - [Worked example](#worked-example-enterprise-omop-broad-re-use-of-de-identified-data) — an illustrative NHSRD completed by an Enterprise OMOP team member
    - [What to keep on file](#record-keeping-and-retention) — the form responses **and** the IRB memo
    - [Audits](#audits) and [edge cases](#caveats-and-edge-cases) — funding, external sharing, VA, "exempt", re-determination

---

## When to use this

Emory does **not** require IRB review of studies that do not meet the federal definition of **"human subjects research"** (DHHS / Common Rule) or **"clinical investigation"** (FDA). The NHSRD Electronic Form is the tool that documents that conclusion. Use it when **all** of the following are true:

- The project is performed by **Emory or Emory Healthcare (EHC) affiliates** doing work **for Emory purposes**.
- The activity in scope analyzes **data or specimens that already exist** before the project starts (a secondary analysis).
- The data is **de-identified** (or otherwise carries no identifiable private information) and **no member of the team can re-identify** it — directly or through a code/key.
- There is **no intervention or interaction** with living individuals and **no FDA-regulated test article** (drug, device, biologic, software/app, in-vitro assay).

!!! warning "Use eIRB instead when the project involves any of the following"

    - Identifiable private information, or a code/key the team can access to re-identify
    - Prospective collection of data, specimens, surveys, scans, or any interaction with participants
    - An FDA test article, or device/software/assay testing on individuals' specimens or data
    - A DHHS award where **Emory is the prime recipient** and the application indicates human subjects will be involved (IRB submission is required regardless — see [Caveats](#caveats-and-edge-cases))

    A project being **for academic credit at another institution** must seek its determination from **that institution's IRB**, not this form.

!!! info "Scope only what Emory affiliates do in *this* project"

    When answering the form, consider **only** the activities performed by Emory/EHC affiliates in the **current** proposed project. For a secondary data analysis, do **not** count the original primary data collection. If Emory is a **subrecipient**, consider only Emory's own activities even if another site is doing human-subjects research under the same award.

---

## The definitions that drive the outcome

The determination is a logic test against three federal definitions. Understanding them is what lets you answer the form confidently.

=== "Research"

    **A systematic investigation designed to develop or contribute to generalizable knowledge** (45 CFR 46.102(l)). Data analysis intended to produce publishable or broadly applicable findings is research. Note that **case study/series, classroom activities, public-health practice, program evaluation, and quality improvement** are often *not* research — review the IRB's [getting-started guidance](https://www.irb.emory.edu/guidance/getting-started/review.html) if your project might be one of these.

=== "Human subject"

    **A living individual about whom an investigator obtains** either (i) information or biospecimens **through intervention or interaction** and uses/studies/analyzes them, **or** (ii) **identifiable private information** or identifiable biospecimens (45 CFR 46.102(e)). The pivot for secondary data work is *identifiability*: de-identified, pre-existing data that the team cannot re-identify means there is **no human subject** — even though the data describes living people.

=== "Clinical investigation (FDA)"

    An experiment involving a **test article** (drug, medical device, biologic) and one or more human subjects (21 CFR 50.3 / 56.102). Also captured: testing any **device — including software, apps, or in-vitro assays — using individuals' specimens or data, even if completely de-identified**.

!!! tip "The key insight for de-identified secondary analysis"

    Such a project **is research** (systematic, generalizable) and it **does obtain information about living individuals** — so the form will have you answer "Yes" to those. It is **not human-subjects research** because the information is **not identifiable private information** and the team **cannot re-identify** it. Research + not-human-subjects + not-an-FDA-investigation ⇒ **no IRB review required**.

---

## The workflow, step by step

1. **Read the IRB review guidance** at <https://www.irb.emory.edu/guidance/getting-started/review.html>. Confirm your project is research and decide whether any non-research category (QI, program evaluation, etc.) applies. If unsure, call the IRB at (404) 712-0720 *before* filling out the form.
2. **Write a short project proposal/description** first. The IRB audits the form **against your written proposal** (see [Audits](#audits)), so the two must tell the same story. Keep it with your records.
3. **Open the NHSRD Electronic Form** from the IRB guidance page. It is a Microsoft Forms questionnaire. (Use the official link on the IRB site — do not reuse another person's saved-response link, which is tied to their submission.)
4. **Answer the questions** about funding, external sharing, VA involvement, the research/human-subjects/FDA criteria, and identifiability. Answer for **only** the Emory affiliates' activities in the current project (see scope note above).
5. **Reach the determination.** When the answers establish that the project is not human-subjects research and not a clinical investigation, the form presents the closing attestation: *"This project does not require IRB review … This project should not be described as 'exempt.'"* Select it.
6. **Save and file.** Use **Print to PDF** to save a copy of your responses. File that PDF together with the **IRB policy memo** (the standing memo authorizing this self-determination mechanism) in your project records. See [Record-keeping](#record-keeping-and-retention).

---

## How the form decides

The form is a branching questionnaire. The path that leads to **"no IRB review required"** for a de-identified secondary analysis is:

```
Research?  (systematic investigation → designed for generalizable knowledge)
   │  YES — it IS research
   ▼
Human subject?  (obtains information about living individuals)
   │  YES — but examine HOW:
   ├─ Intervention / interaction with individuals?           → NO
   ├─ Accessing/generating identifiable AND private info?     → NO
   ├─ Analysis of existing data, all data pre-exists study?   → YES
   └─ Could ANY team member re-identify (directly or by key)? → NO
   ▼  ⇒ NOT human-subjects research
FDA clinical investigation?
   ├─ Anyone receives a test article / is a control?          → NO
   └─ Any device/software/assay tested on individuals' data?  → NO
   ▼  ⇒ NOT a clinical investigation
═════════════════════════════════════════════════════════════
RESULT: No IRB review required.  (NOT "exempt.")
```

If any branch flips — for example, the team *can* re-identify, or data is collected prospectively, or an FDA test article is involved — the form routes you toward an eIRB submission instead.

---

## Worked example: Enterprise OMOP broad re-use of de-identified data

To illustrate the procedure, an Enterprise OMOP team member — Daniel Smith — completed the NHSRD form for an example project: a broad, ongoing secondary analysis of de-identified OMOP CDM data. This is a practice walkthrough prepared for this guide, **not a filed determination**, but the responses below show how each question is answered for this kind of work.

| # | Question | Answer |
|---|----------|--------|
| 1 | Project Title | *Emory Enterprise OMOP Broad Re-use of De-identified Data* |
| 2 | Project Leader | Daniel Smith |
| 3 | Externally-funded with Emory as prime — funder verified as non-human-subjects? | No |
| 4 | Sharing data/specimens (identified or de-identified) outside Emory? | No |
| 5 | Involves Veterans Affairs (site, data source, or affiliation)? | No |
| 6 | **Research** — a systematic investigation? | **Yes** |
| 7 | **Research** — designed to contribute to generalizable knowledge? | **Yes** |
| 8 | **Human subjects** — obtaining information about living individuals (incl. de-identified)? | **Yes** |
| 9 | Intervention or interaction with the individuals? | No |
| 10 | Accessing/generating individually identifiable **and** private information? | **No** |
| 11 | Analysis of existing data/specimens, **all** of which exist before the study starts? | **Yes** |
| 12 | Could **any** team member re-identify the data, directly or via a code/key? | **No** |
| 13 | **FDA** — anyone a recipient of a test article or used as a control? | No |
| 14 | **FDA** — any device/software/assay tested using individuals' data, even de-identified? | No |
| 15 | Closing attestation selected | *"No eIRB submission necessary. I will protect confidentiality and keep a copy of my responses."* |

**Reading the result:** Q6–Q7 establish this **is research**. Q8 is "Yes" because the data describes living people — but Q9–Q12 show the data is de-identified, pre-existing, and not re-identifiable by the team, so there is **no human subject**. Q13–Q14 rule out an FDA clinical investigation. The form therefore returns **no IRB review required**, with the explicit instruction that the project must **not** be called "exempt."

!!! note "Why a determination like this can cover broad re-use"

    A determination of this kind is scoped to a *class* of activity — secondary analysis of the de-identified OMOP CDM — rather than a single hypothesis. As long as a downstream analysis stays inside that envelope (de-identified, pre-existing, no re-identification, no external sharing, no FDA article), it falls within the same determination. The moment an analysis steps outside it — pulling identifiable data, sharing an extract outside Emory, collecting new data — that analysis needs its **own** determination or an eIRB submission. See [Caveats](#caveats-and-edge-cases).

---

## Record-keeping and retention

When the outcome is "no IRB review required," the form **is** your documentation. The standing IRB memo states the study team is **expected to keep a copy of the form responses as an attestation of the researchers' intent**, and that the **form responses and the memo may be provided to others as needed**. Keep all three of the following together in the project record:

- :material-file-document: **The saved form responses** (Print-to-PDF copy of your completed NHSRD).
- :material-email: **The IRB policy memo** authorizing the self-determination mechanism (the standing memo from the IRB office).
- :material-text-box: **Your written project proposal/description**, so the file is audit-ready (the IRB compares the form to your proposal).

!!! warning "Do not call it 'exempt'"

    "No IRB review required" and "exempt" are different regulatory statuses. Exempt research *is* human-subjects research that meets an exemption category and still goes through the IRB. A non-human-subjects determination never enters the IRB system. The form is explicit: **this project should not be described as "exempt."**

---

## Audits

The IRB **periodically audits** completed NHSRD forms **against the team's written proposal** to confirm the tool produced an accurate result. This is why step 2 of the workflow matters: keep a written description of the project that matches the answers on the form. If the project's data handling changes such that the form's answers would change, re-run the determination (below).

---

## Caveats and edge cases

- **Re-determination when scope changes.** A determination reflects the project *as described*. If you later add identifiable data, prospective collection, an external data share, or an FDA test article, the earlier determination no longer covers that work — complete a new form or submit to eIRB.
- **External sharing.** If you will share data or specimens (identified **or** de-identified) outside Emory, an agreement may be required; review the Office of Technology Transfer forms at <https://ott.emory.edu/resources/forms/index.html> and the team's [de-identification](../../../../Data%20in%20Enterprise%20OMOP/Patient%20Identities/De-identification/) and per-extract sharing guidance.
- **DHHS prime awards.** If Emory is the **prime** recipient of a DHHS award and the application indicates human subjects will be involved, **IRB submission is required** — do not rely on this form. If Emory is prime but contracting all non-exempt human-subjects activities to another site, contact the IRB for guidance.
- **Veterans Affairs.** Any VA involvement (site, data source, or investigator affiliation) changes the regulatory picture; flag it on the form and expect additional review.
- **Academic credit elsewhere.** Emory/EHC affiliates doing a project for academic credit at another institution must obtain the determination from **that** institution's IRB.

---

## References and related pages

- **Emory IRB — Getting Started / Does my project need review?** <https://www.irb.emory.edu/guidance/getting-started/review.html>
- **Emory IRB office** — irb@emory.edu · (404) 712-0720 · <http://www.irb.emory.edu/>
- **PHI identifiers list** (HIPAA 18 identifiers) — <http://www.irb.emory.edu/documents/phi_identifiers.pdf>
- **Office of Technology Transfer — agreements/forms** — <https://ott.emory.edu/resources/forms/index.html>
- **Common Rule** — 45 CFR 46.102 (definitions of *research* and *human subject*)
- **FDA** — 21 CFR 50.3 / 56.102 (*clinical investigation*, *test article*)
- Related Enterprise OMOP pages: [De-identification](../../../../Data%20in%20Enterprise%20OMOP/Patient%20Identities/De-identification/) · [Database access requests](../../../../Support/Access%20Requests/Databases/) · [LLM Use Disclosure](../../../LLM%20Use%20Disclosure/)
