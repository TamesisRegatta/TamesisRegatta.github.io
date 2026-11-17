---
# Not in the nav: linked from the footer of every page.
pdf: false
---

# Accessibility statement

This statement covers this website, tamesisregatta.org, and the PDFs of its documents.
It is run by Fergus Cooper, on behalf of the organisers of Tamesis Regatta at Linacre Boat Club.

We want as many people as possible to be able to use it.
For example, you should be able to:

- use the whole site with a keyboard alone, including the course map: with the map selected, plus and minus zoom, the arrow keys move around, and 0 resets it; on a marker, Enter shows its details and Escape closes them
- zoom in to 400% without losing content, and use the site on a narrow phone screen
- choose light or dark mode with the button at the top of each page
- increase the spacing of letters, words and lines without losing text
- read the PDFs of the rules, FAQs, event plan and risk assessment with a screen reader, as they are tagged, and move around them with their bookmarks

## Known limitations

- **Briefing slides.** The briefing slides, under `/briefings/`, have not yet been checked for accessibility. Their content is covered by the [Rules](rules.md) and the [Event & Safety Plan](event-plan.md).
- **The course map** shows the course, circulation and marshal positions visually. The same information is written out in the [Event & Safety Plan](event-plan.md), in its sections on circulation and on marshals. The course map's PDF is pictures of the maps, without text a screen reader can read.
- **Diagrams in the Event & Safety Plan.** The circulation diagrams in its Appendix 3 are pictures, with short descriptions; the circulation is described in full in the plan's text.
- **Documents and services from others.** The Environment Agency's notices on the [River Notices](river-notices.md) page are its own PDFs, which we cannot change. The draw is published on Google Sheets, and the visit statistics on the [analytics page](analytics.md) come from Plausible Analytics; how accessible they are is up to those services.
- **Testing by hand.** We have not yet tested the site with screen readers, such as NVDA or VoiceOver, or by hand on touch screens.
- The site is only available in English.

## Reporting a problem

If anything on the site is hard to use, or you cannot use it at all, please email us at [{{ contact.email }}](mailto:{{ contact.email }}).
It helps to say what you were trying to do, on which page, and which device, browser and any assistive technology you used.

The regatta is run by volunteers: we read every report, but cannot promise how soon we will reply.
If you need a document in another format, tell us and we will do what we can.

## Technical information

We aim to meet the [Web Content Accessibility Guidelines (WCAG), version 2.2](https://www.w3.org/TR/WCAG22/){ target="_blank" rel="noopener" }, at level AA.
The site has not been audited independently, so we cannot say for certain that it does; the limitations we know of are listed above.

## How we tested the site

When this statement was prepared, we checked every page, in light and dark mode:

- with the axe-core accessibility checker, applying the WCAG 2.2 level A and AA rules and its best practices, including with the course map's courses and details, the risk assessment's controls, search and the phone menu open
- for fitting a narrow screen, keeping all its text with wider letter, word and line spacing, and not animating when less motion is asked for
- with the keyboard, for the order in which things take focus and for showing which has it
- and the PDFs, for tags, language and bookmarks

We fixed the problems these checks found.
Automated checks find only some accessibility problems, so we will keep checking as the site changes.

This statement was prepared on 17 November 2026.
