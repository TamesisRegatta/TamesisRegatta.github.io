# TamesisRegatta.github.io

Static website for Tamesis Regatta, containing the rules, event & safety plan,
and other documents. Built with [MkDocs](https://www.mkdocs.org/) and the
[Material](https://squidfunk.github.io/mkdocs-material/) theme, and deployed to
GitHub Pages at <https://tamesisregatta.github.io/> on every push to `main`.

## Layout

| Path | Purpose |
| :--- | :--- |
| `event.yml` | Key dates and named role holders, in one place. Pages refer to them as `{{ dates.entries_close }}`, `{{ roles.chief_marshal.name }}` etc. |
| `docs/` | The site content (Markdown). One file per page. |
| `mkdocs.yml` | Site configuration, navigation, theme, and plugins. |
| `main.py` | Macros for build-time contact details (see below). |
| `.github/workflows/deploy.yml` | Builds the site (including PDFs) and deploys it to GitHub Pages. |

## Editing

- **Change a date or role holder**: edit `event.yml` only. Every page and PDF
  picks it up on the next build. Each page also has an edit (pencil) button
  linking straight to its source on GitHub.
- **Dates are ISO 8601** (`2026-11-25`, times as `04:00:00`) and parsed into
  real date objects, so invalid dates fail the build. Every date is set
  explicitly in `event.yml`. Pages control rendering with filters:
  `{{ dates.regatta_start | ukdate }}` → "Wed 25 Nov 2026", `ukdatetime`
  (24-hour clock) → "Wed 11 Nov 2026, 04:00", and
  `{{ daterange(dates.regatta_start, dates.regatta_end) }}` →
  "Wed 25 – Sat 28 Nov 2026".
- **Rule anchors**: every rule has a permanent, *named* anchor so it can be
  linked to (e.g. `/rules/#bow-balls`) even if rules are renumbered. Add one by
  putting `{ #short-name }` on its own line directly beneath the rule text, at
  the same indentation. Treat published anchor names as permanent.
- **Changelog**: each document ends with a changelog table; add a row when
  making a meaningful change.

## Contact details

Personal phone numbers and email addresses are **never stored in this
repository**. Pages reference them as `{{ phone('fergus_cooper') }}` /
`{{ email('sydney_rose') }}`; at build time `main.py` reads the values from
`PHONE_*` / `EMAIL_*` environment variables, which CI populates from GitHub
Actions **repository secrets** (see the `env:` block in the deploy workflow
for the expected names). Values are rendered lightly obfuscated — encoded in
the HTML and decoded by JavaScript in the browser — so the plain numbers do
not appear in the page source for scrapers to harvest. Anyone can still read
and dial them normally.

If a secret is unset (including all local builds), the page shows
`[number withheld]` / `[email withheld]` instead.

The generic mailbox in `event.yml` (`contact.email`) is public by design and
rendered as a normal clickable link.

## Local preview

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve   # http://127.0.0.1:8000, rebuilds on save
```

## PDFs

Each page gets a "Download as PDF" button. PDFs are rendered headlessly with
Chromium via [mkdocs-exporter](https://adrienbrignon.github.io/mkdocs-exporter/).
Generation is skipped locally by default (it slows the edit loop); CI always
builds them. To build them locally:

```bash
.venv/bin/playwright install chromium
sudo .venv/bin/playwright install-deps chromium   # system libraries, once
PDF_EXPORT=true .venv/bin/mkdocs build
```
