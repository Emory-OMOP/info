(function () {
  "use strict";

  /* -----------------------------------------------------------
     Configuration — update these when deploying
     ----------------------------------------------------------- */
  var AGENT_URL = "http://localhost:8000";
  var PASSKEY = "changeme";
  var DEBUG = true; // TODO: set false before deploying

  var MODELS = [
    { provider: "claude",    model: "claude-haiku-4-5-20251001", label: "Haiku 4.5",           group: "Claude" },
    { provider: "claude",    model: "claude-sonnet-4-20250514",  label: "Sonnet 4",            group: "Claude" },
    { provider: "openai",    model: "gpt-4o-mini",               label: "GPT-4o Mini",         group: "OpenAI" },
    { provider: "openai",    model: "gpt-4o",                    label: "GPT-4o",              group: "OpenAI" },
    { provider: "gemini",    model: "gemini-2.0-flash",          label: "Gemini 2.0 Flash",    group: "Gemini" },
    { provider: "gemini",    model: "gemini-2.5-pro-preview-05-06", label: "Gemini 2.5 Pro",   group: "Gemini" },
    { provider: "deepseek",  model: "deepseek-chat",             label: "DeepSeek Chat",       group: "DeepSeek" },
    { provider: "deepseek",  model: "deepseek-reasoner",         label: "DeepSeek Reasoner",   group: "DeepSeek" },
  ];

  /* -----------------------------------------------------------
     State
     ----------------------------------------------------------- */
  var token = null;
  var sessionId = null;
  var streaming = false;
  var selectedModel = 0;
  var pickerOpen = false;
  var els = {};

  /* -----------------------------------------------------------
     Boot
     ----------------------------------------------------------- */
  function init() {
    els.container = document.getElementById("chat-container");
    if (!els.container) return; // not on homepage

    els.messages = document.getElementById("chat-messages");
    els.form = document.getElementById("chat-form");
    els.input = document.getElementById("chat-input");
    els.send = document.getElementById("chat-send");
    els.suggestions = document.getElementById("chat-suggestions");
    els.status = document.getElementById("chat-status");
    els.welcome = document.getElementById("chat-welcome");
    els.picker = document.getElementById("chat-picker");
    els.pickerTrigger = document.getElementById("chat-picker-trigger");
    els.pickerLabel = document.getElementById("chat-picker-label");
    els.pickerDropdown = document.getElementById("chat-picker-dropdown");

    buildPicker();
    els.form.addEventListener("submit", onSubmit);

    els.suggestions.querySelectorAll("button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        sendMessage(btn.dataset.prompt);
      });
    });

    authenticate();
  }

  /* -----------------------------------------------------------
     Auth
     ----------------------------------------------------------- */
  async function authenticate() {
    setStatus("connecting");
    try {
      var res = await fetch(AGENT_URL + "/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ passkey: PASSKEY }),
      });
      if (!res.ok) throw new Error("auth");
      var data = await res.json();
      token = data.token;
      setStatus("connected");
    } catch (_) {
      setStatus("offline");
    }
  }

  /* -----------------------------------------------------------
     Status management
     ----------------------------------------------------------- */
  function setStatus(s) {
    els.status.className = "mdx-chat__status mdx-chat__status--" + s;
    var active = s === "connected";
    els.input.disabled = !active;
    els.send.disabled = !active;
    els.pickerTrigger.disabled = !active;

    switch (s) {
      case "connecting":
        els.status.textContent = "Connecting to OHDSI Agent\u2026";
        break;
      case "connected":
        els.status.textContent = "";
        els.input.focus({ preventScroll: true });
        break;
      case "offline":
        els.status.textContent =
          "Agent offline \u2014 start the OHDSI Agent to chat with the data";
        break;
      case "streaming":
        els.status.textContent = "";
        els.input.disabled = true;
        els.send.disabled = true;
        els.pickerTrigger.disabled = true;
        closePicker();
        break;
    }
  }

  /* -----------------------------------------------------------
     Model picker (custom dropdown)
     ----------------------------------------------------------- */
  function buildPicker() {
    var drop = els.pickerDropdown;
    var lastGroup = null;

    MODELS.forEach(function (m, i) {
      if (m.group !== lastGroup) {
        var heading = document.createElement("div");
        heading.className = "mdx-chat__picker-group";
        heading.textContent = m.group;
        drop.appendChild(heading);
        lastGroup = m.group;
      }
      var chip = document.createElement("button");
      chip.type = "button";
      chip.className = "mdx-chat__picker-chip";
      chip.dataset.index = i;
      chip.textContent = m.label;
      if (i === 0) chip.classList.add("mdx-chat__picker-chip--active");
      chip.addEventListener("click", function () { selectModel(i); });
      drop.appendChild(chip);
    });

    els.pickerLabel.textContent = MODELS[0].label;

    els.pickerTrigger.addEventListener("click", function () {
      if (pickerOpen) closePicker(); else openPicker();
    });

    document.addEventListener("click", function (e) {
      if (pickerOpen && !els.picker.contains(e.target)) closePicker();
    });
  }

  function openPicker() {
    pickerOpen = true;
    els.picker.classList.add("mdx-chat__picker--open");
  }

  function closePicker() {
    pickerOpen = false;
    els.picker.classList.remove("mdx-chat__picker--open");
  }

  function selectModel(i) {
    var prev = selectedModel;
    selectedModel = i;
    els.pickerLabel.textContent = MODELS[i].label;
    els.pickerDropdown.querySelectorAll(".mdx-chat__picker-chip").forEach(function (c) {
      c.classList.toggle("mdx-chat__picker-chip--active", +c.dataset.index === i);
    });
    closePicker();

    if (prev !== i && sessionId) {
      sessionId = null;
      addSystemNotice("Model changed — context reset. Switching to " + MODELS[i].label);
    }
  }

  /* -----------------------------------------------------------
     Send
     ----------------------------------------------------------- */
  function onSubmit(e) {
    e.preventDefault();
    var msg = els.input.value.trim();
    if (!msg || streaming) return;

    if (DEBUG && msg.startsWith("/viz")) {
      els.input.value = "";
      debugViz(msg.slice(4).trim());
      return;
    }

    sendMessage(msg);
  }

  async function sendMessage(message) {
    if (streaming) return;
    streaming = true;
    setStatus("streaming");

    // Hide welcome + suggestions on first message
    if (els.welcome) {
      els.welcome.style.display = "none";
      els.welcome = null;
    }
    els.suggestions.style.display = "none";

    addMessage("user", message);
    els.input.value = "";

    var assistantEl = addMessage("assistant", "");
    var textAccum = "";

    try {
      var res = await fetch(AGENT_URL + "/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
        body: JSON.stringify({
          message: message,
          session_id: sessionId,
          provider: MODELS[selectedModel].provider,
          model: MODELS[selectedModel].model,
        }),
      });

      if (!res.ok) throw new Error(res.status);

      var reader = res.body.getReader();
      var decoder = new TextDecoder();
      var buffer = "";
      var currentEvent = null;

      while (true) {
        var chunk = await reader.read();
        if (chunk.done) break;

        buffer += decoder.decode(chunk.value, { stream: true });
        var lines = buffer.split("\n");
        buffer = lines.pop();

        for (var i = 0; i < lines.length; i++) {
          var line = lines[i];
          if (line.startsWith("event: ")) {
            currentEvent = line.slice(7);
          } else if (line.startsWith("data: ") && currentEvent) {
            handleEvent(currentEvent, JSON.parse(line.slice(6)), assistantEl);
            currentEvent = null;
          }
        }
      }
    } catch (_) {
      if (!textAccum) {
        assistantEl.querySelector(".mdx-chat__text").innerHTML =
          "<em>Could not reach the agent.</em>";
      }
    }

    streaming = false;
    setStatus("connected");

    /* -- inner helper to accumulate text -- */
    var afterTool = false;
    function handleEvent(evt, data, el) {
      switch (evt) {
        case "text":
          if (data.text) {
            if (afterTool && textAccum) {
              textAccum += "\n\n";
              afterTool = false;
            }
            textAccum += data.text;
            // Extract ```viz payloads, render text, then append charts
            var extracted = extractVizBlocks(textAccum);
            el.querySelector(".mdx-chat__text").innerHTML = renderMd(extracted.text);
            // Re-append any already-rendered chart canvases
            var chartBox = el.querySelector(".mdx-chat__charts");
            if (!chartBox && extracted.charts.length) {
              chartBox = document.createElement("div");
              chartBox.className = "mdx-chat__charts";
              el.appendChild(chartBox);
            }
            if (chartBox) {
              // Render new charts that haven't been rendered yet
              var existing = chartBox.querySelectorAll(".mdx-chat__chart").length;
              for (var ci = existing; ci < extracted.charts.length; ci++) {
                renderChartInto(chartBox, extracted.charts[ci]);
              }
            }
            scrollBottom();
          }
          break;
        case "tool_call":
          afterTool = true;
          addTool(el, data.name);
          scrollBottom();
          break;
        case "tool_result":
          afterTool = true;
          updateTool(el, data.name);
          break;
        case "session":
          sessionId = data.session_id;
          break;
        case "visualization":
          renderChart(el, data);
          scrollBottom();
          break;
        case "error":
          textAccum += "\n\n**Error:** " + data.error;
          el.querySelector(".mdx-chat__text").innerHTML = renderMd(textAccum);
          break;
      }
    }
  }

  /* -----------------------------------------------------------
     Viz-block extraction from streamed text
     ----------------------------------------------------------- */
  var msgCounter = 0;

  function extractVizBlocks(text) {
    var pattern = /```viz\s*\n?([\s\S]*?)```/g;
    var match;
    var cleaned = text;
    var charts = [];

    while ((match = pattern.exec(text)) !== null) {
      try {
        var payload = JSON.parse(match[1].trim());
        charts.push(payload);
        cleaned = cleaned.replace(match[0], "");
      } catch (_) {
        // Incomplete JSON while still streaming — leave in text
      }
    }

    return { text: cleaned.trim(), charts: charts };
  }

  /* -----------------------------------------------------------
     DOM helpers
     ----------------------------------------------------------- */
  function addMessage(role, content) {
    var el = document.createElement("div");
    el.id = "msg-" + (++msgCounter);
    el.className = "mdx-chat__msg mdx-chat__msg--" + role;

    var label = document.createElement("div");
    label.className = "mdx-chat__label";
    label.textContent = role === "user" ? "You" : "OHDSI Agent";

    var tools = document.createElement("div");
    tools.className = "mdx-chat__tools";

    var text = document.createElement("div");
    text.className = "mdx-chat__text";
    if (content) {
      text.innerHTML = role === "user" ? esc(content) : renderMd(content);
    }

    el.appendChild(label);
    el.appendChild(tools);
    el.appendChild(text);
    els.messages.appendChild(el);
    scrollBottom();
    return el;
  }

  function addSystemNotice(text) {
    var el = document.createElement("div");
    el.className = "mdx-chat__notice";
    el.textContent = text;
    els.messages.appendChild(el);
    scrollBottom();
  }

  function addTool(msgEl, name) {
    var pill = msgEl.querySelector('[data-tool="' + name + '"]');
    if (pill) {
      var total = (+pill.dataset.total || 1) + 1;
      pill.dataset.total = total;
      pill.dataset.pending = (+pill.dataset.pending || 1) + 1;
      refreshToolPill(pill);
    } else {
      pill = document.createElement("span");
      pill.className = "mdx-chat__tool mdx-chat__tool--running";
      pill.dataset.tool = name;
      pill.dataset.total = 1;
      pill.dataset.pending = 1;
      refreshToolPill(pill);
      msgEl.querySelector(".mdx-chat__tools").appendChild(pill);
    }
  }

  function updateTool(msgEl, name) {
    var pill = msgEl.querySelector('[data-tool="' + name + '"]');
    if (!pill) return;
    var pending = Math.max(0, (+pill.dataset.pending || 1) - 1);
    pill.dataset.pending = pending;
    if (pending === 0) {
      pill.className = "mdx-chat__tool mdx-chat__tool--done";
    }
    refreshToolPill(pill);
  }

  function refreshToolPill(pill) {
    var label = pill.dataset.tool.replace(/_/g, " ");
    var total = +pill.dataset.total || 1;
    pill.textContent = total > 1 ? label + " \u00d7" + total : label;
  }

  /* -----------------------------------------------------------
     Chart rendering (Chart.js)
     ----------------------------------------------------------- */
  var CHART_COLORS = [
    "hsla(213, 70%, 50%, .8)",
    "hsla(340, 70%, 50%, .8)",
    "hsla(160, 60%, 45%, .8)",
    "hsla(40,  80%, 50%, .8)",
    "hsla(270, 60%, 55%, .8)",
    "hsla(15,  75%, 55%, .8)",
    "hsla(190, 65%, 45%, .8)",
    "hsla(95,  55%, 45%, .8)",
  ];

  function renderChart(msgEl, data) {
    var container = msgEl.querySelector(".mdx-chat__charts");
    if (!container) {
      container = document.createElement("div");
      container.className = "mdx-chat__charts";
      msgEl.appendChild(container);
    }
    return renderChartInto(container, data);
  }

  function renderChartInto(container, data) {
    if (typeof Chart === "undefined") {
      console.warn("[viz] Chart.js not loaded — cannot render chart");
      return false;
    }

    var wrap = document.createElement("div");
    wrap.className = "mdx-chat__chart";
    var canvas = document.createElement("canvas");
    wrap.appendChild(canvas);
    container.appendChild(wrap);

    var type = data.type || "bar";
    var labels = data.labels || [];
    var values = data.values || [];
    var title = data.title || "";

    var isPie = type === "pie" || type === "doughnut";

    var chartData = {
      labels: labels,
      datasets: [{
        data: values,
        backgroundColor: isPie
          ? CHART_COLORS.slice(0, values.length)
          : CHART_COLORS[0],
        borderColor: isPie
          ? CHART_COLORS.slice(0, values.length).map(function (c) { return c.replace(".8)", "1)"); })
          : CHART_COLORS[0].replace(".8)", "1)"),
        borderWidth: isPie ? 2 : 1,
        borderRadius: isPie ? 0 : 3,
      }],
    };

    var options = {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display: isPie },
        title: {
          display: !!title,
          text: title,
          font: { size: 13, weight: "600" },
        },
      },
    };

    if (!isPie) {
      options.scales = {
        y: { beginAtZero: true, ticks: { font: { size: 11 } } },
        x: { ticks: { font: { size: 11 } } },
      };
    }

    new Chart(canvas, { type: type, data: chartData, options: options });
    return true;
  }

  function scrollBottom() {
    els.messages.scrollTop = els.messages.scrollHeight;
  }

  /* -----------------------------------------------------------
     Minimal Markdown → HTML
     ----------------------------------------------------------- */
  function esc(t) {
    var d = document.createElement("div");
    d.textContent = t;
    return d.innerHTML;
  }

  function renderMd(text) {
    var h = text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    // Code blocks
    h = h.replace(/```[\w]*\n?([\s\S]*?)```/g, "<pre><code>$1</code></pre>");
    // Inline code
    h = h.replace(/`([^`]+)`/g, "<code>$1</code>");
    // Bold
    h = h.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    // Newlines → <br> (CSS hides <br> inside <pre>)
    h = h.replace(/\n/g, "<br>");
    return h;
  }

  /* -----------------------------------------------------------
     Debug — /viz command and window.debugViz()
     ----------------------------------------------------------- */
  var DEBUG_SAMPLES = {
    bar: {
      type: "bar",
      title: "Top 5 Conditions by Patient Count",
      labels: ["Type 2 Diabetes", "Hypertension", "Heart Failure", "CKD", "COPD"],
      values: [12340, 9870, 6540, 4320, 3210],
    },
    line: {
      type: "line",
      title: "Monthly New Diagnoses (2025)",
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      values: [120, 145, 132, 168, 190, 175, 203, 215, 198, 220, 245, 230],
    },
    pie: {
      type: "pie",
      title: "Gender Distribution",
      labels: ["Female", "Male", "Unknown"],
      values: [54200, 45100, 700],
    },
    doughnut: {
      type: "doughnut",
      title: "Race Distribution",
      labels: ["White", "Black", "Asian", "Hispanic", "Other"],
      values: [38000, 32000, 12000, 10500, 7500],
    },
  };

  function debugViz(input) {
    if (!els.messages) return;

    // Hide welcome + suggestions
    if (els.welcome) {
      els.welcome.style.display = "none";
      els.welcome = null;
    }
    if (els.suggestions) els.suggestions.style.display = "none";

    // No args → show help
    if (!input) {
      addSystemNotice(
        '/viz bar | /viz line | /viz pie | /viz doughnut\n' +
        '/viz {"type":"bar","title":"...","labels":["A","B"],"values":[10,20]}'
      );
      return;
    }

    var payload;

    if (DEBUG_SAMPLES[input]) {
      payload = DEBUG_SAMPLES[input];
    } else {
      try {
        payload = JSON.parse(input);
      } catch (_) {
        addSystemNotice(
          'Invalid JSON. Format:\n' +
          '/viz {"type":"bar","title":"Title","labels":["A","B"],"values":[10,20]}'
        );
        return;
      }
    }

    addMessage("user", "/viz " + (payload.type || "bar"));
    var msgEl = addMessage("assistant", "");
    renderChart(msgEl, payload);
    scrollBottom();
  }

  if (DEBUG) {
    window.debugViz = function (data) {
      if (typeof data === "string") return debugViz(data);
      if (!els.messages) return;
      if (els.welcome) { els.welcome.style.display = "none"; els.welcome = null; }
      if (els.suggestions) els.suggestions.style.display = "none";
      addMessage("user", "/viz (console)");
      var msgEl = addMessage("assistant", "");
      renderChart(msgEl, data || DEBUG_SAMPLES.bar);
      scrollBottom();
    };
  }

  /* -----------------------------------------------------------
     Go
     ----------------------------------------------------------- */
  document.addEventListener("DOMContentLoaded", init);
})();
