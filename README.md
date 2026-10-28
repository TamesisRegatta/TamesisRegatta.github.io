# TamesisRegatta.github.io

Static website for Tamesis Regatta, containing the rules, event & safety plan,
risk assessment, and other documents. Built with
[MkDocs](https://www.mkdocs.org/) and the
[Material](https://squidfunk.github.io/mkdocs-material/) theme, and deployed
to GitHub Pages at <https://tamesisregatta.org/> on every push to
`main`.

## Layout

| Path | Purpose |
| :--- | :--- |
| `event.yml` | Key dates and named role holders, in one place. Pages refer to them as `{{ dates.entries_close }}`, `{{ roles.chief_marshal.name }}` etc. |
| `risk_matrix.yml` | The official severity × probability risk matrix (labels, level lookup, definitions). See [Risk assessment](#risk-assessment). |
| `docs/` | The site content (Markdown), one file per page, plus `assets/` for CSS/JS/images. |
| `mkdocs.yml` | Site configuration, navigation, theme, and plugins. |
| `main.py` | Macros used by pages: dates, contact details, risk badges (see below). |
| `.github/workflows/deploy.yml` | Builds the site (including PDFs) and deploys it to GitHub Pages. |

## Editing

- **Change a date or role holder**: edit `event.yml` only. Every page and PDF
  picks it up on the next build. Each page also has an edit (pencil) button
  linking straight to its source on GitHub.
- **Dates are ISO 8601** (`2026-11-25`, times as `04:00:00`) and parsed into
  real date objects, so invalid dates fail the build. Every date is set
  explicitly in `event.yml`; nothing is calculated relative to another date.
  Pages control rendering with filters: `{{ dates.regatta_start | ukdate }}`
  → "Wed 25 Nov 2026", `ukdatetime` (24-hour clock) → "Wed 11 Nov 2026,
  04:00", and `{{ daterange(dates.regatta_start, dates.regatta_end) }}` →
  "Wed 25 – Sat 28 Nov 2026".
- **Permanent anchors**: rules and risk assessment entries each have a
  stable, *named* anchor (e.g. `/rules/#bow-balls`,
  `/risk-assessment/#capsize-submerge`) so links keep working even if items
  are added, removed, or renumbered. Add one with `{ #short-name }` on its
  own indented line directly beneath the anchored text (a rule's list item,
  or a risk's Hazard field). Treat published anchor names as permanent.
- **Changelog**: each document ends with a changelog table; add a row when
  making a meaningful change.

## Risk assessment

Each risk in `docs/risk-assessment.md` is a
[definition list](https://python-markdown.github.io/extensions/definition_lists/)
with exactly five fields (Hazard, Consequences, Persons at risk,
Responsible, Residual risk), which `extra.css` renders as a compact
label/value grid instead of Markdown's default stacked layout:

```markdown
Hazard
:   Capsize or submerge: boats on the water for racing, or on rafts waiting
    to push off/land
    { #capsize-submerge }

Consequences
:   Hypothermia, Drowning, Infection, Trapped inside the boat, Collision

Persons at risk
:   Competitors & river users

Responsible
:   Crews, Coxswains, Boat club committees, Marshals, Event committee

Residual risk
:   {{ risk(severity=2, probability='B') }}

??? success "Controls"
    - Rescue with launch. Administer first aid. ...
```

- **Hazard** combines the original risk assessment's "Hazard" and
  "Description of hazardous event" columns into one line, and carries the
  entry's permanent anchor.
- **Residual risk** is never written as text. `{{ risk(severity, probability)
  }}` (a macro in `main.py`) looks the level up in `risk_matrix.yml` and
  renders the colour-coded badge, so a risk's severity/probability can never
  silently disagree with its stated level. An invalid combination fails
  `mkdocs build --strict`. The matrix legend further down the page
  (`risk_matrix_table()`) is generated from the same file, so it can't drift
  from what the badges show either.
- **Controls** go in a `??? success "Controls"` collapsible section. It uses
  `success` rather than the ordinary `note` type so it gets a distinct
  checkbox icon (set once in `mkdocs.yml`'s `theme.icon.admonition.success`);
  print CSS in `extra.css` forces these open in generated PDFs, so nothing is
  hidden in print.
- Each `## Category` heading (Water, Weather, Land based) automatically gets
  a strip of colour-coded squares linking to the risks beneath it;
  `docs/assets/risk-summary.js` builds this from the rendered badges and
  anchors after the page loads, so there's nothing to keep in sync by hand.

## Contact details

Personal phone numbers and email addresses are **never stored in this repository** and never appear on the live site.
Pages reference them as `{{ phone('fergus_cooper') }}` / `{{ email('sydney_rose') }}`, and the live site always shows `[number withheld]` / `[email withheld]` in their place.
The event plan then opens with a "Public version: contact details removed" notice, on the page and in its PDF.

Organisations' phone numbers that the organisation itself publishes (checked on its own website) are not personal: they live in `public_phones` in `event.yml` and are shown as they are.
Any number not confirmed as public is treated like a personal one.

To build the full version, with contact details, copy `contacts.local.example.yml` to `contacts.local.yml` and fill in the values, then build locally (see "PDFs" below).
That file is git-ignored and must never be committed.
`main.py` reads it when it exists; anything left blank is still withheld.
Only a build with every value filled in leaves out the "Public version" notice.
`contacts.local.example.yml` is the canonical list of contact keys: the build fails if a page uses a key that is not listed there.
Values are rendered lightly obfuscated in the HTML, decoded by JavaScript in the browser, and as plain text in the PDFs.
Restart `mkdocs serve` after editing the file, as it is only read at startup.

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

## Course map

The Course Map page (`docs/map.md`) is built from Bernard Tao's Oxford Isis Maps, an Inkscape SVG with layers for every event on the river.
That source file is not kept in this repository.
`scripts/strip_map.py` extracts the layers Tamesis uses into `docs/assets/map/`:

```bash
.venv/bin/python scripts/strip_map.py path/to/IsisMap.svg docs/assets/map
```

Layers are found by their names in Inkscape's Layers panel, so a renamed layer stops the script with an error naming it.
To add a course, add its layer to `OUTPUTS` in the script, rerun it, and add a `<figure>` for its print image to the print section of `docs/map.md`; the page's controls pick it up from the SVG.
The page's downloadable PDF is assembled by `hooks/map_pdf.py`, one page per map, each sized to its map.

## Third-party assets

Everything the site needs is served from this repository, with no external CDNs or font services.
Each item below keeps its licence alongside it, and the licence terms require those notices to stay with the files.

| Asset | Location | Licence |
| :- | :- | :- |
| Noto Sans and Noto Sans Mono (from [Fontsource](https://fontsource.org/) 5.3.0) | `docs/assets/fonts/` | SIL Open Font License 1.1, see `OFL.txt` there |
| [d3-zoom](https://github.com/d3/d3-zoom) and its eight D3 dependencies | `docs/assets/vendor/d3/` | ISC, and BSD-3-Clause for d3-ease; full texts in `LICENSE` there and at the top of `d3-zoom.min.js` |
| Oxford Isis Maps by Bernard Tao | `docs/assets/map/tamesis-map.svg` | CC-BY 3.0; the attribution is drawn on the map and must stay visible |

The D3 file is the official `dist/*.min.js` of each module, unmodified and concatenated in dependency order; the versions are listed in its header.
To update it, download the newer files from each package and rebuild the header and `LICENSE` to match.
