# /// script
# dependencies = ["playwright"]
# ///
"""Export community_overlap.html to PDF and/or PNG images.

Usage:
    # First time only: install browser
    uv run scripts/export_community_report.py --install

    # Export full-page PDF
    uv run scripts/export_community_report.py --pdf

    # Export section PNGs
    uv run scripts/export_community_report.py --png

    # Both
    uv run scripts/export_community_report.py --pdf --png
"""

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).parent
DATA_DIR = HERE / "community_data"
HTML_PATH = DATA_DIR / "community_overlap.html"
PDF_PATH = DATA_DIR / "community_overlap.pdf"
PNG_DIR = DATA_DIR / "exports"

# Sections to capture as individual PNGs (CSS selector, filename)
SECTIONS = [
    ("body", "00_full_page.png"),
    (".chart-container", "01_venn_diagram.png"),
    (".stats", "02_stat_cards.png"),
    (".total-bar", "03_proportional_bar.png"),
    (".names-section", "04_roster.png"),
    (".funding-hero", "05_funding_hero.png"),
    (".som-venn", "06_som_venn.png"),
    (".som-stats", "07_som_stat_cards.png"),
]


def install_browser():
    import subprocess
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    print("Chromium installed.")


def export_pdf():
    from playwright.sync_api import sync_playwright

    if not HTML_PATH.exists():
        sys.exit(f"HTML not found: {HTML_PATH}\nRun generate_community_report.py first.")

    url = HTML_PATH.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 800, "height": 600})
        page.goto(url, wait_until="networkidle")
        page.pdf(path=str(PDF_PATH), format="Letter", print_background=True,
                 margin={"top": "0.5in", "bottom": "0.5in", "left": "0.4in", "right": "0.4in"})
        browser.close()

    print(f"PDF: {PDF_PATH}")


def export_pngs():
    from playwright.sync_api import sync_playwright

    if not HTML_PATH.exists():
        sys.exit(f"HTML not found: {HTML_PATH}\nRun generate_community_report.py first.")

    PNG_DIR.mkdir(exist_ok=True)
    url = HTML_PATH.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 800, "height": 600}, device_scale_factor=2)
        page.goto(url, wait_until="networkidle")

        for selector, filename in SECTIONS:
            out = PNG_DIR / filename
            try:
                el = page.query_selector(selector)
                if el:
                    el.screenshot(path=str(out))
                    print(f"PNG: {out}")
                else:
                    print(f"SKIP: {selector} not found")
            except Exception as e:
                print(f"SKIP: {selector} — {e}")

        # Also capture each funding table
        tables = page.query_selector_all(".funding-table")
        for i, table in enumerate(tables):
            out = PNG_DIR / f"08_funding_table_{i+1}.png"
            table.screenshot(path=str(out))
            print(f"PNG: {out}")

        browser.close()

    print(f"\nAll PNGs in: {PNG_DIR}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export community report to PDF/PNG")
    parser.add_argument("--install", action="store_true", help="Install Chromium browser")
    parser.add_argument("--pdf", action="store_true", help="Export full-page PDF")
    parser.add_argument("--png", action="store_true", help="Export section PNGs")
    args = parser.parse_args()

    if not (args.install or args.pdf or args.png):
        parser.print_help()
        sys.exit(1)

    if args.install:
        install_browser()
    if args.pdf:
        export_pdf()
    if args.png:
        export_pngs()
