// Open every link to the draw's short link (/draw/, see hooks/draw_redirect.py)
// in a new tab, and have Plausible count clicks on it as a "Draw" event (the
// class names the event). Links written in Markdown set both themselves; this
// is for the nav's Draw entry, which MkDocs cannot give a target or class.
// Without JavaScript the nav entry still works, in the same tab.
document.querySelectorAll('a[href="/draw/"]').forEach((link) => {
  link.target = "_blank";
  link.rel = "noopener";
  link.title = "Opens the draw on Google Sheets, in a new tab";
  link.classList.add("plausible-event-name--Draw");
});
