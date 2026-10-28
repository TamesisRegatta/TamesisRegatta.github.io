// Mark key dates on the home page as past, on now, or next, by the visitor's
// clock. Each date is a <time> element from the when() macro (main.py), with
// data-from and data-until in UK time, so the table stays current without
// rebuilding the site. Rows must be in date order. The styles are screen-only
// (extra.css), so PDFs list every date plainly.
(function () {
  var now = Date.now();
  var next = null;
  document.querySelectorAll("time[data-until]").forEach(function (el) {
    var row = el.closest("tr");
    if (!row) return;
    if (Date.parse(el.dataset.until) <= now) {
      row.classList.add("tr-past");
    } else if (Date.parse(el.dataset.from) <= now) {
      row.classList.add("tr-now");
    } else if (!next) {
      next = row;
      row.classList.add("tr-next");
    }
  });
})();
