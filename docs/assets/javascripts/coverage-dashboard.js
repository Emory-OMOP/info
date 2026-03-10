/**
 * CVB Mapping Coverage Dashboard — Chart.js visualizations.
 *
 * Expects a global `CVB_COVERAGE_DATA` object set before this script loads,
 * OR fetches coverage-data.json from the same directory as the page.
 */
(function () {
  "use strict";

  /* ── colour palette (Emory Navy + complements) ── */
  const COLORS = [
    "hsla(226, 97%, 21%, .85)",  // Emory Navy
    "hsla(213, 70%, 50%, .85)",  // Steel blue
    "hsla(160, 55%, 45%, .85)",  // Teal
    "hsla(36,  85%, 55%, .85)",  // Gold
    "hsla(0,   65%, 55%, .85)",  // Coral
    "hsla(280, 50%, 55%, .85)",  // Purple
    "hsla(100, 45%, 50%, .85)",  // Green
    "hsla(190, 60%, 50%, .85)",  // Cyan
  ];

  const COLORS_LIGHT = COLORS.map(c => c.replace(/[\d.]+\)$/, ".25)"));

  /* ── helpers ── */
  function pct(n, d) { return d ? Math.round(n / d * 1000) / 10 : 0; }
  function fmt(n) { return n.toLocaleString(); }

  function el(id) { return document.getElementById(id); }

  function createChart(canvasId, config) {
    var canvas = el(canvasId);
    if (!canvas) return null;
    return new Chart(canvas.getContext("2d"), config);
  }

  /* ── summary cards ── */
  function renderSummary(data) {
    var s = data.summary;
    setText("cvb-total-vocabs", s.total_vocabs);
    setText("cvb-total-rows", fmt(s.total_rows));
    setText("cvb-total-mapped", fmt(s.total_mapped));
    setText("cvb-overall-coverage", s.overall_coverage + "%");
    setText("cvb-generated", data.generated);
  }

  function setText(id, value) {
    var node = el(id);
    if (node) node.textContent = value;
  }

  /* ── chart 1: per-vocab coverage bar ── */
  function renderCoverageChart(data) {
    var labels = data.vocabs.map(function (v) { return v.name; });
    var mapped = data.vocabs.map(function (v) { return v.totals.mapped; });
    var unmapped = data.vocabs.map(function (v) { return v.totals.unmapped; });

    createChart("cvb-chart-coverage", {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Mapped",
            data: mapped,
            backgroundColor: COLORS[2],
          },
          {
            label: "Unmapped",
            data: unmapped,
            backgroundColor: COLORS[4],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: { display: true, text: "Mapping Coverage by Vocabulary", font: { size: 14 } },
          legend: { position: "bottom" },
          tooltip: {
            callbacks: {
              afterBody: function (ctx) {
                var i = ctx[0].dataIndex;
                var v = data.vocabs[i].totals;
                return "Coverage: " + v.coverage + "%";
              },
            },
          },
        },
        scales: {
          x: { stacked: true },
          y: { stacked: true, title: { display: true, text: "Source Concepts" } },
        },
      },
    });
  }

  /* ── chart 2: coverage donut ── */
  function renderDonutChart(data) {
    var s = data.summary;
    createChart("cvb-chart-donut", {
      type: "doughnut",
      data: {
        labels: ["Mapped", "Unmapped"],
        datasets: [{
          data: [s.total_mapped, s.total_unmapped],
          backgroundColor: [COLORS[2], COLORS[4]],
          borderWidth: 2,
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: { display: true, text: "Overall Coverage", font: { size: 14 } },
          legend: { position: "bottom" },
        },
      },
    });
  }

  /* ── chart 3: predicate distribution stacked bar ── */
  function renderPredicateChart(data) {
    // Collect all unique predicates across all files
    var predSet = {};
    data.vocabs.forEach(function (v) {
      v.files.forEach(function (f) {
        Object.keys(f.predicates).forEach(function (p) {
          if (p) predSet[p] = true;
        });
      });
    });
    var predicates = Object.keys(predSet).sort();

    var labels = data.vocabs.map(function (v) { return v.name; });
    var datasets = predicates.map(function (pred, i) {
      return {
        label: pred,
        data: data.vocabs.map(function (v) {
          var count = 0;
          v.files.forEach(function (f) { count += f.predicates[pred] || 0; });
          return count;
        }),
        backgroundColor: COLORS[i % COLORS.length],
      };
    });

    createChart("cvb-chart-predicates", {
      type: "bar",
      data: { labels: labels, datasets: datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: { display: true, text: "Predicate Distribution by Vocabulary", font: { size: 14 } },
          legend: { position: "bottom" },
        },
        scales: {
          x: { stacked: true },
          y: { stacked: true, title: { display: true, text: "Mappings" } },
        },
      },
    });
  }

  /* ── table: top unmapped items ── */
  function renderUnmappedTable(data) {
    var tbody = el("cvb-unmapped-tbody");
    if (!tbody) return;

    var rows = [];
    data.vocabs.forEach(function (v) {
      v.files.forEach(function (f) {
        if (f.top_unmapped && f.top_unmapped.length) {
          f.top_unmapped.forEach(function (item) {
            rows.push({
              vocab: v.name,
              code: item.code,
              description: item.description,
              frequency: item.frequency,
              status: item.status,
            });
          });
        }
      });
    });

    rows.sort(function (a, b) { return b.frequency - a.frequency; });
    rows = rows.slice(0, 25);

    if (rows.length === 0) {
      tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;color:var(--md-default-fg-color--light)">No frequency data available for unmapped items</td></tr>';
      return;
    }

    tbody.innerHTML = rows.map(function (r) {
      return "<tr>"
        + "<td>" + r.vocab + "</td>"
        + "<td><code>" + r.code + "</code></td>"
        + "<td>" + r.description + "</td>"
        + "<td style='text-align:right'>" + fmt(r.frequency) + "</td>"
        + "<td>" + r.status + "</td>"
        + "</tr>";
    }).join("");
  }

  /* ── vocab detail cards ── */
  function renderVocabDetails(data) {
    var container = el("cvb-vocab-details");
    if (!container) return;

    var html = data.vocabs.map(function (v) {
      var t = v.totals;
      var coverageClass = t.coverage >= 90 ? "cvb-badge--green"
        : t.coverage >= 50 ? "cvb-badge--gold"
        : "cvb-badge--red";

      var filesHtml = v.files.map(function (f) {
        var mc = f.metadata_completeness;
        var toolPct = pct(mc.mapping_tool.count, mc.mapping_tool.total);
        var mapperPct = pct(mc.mapper.count, mc.mapper.total);
        var reviewerPct = pct(mc.reviewer.count, mc.reviewer.total);

        return '<div class="cvb-file">'
          + '<strong>' + f.filename + '</strong>'
          + ' <span class="cvb-file-date">modified ' + f.last_modified + '</span>'
          + '<div class="cvb-file-stats">'
          + fmt(f.total) + ' rows &middot; '
          + fmt(f.mapped) + ' mapped &middot; '
          + f.coverage + '% coverage'
          + '</div>'
          + '<div class="cvb-file-meta">'
          + 'Tool: ' + toolPct + '% &middot; '
          + 'Mapper: ' + mapperPct + '% &middot; '
          + 'Reviewer: ' + reviewerPct + '%'
          + '</div>'
          + '</div>';
      }).join("");

      return '<div class="cvb-vocab-card">'
        + '<div class="cvb-vocab-header">'
        + '<h3>' + v.name + '</h3>'
        + '<span class="cvb-badge ' + coverageClass + '">' + t.coverage + '%</span>'
        + '</div>'
        + '<div class="cvb-vocab-summary">'
        + fmt(t.total) + ' concepts &middot; '
        + fmt(t.mapped) + ' mapped &middot; '
        + fmt(t.unmapped) + ' unmapped'
        + '</div>'
        + filesHtml
        + '</div>';
    }).join("");

    container.innerHTML = html;
  }

  /* ── source mapping links ── */
  function renderSourceMappings(data) {
    var container = el("cvb-source-mappings");
    if (!container) return;

    var links = [];
    data.vocabs.forEach(function (v) {
      if (v.source_mappings && v.source_mappings.length) {
        v.source_mappings.forEach(function (sm) {
          links.push({
            vocab: v.name,
            file: sm.file,
            url: sm.url,
          });
        });
      }
    });

    if (links.length === 0) {
      container.innerHTML = '<p style="color:var(--md-default-fg-color--light)">No source mappings available</p>';
      return;
    }

    var html = '<div class="admonition info">'
      + '<p class="admonition-title">Authorized access required</p>'
      + '<p>Source mapping files are maintained in the CVB repository and are only accessible to qualified Emory OMOP team members. '
      + 'Contact the Enterprise OMOP team on the <strong>OMOP Enterprise</strong> Teams channel to request access.</p>'
      + '<ul>';

    links.forEach(function (l) {
      html += '<li><a href="' + l.url + '">' + l.vocab + ' / ' + l.file + '</a></li>';
    });

    html += '</ul></div>';
    container.innerHTML = html;
  }

  /* ── main ── */
  function init(data) {
    renderSummary(data);
    renderCoverageChart(data);
    renderDonutChart(data);
    renderPredicateChart(data);
    renderUnmappedTable(data);
    renderVocabDetails(data);
    renderSourceMappings(data);
  }

  // Load data: prefer inline global, fall back to fetch
  if (window.CVB_COVERAGE_DATA) {
    init(window.CVB_COVERAGE_DATA);
  } else {
    fetch("coverage-data.json")
      .then(function (r) { return r.json(); })
      .then(init)
      .catch(function (err) {
        console.error("Failed to load coverage data:", err);
        var msg = el("cvb-load-error");
        if (msg) msg.style.display = "block";
      });
  }
})();
