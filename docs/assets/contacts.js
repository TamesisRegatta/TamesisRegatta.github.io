// Decode obfuscated contact details (see main.py). Values are stored
// reversed and base64-encoded in data-c so that plain phone numbers and
// email addresses never appear in the page source.
//
// Decoding runs as soon as this script loads, not on DOMContentLoaded: the
// PDF export (mkdocs-exporter's Paged.js) copies the page into its layout
// when parsing finishes, before DOMContentLoaded listeners run, so details
// decoded later never reach the PDF. Material loads extra_javascript at the
// end of the page, so every contact is already in the DOM here; the
// DOMContentLoaded call is a fallback, and each value is decoded only once.
(function () {
  function decode() {
    document.querySelectorAll("span.tr-contact[data-c]").forEach(function (el) {
      el.textContent = atob(el.dataset.c).split("").reverse().join("");
      el.removeAttribute("data-c");
    });
  }

  decode();
  document.addEventListener("DOMContentLoaded", decode);
})();
