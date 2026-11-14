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
| `briefings/` | Briefing slide decks, built with Slidev. See [Briefing slides](#briefing-slides). |
| `.github/workflows/deploy.yml` | Builds the site (including PDFs) and the briefing slides, and deploys them to GitHub Pages. |

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
- **Key dates** on the home page use `{{ when(dates.entries_close) }}`, which renders the date and records when it starts and is over (in UK time).
  `docs/assets/key-dates.js` then marks each row as past, on now or next by the visitor's clock, so the table stays current without rebuilding the site.
  Keep the rows in date order.
- **Permanent anchors**: rules and risk assessment entries each have a
  stable, *named* anchor (e.g. `/rules/#bow-balls`,
  `/risk-assessment/#capsize-submerge`) so links keep working even if items
  are added, removed, or renumbered. Add one with `{ #short-name }` on its
  own indented line directly beneath the anchored text (a rule's list item,
  or a risk's Hazard field). Treat published anchor names as permanent.
- **Changelog**: each document starts with a changelog table; add a row when
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
The page's Show line has a checkbox for each overlay layer (`data-overlay` in `OUTPUTS`, such as the AEDs) and for each part of every course listed in `PARTS` (the marshals, and the Racedesk), which also hides that part's rows in the key.

The script also corrects the source where it disagrees with the event plan (`RELABEL`: the Boathouse Island marshal numbers), and skips a correction with a warning once the source no longer needs it.

The source has no intermediate course layer, so that course is derived: a copy of the short course layer, edited by the recipe in `scripts/courses/intermediate.svg`.
`scripts/lift_course.py` writes that recipe from the published circulation PDFs (the ones in Appendix 3 of the event plan, kept beside the repository but not in it).
It lifts what the intermediate PDF has and the short course PDF does not (the start, the lanes and arrows down to it, the Gut and Donnington Bridge arrows, marshal 11) and moves them onto the current map; everything the two courses share comes from Bernard's current short course layer.
It needs PyMuPDF, which the site itself does not use:

```bash
pip install pymupdf
python scripts/lift_course.py "Tamesis 2026 Circulation Intermediate Course.pdf" "Tamesis 2026 Circulation Short Course.pdf" scripts/courses/intermediate.svg
```

Rerun `strip_map.py` after changing the recipe.
The script's comments say what is lifted, what is left out and why.
If Bernard adds an intermediate course layer to the source, use that instead and delete the recipe.

The time trial is derived the same way, from the recipe in `scripts/courses/time-trial.svg`.
Time trials run on the short course, so the recipe takes the racing lanes out of a copy of the short course and adds the time trial's own circulation.
`scripts/time_trial_recipe.py` writes it, following the published time trial PDF; that PDF is drawn on an older version of the map, so nothing is lifted from it, and its notes are set as text.
This script needs nothing beyond Python:

```bash
python scripts/time_trial_recipe.py scripts/courses/time-trial.svg
```

## Briefing slides

The briefings are [Slidev](https://sli.dev/) decks in `briefings/`, published on the same site at `/briefings/<deck>/`, for example <https://tamesisregatta.org/briefings/coxing/>.
Each deck is a `briefings/<deck>/slides.md`, and each has a PDF download, built alongside it.
They need Node (version in `briefings/.nvmrc`):

```bash
cd briefings
npm ci
npx slidev --open coxing/slides.md   # live preview while editing
./build.sh                           # every deck, with PDFs, into ../site/briefings/
```

`build.sh` writes into `site/`, so run it after `mkdocs build`, which clears that directory; this is what the deploy workflow does.
The PDF export needs Playwright's Chromium for Node (`npx playwright install chromium`), separate from the Python one.

`overrides` in `briefings/package.json` lift two of Slidev's dependencies past security advisories that Slidev itself has not picked up yet: `dompurify` (pinned by `monaco-editor`, the dev server's code editor) and `image-size` (declared by `pptxgenjs`, the PowerPoint export, which never calls it).
Neither reaches the published decks.
Remove each override once `npm ls` shows Slidev depending on a fixed version itself.

The theme, `briefings/theme/`, is modelled on the OxRSE Slidev theme and uses the site's colours, font and logo.
It is light mode only.
Its layouts are `cover` (date from `event.yml` via `when:`, plus `presenters:` and `venue:`), `section`, `figure` (one map or diagram, with an optional `::aside::` column) and `alert`; other slides get a black header bar with the slide's title.

Slides read the same `event.yml` as the site, so dates and names match: in slide Markdown, `{{ ukdatetime(regatta.dates.coxing_briefing) }}` gives "Wed 18 Nov 2026, 18:30" (`ukdate`, `ukdatetime` and `uktime` match the site's filters), and `v-if="regatta.amber_flag_racing"` switches content as the event plan does.
Only public data is passed to the slides: `contacts.local.yml` is never read, so decks never contain personal numbers.
They can import the site's own images from `docs/assets/` by relative path instead of keeping copies.

Decks must not embed YouTube or any other third-party player or resource: the site sets no cookies and stores nothing in visitors' browsers, so it needs no consent banner, and an embed would change that.
Host video and audio clips in the deck's folder instead, trimmed and compressed.

## Third-party assets

Everything the site needs is served from this repository, with no external CDNs or font services.
Each item below keeps its licence alongside it, and the licence terms require those notices to stay with the files.

| Asset | Location | Licence |
| :- | :- | :- |
| Noto Sans and Noto Sans Mono (from [Fontsource](https://fontsource.org/) 5.3.0) | `docs/assets/fonts/` | SIL Open Font License 1.1, see `OFL.txt` there |
| [d3-zoom](https://github.com/d3/d3-zoom) and its eight D3 dependencies | `docs/assets/vendor/d3/` | ISC, and BSD-3-Clause for d3-ease; full texts in `LICENSE` there and at the top of `d3-zoom.min.js` |
| Oxford Isis Maps by Bernard Tao | `docs/assets/map/`, and the intermediate course and time trial recipes in `scripts/courses/` (after his circulation PDFs) | CC-BY 3.0; the attribution is drawn on the map and must stay visible |
| Gas fog horn by Joseph Sardin, [BigSoundBank](https://bigsoundbank.com/), extended from three short blasts to one 10-second blast (the klaxon in the coxing briefing) | `briefings/coxing/public/media/klaxon.mp3` | CC0 1.0 (public domain); no attribution required, but credited here |

The D3 file is the official `dist/*.min.js` of each module, unmodified and concatenated in dependency order; the versions are listed in its header.
To update it, download the newer files from each package and rebuild the header and `LICENSE` to match.
