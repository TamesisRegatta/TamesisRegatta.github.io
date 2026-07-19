// Append a ¶ permalink to every anchored rule or risk (any paragraph, list
// item, or definition-list description with an explicit id), matching the
// permalinks Material adds to headings.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".md-content :is(p[id], li[id], dd[id])").forEach(function (el) {
    var link = document.createElement("a");
    link.href = "#" + el.id;
    link.className = "tr-rule-anchor";
    link.title = "Permanent link to this rule";
    link.textContent = "¶";
    el.appendChild(link);
  });
});
