// Decode obfuscated contact details (see main.py). Values are stored
// reversed and base64-encoded in data-c so that plain phone numbers and
// email addresses never appear in the page source.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("span.tr-contact[data-c]").forEach(function (el) {
    el.textContent = atob(el.dataset.c).split("").reverse().join("");
  });
});
