# Community Overlap Report

Generates a stakeholder community overlap visualization for the OMOP Enterprise project. The report shows the relationship between the OMOP notification list and tooling users, with a School of Medicine breakdown and multi-department funding analysis.

**Audience:** Madhusmita Behera (CRIO) and SOM leadership. The report is used to demonstrate the breadth of SOM engagement with OMOP and justify continued investment.

**Last updated:** 2026-03-05

## CRIO Feedback & Progress

Feedback from Madhusmita Behera (CRIO) on 2026-03-05 and Benny Budiman (SOM Research Informatics):

### Completed

- [x] **Remove user count from hero** — replace "to support 64 users" with "for OMOP infrastructure and associated projects" (CRIO: don't quote a user count)
- [x] **Push Winship, Brain Health, BMI into SOM** — these are all SOM divisions; reclassify their faculty as SOM-affiliated (CRIO: "show higher % of users from SOM than 53%")
- [x] **Roll Rollins into BHC → SOM** — Rollins SPH faculty on OMOP are affiliated through BHC
- [x] **CASSIDY is an SOM funding source** — funds Dept of Family and Preventive Medicine, which is SOM
- [x] **Rename Brain Health → Goizueta Brain Health Institute** — confirmed SOM-affiliated; director is SOM Neurology faculty
- [x] **Remove duplicate % subtitle** — "61 of 88 stakeholders (69%)" conflicted with the 67% callout inside the hero
- [x] **CASSIDY uppercase** — brand style
- [x] **Funding section page break** — Investment by Funding Source now starts on its own page in PDF
- [x] **Minimum width on funding bar segments** — prevents label truncation for small sources (BMI, U01)
- [x] **Jeselyn Rhodes funding split** — SOM:45 + U01:10 (U01 grant beginning 2026)
- [x] **Xueqiong (Joan) Zhang** — title corrected to Business Analyst
- [x] **SOM department groups added** — Goizueta Brain Health Institute, Pathology & Lab Medicine, Infectious Diseases popped out from "Other"
- [x] **People reclassified per CRIO/Benny feedback:**
  - Shirley Mullins → BHC (Brain Health Center)
  - Chad Robichaux → BMI
  - Rohan Satya Isaac → Radiology
  - Vishnu Ravi Kumar → Other SOM (Biology, not Neurology)
  - Paula Edwards, Petek Ozgul, Jon Frisch, Geoffrey Smith, Octavia Larentis → GBHI
  - Xiaolan Zhang → LITS/OIT (was incorrectly listed as SOM)

### People changes (2026-03-05)

**Removed:**
- George Peckham-Rooney (moved to Alumni Relations, Feb 2025 — per Benny)
- Kendra Little, Sallie Owens, Emma Wang (left Emory — per Benny)
- Swapna Ashish Patel (removed)

**Added (Notification):**
- Vincent C. Marconi — SOM, Infectious Diseases (was "VC Marco" with missing info)
- Hui Shao — Rollins SPH / SOM, Global Health / Family and Preventive Medicine
- Mohammed K. Ali — Rollins SPH / SOM, Global Health / Family and Preventive Medicine
- Nadjo Hatchett — SOM, Winship Cancer Institute (Director of Cancer Registry)
- Sherita Hearn — SOM, Winship Cancer Institute (Tumor Registry)
- Veta Williamson — LITS/OIT
- Lauren Marshman — SOM, BHPMI-WHSC
- Kate Sanders — SOM, Goizueta Brain Health Institute
- Asif Jehaludi — SOM, GBHI (Consultant, Himformatics)
- Hatchett Nadjo → corrected to Nadjo Hatchett
- Jeanne E. Hendrickson — SOM, Pathology and Laboratory Medicine
- Andrea B. Moffitt — SOM, Hematology and Medical Oncology / Human Genetics
- Michael L. Hollingsworth — SOM, Winship Cancer Institute
- Walter Iacullo — SOM, Pathology and Laboratory Medicine
- Maria Diaz — Not found
- Alice Lever — SOM, GME
- Erin F. Glen — SOM, Psychiatry
- Divine McCaslin — SOM, Infectious Diseases
- Claire Williams — SOM, Infectious Diseases
- Ana Moldoveanu — SOM, Infectious Diseases
- Shanil M. Fuller — SOM, Infectious Diseases
- Donna Williams — Grady Memorial Hospital
- Mastewal Adane Mellese — Grady Memorial Hospital

**Added (Both):**
- Saima Rathore — SOM, Biomedical Informatics

**Reclassified to Both:**
- Xiaolan Zhang (was User, now on notification list too)
- Xiangqin Cui (was User, now on notification list too)
- Wenhui (Vivian) Zhang (merged two rows — was User + separate Notification row)

### Still needed

- [ ] SOM user % is ~67-70% — CRIO may want it higher; remaining non-SOM users are mostly LITS and Nursing
- [ ] Nursing faculty could potentially roll into SOM if CRIO confirms
- [ ] Several "Not found" entries need department/title info: Maria Diaz, Donna Williams, Mastewal Adane Mellese
- [ ] Verify guessed email addresses (Sherita Hearn, Kate Sanders, Asif Jehaludi)
- [ ] Report version naming cleanup (`community_overlap_v4.pdf` vs generated `community_overlap.pdf`)
- [ ] Regenerate and re-export PDF after all current changes

## Files

| File | Tracked | Description |
|------|---------|-------------|
| `emory_people_lookup_v2.csv` | Yes | Source data — edit this to update the report |
| `README.md` | Yes | This file |
| `community_overlap.html` | No | Generated HTML report |
| `community_overlap*.pdf` | No | Generated PDF export |
| `exports/` | No | Generated PNG exports |

Scripts in the parent directory:

| File | Description |
|------|-------------|
| `generate_community_report.py` | Reads CSV, applies classification logic, produces HTML |
| `export_community_report.py` | Converts HTML to PDF/PNG via Playwright |

## Quick Start

```bash
cd emory-omop

# Generate the HTML report
uv run scripts/generate_community_report.py

# View it
open scripts/community_data/community_overlap.html

# Export to PDF
uv run scripts/export_community_report.py --pdf

# Export section PNGs (2x retina)
uv run scripts/export_community_report.py --png
```

No dependencies for HTML generation (stdlib only). PDF/PNG export uses Playwright (`uv run` handles installation). First-time setup: `uv run scripts/export_community_report.py --install`.

## Report Sections

1. **Venn diagram** — Notification vs User communities with overlap count
2. **Stat cards** — Notification-only, Both, User-only counts
3. **Proportional bar** — visual breakdown of all stakeholders
4. **Roster** — names listed by community membership
5. **SOM Breakdown** (page 2):
   - **Funding hero** — total FTE invested, funding bar by source, SOM user % callout, department count
   - **SOM Venn diagram** — same as above but filtered to SOM-affiliated
   - **Department breakdown table** — per-department counts with name badges
6. **Investment by Funding Source** (page 3):
   - **By-source table** — FTE and % share per source with staff names
   - **Staff funding detail** — per-person funding breakdown

## SOM Classification Logic

A person is classified as SOM-affiliated if **any** of these are true:

1. **School field** starts with "School of Medicine"
2. **School or department** contains any of: `winship`, `brain health`, `goizueta brain health`, `biomedical informatics`, `bhpmi`, `rollins`
3. **Funded by an SOM division** — funding source matches: `som`, `winship`, `bmi`, `bhc`, `cassidy`

### Why Rollins is included

Rollins School of Public Health faculty working on OMOP are affiliated through the Brain Health Center (BHC), which is an SOM division. Rollins people are rolled into BHC, and BHC rolls into SOM.

### Why CASSIDY is included

CASSIDY funds the Department of Family and Preventive Medicine, which is SOM.

### Why some LITS staff are included

LITS staff are generally **not** SOM-affiliated, but individuals contracted to work on OMOP by SOM divisions are included. This is captured via the funding field (e.g., `SOM:100`, `Winship:75;SOM:25`). Examples: Daniel Smith, Jorge Marquez, Jeselyn Rhodes, Matt Holland.

### Non-SOM funding sources

- `SON` (School of Nursing) — does **not** roll into SOM

### SOM Department Groups

Configured via `SOM_DEPT_GROUPS` in `generate_community_report.py`:

1. Winship Cancer Institute
2. Biomedical Informatics
3. Radiology & Imaging Sciences
4. Hematology & Medical Oncology
5. Neurology
6. Surgery / Anesthesiology
7. Goizueta Brain Health Institute
8. BHPMI-WHSC
9. Infectious Diseases
10. Pathology & Laboratory Medicine
11. Critical Care / Emergency Med
12. Other SOM Departments (catch-all)

## Design Decisions

- **Funding hero text** says "invested by N departments for OMOP infrastructure and associated projects" — intentionally avoids quoting a user count (per CRIO feedback).
- **SOM subtitle removed** — previously showed stakeholder % above the hero box, conflicting with the user % inside. Dropped to avoid confusion.
- **CASSIDY** is uppercase (brand style).
- **U01** — new funding source for Jeselyn Rhodes (U01 grant beginning 2026). Purple color in the bar.
- **Funding section page break** — `break-before: page` on `.funding-section` keeps the heading and table together.
- **Min-width on hero bar segments** — 40px minimum prevents label truncation.
- **Funding source colors** are configured via `FUNDING_SOURCE_COLORS` dict in the script.

## CSV Format

| Column | Description |
|--------|-------------|
| `name` | Full name |
| `email` | Email address(es), semicolon-separated if multiple |
| `school` | School or org (e.g., `School of Medicine`, `LITS / IT Services`) |
| `department` | Department within school |
| `title` | Job title |
| `community` | One of: `User`, `Notification`, `Both` |
| `funding` | Optional. OMOP funding sources as `Source:pct;Source:pct` (e.g., `Winship:75;SOM:25`) |

### Community values

- **User** — uses OMOP tooling
- **Notification** — on the notification/stakeholder list only
- **Both** — both a tooling user and on the notification list

### Funding format

Leave blank for community members without dedicated OMOP funding. For funded staff, use `Source:pct` pairs separated by semicolons:

```
SOM:100           # 100% SOM-funded
Winship:75;SOM:25 # split across two sources
BMI:10            # even 10% counts
```

Current funding sources: `SOM`, `Winship`, `BHC`, `SON`, `CASSIDY`, `BMI`, `U01`. New sources are picked up automatically — just add them to a person's funding field.

## Updating the Report

1. Edit `emory_people_lookup_v2.csv` (add/remove rows, change community, update funding)
2. Run `uv run scripts/generate_community_report.py`
3. Optionally export: `uv run scripts/export_community_report.py --pdf --png`

## See also

- [Repository README](../../README.md) — repo overview and quick start
- [Data Quality release pipeline](../README.md) — DQD/DBT automation scripts
- [News & Opportunities blog](../../docs/blog/README.md) — posting guide for the researcher news feed
