# Tamesis Regatta {{ dates.year }}: Risk Assessment

<div class="tr-cover" markdown="1">

**Linacre Boat Club**

**Version {{ risk_assessment.version }}**, {{ risk_assessment.date | ukdate }}

Prepared by {{ risk_assessment.prepared_by }}

Prior to the event, this risk assessment and the associated [Event Plan](event-plan.md) will be circulated to all involved boat club committees.

</div>

### Changelog

| Version | Date | Notes |
| :--- | :--- | :--- |
| 2026.0 | 2026-07-19 | Converted from the 2025 risk assessment |
| 2026.1 | 2026-10-14 | <ul>{% if amber_flag_racing %}<li>Add a risk for limited racing on Low Amber Flag, with its safety controls</li>{% endif %}<li>Add a risk for lack of training time before the regatta</li><li>Re-rate unrowable conditions after controls, and add rower status restrictions</li><li>Merge the two risks for ice on the water</li><li>Add this cover block and changelog</li></ul> |

!!! tip "Linking to a risk"
    Every risk has a permanent anchor on its Hazard row — hover over it and
    click the **¶** symbol to get a link directly to it, e.g.
    `#capsize-submerge`.

Each risk states a **severity** (1–5) and **probability** (A–E) only; the
**residual risk** shown is always calculated from those two values using the
[matrix below](#how-levels-are-calculated) — it is never entered separately,
so it cannot silently disagree with the severity/probability that produced
it.

!!! info "What is residual risk?"
    The **residual risk** is the risk remaining *after* the listed controls
    have been applied, and not the risk before any mitigation. Its severity and
    probability already reflect the effect of those controls.

## Risks: water-based { .tr-new-page }

Hazard
:   Capsize or submerge — boats on the water for racing, or on rafts waiting
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
    - Rescue with launch. Administer first aid. Warm casualty up slowly.
    - Marshals to fire klaxon to immediately stop racing in the event anyone
      is in the water.
    - Marshals to carry out boat checks prior to boating (heel restraints,
      bow ball, hatch covers if applicable). Information on necessary boat
      checks will be available to marshals. Boats that do not meet the
      criteria will not be permitted to push off.
    - All competitors must have passed an OURC-approved swim test to
      qualify for racing.

---

Hazard
:   Collision into obstacles or other boats — boats on the water for racing,
    or on rafts waiting to push off/land
    { #collision-into-obstacles }

Consequences
:   Injury to crews/river users, Damage to boats, Damage to moored boats,
    Crew members in the water

Persons at risk
:   Competitors & river users

Responsible
:   Crews, Coxswains, Boat club committees, Marshals, Event committee

Residual risk
:   {{ risk(severity=3, probability='C') }}

??? success "Controls"
    - Rescue with launch. Administer first aid.
    - Marshals to fire klaxon to immediately stop racing in the event anyone
      is in the water.
    - Marshals to liaise with other river users to keep clear of the racing
      line, and to fire klaxon to stop racing if anything or anyone is
      impeding the racing line.
    - Marshals to carry out boat checks prior to boating (heel restraints,
      bow ball, hatch covers if applicable).
    - Coxes to attend a briefing prior to the event. All novice coxes must
      have a bank rider.
    - Circulation pattern sent to all crews in advance; competitors and bank
      riders are expected to understand and follow it.
    - All competitors must have passed an OURC-approved swim test to
      qualify for racing.

---

Hazard
:   Collision into moored boats — boats on the water for racing, or on
    rafts waiting to push off/land
    { #collision-into-moored-boats }

Consequences
:   Damage to moored boats, Damage to rowing boats

Persons at risk
:   Competitors & moored boat owners

Responsible
:   Crews, Coxswains, Boat club committees, Marshals, Event committee

Residual risk
:   {{ risk(severity=2, probability='B') }}

??? success "Controls"
    - Circulation pattern sent to all crews in advance; competitors and bank
      riders are expected to understand and follow it.
    - In the event of an inevitable collision, marshals should sound the
      klaxon and racing should immediately stop.
    - In the event of a collision, the event committee will put the
      offending club in contact with the moored boat owner to discuss
      options.

---

Hazard
:   Collision between a boat and a person in the water — boats on the water
    for racing, or on rafts waiting to push off/land
    { #collision-with-person-in-water }

Consequences
:   Injury, Unconsciousness, Drowning

Persons at risk
:   Competitors & river users

Responsible
:   Crews, Coxswains, Boat club committees, Marshals, Event committee

Residual risk
:   {{ risk(severity=4, probability='B') }}

??? success "Controls"
    - Rescue with launch. Administer first aid.
    - Marshals to fire klaxon to immediately stop racing in the event anyone
      is in the water.
    - Circulation pattern sent to all crews in advance; competitors and bank
      riders are expected to understand and follow it.
    - Crews entered must be able to row all eight safely; crews deemed
      unsafe may be asked to land at any point and may be pulled from
      racing, at the discretion of the event committee.
    - All competitors must have passed an OURC-approved swim test to
      qualify for racing.

---

Hazard
:   Over-exertion — boats on the water for racing, or on rafts waiting to
    push off/land
    { #over-exertion }

Consequences
:   Injury

Persons at risk
:   Competitors

Responsible
:   Crews, Coxswains, Boat club committees

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - Crews expected to fully warm up on land prior to boating.
    - Captains/coaches expected to enter crews who are physically capable of
      racing.
    - Crews deemed unsafe may be asked to land at any point and may be
      pulled from racing, or removed, at the discretion of the event
      committee.

---

Hazard
:   Faulty or poorly maintained equipment — boats on the water for racing,
    or on rafts waiting to push off/land
    { #faulty-equipment }

Consequences
:   Collision due to steering, Crews trapped in boats, Life jackets not
    inflating

Persons at risk
:   Competitors & river users

Responsible
:   Crews, Coxswains, Boat club committees, Marshals

Residual risk
:   {{ risk(severity=2, probability='B') }}

??? success "Controls"
    - Competitors are expected to check their equipment is safe to race.
    - Marshals to carry out boat checks prior to boating; information on
      necessary boat checks will be available to marshals.
    - In the case of a capsize or serious collision, a launch will assist
      and first aid will be administered.

---

Hazard
:   Pre-existing health conditions — boats on the water for racing, or on
    rafts waiting to push off/land
    { #pre-existing-health-conditions }

Consequences
:   Health implications

Persons at risk
:   Competitors

Responsible
:   Crews, Coxswains, Boat club committees

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - Crew members are responsible for carrying their own medication if
      required (e.g. an inhaler).
    - First aid to be administered if applicable.

---

Hazard
:   Capsize, collision, or being caught in the propeller — launches on the
    course
    { #launch-incident }

Consequences
:   Damage to launch, Drowning

Persons at risk
:   Launch drivers, Passengers

Responsible
:   Launch drivers, Event committee

Residual risk
:   {{ risk(severity=2, probability='B') }}

??? success "Controls"
    - All launch drivers must have an RYA Powerboat Level 2 qualification
      (or equivalent).
    - All launch drivers and passengers must wear life jackets.
    - A second launch will assist if needed.
    - Drivers must wear kill cords at all times whilst operating a launch.

---

Hazard
:   Capsize, collision, or crash — crews containing visually impaired
    rowers (not coxswains)
    { #visually-impaired-rowers }

Consequences
:   Visually impaired athletes may become disorientated in the event of a
    capsize

Persons at risk
:   The visually impaired athlete, The crew

Responsible
:   Launch drivers, Event committee, Captains, Coxswains, Athletes, Boat
    committees, SU

Residual risk
:   {{ risk(severity=4, probability='B') }}

??? success "Controls"
    - Crews containing visually impaired athletes must identify themselves
      to the race secretary well in advance of the event. Attempts will be
      made to schedule these crews to race in broad daylight.
    - Crews should conduct their own risk assessment and have a capsize
      procedure in place, ensuring the coxswain is confident what to do if
      the risk occurs.
    - Crews are advised to conduct a clear "numbering off" procedure in the
      event of a capsize, to ensure all rowers are accounted for and not
      injured.
    - A launch, the event committee, and the SU will be made aware when
      crews containing visually impaired athletes are racing, and a launch
      will be on alert.
    - In the event of a serious collision, capsize, or athlete in the
      water, a klaxon will be sounded and crews will hold it up immediately
      to allow a launch to access them. Administer first aid and warm the
      athlete thoroughly as normal procedure dictates.

---

## Risks: weather-related

Hazard
:   Conditions unrowable — high stream or bad weather leaving novice coxes
    and crews unable to cope
    { #un-rowable-conditions }

Consequences
:   Equipment damage, Rowers injured, Collision, Exertion, Unnecessary
    stress on novice coxes

Persons at risk
:   Competitors

Responsible
:   SU and Event committee

Residual risk
:   {{ risk(severity=3, probability='C') }}

??? success "Controls"
    - Senior Umpire to assess weather and conditions in consultation with
      the Event Committee to decide if racing is safe to occur.
    - Racing will not take place if the risk is judged unacceptable.
    - Implement rower status restrictions and/or coxing status restrictions
      at the discretion of the Event Committee.

{% if amber_flag_racing %}
---

Hazard
:   Racing in higher stream — racing on Low Amber Flag (≤ 4.5 bucks
    equivalent)
    { #racing-on-low-amber-flag }

Consequences
:   Crews unable to control their boat, Collision, Capsize, Crews carried
    downstream towards the Gut and weir streams

Persons at risk
:   Competitors & river users

Responsible
:   SU and Event committee, Launch drivers, Coxswains, Boat club committees

Residual risk
:   {{ risk(severity=4, probability='B') }}

??? success "Controls"
    - Racing on Low Amber Flag only as set out in the
      [Event Plan](event-plan.md#racing-on-low-amber-flag): on Days 3 and 4
      only, and only if there was racing on both Days 1 and 2, so that the
      least proficient crews have already been eliminated.
    - Short course only, at the discretion of the Senior Umpires and the
      Event Committee, and only if no other condition (such as wind or
      visibility) adds to the safety concerns. Never guaranteed.
    - At least two launches on the water at all times, downstream of all
      marshalling crews, to assist any crew that needs help.
    - Every crew must have senior rowers (≥ 3 full terms of rowing
      experience) at bow and 2.
    - Coxes must be S status, or X status upgraded more than 12 months
      before the day of racing.
    - Crews must spin under the direction of race officials, well above the
      Longbridges raft.
    - Entrants notified by 5pm the day before, so crews can arrange senior
      bow pairs and eligible coxes.
{% endif %}

---

Hazard
:   Struck by lightning — crews, marshals and the event committee caught in
    a storm while racing or at the riverside
    { #struck-by-lightning }

Consequences
:   Electrical burns, Shock

Persons at risk
:   Competitors, marshals and event committee

Responsible
:   Coxswains, Boat club committees, Marshals, Event committee, SU

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - All crews to leave the water and seek appropriate shelter immediately;
      the "30-30 Rule" is used, as advised by British Rowing.
    - Senior Umpire issues instructions to everyone at the river by radio.
    - Crews that have yet to boat should not push off, and should seek
      shelter.
    - Crews that have pushed off and are warming up or waiting to race
      should land under marshal/umpire instructions.
    - Crews that are mid-race may be advised to stop or complete the race —
      the safest course of action is decided by the SU.
    - Once crews have landed they must seek shelter, preferably within a
      boathouse. No crews may boat again until the SU/Event Committee has
      deemed it safe to do so.
    - Coxes are briefed on what to do in the event of lightning at the
      pre-event briefing.

---

Hazard
:   Crews become too cold — extreme cold
    { #extreme-cold-crews }

Consequences
:   Mild hypothermia, Cold muscles leading to injury, Delayed reaction
    times

Persons at risk
:   All competitors, especially coxswains

Responsible
:   Crews, Coxswains, Marshals, Boat club committees

Residual risk
:   {{ risk(severity=2, probability='C') }}

??? success "Controls"
    - Rowers to complete a full warm-up on land prior to boating.
    - Competitors to wear sufficient layers during warm-up and racing, and
      bring a change of dry kit for afterwards.
    - During the coxing briefing, it will be stressed that all crews should
      bring a dry change of kit, and the signs of hypothermia will be
      covered.
    - SU and event committee to monitor conditions and make a judgement
      call on extreme cold.

---

Hazard
:   Marshals become too cold — extreme cold
    { #extreme-cold-marshals }

Consequences
:   Mild hypothermia, Delayed reaction times

Persons at risk
:   Marshals and event committee

Responsible
:   Marshals, Event committee

Residual risk
:   {{ risk(severity=2, probability='D') }}

??? success "Controls"
    - Marshals advised to wear plenty of layers beforehand.
    - Regular welfare checks for marshals, with warm drinks available at
      race desk before and after shifts.
    - Marshals made aware of the warning signs of hypothermia prior to
      their shift.
    - SU and event committee to monitor conditions and make a judgement
      call on extreme cold.

---

Hazard
:   Collision — ice on the water
    { #ice-on-the-water }

Consequences
:   Equipment damage, Injury

Persons at risk
:   Competitors & river users

Responsible
:   Event committee, SU

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - SU, event committee, race officials and marshals to monitor weather
      conditions.
    - Safety launches to clear small quantities of ice from the racing
      course.
    - Racing cancelled if launches cannot sufficiently clear the course of
      ice.

---

Hazard
:   Collision, or the outcome of a race undetermined — low visibility (fog)
    { #low-visibility-fog }

Consequences
:   Equipment damage, Injury

Persons at risk
:   Competitors & river users

Responsible
:   Crews, Coxswains, Boat club committees, Marshals, Event committee

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - SU and event committee to monitor conditions.
    - Use adequate lighting on boats.
    - If visibility is reduced to less than 100m on any part of the racing
      course, racing is suspended or cancelled.

---

Hazard
:   Collision, or the outcome of a race undetermined — low visibility
    (failing light)
    { #low-visibility-light }

Consequences
:   Equipment damage, Injury

Persons at risk
:   Competitors & river users

Responsible
:   Crews, Coxswains, Boat club committees, Marshals, Event committee

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - SU and event committee to monitor conditions. Use adequate lighting
      on boats.
    - All boats must have lights if they will be on the water 1 hour before
      sunset.
    - If visibility is reduced to less than 100m on any part of the racing
      course, racing is suspended or cancelled.

---

Hazard
:   Novice crews unable to race safely — high stream or bad weather leading
    to a lack of training time before the regatta
    { #lack-of-training-time }

Consequences
:   Equipment damage, Rowers injured, Collision

Persons at risk
:   Competitors & river users

Responsible
:   SU and Event committee

Residual risk
:   {{ risk(severity=3, probability='C') }}

??? success "Controls"
    - Senior Umpire to assess the recent history of weather and conditions
      that allowed training, in consultation with the Event Committee, to
      decide if racing is safe to occur.
    - Each novice rower is recommended to have had no fewer than 5 training
      outings before racing; crews that the Senior Umpires or the Event
      Committee deem unsafe to race may be disqualified.
    - Implement rower status restrictions and/or coxing status restrictions
      at the discretion of the Event Committee.

---

## Risks: land-based

Hazard
:   Collision or injury — boats being moved on the land
    { #boats-moved-on-land }

Consequences
:   Injury to crews, Injury to bystanders

Persons at risk
:   Competitors, Bystanders

Responsible
:   Coxswains, crews

Residual risk
:   {{ risk(severity=2, probability='C') }}

??? success "Controls"
    - Crew and coxswains to remain aware of surroundings when manoeuvring
      boats (few spectators expected).
    - Contact marshals/race desk if first aid is needed.

---

Hazard
:   Collision involving accompanying cyclists or pedestrians — bank riders
    accompanying crews on the towpath
    { #bank-rider-collision }

Consequences
:   Injury to cyclists and pedestrians, Falling in the river

Persons at risk
:   Bank riders, Pedestrians

Responsible
:   Bank riders, Boat club committee

Residual risk
:   {{ risk(severity=1, probability='D') }}

??? success "Controls"
    - Bank riders must check bikes have working brakes and lights, and are
      advised to wear a helmet whilst cycling.
    - One bank rider is permitted per crew, unless training novice coxes, in
      which case approval must be obtained from the event committee.
    - Expected spectator numbers are low and only two crews race at once, so
      the chance of collision with spectators is low.
    - Marshals to fire klaxon in the event anyone is in the water, and
      launches to assist with first aid administered.

---

Hazard
:   Collision, possible immersion, or falling off a bike — ice on the
    towpath
    { #ice-on-the-towpath }

Consequences
:   Injury to cyclists and pedestrians, Falling in the river

Persons at risk
:   Bank riders, Pedestrians

Responsible
:   SU and Event committee

Residual risk
:   {{ risk(severity=3, probability='B') }}

??? success "Controls"
    - SU and event committee to assess conditions.
    - If deemed not bikeable, the event may be cancelled or restricted to
      only X/S coxes, so bank riders are no longer required.

---

## How levels are calculated

The level of risk is read off this matrix by severity (rows) and probability
(columns). It is generated directly from `risk_matrix.yml`, the same file
the badges above are calculated from.

<div class="risk-matrix-wrapper" markdown>
{{ risk_matrix_table() }}
</div>

??? note "Probability definitions"
    - **A** — {{ risk_matrix.probability.A }}
    - **B** — {{ risk_matrix.probability.B }}
    - **C** — {{ risk_matrix.probability.C }}
    - **D** — {{ risk_matrix.probability.D }}
    - **E** — {{ risk_matrix.probability.E }}

??? note "Severity definitions"
    - **1** — {{ risk_matrix.severity[1].injury }} / {{ risk_matrix.severity[1].damage }}
    - **2** — {{ risk_matrix.severity[2].injury }} / {{ risk_matrix.severity[2].damage }}
    - **3** — {{ risk_matrix.severity[3].injury }} / {{ risk_matrix.severity[3].damage }}
    - **4** — {{ risk_matrix.severity[4].injury }} / {{ risk_matrix.severity[4].damage }}
    - **5** — {{ risk_matrix.severity[5].injury }} / {{ risk_matrix.severity[5].damage }}

??? note "What each level means"
    - **Low** — {{ risk_matrix.definitions.low }}
    - **Moderate** — {{ risk_matrix.definitions.moderate }}
    - **Substantial** — {{ risk_matrix.definitions.substantial }}
    - **Intolerable** — {{ risk_matrix.definitions.intolerable }}

