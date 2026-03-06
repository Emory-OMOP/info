"""Generate community_overlap.html from the people lookup CSV.

Usage:
    uv run scripts/generate_community_report.py

No external dependencies — stdlib only.
"""

import csv
from html import escape
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).parent
DATA_DIR = HERE / "community_data"
CSV_PATH = DATA_DIR / "emory_people_lookup_v2.csv"
HTML_PATH = DATA_DIR / "community_overlap.html"

# ── SOM department grouping ──────────────────────────────────────────
# Keys = display name, values = substrings matched against the department field.
# Order here determines row order in the output table.
SOM_DEPT_GROUPS = {
    "Winship Cancer Institute": ["Winship"],
    "Biomedical Informatics": ["Biomedical Informatics"],
    "Radiology & Imaging Sciences": ["Radiology"],
    "Hematology & Medical Oncology": ["Hematology"],
    "Neurology": ["Neurology"],
    "Surgery / Anesthesiology": ["Surgery", "Anesthesiology"],
    "Goizueta Brain Health Institute": ["Goizueta Brain Health", "Brain Health"],
    "BHPMI-WHSC": ["BHPMI"],
    "Infectious Diseases": ["Infectious Diseases"],
    "Pathology & Laboratory Medicine": ["Pathology"],
    "Critical Care / Emergency Med": ["Critical Care", "Emergency", "Pulmonary"],
}
OTHER_LABEL = "Other SOM Departments"

# Display order and colors for funding sources
FUNDING_SOURCE_COLORS = {
    "SOM": "#1b4f72",
    "Winship": "#5b9bd5",
    "BHC": "#2e86c1",
    "SON": "#85c1e9",
    "CASSIDY": "#34495e",
    "BMI": "#aab7b8",
    "U01": "#6c3483",
}
FUNDING_DEFAULT_COLOR = "#7f8c8d"


# ── Helpers ──────────────────────────────────────────────────────────
def classify_som_dept(department: str) -> str:
    """Return the display-name group for an SOM person's department."""
    for group_name, substrings in SOM_DEPT_GROUPS.items():
        for sub in substrings:
            if sub.lower() in department.lower():
                return group_name
    return OTHER_LABEL


def pct(n: int, total: int) -> float:
    return round(n / total * 100, 1) if total else 0


def badge(name: str, community: str) -> str:
    cls = {"Both": "badge-b", "User": "badge-u", "Notification": "badge-n"}[community]
    return f'<span class="badge {cls}">{escape(name)}</span>'


def parse_funding(raw: str) -> list[tuple[str, float]]:
    """Parse 'Source:pct;Source:pct' into [(source, pct), ...]."""
    if not raw:
        return []
    entries = []
    for part in raw.split(";"):
        part = part.strip()
        if ":" in part:
            source, val = part.rsplit(":", 1)
            entries.append((source.strip(), float(val.strip())))
    return entries


# ── Read CSV ─────────────────────────────────────────────────────────
def load_people() -> list[dict]:
    rows = []
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row["name"].strip()
            if not name:
                continue
            funding_raw = row.get("funding", "").strip()
            rows.append({
                "name": name,
                "email": row["email"].strip(),
                "school": row["school"].strip(),
                "department": row["department"].strip(),
                "title": row["title"].strip(),
                "community": row["community"].strip(),
                "funding": parse_funding(funding_raw),
            })
    return rows


# ── Build HTML ───────────────────────────────────────────────────────
def render(people: list[dict]) -> str:
    notif_only = sorted([p for p in people if p["community"] == "Notification"], key=lambda p: p["name"])
    user_only = sorted([p for p in people if p["community"] == "User"], key=lambda p: p["name"])
    both = sorted([p for p in people if p["community"] == "Both"], key=lambda p: p["name"])

    n_notif = len(notif_only)
    n_user = len(user_only)
    n_both = len(both)
    total = n_notif + n_user + n_both
    n_notif_community = n_notif + n_both
    n_user_community = n_user + n_both

    # SOM subset — Winship, Brain Health, and BMI are SOM divisions.
    # People count as SOM if: (a) school says SOM, (b) department is an
    # SOM division, or (c) they are funded/contracted by an SOM division.
    _SOM_DEPT_KEYWORDS = ["winship", "brain health", "goizueta brain health", "biomedical informatics", "bhpmi", "rollins"]
    _SOM_FUNDING_SOURCES = {"som", "winship", "bmi", "bhc", "cassidy"}

    def _is_som(p: dict) -> bool:
        if p["school"].lower().startswith("school of medicine"):
            return True
        # Check both school and department for SOM division keywords
        combined = (p["school"] + " " + p["department"]).lower()
        if any(kw in combined for kw in _SOM_DEPT_KEYWORDS):
            return True
        # Contracted/funded by an SOM division
        return any(s.lower() in _SOM_FUNDING_SOURCES for s, _ in p["funding"])

    som = [p for p in people if _is_som(p)]
    som_notif = len([p for p in som if p["community"] == "Notification"])
    som_user = len([p for p in som if p["community"] == "User"])
    som_both = len([p for p in som if p["community"] == "Both"])
    som_total = som_notif + som_user + som_both
    som_notif_community = som_notif + som_both
    som_user_community = som_user + som_both
    som_pct_of_total = round(som_total / total * 100) if total else 0

    # SOM department grouping
    dept_groups: dict[str, list[dict]] = defaultdict(list)
    for p in som:
        dept_groups[classify_som_dept(p["department"])].append(p)

    # SOM as % of all users (User + Both communities)
    som_users = [p for p in som if p["community"] in ("User", "Both")]
    all_users = [p for p in people if p["community"] in ("User", "Both")]
    som_user_pct = round(len(som_users) / len(all_users) * 100) if all_users else 0

    # Number of distinct SOM departments represented
    som_dept_count = len(dept_groups)

    # ── Multi-source funding ─────────────────────────────────────
    funded_staff = [p for p in people if p["funding"]]

    # Aggregate FTE by source
    source_fte: dict[str, float] = defaultdict(float)
    for p in funded_staff:
        for source, pct_val in p["funding"]:
            source_fte[source] += pct_val / 100

    grand_total_fte = sum(source_fte.values())
    n_funding_sources = len(source_fte)

    # Sort sources by FTE descending
    sorted_sources = sorted(source_fte.items(), key=lambda x: x[1], reverse=True)

    # SOM-specific funding
    som_fte = source_fte.get("SOM", 0.0)
    som_funding_pct = round(som_fte / grand_total_fte * 100) if grand_total_fte else 0

    # Build ordered department rows (configured groups first, then Other)
    dept_rows = []
    for group_name in SOM_DEPT_GROUPS:
        if group_name in dept_groups:
            dept_rows.append((group_name, dept_groups[group_name]))
    if OTHER_LABEL in dept_groups:
        dept_rows.append((OTHER_LABEL, dept_groups[OTHER_LABEL]))

    def dept_table_rows() -> str:
        lines = []
        for dept_name, members in dept_rows:
            d_both = sorted([p for p in members if p["community"] == "Both"], key=lambda p: p["name"])
            d_user = sorted([p for p in members if p["community"] == "User"], key=lambda p: p["name"])
            d_notif = sorted([p for p in members if p["community"] == "Notification"], key=lambda p: p["name"])
            d_total = len(members)
            badges = "".join(
                [badge(p["name"], "Both") for p in d_both]
                + [badge(p["name"], "User") for p in d_user]
                + [badge(p["name"], "Notification") for p in d_notif]
            )
            lines.append(f"""      <tr>
        <td class="dept-name">{escape(dept_name)}</td>
        <td style="text-align: center; font-weight: 600;">{d_total}</td>
        <td style="text-align: center;">{len(d_notif)}</td>
        <td style="text-align: center;">{len(d_both)}</td>
        <td style="text-align: center;">{len(d_user)}</td>
        <td>
          {badges}
        </td>
      </tr>""")
        return "\n".join(lines)

    def funding_source_rows() -> str:
        """Build rows for the by-source funding table."""
        lines = []
        for source, fte in sorted_sources:
            color = FUNDING_SOURCE_COLORS.get(source, FUNDING_DEFAULT_COLOR)
            bar_w = round(fte / grand_total_fte * 200) if grand_total_fte else 0
            pct_val = round(fte / grand_total_fte * 100) if grand_total_fte else 0
            # Find staff funded by this source
            staff_names = []
            for p in funded_staff:
                for s, v in p["funding"]:
                    if s == source:
                        staff_names.append(f"{escape(p['name'])} ({v:.0f}%)")
            lines.append(f"""      <tr>
        <td style="font-weight: 600; color: {color};">{escape(source)}</td>
        <td style="text-align: center; font-weight: 600;">{fte:.2f}</td>
        <td style="text-align: center;">{pct_val}%</td>
        <td><span class="funding-bar" style="width: {bar_w}px; background: {color};"></span></td>
        <td style="font-size: 0.7rem; color: #555;">{", ".join(staff_names)}</td>
      </tr>""")
        return "\n".join(lines)

    def funding_staff_rows() -> str:
        """Build rows for the per-person funding detail table."""
        lines = []
        for p in sorted(funded_staff, key=lambda x: sum(v for _, v in x["funding"]), reverse=True):
            total_pct = sum(v for _, v in p["funding"])
            sources_html = ", ".join(
                f'<span style="color: {FUNDING_SOURCE_COLORS.get(s, FUNDING_DEFAULT_COLOR)}; font-weight: 600;">'
                f'{escape(s)}</span> {v:.0f}%'
                for s, v in p["funding"]
            )
            lines.append(f"""      <tr>
        <td style="font-weight: 500;">{escape(p["name"])}</td>
        <td style="font-size: 0.75rem;">{escape(p["title"])}</td>
        <td style="text-align: center;">{total_pct:.0f}%</td>
        <td>{sources_html}</td>
      </tr>""")
        return "\n".join(lines)

    def name_list(people_list: list[dict]) -> str:
        return "\n".join(f"        <li>{escape(p['name'])}</li>" for p in people_list)

    # Build the funding bar segments for the hero
    hero_bar_segs = ""
    for source, fte in sorted_sources:
        color = FUNDING_SOURCE_COLORS.get(source, FUNDING_DEFAULT_COLOR)
        w = round(fte / grand_total_fte * 100, 1) if grand_total_fte else 0
        hero_bar_segs += (
            f'<div style="width: {w}%; min-width: 40px; background: {color}; height: 100%; display: flex; '
            f'align-items: center; justify-content: center; font-size: 0.6rem; color: #fff; '
            f'font-weight: 600; white-space: nowrap; overflow: visible;">{escape(source)}</div>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Community Overlap — OMOP Stakeholders</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #ffffff; color: #1a1a2e; display: flex; flex-direction: column; align-items: center; min-height: 100vh; padding: 2rem; }}
  h1 {{ font-size: 1.5rem; font-weight: 600; margin-bottom: 0.25rem; color: #012169; }}
  .subtitle {{ font-size: 0.875rem; color: #555; margin-bottom: 2rem; }}
  .chart-container {{ position: relative; width: 700px; height: 420px; }}
  svg {{ width: 100%; height: 100%; }}
  .circle-notification {{ fill: rgba(1, 33, 105, 0.2); stroke: #012169; stroke-width: 2.5; }}
  .circle-user {{ fill: rgba(242, 169, 0, 0.2); stroke: #f2a900; stroke-width: 2.5; }}
  .label {{ font-size: 14px; font-weight: 600; text-anchor: middle; }}
  .count {{ font-size: 36px; font-weight: 700; text-anchor: middle; dominant-baseline: central; }}
  .count-notification {{ fill: #012169; }}
  .count-user {{ fill: #b07800; }}
  .count-both {{ fill: #012169; }}
  .count-label {{ font-size: 12px; fill: #666; text-anchor: middle; }}
  .stats {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 2rem; width: 700px; }}
  .stat-card {{ background: #f8f9fa; border-radius: 12px; padding: 1.25rem; text-align: center; border: 1px solid #e0e0e0; }}
  .stat-number {{ font-size: 2rem; font-weight: 700; }}
  .stat-label {{ font-size: 0.8rem; color: #666; margin-top: 0.25rem; }}
  .stat-notification .stat-number {{ color: #012169; }}
  .stat-user .stat-number {{ color: #b07800; }}
  .stat-both .stat-number {{ color: #0033a0; }}
  .total-bar {{ width: 700px; margin-top: 2rem; }}
  .bar-label {{ font-size: 0.8rem; color: #666; margin-bottom: 0.5rem; }}
  .bar-track {{ height: 32px; background: #f0f0f0; border-radius: 8px; display: flex; overflow: hidden; border: 1px solid #ddd; }}
  .bar-seg {{ display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 600; transition: width 0.6s ease; }}
  .bar-seg.notif {{ background: #012169; color: #fff; }}
  .bar-seg.both {{ background: #0033a0; color: #fff; }}
  .bar-seg.user {{ background: #f2a900; color: #1a1a2e; }}
  .names-section {{ width: 700px; margin-top: 2rem; }}
  .names-section h2 {{ font-size: 1rem; margin-bottom: 1rem; color: #012169; }}
  .names-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }}
  .names-col h3 {{ font-size: 0.8rem; font-weight: 600; margin-bottom: 0.5rem; padding-bottom: 0.25rem; border-bottom: 2px solid; }}
  .names-col.notif h3 {{ color: #012169; border-color: #012169; }}
  .names-col.user h3 {{ color: #b07800; border-color: #f2a900; }}
  .names-col.overlap h3 {{ color: #0033a0; border-color: #0033a0; }}
  .names-col ul {{ list-style: none; font-size: 0.7rem; color: #333; line-height: 1.6; }}
  /* SOM subsection */
  .som-section {{ width: 700px; margin-top: 3rem; padding-top: 2rem; border-top: 2px solid #012169; }}
  .som-section h2 {{ font-size: 1.25rem; font-weight: 600; color: #012169; margin-bottom: 0.25rem; }}
  .som-subtitle {{ font-size: 0.875rem; color: #555; margin-bottom: 1.5rem; }}
  .som-venn {{ width: 500px; height: 300px; margin: 0 auto; }}
  .som-stats {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1.5rem; }}
  .dept-table {{ width: 100%; border-collapse: collapse; margin-top: 1.5rem; font-size: 0.8rem; }}
  .dept-table th {{ text-align: left; padding: 0.5rem 0.75rem; border-bottom: 2px solid #012169; color: #012169; font-weight: 600; }}
  .dept-table td {{ padding: 0.4rem 0.75rem; border-bottom: 1px solid #e0e0e0; }}
  .dept-table tr:hover {{ background: #f8f9fa; }}
  .dept-table .dept-name {{ font-weight: 500; }}
  .badge {{ display: inline-block; padding: 1px 6px; border-radius: 4px; font-size: 0.65rem; font-weight: 600; margin-left: 2px; }}
  .badge-b {{ background: #e8edf5; color: #012169; }}
  .badge-u {{ background: #fef3cd; color: #856404; }}
  .badge-n {{ background: #d1ecf1; color: #0c5460; }}
  .dept-bar {{ display: flex; height: 16px; border-radius: 4px; overflow: hidden; min-width: 60px; }}
  .dept-bar div {{ height: 100%; }}
  /* Funding hero callout */
  .funding-hero {{ background: #012169; color: #fff; border-radius: 16px; padding: 2rem 1.5rem; margin-bottom: 2rem; text-align: center; }}
  .funding-hero-number {{ font-size: 3.5rem; font-weight: 800; color: #f2a900; line-height: 1; }}
  .funding-hero-label {{ font-size: 1rem; color: rgba(255,255,255,0.9); margin-top: 0.25rem; }}
  .funding-hero-sublabel {{ font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 0.15rem; }}
  .funding-hero-divider {{ width: 60px; height: 2px; background: #f2a900; margin: 1.25rem auto; opacity: 0.5; }}
  .funding-hero-context {{ display: grid; grid-template-columns: 1fr auto 1fr; gap: 0; align-items: center; margin-top: 0; }}
  .funding-hero-stat {{ text-align: center; padding: 0 1.5rem; }}
  .funding-hero-stat .num {{ font-size: 2rem; font-weight: 700; color: #f2a900; }}
  .funding-hero-stat .lbl {{ font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.15rem; }}
  .funding-hero-sep {{ width: 1px; height: 48px; background: rgba(255,255,255,0.2); }}
  .funding-hero-bar {{ height: 24px; border-radius: 6px; overflow: hidden; display: flex; margin-top: 1.25rem; }}
  /* Funding tables */
  .funding-table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; font-size: 0.8rem; }}
  .funding-table th {{ text-align: left; padding: 0.5rem 0.75rem; border-bottom: 2px solid #012169; color: #012169; font-weight: 600; }}
  .funding-table td {{ padding: 0.4rem 0.75rem; border-bottom: 1px solid #e0e0e0; }}
  .funding-table tr:hover {{ background: #f8f9fa; }}
  .funding-bar {{ height: 14px; border-radius: 3px; display: inline-block; vertical-align: middle; }}
  /* Print / PDF page break control */
  @media print {{
    .chart-container, .stats, .total-bar {{ break-inside: avoid; }}
    .names-section {{ break-inside: avoid; }}
    .som-section {{ break-before: page; }}
    .funding-hero {{ break-inside: avoid; }}
    .som-venn {{ break-inside: avoid; }}
    .som-stats {{ break-inside: avoid; }}
    .funding-section {{ break-before: page; }}
  }}
</style>
</head>
<body>

<h1>OMOP Enterprise — Stakeholder Communities</h1>
<p class="subtitle">Notification list vs. tooling users &middot; {total} unique individuals</p>

<div class="chart-container">
  <svg viewBox="0 0 700 420">
    <circle class="circle-notification" cx="250" cy="210" r="180" />
    <circle class="circle-user" cx="450" cy="210" r="195" />

    <text class="label" x="165" y="170" style="fill: #012169;">NOTIFICATION</text>
    <text class="label" x="165" y="186" style="fill: #012169; font-size: 10px; font-weight: 400;">Community ({n_notif_community})</text>
    <text class="count count-notification" x="165" y="225">{n_notif}</text>
    <text class="count-label" x="165" y="255">only</text>

    <text class="count count-both" x="350" y="200">{n_both}</text>
    <text class="count-label" x="350" y="230">Both</text>

    <text class="label" x="535" y="170" style="fill: #b07800;">USER</text>
    <text class="label" x="535" y="186" style="fill: #b07800; font-size: 10px; font-weight: 400;">Community ({n_user_community})</text>
    <text class="count count-user" x="535" y="225">{n_user}</text>
    <text class="count-label" x="535" y="255">only</text>
  </svg>
</div>

<div class="stats">
  <div class="stat-card stat-notification">
    <div class="stat-number">{n_notif}</div>
    <div class="stat-label">Notification Only</div>
  </div>
  <div class="stat-card stat-both">
    <div class="stat-number">{n_both}</div>
    <div class="stat-label">Both Communities</div>
  </div>
  <div class="stat-card stat-user">
    <div class="stat-number">{n_user}</div>
    <div class="stat-label">User Only</div>
  </div>
</div>

<div class="total-bar">
  <div class="bar-label">Proportional breakdown of {total} unique stakeholders</div>
  <div class="bar-track">
    <div class="bar-seg notif" style="width: {pct(n_notif, total)}%;">{n_notif} ({round(pct(n_notif, total))}%)</div>
    <div class="bar-seg both" style="width: {pct(n_both, total)}%;">{n_both} ({round(pct(n_both, total))}%)</div>
    <div class="bar-seg user" style="width: {pct(n_user, total)}%;">{n_user} ({round(pct(n_user, total))}%)</div>
  </div>
</div>

<div class="names-section">
  <h2>Roster</h2>
  <div class="names-grid">
    <div class="names-col notif">
      <h3>Notification Only ({n_notif})</h3>
      <ul>
{name_list(notif_only)}
      </ul>
    </div>
    <div class="names-col overlap">
      <h3>Both ({n_both})</h3>
      <ul>
{name_list(both)}
      </ul>
    </div>
    <div class="names-col user">
      <h3>User Only ({n_user})</h3>
      <ul>
{name_list(user_only)}
      </ul>
    </div>
  </div>
</div>

<!-- ============ SOM SUBSECTION ============ -->
<div class="som-section">
  <h2>School of Medicine Breakdown</h2>

  <div class="funding-hero">
    <div class="funding-hero-number">{grand_total_fte:.1f} FTE</div>
    <div class="funding-hero-label">invested by {n_funding_sources} departments for OMOP infrastructure and associated projects</div>
    <div class="funding-hero-sublabel">SOM provides {som_fte:.1f} FTE ({som_funding_pct}%) &mdash; the rest comes from {n_funding_sources - 1} other sources</div>
    <div class="funding-hero-bar">{hero_bar_segs}</div>
    <div class="funding-hero-divider"></div>
    <div class="funding-hero-context">
      <div class="funding-hero-stat">
        <div class="num">{som_user_pct}%</div>
        <div class="lbl">of all users are from SOM</div>
      </div>
      <div class="funding-hero-sep"></div>
      <div class="funding-hero-stat">
        <div class="num">{som_dept_count}</div>
        <div class="lbl">SOM departments represented</div>
      </div>
    </div>
  </div>

  <div class="som-venn">
    <svg viewBox="0 0 500 280">
      <circle cx="180" cy="145" r="130" style="fill: rgba(1,33,105,0.18); stroke: #012169; stroke-width: 2;" />
      <circle cx="320" cy="145" r="125" style="fill: rgba(242,169,0,0.18); stroke: #f2a900; stroke-width: 2;" />

      <text class="label" x="115" y="110" style="fill: #012169; font-size: 12px;">NOTIFICATION</text>
      <text class="label" x="115" y="124" style="fill: #012169; font-size: 9px; font-weight: 400;">SOM ({som_notif_community})</text>
      <text class="count count-notification" x="115" y="160" style="font-size: 30px;">{som_notif}</text>
      <text class="count-label" x="115" y="182">only</text>

      <text class="count count-both" x="250" y="145" style="font-size: 30px;">{som_both}</text>
      <text class="count-label" x="250" y="167">Both</text>

      <text class="label" x="385" y="110" style="fill: #b07800; font-size: 12px;">USER</text>
      <text class="label" x="385" y="124" style="fill: #b07800; font-size: 9px; font-weight: 400;">SOM ({som_user_community})</text>
      <text class="count count-user" x="385" y="160" style="font-size: 30px;">{som_user}</text>
      <text class="count-label" x="385" y="182">only</text>
    </svg>
  </div>

  <div class="som-stats">
    <div class="stat-card stat-notification">
      <div class="stat-number">{som_notif}</div>
      <div class="stat-label">SOM Notification Only</div>
    </div>
    <div class="stat-card stat-both">
      <div class="stat-number">{som_both}</div>
      <div class="stat-label">SOM Both</div>
    </div>
    <div class="stat-card stat-user">
      <div class="stat-number">{som_user}</div>
      <div class="stat-label">SOM User Only</div>
    </div>
  </div>

  <div class="total-bar" style="width: 100%; margin-top: 1.5rem;">
    <div class="bar-label">SOM proportional breakdown ({som_total} people)</div>
    <div class="bar-track">
      <div class="bar-seg notif" style="width: {pct(som_notif, som_total)}%;">{som_notif} ({round(pct(som_notif, som_total))}%)</div>
      <div class="bar-seg both" style="width: {pct(som_both, som_total)}%;">{som_both} ({round(pct(som_both, som_total))}%)</div>
      <div class="bar-seg user" style="width: {pct(som_user, som_total)}%;">{som_user} ({round(pct(som_user, som_total))}%)</div>
    </div>
  </div>

  <!-- Department breakdown table -->
  <h3 style="font-size: 0.95rem; color: #012169; margin-top: 2rem; margin-bottom: 0.5rem;">By SOM Department</h3>
  <table class="dept-table">
    <thead>
      <tr>
        <th>Department</th>
        <th style="text-align: center;">Total</th>
        <th style="text-align: center;">Notif</th>
        <th style="text-align: center;">Both</th>
        <th style="text-align: center;">User</th>
        <th>People</th>
      </tr>
    </thead>
    <tbody>
{dept_table_rows()}
    </tbody>
  </table>
  <p style="font-size: 0.7rem; color: #888; margin-top: 0.5rem;">
    Badge colors: <span class="badge badge-n">Notification</span> <span class="badge badge-b">Both</span> <span class="badge badge-u">User</span>
  </p>

  <!-- Funding by source -->
  <div class="funding-section">
  <h3 style="font-size: 0.95rem; color: #012169; margin-top: 2rem; margin-bottom: 0.5rem;">Investment by Funding Source</h3>
  <table class="funding-table">
    <thead>
      <tr>
        <th>Source</th>
        <th style="text-align: center;">FTE</th>
        <th style="text-align: center;">Share</th>
        <th></th>
        <th>Staff</th>
      </tr>
    </thead>
    <tbody>
{funding_source_rows()}
    </tbody>
    <tfoot>
      <tr style="border-top: 2px solid #012169;">
        <td style="font-weight: 600;">Total</td>
        <td style="text-align: center; font-weight: 700;">{grand_total_fte:.2f}</td>
        <td style="text-align: center; font-weight: 600;">100%</td>
        <td></td>
        <td style="font-size: 0.7rem; color: #555;">{len(funded_staff)} staff across {n_funding_sources} sources</td>
      </tr>
    </tfoot>
  </table>

  <!-- Per-person detail -->
  <h3 style="font-size: 0.95rem; color: #012169; margin-top: 2rem; margin-bottom: 0.5rem;">Staff Funding Detail</h3>
  <table class="funding-table">
    <thead>
      <tr>
        <th>Staff Member</th>
        <th>Role</th>
        <th style="text-align: center;">OMOP %</th>
        <th>Funded By</th>
      </tr>
    </thead>
    <tbody>
{funding_staff_rows()}
    </tbody>
  </table>
  </div><!-- .funding-section -->
</div>

</body>
</html>
"""


# ── Main ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    people = load_people()
    html = render(people)
    HTML_PATH.write_text(html, encoding="utf-8")

    # Quick summary
    n = len([p for p in people if p["community"] == "Notification"])
    b = len([p for p in people if p["community"] == "Both"])
    u = len([p for p in people if p["community"] == "User"])
    funded = [p for p in people if p["funding"]]
    sources = defaultdict(float)
    for p in funded:
        for s, v in p["funding"]:
            sources[s] += v / 100
    total_fte = sum(sources.values())
    print(f"Wrote {HTML_PATH.name}  —  {n} notif / {b} both / {u} user  =  {n+b+u} total")
    print(f"Funding: {total_fte:.2f} FTE across {len(sources)} sources: "
          + ", ".join(f"{s} {v:.2f}" for s, v in sorted(sources.items(), key=lambda x: x[1], reverse=True)))
