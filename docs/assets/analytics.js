// The analytics page's embedded Plausible dashboard, drawn in the site's
// light or dark mode: Material marks the body with data-md-color-scheme
// ("default" or "slate"), and changes it when the visitor switches mode.
// A transparent background lets the page's own colour show around the
// dashboard's panels, which keep Plausible's colours for the mode.
const frame = document.querySelector("iframe.tr-analytics");
if (frame) {
  const show = () => {
    const theme = document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "light";
    const src = `${frame.dataset.src}&embed=true&theme=${theme}&background=transparent`;
    if (frame.src !== src) frame.src = src;
  };
  show();
  new MutationObserver(show).observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
}
