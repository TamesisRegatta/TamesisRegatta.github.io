# Tamesis Regatta {{ dates.year }}: Rules

<div class="tr-cover" markdown="1">

**Linacre Boat Club**

**Version {{ rules.version }}**, {{ rules.date | ukdate }}

Prepared by {{ rules.prepared_by }}

</div>

### Changelog

| Version | Date | Notes |
| :--- | :--- | :--- |
| 2026.0 | 2026-07-19 | 2025 rules converted to website format, with dates updated for 2026 |
| 2026.1 | 2026-10-15 | <ul><li>Racing finishes half an hour before sunset; in adverse conditions coxes may cox more than one crew (rule 1.4)</li><li>Event Plan safety contingencies take precedence (rule 1.7)</li><li>Cite the OURCs membership rules by section name, with a link (rule 2.4)</li><li>Crews must be safe to race (rule 2.16)</li><li>Coxes' PFDs per the OURCs Code of Conduct (rule 3.2)</li></ul> |
| 2026.2 | 2026-10-28 | <ul><li>Clarify friendly crews, swim tests, coxing briefing exemptions, identification and one crew per person, in line with the Event Plan (section 2)</li><li>Clubs provide one marshal per crew (rule 2.16)</li><li>Lights required on the water after 15:00 (rule 3.1.6)</li><li>Describe the racing format; on-the-day decisions rest with the Race Committee (section 4)</li><li>Add section 6: entry fees, scratching and refunds, with the scratch deadline moved to Monday 04:00</li><li>Add this cover block and changelog</li></ul> |

Questions about these rules should be sent to
[{{ contact.email }}](mailto:{{ contact.email }}).

## 0. Definitions { #definitions .tr-new-page }

1. The '**Event Committee**' refers to the {{ roles.regatta_captains.title }}, {{ roles.regatta_captains.name }}; the {{ roles.safety_advisor.title }}, {{ roles.safety_advisor.name }}; the {{ roles.coordinating_senior_umpire.title }}, {{ roles.coordinating_senior_umpire.name }}; the {{ roles.senior_member.title }}, {{ roles.senior_member.name }}; the {{ roles.chief_marshal.title }}, {{ roles.chief_marshal.name }}; the {{ roles.captain_of_coxes.title }}, {{ roles.captain_of_coxes.name }}, and any other individuals chosen in advance to help in the organisation of the event.
    { #event-committee }

2. The '**Race Committee**' refers to any set of the above at Race Desk actively running the event at any given time.
    { #race-committee }

3. The '**Senior Umpires**' are {{ roles.senior_umpires.name }}. On the water, a Senior Umpire may act on behalf of the Race Committee.
    { #senior-umpires }

## 1. General { #general }

1. The Event Committee reserves the right to alter any of the rules without notice and reserves the right to interpret these rules in any way that stays within their spirit, especially with respect to eligibility.
    { #rule-alterations }

2. The Race Committee reserves the right to disqualify any crew or boat club which infringes these rules, and there will be no refunds in case a crew or entire boat club is disqualified. The Race Committee's decision in the event of any dispute shall be final. No decision taken by the Race Committee shall be deemed to set or have set precedent; each case will be decided on its own merit.
    { #disqualification }

3. The Race Committee reserves the right to postpone or reschedule races, if necessary even until another day (e.g. if conditions become unsafe or the schedule is delayed for any reason).
    { #postponement }

4. The Regatta shall be held from {{ dates.regatta_start | ukdate }} until {{ dates.regatta_end | ukdate }} on the Isis, from noon on Wednesday–Friday and from 11am on Saturday, until half an hour before sunset each day, provided that the weather conditions allow it to be run safely. In case of adverse conditions, the Event Committee will decide whether to allow coxes to cox more than one crew (relaxing [rule 2.11](#one-crew-per-person), for example when only X or S status coxes may race), postpone or cancel races, convert some or all rounds into time trials instead of side-by-side races, or to cancel the whole event. The format for the next day's racing will be confirmed no later than 5pm each day. However, if conditions worsen after 5pm the race day may be called off entirely on shorter notice. If conditions worsen during a day's racing it is the Race Committee's primary concern to ensure everyone's safety, and racing may be suspended or cancelled at any time.
    { #event-dates }

5. All participants take part at their own risk. The Event Committee and Race Committee can accept no responsibility for damage or injury, however caused.
    { #own-risk }

6. All participants agree to the provisions set out in the [Event Plan](event-plan.md).
    { #event-plan }

7. Safety contingencies set out in the [Event Plan](event-plan.md) may override some of these rules. Where they do, the Event Plan takes precedence.
    { #safety-contingencies }

## 2. Entries and Eligibility { #entries }

1. A rower is considered to be a novice if, prior to {{ dates.novice_cutoff | ukdate }}, they have **not** competed as a rower (sculling or sweep) in any of the following:
    { #novice-definition }

    1. Any British Rowing (or foreign, regional, or international equivalent) regatta or head race.
        { #novice-br-events }

    2. Any other event where they represented their school, college, or university (for example, bumps races including rowing on, Isis Winter League, Clare Novices Regatta, Oriel Regatta, etc.)
        { #novice-club-events }

    For the avoidance of doubt, rowers who learned to row before {{ dates.novice_cutoff | ukdate }} are eligible, as long as they had not competed in any of the above before that date.
    { #novice-learned-early }

2. A **competitive** crew must consist of one cox and eight novice rowers.
    { #competitive-crews }

3. A **friendly** crew must consist of one cox and a minimum of five novice rowers and up to three non-novice rowers.
    { #friendly-crews }

    1. In a heat, the result stands as raced. A competitive crew that finishes behind a friendly crew proceeds to the repechage instead of to round one, and the friendly crew proceeds to round one.
        { #friendly-repechage }

    2. In the repechage and every later round, a competitive crew racing a friendly crew is always deemed the winner, so a friendly crew can never eliminate a competitive crew.
        { #friendly-lose }

4. All athletes must be members of their respective college boat club, per the membership definitions in the General rules of racing of the [OURCs Rules of Racing](https://ourcs.co.uk/organisation/racing/). A maximum of 2 associate members are permitted in any crew.
    { #club-membership }

5. At the discretion of the Event Committee, composite crews (composed of novice rowers, within the eligibility rules, from more than one boat club) may be permitted to row as a competitive crew. This rule is intended to allow novices to race who would otherwise not have a seat, and the Event Committee will be unlikely to permit composite crews which have been created for reasons other than this.
    { #composite-crews }

6. All competitors (rowers and coxes) must have an in-date swim test on the OURCs entry system. Competitors booked into a swim test after the close of entries but before racing may still be eligible, and should contact the OURCs Rowing Sabbatical Officer to confirm.
    { #swim-test }

7. All coxes must hold an OURCs coxing licence and must attend the coxing briefing, held in conjunction with OURCs on {{ dates.coxing_briefing | ukdate }}. In cases of illness or academic clashes, the {{ roles.captain_of_coxes.title }} may, in consultation with OURCs, exempt a cox from attending. Exemptions must be requested by email to [{{ contact.email }}](mailto:{{ contact.email }}) no later than 11am on the day of the briefing, giving the cox's name and coxing history, and can only be given to X or S status coxes. Exempted coxes must review the briefing materials, especially the circulation pattern, which will be made available on this website and circulated to all boat clubs by email.
    { #coxing-licence }

    1. N status coxes must have a bankrider at all times that they are on the water. X or S coxes are not required to have a bankrider, but may if they wish.
        { #novice-cox-bankriders }

    2. A maximum of one bankrider is permitted to follow each crew. The Race Committee may grant permission for an additional bankrider for the purpose of teaching novice coxes.
        { #bankrider-limit }

    3. Any crew may have a cox of any status, although in the spirit of the event clubs are encouraged to put novice coxes in their higher ranked boats.
        { #cox-status }

8. Coxes must carry identification for every member of their crew while on the water. Each identification must include a photograph of the person; a printout or photocopy of a University card, or a coxing licence, is sufficient. Crews who fail an identity check will not be allowed to push off or, if the check takes place after racing, may be disqualified.
    { #crew-identification }

9. Substitutions may be made freely within these eligibility rules. The Race Committee must be informed of any substitutions before the crew in question boats, either on the entry system up to the online substitution deadline, or in person at Race Desk. If a crew races as a friendly crew, it shall remain friendly from that point on.
    { #substitutions }

10. Women may row in men's events, but men may not row in women's events. Coxes may compete in any event regardless of gender.
    { #gender-eligibility }

11. No person may row in more than one crew, or cox more than one crew, at any point in the regatta. Although it is permitted to row in one crew and cox another, this is done entirely at the club's own risk and the Event Committee makes no promises that the schedule will accommodate it.
    { #one-crew-per-person }

12. The Event Committee will not be able to make any changes to the draw in order to accommodate kit clashes, unless this request is made at the time of entry.
    { #kit-clashes }

13. Crews must be complete, legal, and swim-tested in the OURCs entries database by the close of entries ({{ dates.entries_close | ukdatetime }}), or else they will be scratched by the committee.
    { #entries-deadline }

14. The Event Committee reserves the right to scratch any crews for any reason, including but not limited to loss of race time.
    { #committee-scratches }

15. Clubs must only enter crews who can row safely. Each novice rower should have had no fewer than 5 training outings before racing. Crews that the Senior Umpires or the Event Committee deem unsafe to race may be asked to land, withdrawn from racing, or disqualified.
    { #safe-to-race }

16. Each club must provide one experienced marshal for each crew it enters. Marshals must have marshalled before, must be registered with the Race Committee before the regatta, and must attend the marshal briefing on {{ dates.marshal_briefing | ukdate }} (online, if attending in person is impossible). This applies to crews scratched after the scratch deadline too (rule [6.2](#scratch-deadline)).
    { #marshals }

## 3. Equipment { #equipment }

1. All competing boats shall comply with OURCs rules and RowSafe guidelines for equipment. Crews are required to get their boat checked by a marshal before going afloat and any boat which does not meet the following points, or which is judged by the marshal to be unsafe for any other reason, shall not be allowed to boat until the issue is remedied.
    { #boat-checks }

    1. Bow-balls. A solid ball, of not less than 4 cm diameter, made of rubber or material of similar resilience, shall be firmly attached to the bows and the fixing shall not itself present a hazard.
        { #bow-balls }

    2. Foot Release. In all boats, each shoe shall be independently restrained such that when the heel reaches the horizontal position the foot will be released from the shoe. In addition, where laces, Velcro or similar material needs to be opened before the rower can remove their feet from the shoes, all such materials shall be able to be released immediately by the rower with a single quick hand action of pulling on one easily accessible strap.
        { #foot-release }

    3. Backstays. The forward port and starboard rigger on all boats shall be protected by a backstay. For the avoidance of doubt, riggers of a "reverse" design are considered to have a backstay.
        { #backstays }

    4. Hatch Covers. All hatch covers and bungs for which the boat has been designed shall be fitted in the proper place. If a boat was not designed to take such covers then it is not a requirement that it be retrofitted to take them.
        { #hatch-covers }

    5. Boat Codes. All boats shall be identifiable by a three-letter code as determined by British Rowing, together with a three-digit fleet number determined by the club.
        { #boat-codes }

    6. Lights. Boats on the water after 15:00 must carry bright white lights, switched on, attached to the stern and bow, which together are visible through 360 degrees. Failure to use lights will result in disqualification.
        { #lights }

2. Coxes shall wear a personal flotation device (PFD), in line with the [OURCs Code of Conduct](https://ourcs.co.uk/organisation/conduct/), and be familiar with its method of operation.
    { #cox-lifejackets }

3. All bankriders must have a roadworthy bicycle equipped with properly functioning brakes and, if appropriate, lights. Bankriders must not hold cameras or other devices while cycling.
    { #bankrider-bikes }

## 4. Conduct of the Race { #conduct }

1. Competitors, crews, coaches, groups of club members or supporters of a club who do any of the following shall be considered to have engaged in unsportsmanlike behaviour and may be penalised per rule [1.2](#disqualification).
    { #unsportsmanlike }

    1. wilfully disobey safety instructions
        { #disobeying-safety-instructions }

    2. set out to subvert the application of these rules
        { #subverting-rules }

    3. refuse to follow the instructions of a marshal or properly appointed official
        { #refusing-instructions }

    4. delay the Start without just cause or disrupt the start by shouting, banging, etc.
        { #delaying-start }

    5. physically or verbally threaten or abuse another competitor, official, helper or member of the public
        { #threatening-behaviour }

    6. use foul or obscene language in the public hearing, or use foul or obscene gestures in the public view
        { #foul-language }

    7. display any other form of misconduct deemed by an official to be unsportsmanlike
        { #other-misconduct }

2. The format
    { #format }

    1. All crews race a side-by-side heat on the first day. Crews that lose their heat race in a repechage, normally the next day. Crews that win their heat or repechage go on to a side-by-side knock-out, up to the final. Unless conditions require changes, every crew is guaranteed at least two races.
        { #format-rounds }

    2. The draw will be published before racing, showing when each crew races and its path through to the final.
        { #the-draw }

    3. This is the intended format. The contingencies in the Event Plan for [dangerous conditions](event-plan.md#dangerous-conditions) and [bad weather before the regatta](event-plan.md#appendix-1-contingency-plans-for-pre-regatta-bad-weather) may require changes to it, and to the draw, at short notice.
        { #format-changes }

3. The start
    { #the-start }

    1. Each crew is responsible for being on time for their race.
        { #race-punctuality }

    2. When it is time for their race the starter shall call over the crews to the start. Coxes are responsible for positioning their crew within their lane such that they do not collide with anything off the start.
        { #start-positioning }

    3. Coxes should raise their arm to indicate to the starter if they are not ready, and should lower it as soon as they are. Note that this is advisory only and the starter may start the race even if coxes have their hands raised.
        { #start-readiness }

    4. The starter shall align the crews, including a stagger between them to account for the differences between the lanes. Crews must not try to alter this stagger unless instructed by the starter.
        { #start-stagger }

    5. The starter shall name the two crews, then shall say "Attention" and raise a red flag. After a brief pause, the starter shall give the start signal by saying "go" and simultaneously dropping the red flag.
        { #start-signal }

    6. In the event of a false start, or a collision immediately off the start, the starter shall tell both crews to stop, then will re-align them and start the race again. Any crew which causes multiple false starts may be disqualified.
        { #false-starts }

4. The race
    { #the-race }

    1. Each crew shall remain in its own lane for the duration of the race.
        { #stay-in-lane }

    2. Any crew which, through leaving its lane, gains an advantage or interferes with or fouls the other crew may be disqualified if the Race Committee deems that such action impacted the outcome of the race.
        { #leaving-lane }

    3. In the event that the race needs to be stopped for any reason, the marshals will fire a klaxon. All crews on the water must immediately stop and await further instructions from the marshals.
        { #klaxon }

    4. All crews are responsible for their own accidents.
        { #own-accidents }

5. The finish
    { #the-finish }

    1. The finish shall be marked by a white post known as the clacker. Upon crossing the finish line, a "clack" sound will indicate to crews that they have finished. Crews should keep paddling until they are fully clear of the finish.
        { #the-clacker }

    2. The finish shall be judged by the bows. Any margin between the crews, however small, decides the race.
        { #finish-judging }

        1. In the event of a dead heat, the finish marshal shall inform the crews and they shall proceed immediately back to the start to re-row.
            { #dead-heats }

    3. Appeals against the result of the race should be made by the cox raising their arm upon crossing the finish line. The finish judge shall communicate the appeal to the Race Committee, who shall determine whether the result stands. The decision of the Race Committee shall be final.
        { #appeals }

## 5. Bystander Safety { #bystander-safety }

1. Marshals are responsible for the safety of bystanders, and will warn pedestrians of oncoming races, supported by signs at entry points onto the towpath. Spectators must follow the instructions of marshals. In the event of unsafe or disruptive behaviour by spectators, the Race Committee may postpone the start of a division or contact the Police as appropriate.
    { #bystander-marshals }

2. **Numbers of cyclists accompanying races will be strictly controlled.** Only one bankrider may accompany each crew (rule [2.7.2](#bankrider-limit)), and clubs that break this rule may be sanctioned. The Race Committee may permit an additional bankrider, for example to help train a novice cox. Bankriders must give way to pedestrians and must not interfere with the public's enjoyment of the public right of way.
    { #cyclist-numbers }

3. During racing, any bankrider involved in an incident on the towpath must stop and provide initial assistance and/or information as required, alerting the nearest marshal, who will inform Race Desk if the crew's cox is N status. If the cox is N status, the crew will be held at the finish until either the bankrider can join them to accompany them back to their raft (if no longer needed at the accident), or the Race Desk can send a substitute bankrider. If the cox is X or S status, the crew can proceed unaccompanied while the bankrider ensures that their part in the incident has been logged along with their contact details.
    { #incidents-during-racing }

4. During warm-up and return to the boathouse, any bankrider involved in an incident on the towpath must stop, as must their crew. The bankrider must alert the nearest marshal and proceed as above, with the Race Desk expediting substitute bankriders if the crew is yet to race.
    { #incidents-during-warmup }

5. Clubs are responsible for the conduct of their coaches and bankriders, and may be sanctioned for dangerous or inappropriate behaviour. Marshals will report unsafe cycling, and any accident, to the Race Committee.
    { #cyclist-conduct }

## 6. Fees, Scratching and Refunds { #fees-refunds }

1. The entry fee is £{{ entry_fee }} per crew. It is set by OURCs, and is the same as the entry fee for Torpids and Summer Eights in the same calendar year.
    { #entry-fee }

2. The deadline to scratch crews with a full refund is {{ dates.scratch_deadline | ukdatetime }}. Crews scratched after this deadline, by their club or by the Event Committee, are still charged the entry fee, and their club must still provide marshals for them (rule [2.16](#marshals)).
    { #scratch-deadline }

3. Crews that are not complete, legal and swim-tested by the close of entries are scratched by the Event Committee (rule [2.13](#entries-deadline)) before the scratch deadline, and are not charged.
    { #incomplete-crews }

4. There are no refunds for crews or clubs that are disqualified (rule [1.2](#disqualification)).
    { #disqualification-refunds }

5. If the whole regatta is cancelled before any racing has taken place (for example because of high water), entry fees will be refunded, less any costs the organisers have already incurred.
    { #cancellation-refunds }

6. Once racing has started, there will generally be no refunds if racing is lost, cancelled or changed (for example converted to time trials), including if the rest of the regatta is cancelled. The Event Committee will make every effort to reduce costs where it can, but cannot guarantee any refund.
    { #lost-racing-refunds }
