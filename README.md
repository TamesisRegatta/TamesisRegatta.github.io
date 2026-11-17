# Tamesis Regatta website

The website of Tamesis Regatta, Oxford's novice regatta, at <https://tamesisregatta.org/>: the rules, FAQs, event and safety plan, risk assessment, course map and briefing slides.
It is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, with the briefings in [Slidev](https://sli.dev/), and deployed to GitHub Pages from `main`.

## Running it locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve                            # http://127.0.0.1:8000, rebuilds on save
```

PDFs are only built when `PDF_EXPORT` is set, as they slow the edit loop:

```bash
.venv/bin/playwright install --with-deps chromium  # once
PDF_EXPORT=true .venv/bin/mkdocs build --strict
```

The briefing decks need Node (version in `briefings/.nvmrc`):

```bash
cd briefings && npm ci
npx slidev --open coxing/slides.md                # live preview
./build.sh                                        # every deck, with PDFs, into ../site/briefings/ (after mkdocs build)
```

Never use `-q` with `--strict`: it hides the warnings that strict fails on.

## Making changes

Make changes through a pull request.
Every pull request is built exactly as for a deploy, with PDFs and decks, and checked by `tests/check_site.py`; merging to `main` deploys it.

| Path | What it holds |
| :- | :- |
| `event.yml` | Dates, role holders, the draw's link and other values the pages and decks use |
| `docs/` | One Markdown file per page, and `assets/` for CSS, JavaScript, images and fonts |
| `mkdocs.yml` | Navigation, theme, plugins, hooks and the Plausible settings |
| `main.py` | Macros for the pages: dates, contact details, risk badges |
| `risk_matrix.yml` | The risk matrix that the risk badges and the matrix table are drawn from |
| `hooks/` | Build steps: the map PDF, tagged PDFs, PDF links, the draw's short link |
| `overrides/` | Changes to Material's templates, each explained at its top |
| `briefings/` | The Slidev decks and their theme |
| `scripts/` | Tools for regenerating the course map |
| `tests/check_site.py` | Accessibility, privacy and PDF checks of the built site |

Each script, hook and component explains itself at its top; read that before changing it.

Things to keep to:

- **Dates and names** live only in `event.yml`, as ISO 8601 (`2026-11-25`, `04:00:00`), so a mistake fails the build.
  Pages show them with filters such as `{{ dates.regatta_start | ukdate }}`; the home page's key dates use `{{ when(...) }}`, and must stay in date order.
- **Anchors are permanent.**
  Rules and risks have named anchors (`{ #short-name }` on its own line under the item, as in `/rules/#bow-balls`); never rename a published one.
- **Changelogs.**
  Each document opens with one; add a row for a meaningful change.
  The event plan and risk assessment are approved by the University safety office, so any change to their wording is a new version for it to approve.
- **Risks** follow the pattern of the existing ones: five fields, with the residual risk always given as `{{ risk(severity=..., probability=...) }}`, never as text, and the controls in a `??? success "Controls"` box.
- **Navigation** lists the crews' pages first, then the safety documents, under a divider drawn above Event Plan (so keep it straight after FAQs).
  Each page sets its icon in its front matter (`icon: material/...`).
- **The draw.**
  Set `draw_url` in `event.yml`; the site then serves <https://tamesisregatta.org/draw/> as a short link to it, and adds it to the nav.
  Give the short link in anything printed or sent out.
- **Icons** come from Material's bundled sets (`:material-...:`); plain emoji shortcodes load from a CDN.

## Personal contact details

Personal phone numbers and email addresses are never stored in this repository and never appear on the live site.
Pages refer to them as `{{ phone('fergus_cooper') }}` or `{{ email('sydney_rose') }}`, which the live site shows as `[number withheld]`, with a "Public version" notice on the event plan.
Organisations' numbers go in `public_phones` in `event.yml`, and are shown, only if the organisation publishes them on its own website; any other number is treated as personal.

For the full version, copy `contacts.local.example.yml` to `contacts.local.yml`, fill it in, and build locally (restart `mkdocs serve` after editing it).
That file is git-ignored and must never be committed; neither must PDFs built from it.
`contacts.local.example.yml` lists every key a page may use.

## Privacy and accessibility

The site sets no cookies and needs no consent banner.
Its only third-party content is [Plausible Analytics](https://plausible.io/), which counts visits on Oxford Research Software Engineering's server without cookies or storage; the analytics page embeds its dashboard.
Nothing else from another site may be embedded, in the site or the decks (no YouTube, fonts or CDNs): host media in the repository instead.
To stop Plausible counting your own visits, run `localStorage.plausible_ignore = "true"` in your browser's console on the live site.

The site aims to meet [WCAG 2.2](https://www.w3.org/TR/WCAG22/) at level AA.
The privacy policy (`docs/privacy.md`) and accessibility statement (`docs/accessibility.md`) say what the site counts, stores and has been tested for; keep them, and their dates, in step with changes.
`tests/check_site.py` fails on cookies, unexpected storage or third-party requests, accessibility problems, and untagged PDFs; to run it locally, after building with `PDF_EXPORT=true` and `npm ci` in `briefings/`:

```bash
.venv/bin/python tests/check_site.py site briefings/node_modules/axe-core/axe.min.js
```

The briefing decks are not checked yet, and the accessibility statement says so.

## Course map

The course map is drawn from Bernard Tao's Oxford Isis Maps, an Inkscape SVG that is not kept in this repository.
`scripts/strip_map.py` extracts the layers the site uses into `docs/assets/map/`; the intermediate course and time trial, which the source lacks, are derived from its short course by the recipes in `scripts/courses/`, written by `scripts/lift_course.py` and `scripts/time_trial_recipe.py`.
Each script's docstring says how to run it.

## Briefing slides

Each deck is `briefings/<deck>/slides.md`, published at `/briefings/<deck>/` with a PDF.
The theme in `briefings/theme/` uses the site's colours and font, is light mode only, and reads `event.yml`, but never `contacts.local.yml`.
Its layouts are `cover` (with `draft: true` for a "not for circulation" band until a deck is final), `section`, `figure` and `alert`; `RaceCycle` animates a crew's race cycle from a route in `briefings/coxing/race-cycles/`.

`overrides` in `briefings/package.json` lift `dompurify` and `image-size` past security advisories Slidev has not picked up; remove each once `npm ls` shows Slidev on a fixed version.

## Third-party assets

Each keeps its licence beside it, as the licences require.

| Asset | Location | Licence |
| :- | :- | :- |
| Noto Sans and Noto Sans Mono, from [Fontsource](https://fontsource.org/) 5.3.0 | `docs/assets/fonts/` | SIL Open Font License 1.1 (`OFL.txt`) |
| [d3-zoom](https://github.com/d3/d3-zoom) and its eight D3 dependencies, unmodified, versions in the file's header | `docs/assets/vendor/d3/` | ISC, and BSD-3-Clause for d3-ease (`LICENSE`) |
| Oxford Isis Maps by Bernard Tao | `docs/assets/map/`, `scripts/courses/` | CC BY 3.0; the attribution drawn on the map must stay visible |
| Gas fog horn by Joseph Sardin, [BigSoundBank](https://bigsoundbank.com/), lengthened to one 10-second blast | `briefings/coxing/public/media/klaxon.mp3` | CC0 1.0 |
