# Vocabulary Mapping Coverage

<link rel="stylesheet" href="../../../assets/stylesheets/coverage-dashboard.css">

<p id="cvb-load-error" style="display:none;color:red">
  Failed to load coverage data. Check that <code>coverage-data.json</code> is present.
</p>

<div class="cvb-dashboard" markdown>

<!-- Summary cards -->
<div class="cvb-summary-row">
  <div class="cvb-summary-card">
    <div class="cvb-summary-value" id="cvb-total-vocabs">—</div>
    <div class="cvb-summary-label">Vocabularies</div>
  </div>
  <div class="cvb-summary-card">
    <div class="cvb-summary-value" id="cvb-total-rows">—</div>
    <div class="cvb-summary-label">Source Concepts</div>
  </div>
  <div class="cvb-summary-card">
    <div class="cvb-summary-value" id="cvb-total-mapped">—</div>
    <div class="cvb-summary-label">Mapped</div>
  </div>
  <div class="cvb-summary-card">
    <div class="cvb-summary-value cvb-summary-value--highlight" id="cvb-overall-coverage">—</div>
    <div class="cvb-summary-label">Overall Coverage</div>
  </div>
</div>

<!-- Charts row -->
<div class="cvb-charts-row">
  <div class="cvb-chart-container">
    <canvas id="cvb-chart-coverage"></canvas>
  </div>
  <div class="cvb-chart-container cvb-chart-container--small">
    <canvas id="cvb-chart-donut"></canvas>
  </div>
</div>

<!-- Predicate chart -->
<div class="cvb-chart-container cvb-chart-container--wide">
  <canvas id="cvb-chart-predicates"></canvas>
</div>

## Vocabulary Details

<div id="cvb-vocab-details">
  <p style="color:var(--md-default-fg-color--light)">Loading…</p>
</div>

---

<small>
  Data generated on <span id="cvb-generated">—</span> from the
  <a href="https://github.com/Emory-OMOP/CVB">CVB repository</a>.
  Coverage is computed by <code>mapping-coverage.py</code>.
</small>

</div>

<!-- Chart.js CDN + dashboard script (page-scoped, not loaded globally) -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script src="../../../assets/javascripts/coverage-dashboard.js"></script>
