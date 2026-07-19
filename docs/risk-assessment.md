# Risk Assessment

Tamesis Regatta {{ dates.year }} · Linacre Boat Club

!!! tip "Linking to a risk"
    Every risk has a permanent anchor on its Hazard row — hover over it and
    click the **¶** symbol to get a link directly to it, e.g.
    `#capsize-submerge`. Anchors are named, not numbered, so links keep
    working even if risks are added, removed, or renumbered.

!!! note "Work in progress"
    This page currently shows the first two risks per category, while the
    rest of the risk assessment is transcribed.

Each risk states a **severity** (1–5) and **probability** (A–E) only; the
**residual risk** shown is always calculated from those two values using the
[matrix below](#how-levels-are-calculated) — it is never entered separately,
so it cannot silently disagree with the severity/probability that produced
it.

!!! info "What is residual risk?"
    The **residual risk** is the risk remaining *after* the listed controls
    have been applied — not the risk before any mitigation. Its severity and
    probability should already reflect the effect of those controls.

## Water { #water }

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

## Weather { #weather }

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
:   {{ risk(severity=3, probability='D') }}

??? success "Controls"
    - Senior Umpire to assess weather and conditions in consultation with
      the Event Committee to decide if racing is safe to occur.
    - Implement coxing status restrictions at the discretion of the Event
      Committee.

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

## Land based { #land-based }

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

## How levels are calculated { #how-levels-are-calculated }

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

## Changelog { #changelog }

| Version number | Date | Notes |
| :--- | :--- | :--- |
| 2026.1 | 2026-07-19 | First preview: one example risk per category, converted from the 2025 risk assessment |
| 2026.2 | 2026-07-19 | Added second risk per category |
