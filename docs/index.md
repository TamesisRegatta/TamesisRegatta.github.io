# Tamesis Regatta {{ dates.year }}

Tamesis Regatta is Oxford's novice regatta, held on the Isis and organised by
Linacre Boat Club. Racing is side-by-side over a short course from the
Greenbank to the Cox Stone, and takes place from
**{{ daterange(dates.regatta_start, dates.regatta_end) }}**.

## Key dates

| | |
| :--- | :--- |
| Novice cut-off (see the [novice definition](rules.md#novice-definition)) | {{ when(dates.novice_cutoff) }} |
| Entries open | {{ when(dates.entries_open) }} |
| Marshal sign-ups open | {{ when(dates.marshal_signups_open) }} |
| Entries close, and crews must be complete | {{ when(dates.entries_close) }} |
| Scratch deadline (full refund) | {{ when(dates.scratch_deadline) }} |
| Draw published (our aim, but not guaranteed) | {{ when(dates.draw_published) }} |
| Coxing briefing (time and venue TBC) | {{ when(dates.coxing_briefing) }} |
| Marshal briefing (time and venue TBC) | {{ when(dates.marshal_briefing) }} |
| Racing | {{ when(dates.regatta_start, dates.regatta_end) }} |
| Awards ceremony, at Race Desk | {{ when(dates.awards_ceremony, about=True) }} |

## Documents

- **[Rules](rules.md)**: eligibility, equipment, conduct of racing, and
  bystander safety.
- **[FAQs](faqs.md)**: answers to common questions, for captains.
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
