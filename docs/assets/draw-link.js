// Open every link to the draw's short link (/draw/, see hooks/draw_redirect.py)
// in a new tab. Links written in Markdown set this themselves; this is for the
// nav's Draw entry, which MkDocs cannot give a target. Without JavaScript the
// nav entry still works, in the same tab.
document.querySelectorAll('a[href="/draw/"]').forEach((link) => {
  link.target = "_blank";
  link.rel = "noopener";
  link.title = "Opens the draw on Google Sheets, in a new tab";
});
