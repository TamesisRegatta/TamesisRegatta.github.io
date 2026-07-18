# Tamesis Regatta {{ dates.year }}

Tamesis Regatta is Oxford's novice regatta, held on the Isis and organised by
Linacre Boat Club. Racing is side-by-side over a short course from the
Greenbank to the Cox Stone, and takes place from
**{{ daterange(dates.regatta_start, dates.regatta_end) }}**.

## Key dates

| | |
| :--- | :--- |
| Entries close | {{ dates.entries_close | ukdatetime }} |
| Scratch deadline (full refund) | {{ dates.scratch_deadline | ukdate }} |
| Coxing briefing | {{ dates.coxing_briefing | ukdate }} |
| Racing | {{ daterange(dates.regatta_start, dates.regatta_end) }} |

Dates and role holders are configured in a single file —
[edit event.yml on GitHub](https://github.com/TamesisRegatta/TamesisRegatta.github.io/edit/main/event.yml).

## Documents

- **[Rules](rules.md)** — eligibility, equipment, conduct of racing, and
  bystander safety. Every rule has a permanent link.
- **[Event & Safety Plan](event-plan.md)** — how the regatta is organised and
  run: marshalling, circulation, emergency procedures, and contacts.

Each document can also be downloaded as a PDF using the button at the top of
the page. Spotted a mistake? Every page has an edit (pencil) button that opens
the page source on GitHub.

## Contact

For any questions about the regatta, email the {{ roles.regatta_captains.title }}
({{ roles.regatta_captains.name }}) at
[{{ contact.email }}](mailto:{{ contact.email }}).
