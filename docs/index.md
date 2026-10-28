# Tamesis Regatta {{ dates.year }}

Tamesis Regatta is Oxford's novice regatta, held on the Isis and organised by
Linacre Boat Club. Racing is side-by-side over a short course from the
Greenbank to the Cox Stone, and takes place from
**{{ daterange(dates.regatta_start, dates.regatta_end) }}**.

## Key dates

| | |
| :--- | :--- |
| Entries close | {{ dates.entries_close | ukdatetime }} |
| Scratch deadline (full refund) | {{ dates.scratch_deadline | ukdatetime }} |
| Coxing briefing | {{ dates.coxing_briefing | ukdate }} |
| Racing | {{ daterange(dates.regatta_start, dates.regatta_end) }} |

## Documents

- **[Rules](rules.md)**: eligibility, equipment, conduct of racing, and
  bystander safety.
- **[Event & Safety Plan](event-plan.md)**: how the regatta is organised and
  run: marshalling, circulation, emergency procedures, and contacts.
- **[Risk Assessment](risk-assessment.md)**: the hazards of the event, and the
  controls in place for each.
- **[Course Map](map.md)**: an interactive map of the course, circulation and
  marshal positions.

Each document can also be downloaded as a PDF using the button at the top of
the page. Spotted a mistake, or something unclear? Use the edit (pencil) button
at the top of any page to suggest a change on GitHub, or email us using the
contact details below.

## Contact

For any questions about the regatta, email the {{ roles.regatta_captains.title }}
({{ roles.regatta_captains.name }}) at
[{{ contact.email }}](mailto:{{ contact.email }}).
