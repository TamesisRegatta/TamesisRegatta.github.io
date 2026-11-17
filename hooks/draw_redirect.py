"""Serve /draw/ as a short link to the draw.

The draw is a Google Sheet published to the web, whose URL is long and
unreadable. Once draw_url in event.yml is set, this writes site/draw/index.html,
a page that sends the browser straight on to it, so the site, the briefing
slides and anything printed can give tamesisregatta.org/draw instead. If the
draw moves to another sheet, changing draw_url keeps every copy of the short
link working.

The page loads nothing itself (no scripts, styles or images, and nothing from
Google): the visitor's browser only goes on to Google as if they had clicked
a link, so the site still sets no cookies (see "Privacy" in the README).
While draw_url is empty, nothing is written, so /draw/ does not exist.
"""
import html
from pathlib import Path
from urllib.parse import urlparse

import yaml

EVENT = Path(__file__).parent.parent / "event.yml"

PAGE = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
<title>Tamesis Regatta draw</title>
</head>
<body>
<p>Taking you to the Tamesis Regatta draw, on Google Sheets. If nothing happens, <a href="{url}">open the draw</a>.</p>
</body>
</html>
"""


def on_post_build(config, **kwargs):
    url = (yaml.safe_load(EVENT.read_text(encoding="utf-8")) or {}).get("draw_url") or ""
    url = url.strip()
    if not url:
        return
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError(f"event.yml: draw_url must be a full https:// URL, not {url!r}")
    out = Path(config["site_dir"]) / "draw" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PAGE.format(url=html.escape(url, quote=True)), encoding="utf-8")
