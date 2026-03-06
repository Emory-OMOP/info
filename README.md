# Emory OMOP

Source for the [Emory OMOP documentation site](https://emorydatasolutions.github.io/emory-omop/) — built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Repository structure

```
emory-omop/
├── docs/                        ← MkDocs content pages (the website)
│   ├── Applications/            ← ATLAS, R, SQL tooling guides
│   ├── Data in Enterprise OMOP/ ← Data mapping, quality, releases, conventions
│   ├── OMOP Primers/            ← CDM table reference guides
│   ├── Training/                ← Emory-specific and external training resources
│   ├── blog/                    ← News & Opportunities blog (posts, authors)
│   └── ...
├── overrides/                   ← MkDocs theme overrides (homepage)
├── scripts/                     ← Automation scripts
│   ├── update_dqd_summary.py    ← Data Quality release pipeline
│   ├── dqd_history/             ← DQD JSON results per release
│   ├── dbt_history/             ← DBT artifacts per release
│   ├── community_data/          ← Community overlap report
│   └── README.md                ← Pipeline usage instructions
├── supporting/                  ← Documents not hosted elsewhere
├── mkdocs.yml                   ← Site configuration
└── pyproject.toml               ← Python dependencies (managed by uv)
```

## Quick start

```bash
# Install dependencies
uv sync

# Serve locally
uv run mkdocs serve

# Build static site
uv run mkdocs build
```

## Scripts

### Data Quality release pipeline

Automates updates to the Data Quality Results, Known Issues, DBT Tests, and landing pages when a new OMOP release ships. Full instructions in [`scripts/README.md`](scripts/README.md).

```bash
# Ingest new release artifacts
uv run scripts/update_dqd_summary.py ingest --release v1.1.0 \
  --dqd <dqd_results.json> \
  --dbt-manifest <manifest.json> \
  --dbt-results <run_results.json> \
  --dbt-catalog <catalog.json>

# Regenerate all Data Quality pages
uv run scripts/update_dqd_summary.py generate
```

### Community overlap report

Generates a stakeholder community visualization. See [`scripts/community_data/README.md`](scripts/community_data/README.md).

```bash
uv run scripts/generate_community_report.py
```

## Blog

The News & Opportunities blog surfaces funding opportunities, OHDSI updates, and announcements for the research community. Posts are markdown files in `docs/blog/posts/` with category and tag metadata. See [`docs/blog/README.md`](docs/blog/README.md) for the posting guide.

## Related repositories

| Repository | Description |
|------------|-------------|
| [emory_omop_enterprise](https://github.com/EmoryDataSolutions/emory_omop_enterprise) | ETL pipeline, DBT project, and project management |
| e_omop_dqd | OHDSI Data Quality Dashboard (DQD result generation) |
