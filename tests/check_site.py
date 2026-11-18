"""Check the built site for accessibility and privacy problems, and its PDFs
for accessibility. Run after `mkdocs build` (CI runs it on every pull request
and push; see "Automated checks" in the README):

    python tests/check_site.py site briefings/node_modules/axe-core/axe.min.js

The site is served from the build directory as https://tamesisregatta.org
inside headless Chromium: nothing is uploaded, no server is started, and
Plausible's event requests are answered here, so nothing is counted.

Accessibility (WCAG 2.2 AA; see docs/accessibility.md):
  - axe-core's WCAG 2.0, 2.1 and 2.2 level A and AA rules and its best
    practices, on every page in light and dark mode, and with the course
    map's courses and a marker's details, the risk assessment's controls,
    search, and the phone menu open;
  - reflow: at 320 px wide nothing scrolls sideways and no text is cut off;
  - text spacing: with wider letter, word, line and paragraph spacing, the
    same;
  - reduced motion: nothing animates when less motion is asked for;
  - the keyboard: everything that takes focus can be seen, and shows it.
Privacy (see docs/privacy.md): no cookies, nothing in browser storage but the
light or dark mode, and no requests to sites other than this one and the
Plausible server.
PDFs: each document's PDF is tagged, with its language and bookmarks (the
course map's PDF is pictures, so is left out). Skipped if the build has no
PDFs (PDF_EXPORT unset).

The briefing decks under /briefings/ are not checked yet; the accessibility
statement says so.

Exits non-zero if anything fails, listing each problem with its page.
"""

import sys
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

SITE, AXE = Path(sys.argv[1]), Path(sys.argv[2])
ORIGIN = "https://tamesisregatta.org"
PLAUSIBLE = "plausible-oxrse.fly.dev"
ALLOWED_HOSTS = {urlparse(ORIGIN).netloc, PLAUSIBLE}
# Material keeps the light or dark mode here (its key starts with the base path).
ALLOWED_STORAGE = {"/.__palette"}
AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice"]
# Not pages: the draw's short link (a redirect to Google Sheets), and the
# theme's assets. The briefing decks, in folders under briefings/, are skipped
# too (not checked yet), though the Briefings page that lists them is checked.
SKIP = ("draw/", "assets/", "search/")
# Controls that show focus on something other than themselves: the light or
# dark mode switch is a hidden input whose label is ringed, and the search box
# is ringed round its form (extra.css).
FOCUS_ELSEWHERE = {"input.md-option", "input.md-search__input"}

failures = []


def fail(where, problem):
    failures.append(f"{where}: {problem}")


def pages():
    """Every page of the built site, as a path, and a missing one for 404."""
    found = []
    for index in sorted(SITE.rglob("index.html")):
        folder = index.parent.relative_to(SITE).as_posix()
        path = "/" if folder == "." else f"/{folder}/"
        deck = folder.startswith("briefings/")
        if not deck and not path.lstrip("/").startswith(SKIP):
            found.append(path)
    return found + ["/no-such-page/"]


def serve(route):
    path = urlparse(route.request.url).path
    file = SITE / path.lstrip("/")
    if path.endswith("/"):
        file = file / "index.html"
    if file.is_file():
        route.fulfill(path=str(file))
    else:
        route.fulfill(status=404, path=str(SITE / "404.html"))


def context(browser, hosts, **kwargs):
    ctx = browser.new_context(**kwargs)
    ctx.route(f"{ORIGIN}/**", serve)
    ctx.route(f"https://{PLAUSIBLE}/api/event", lambda route: route.fulfill(status=202, body="ok"))
    ctx.on("request", lambda request: hosts.add(urlparse(request.url).netloc))
    return ctx


def axe(page, where):
    page.add_script_tag(path=str(AXE))
    violations = page.evaluate(
        """tags => axe.run(document, { runOnly: { type: 'tag', values: tags }, iframes: false })
             .then(r => r.violations.map(v => ({ id: v.id, help: v.help,
               targets: v.nodes.map(n => n.target.join(' ')) })))""",
        AXE_TAGS,
    )
    for v in violations:
        sample = ", ".join(v["targets"][:3]) + (f" and {len(v['targets']) - 3} more" if len(v["targets"]) > 3 else "")
        fail(where, f"axe {v['id']}: {v['help']} ({sample})")


def privacy(page, ctx, where):
    cookies = [c["name"] + "@" + c["domain"] for c in ctx.cookies()]
    if cookies:
        fail(where, f"sets cookies: {cookies}")
    keys = set(page.evaluate("Object.keys(localStorage).concat(Object.keys(sessionStorage))"))
    if keys - ALLOWED_STORAGE:
        fail(where, f"stores in the browser: {sorted(keys - ALLOWED_STORAGE)}")


SIDEWAYS = "() => document.documentElement.scrollWidth > window.innerWidth"

CLIPPED = """() => [...document.querySelectorAll('body *')].filter(e => {
  if (e.clientWidth <= 1 || !e.textContent.trim() || e.getClientRects().length === 0) return false;
  if (e.closest('.md-sidebar, .md-search, [hidden]')) return false;
  const s = getComputedStyle(e), hides = o => o === 'hidden' || o === 'clip';
  return (hides(s.overflowX) && e.scrollWidth > e.clientWidth + 1)
      || (hides(s.overflowY) && e.scrollHeight > e.clientHeight + 1);
}).map(e => e.tagName.toLowerCase() + ': ' + e.textContent.trim().slice(0, 40))"""

SPACING = """* { line-height: 1.5 !important; letter-spacing: 0.12em !important; word-spacing: 0.16em !important; }
p { margin-bottom: 2em !important; }"""

FOCUSED = """() => {
  const e = document.activeElement;
  if (!e || e === document.body) return null;
  const s = getComputedStyle(e), r = e.getBoundingClientRect();
  return {
    id: e.tagName.toLowerCase() + '.' + String(e.className).split(' ')[0],
    name: (e.getAttribute('aria-label') || e.innerText || e.title || '').trim().replace(/\\s+/g, ' ').slice(0, 40),
    ring: (s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0) || (s.boxShadow && s.boxShadow !== 'none'),
    seen: r.width > 0 && r.height > 0 && s.visibility !== 'hidden',
  };
}"""


def check_pages(browser, paths):
    hosts = set()
    for scheme in ["light", "dark"]:
        ctx = context(browser, hosts, viewport={"width": 1400, "height": 900}, color_scheme=scheme)
        page = ctx.new_page()
        for path in paths:
            page.goto(ORIGIN + path, wait_until="networkidle")
            axe(page, f"{path} ({scheme})")
            privacy(page, ctx, path)

        if "/map/" in paths:
            page.goto(ORIGIN + "/map/", wait_until="networkidle")
            radios = page.locator(".tamesis-map-group input[type=radio]")
            for i in range(radios.count()):
                radios.nth(i).check()
                page.wait_for_timeout(300)
                axe(page, f"/map/ ({scheme}, course {radios.nth(i).get_attribute('value')})")
            page.locator("[data-select]").first.focus()
            page.keyboard.press("Enter")
            page.wait_for_timeout(400)
            axe(page, f"/map/ ({scheme}, a marker's details open)")

        if "/risk-assessment/" in paths:
            page.goto(ORIGIN + "/risk-assessment/", wait_until="networkidle")
            page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
            axe(page, f"/risk-assessment/ ({scheme}, controls open)")

        page.goto(ORIGIN + "/", wait_until="networkidle")
        page.click(".md-search__input")
        page.keyboard.type("draw")
        page.wait_for_timeout(1200)
        axe(page, f"/ ({scheme}, search open)")
        ctx.close()

        ctx = context(browser, hosts, viewport={"width": 390, "height": 844}, color_scheme=scheme)
        page = ctx.new_page()
        page.goto(ORIGIN + "/", wait_until="networkidle")
        page.click("label.md-header__button[for='__drawer']")
        page.wait_for_timeout(400)
        axe(page, f"/ ({scheme}, phone menu open)")
        ctx.close()

    # Reflow, at 320 px.
    ctx = context(browser, hosts, viewport={"width": 320, "height": 640})
    page = ctx.new_page()
    for path in paths:
        page.goto(ORIGIN + path, wait_until="networkidle")
        if page.evaluate(SIDEWAYS):
            fail(path, "scrolls sideways at 320 px wide (WCAG 1.4.10)")
        for clipped in page.evaluate(CLIPPED):
            fail(path, f"text cut off at 320 px wide (WCAG 1.4.10): {clipped}")
    ctx.close()

    # Reduced motion, text spacing, and the keyboard, page by page.
    ctx = context(browser, hosts, viewport={"width": 1400, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    for path in paths:
        page.goto(ORIGIN + path, wait_until="networkidle")
        animations = page.evaluate("document.getAnimations().length")
        if animations:
            fail(path, f"{animations} animation(s) running when less motion is asked for (WCAG 2.3.3)")
        page.add_style_tag(content=SPACING)
        page.wait_for_timeout(200)
        if page.evaluate(SIDEWAYS):
            fail(path, "scrolls sideways with wider text spacing (WCAG 1.4.12)")
        for clipped in page.evaluate(CLIPPED):
            fail(path, f"text cut off with wider text spacing (WCAG 1.4.12): {clipped}")

        # The keyboard: Tab through the page until focus comes round again.
        page.goto(ORIGIN + path, wait_until="networkidle")
        seen = set()
        for _ in range(80):
            page.keyboard.press("Tab")
            f = page.evaluate(FOCUSED)
            if not f:
                continue
            key = (f["id"], f["name"])
            if key in seen:
                break
            seen.add(key)
            if f["id"] in FOCUS_ELSEWHERE:
                continue
            if not f["seen"]:
                fail(path, f"keyboard focus goes to something that cannot be seen (WCAG 2.4.7): {f['id']} '{f['name']}'")
            # Focus in a frame (the analytics dashboard) is on another site's
            # controls inside it, which show it in their own way.
            elif not f["ring"] and not f["id"].startswith("iframe."):
                fail(path, f"keyboard focus not shown (WCAG 2.4.7): {f['id']} '{f['name']}'")
    ctx.close()

    for host in sorted(hosts - ALLOWED_HOSTS):
        fail("site", f"loads from another site: {host}")


def check_pdfs():
    pdfs = [p for p in sorted(SITE.rglob("*.pdf"))
            if not str(p.relative_to(SITE)).startswith(("assets/", "briefings/", "map/"))]
    if not pdfs:
        print("No PDFs in the build (PDF_EXPORT unset), so they were not checked.")
        return
    for pdf in pdfs:
        reader = PdfReader(pdf)
        root = reader.trailer["/Root"]
        where = str(pdf.relative_to(SITE))
        if "/StructTreeRoot" not in root:
            fail(where, "is not tagged")
        if "/Lang" not in root:
            fail(where, "has no language")
        # An empty /Outlines entry counts for nothing: it needs bookmarks in it.
        if not reader.outline:
            fail(where, "has no bookmarks")
    print(f"Checked {len(pdfs)} PDFs.")


paths = pages()
print(f"Checking {len(paths)} pages: {', '.join(paths)}")
with sync_playwright() as p:
    browser = p.chromium.launch()
    check_pages(browser, paths)
    browser.close()
check_pdfs()

if failures:
    print(f"\n{len(failures)} problem(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("No problems found.")
