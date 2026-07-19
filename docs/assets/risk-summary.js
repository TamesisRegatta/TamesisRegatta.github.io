// Under each "## Category" heading that's followed by one or more risks
// (i.e. has .risk-badge elements before the next heading), inject a strip of
// coloured squares — one per risk, linking to it — derived entirely from
// what's already rendered. No markdown changes are needed to keep this in
// sync: add a risk, and its square appears automatically.
document.addEventListener("DOMContentLoaded", function () {
  var container = document.querySelector(".md-content__inner");
  if (!container) return;

  container.querySelectorAll(":scope > h2[id]").forEach(function (heading) {
    var squares = [];
    var el = heading.nextElementSibling;

    while (el && el.tagName !== "H2") {
      el.querySelectorAll(".risk-badge").forEach(function (badge) {
        var dl = badge.closest("dl");
        var anchor = dl && dl.querySelector("dd[id]");
        if (!anchor) return;

        var level = Array.from(badge.classList).find(function (c) {
          return c.indexOf("risk-") === 0 && c !== "risk-badge";
        });
        if (!level) return;

        squares.push({
          id: anchor.id,
          level: level,
          label: anchor.textContent.trim() + " — " + badge.textContent.trim(),
        });
      });
      el = el.nextElementSibling;
    }

    if (squares.length === 0) return;

    var summary = document.createElement("div");
    summary.className = "risk-summary";

    squares.forEach(function (s) {
      var link = document.createElement("a");
      link.href = "#" + s.id;
      link.className = "risk-summary-square " + s.level;
      link.title = s.label;
      link.setAttribute("aria-label", s.label);
      summary.appendChild(link);
    });

    heading.insertAdjacentElement("afterend", summary);
  });
});
