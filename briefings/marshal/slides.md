---
theme: ../theme
title: Marshal briefing
layout: cover
presenters:
  - Emily Stone
when: marshal_briefing
venue: online via MS Teams
download: true
exportFilename: tamesis-marshal-briefing
favicon: /assets/img/favicon.svg
transition: fade
drawings:
  persist: false
---

Please put your name and college in the Teams chat.

---

# The Essentials: make sure you know...

- <span class="key">Your position: where it is, and what you do there.</span>
- <span class="key">When and how to klaxon.</span>
- <span class="key">Your place in the river check.</span>
- The circulation pattern, so you can direct crews.
- <span class="key">Never leave your post empty:</span> stay until your replacement arrives.

<br>

- Anything on the water goes to the <span class="key">SU</span>; everything else goes to <span class="key">Race Desk</span>.
- The event plan, rules and maps are at <https://tamesisregatta.org/>.

---

# This briefing will cover...

1. **Everyone:** how the regatta runs, your shift, radios, river checks, klaxons, and what to do if racing stops.
2. **Position by position:** where each marshal stands and what they do, from the Head (1) down to Donnington Bridge (11).

These slides are on the website, to look back at or download as a PDF: <https://tamesisregatta.org/briefings/>.
Your position's slide is your guide on the day.

---

# Abbreviations

- <span class="key">SU:</span> Senior Umpire, who starts each race and runs the racing.
- <span class="key">Race Desk:</span> the Event Organisers, in the Merton Small Boats bay on Boathouse Island.
- <span class="key">Univ:</span> University College, and its boathouse and raft on the towpath side, opposite Boathouse Island.
- <span class="key">The Head:</span> the Head of the River, upstream of the finish.
- <span class="key">County Station:</span> the racing lane along the towpath side; <span class="key">City Station:</span> the racing lane in the middle of the river.
- <span class="key">Transit lane:</span> on the City side, for crews not racing.
- <span class="key">N, X, S status:</span> a cox's OURCs status, from novice (N) to senior (S).
- <span class="key">PFD:</span> personal flotation device.

---
layout: section
---

# PART 1: EVERYONE

What every marshal needs to know

---

# The regatta

- Novice crews race side by side, Wednesday to Saturday, from noon until half an hour before sunset. If we need to make up time, Saturday's racing may start at 11am.
- Heats on the first day, then a repechage, then a knock-out up to the finals.
- Wednesday and Thursday on the short course. <span class="key">Friday and Saturday are planned on the longer intermediate course</span>, down to Donnington Bridge, if conditions permit.
- A race every three to four minutes, so the river is rarely quiet for long.
- Many crews have novice coxes: N status coxes must have a bankrider following them.

<Contingency>
<p>In some conditions we change format at short notice: to time trials<span v-if="regatta.amber_flag_racing">, or to racing on Low Amber Flag</span>. Or we may have to stop racing early. Boxes like this one, and slides with a grey header, say what you would do then.</p>
</Contingency>

---

# Who's who

- <span class="key">Senior Umpires ({{ regatta.roles.senior_umpires.name }}):</span> start each race, and run the racing and the river checks.
- <span class="key">Race Desk ({{ regatta.roles.regatta_captains.name }}):</span> the Event Organisers, in the Merton Small Boats bay.
- <span class="key">Chief Marshal ({{ regatta.roles.chief_marshal.name }}):</span> assigns positions and runs the online briefing.
- <span class="key">Incident Controller ({{ regatta.roles.incident_controller.name }}):</span> takes charge of any safety incident.
- <span class="key">Medics:</span> at Race Desk and on the medical launch, which has priority over every crew.
- <span class="key">Safety launches:</span> two, providing cover, and carrying marshals to and from the County side.
- <span class="key">Bankriders:</span> at most one per crew, cycling along the towpath with it.

---

# Your shift

- Your slot and reporting time come by email.
- Each day starts with a briefing at Race Desk: a mock river check, a radio check, and a klaxon test. Then go to your post.
- Posts on the County side may be reached by safety launch.
- There are two shifts a day. <span class="key">Stay at your post until your replacement arrives</span>, and never hand over during a race.
- Last shift of the day: wait for the SU to dismiss you, then return your kit to Race Desk.

---

# Before your shift, and your kit

- Dress for two or more hours standing outside in November, and bring something to eat and drink.
- You must not drink alcohol, or be drunk, on duty.
- Learn some blade colours: <https://tamesisregatta.org/blades/>.

<br>

- <span class="key">Everyone gets:</span> a two-way radio, a klaxon, and a clipboard with your position's duties, the race schedule, blade colours and contact numbers.
- <span class="key">Everyone except the Tower Marshal (6) also gets</span> a high-visibility bib.
- <span class="key">Some positions also get:</span> a loudhailer (see your position's slide).

---
layout: figure
---

<script setup>
import shortCourse from '../../docs/assets/img/circulation-short.svg'
</script>

# Short course: circulation and marshal positions

<img :src="shortCourse" alt="Short course circulation and placement of marshals 1 to 10, with the SU at the start and defibrillator locations">

---
class: dense
---

# Circulation in brief

- Reverse circulation above the Gut: the transit lane is on the City side for the whole course, and never crosses the racing lanes.
- Start at or below Univ; finish near the Cox Stone.
- After finishing, crews go well clear of the line, spin when the Head Marshal says, and come back down the transit lane.
- Crews pair up in the Marshalling Zone, on the Greenbank between the start and Longbridges House, and are started in the order they are ready.
- <span class="key">On the short course, the only crews that go through the Gut are those boating from or landing at a boathouse below it</span>, such as the Isis Boathouse.
- Crews must follow marshals' instructions: refusing to is unsportsmanlike behaviour under the rules.

<Contingency v-if="regatta.amber_flag_racing">
<ul>
<li><b>Low Amber Flag:</b> no crew goes through the Gut at all, not even those based below it.</li>
</ul>
</Contingency>

---

# Intermediate course: Friday and Saturday

- Planned for Friday and Saturday, if conditions permit: we confirm the next day's course by 5pm.
- The course is longer: <span class="key">the start is lower</span>, and the event area runs down to Donnington Bridge.
- <span class="key">Donnington Bridge (11) is staffed</span>, and comes last in the river check, after the Gut.
- Crews based below the Gut go through it as usual.
- Other crews may go through the Gut, as far as Donnington Bridge, <span class="key">only if the SUs and Race Committee allow it</span>, and say so before that day's racing. If they don't, no other crew goes through.
- Your position's slide says what changes for you.

---
layout: figure
---

<script setup>
import intermediateCourse from '../../docs/assets/img/circulation-intermediate.svg'
</script>

# Intermediate course: circulation and marshal positions

<img :src="intermediateCourse" alt="Intermediate course circulation and placement of marshals 1 to 11, with the SU at a lower start and Donnington Bridge (11) below the Gut">

---

<script setup>
import rafts from '../../docs/assets/map/print/boathouse-rafts.svg'
</script>

# Boathouse Island rafts

<div class="grid grid-cols-2 font-600">
  <div>&larr; UPSTREAM (TOWARDS HEAD)</div>
  <div class="text-right">DOWNSTREAM (TOWARDS GUT) &rarr;</div>
</div>

<img :src="rafts" alt="Boathouse Island rafts: landing on the top 5 rafts, boating from the bottom 6" class="w-full my-2">

<div class="grid grid-cols-2">
  <ul><li>Crews <span class="key">land</span> on the upstream 5 rafts: Boathouses A (4).</li></ul>
  <ul><li>Crews <span class="key">boat</span> from the downstream 6 rafts: Boathouses B (5).</li></ul>
</div>

<p class="text-center key">Both boating and landing, bows point downstream.</p>

---

<script setup>
// The radio photo is from the previous marshal briefing's slides; the
// numbered pins mark the same parts as that slide's arrows did, as fractions
// of the photo's width and height.
import radio from './media/radio.jpg'
const pins = [
  { n: 1, x: 7.9, y: 52.2 },
  { n: 2, x: 82.2, y: 21.5 },
  { n: 3, x: 55.6, y: 14.7 },
  { n: 4, x: 72.6, y: 55.8 },
  { n: 5, x: 15.9, y: 72 },
]
</script>

# Your radio

<div class="radio-grid">
<div class="radio-photo">
  <img :src="radio" alt="A handheld two-way radio, numbered: 1, the large push-to-talk button on its left side; 2, the right-hand knob on top, for volume; 3, the left-hand knob on top, for the channel; 4, the grille on the front, the microphone and speaker; 5, two smaller buttons on the left side, below the push-to-talk button">
  <span v-for="p in pins" :key="p.n" class="radio-pin" :style="{ left: p.x + '%', top: p.y + '%' }" aria-hidden="true">{{ p.n }}</span>
</div>
<div>

1. <span class="key">Push to talk.</span> Hold it down while you speak.
2. <span class="key">Volume.</span> Loud enough to hear over the crowd.
3. <span class="key">Channel.</span> Never turn it, unless the SU or Race Desk asks: you'd stop hearing everyone else.
4. <span class="key">Microphone and speaker.</span> Talk into here.
5. <span class="key">Not for talking.</span> Don't press these.

</div>
</div>

<style>
.radio-grid {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 2.5rem;
  align-items: center;
}

.radio-photo {
  position: relative;
}

.slidev-layout .radio-photo img {
  height: 400px;
  width: auto;
  margin: 0;
  border: 2px solid var(--tamesis-black);
  border-radius: 4px;
}

.radio-pin {
  position: absolute;
  width: 1.7em;
  height: 1.7em;
  transform: translate(-50%, -50%);
  display: grid;
  place-items: center;
  background: var(--tamesis-yellow);
  color: var(--tamesis-black);
  border: 2px solid var(--tamesis-black);
  border-radius: 50%;
  font-weight: 800;
  line-height: 1;
}
</style>

---

# Using your radio

- Hold the button down for one second, to wake the repeater, then speak slowly and clearly, and let go when you've finished.
- Wait for a gap: if two people talk at once, everyone hears only interference.
- Say who you're calling, then who you are: <span class="key">"SU, SU, this is Gut Marshal, come in."</span>
- Listen out for your position being called.
- Set the volume so you can hear it over the crowd, but <span class="key">never change the channel</span> unless the SU or Race Desk asks.
- <span class="key">Never put your radio down or hand it to anyone</span>: people do take them, and use them to disrupt racing.
- Keep it dry, and out of the river. Battery gone? Use the nearest marshal's radio, or phone Race Desk.

---

# Whom to call

- <span class="key">The SU:</span> anything on the water. River traffic, obstructions, crews in the wrong place, equipment failures, crews not ready.
- <span class="key">Race Desk:</span> everything else. Results, appeals, identity checks, kit, and questions from the public or officials.
- Not sure? Call the SU during racing, and Race Desk between races. <span class="key">Race Desk and the SUs are both listening</span>, so whoever you call, the other hears it too.

---
class: dense
---

# River checks

- The SU or their assistant asks for a river check at the start of each shift, during long pauses, and whenever they need one: <span class="key">"Let's have a river check, starting from the Head, GO!"</span>
- <span class="key">Positions report in number order</span>, from the Head downstream:

<p class="text-center font-600">Head (1), Finish (2), Meadow (3), Boathouses A (4), Boathouses B (5), Tower (6), Univ (7), Greenbanks (8), Longbridges (9), Gut (10)<span class="font-400">, and Donnington Bridge (11) on the intermediate course.</span></p>

- Nothing to report? <span class="key">"Head, clear."</span>
- Something to report? Say what it is, where it is, and where it is going: "Boathouses A, a narrowboat moving downstream along Boathouse Island."
- The marshal before you doesn't answer? Wait a few seconds, then give your own report.
- We cannot start races with other boats on the course, and <span class="key">racing stops if a post in the river check is left empty.</span>

---
class: dense
---

# What to report

<div class="grid grid-cols-2 gap-8">
<div>

<span class="key">Report:</span>

- Swans, especially any hiding by the bank.
- Kayaks and canoes: they appear suddenly, from under the bridges and out of the Cherwell Cut.
- Punts, rowing boats, cruisers, narrowboats.
- Swimmers. Yes, really.
- Anyone fishing from the bank of the course.
- Anything floating in the river that a crew could hit.

</div>
<div>

<span class="key">No need to report:</span>

- The event launches.
- The Environment Agency's river inspector.
- Geese: unlike swans, they are not protected.
- Our crews, in the right place: unless they are late, lost or in trouble.

</div>
</div>

---

# Do we really have to stop races for swans?

- In Summer Eights 2012, a crew clipped the wing of a swan hiding along the Greenbank.
- OURCs spent two hours following the injured swan up the Cherwell, and its wing was later amputated.
- The story drew wide negative attention in the local press.
- <span class="key">Harming a swan is a criminal offence.</span> Klaxoning a race is a nuisance; a prosecution is much worse.

---

# Let's practise a river check

<p class="text-2xl text-center my-8 key">"Let's have a river check, starting from the Head, GO!"</p>

- Answer when it's your turn, in number order, with "clear" or a short report.
- On the day, wind and nearby crowds make the radio hard to hear: listen out for the marshal before you.

---
layout: alert
class: text-center
---

<script setup>
// The klaxon sound is the coxing deck's (coxing/public/media/klaxon.mp3; see
// the README for its source and licence), bundled into this deck by Vite.
// The PDF can't play it, so it links to the published file instead.
import klaxon from '../coxing/public/media/klaxon.mp3'
import { inPdf } from '../theme/utils/print.js'
const klaxonUrl = 'https://tamesisregatta.org/briefings/coxing/media/klaxon.mp3'
const pdf = inPdf()
</script>

Every position has a

<div class="text-8xl font-800 leading-tight my-6">KLAXON</div>

<p class="font-700">This is by far the most safety-critical part of your role: you are the first line of defence in your part of the river.</p>

<audio v-if="!pdf" controls preload="none" :src="klaxon" class="mx-auto mt-4"></audio>
<p v-if="pdf" class="text-base">Listen to it: <a :href="klaxonUrl">{{ klaxonUrl }}</a></p>

---
class: dense
---

# When to klaxon

During a race, <span class="key">klaxon at once</span> if:

- Anyone falls in the water: rower, cox or spectator.
- Someone in a boat needs First Aid.
- A <span class="key underline underline-offset-4">dangerous</span> collision is about to happen: with another boat, a bank, debris, a swan or a person.
- Something blocks the course.
- <span class="key">You hear another klaxon</span>, live or over the radio.

Not every clash is dangerous: a clash of blades, or a light touch between boats, is not on its own a reason to klaxon. The cox can appeal at the finish.

Someone lying down in a boat? Tell them to sit up. If they don't, ask why, and whether they need First Aid: if they do, klaxon.

<p class="text-center key mt-6">If you don't pay attention, and a dangerous crash happens in your part of the river because you did not klaxon, lives could be at stake.</p>

---
class: dense
---

# How to klaxon

1. <span class="key">Sound your klaxon</span> in all directions for at least 10 seconds, holding your radio button down so every marshal hears it. Keep going until everything you can see has stopped.
2. Then, on the radio: <span class="key">your position, whether First Aid is needed, and why you klaxoned.</span> The first question will always be "Is First Aid required?": if you're not sure, say so, and they will be sent anyway.
3. Your klaxon fails? Say <span class="key">"KLAXON! KLAXON! KLAXON!"</span> into your radio.

<br>

- <span class="key">You hear a klaxon?</span> Sound yours, through your radio too, until every crew near you has stopped. Then keep the radio quiet, unless there's a medical emergency near you.
- Every crew stays stopped, holding it up, until <span class="key">the SU says racing can resume.</span> They move only to make way for the medical launch.
- Keep your klaxon with you: never put it down.

---

# Never say "klaxon" on the radio

- Unless you are stopping a race, <span class="key">never say the word "klaxon" on the radio</span>: just saying it can stop the racing.
- Not sure what's happening? Ask <span class="key">"Is the race still live?"</span>, or "What was that noise?", and listen to the radio.
- Something wrong with your klaxon? Wait until the race is over, and call it an <span class="key">"air horn"</span>.

---

# River traffic and the public

- The Environment Agency's river restriction notice (on the website's River Notices page) lets you direct river traffic. Do not give the public any other orders.
- Smaller craft (kayaks, canoes, hire boats, narrowboats) going downstream use the transit lane; going upstream, the County Station.
- Larger craft, such as Salter's cruisers, use the City Station, in either direction.
- While a race is on, ask craft to wait at <span class="key">Holding Point A</span> (the Head) or <span class="key">Holding Point B</span> (Top Gut). If a craft insists on coming onto the course during a race, tell the SU: the race will be stopped.
- Warn pedestrians of oncoming races, and look out for boats being carried through crowds.
- Bankriders must give way to pedestrians, ride roadworthy bikes, and hold no cameras or phones. At most one bankrider per crew.

---

# Bankrider incidents

- A bankrider in an incident on the towpath must stop, help, and alert the nearest marshal.
- <span class="key">If their crew's cox is N status</span>, tell Race Desk. The crew is held at the finish until its bankrider, or a substitute that Race Desk sends, can take it back to its raft.
- If the cox is X or S status, the crew may go back on its own.
- Report dangerous cycling, or a complaint from the public, to Race Desk.

---
class: dense
---

# Raft marshals (4, 5, 7, 9)

Boathouses A (4), Boathouses B (5), Univ (7) and Longbridges (9):

- <span class="key">Check every boat before it pushes off</span>. A boat that fails, or that you judge unsafe for any other reason, does not boat until it is fixed:
  - Bow ball: firmly attached, not just taped.
  - Heel restraints: heels can't rise above the lowest fixed point of the shoe.
  - Backstays on the front riggers, and hatch covers in place if the boat has watertight compartments.
  - Cox wearing a PFD, on top of all other clothing.
  - After 15:00: white lights at bow and stern, switched on, visible all round.
- <span class="key">Identity checks</span>, when Race Desk asks: collect the crew's photo IDs from the cox as they land, and tell Race Desk, who will talk you through the rest. A crew that fails may not boat, or may be disqualified.
- <span class="key">Equipment failure?</span> Find out what's wrong and how long it will take to fix, then tell the SU.
- Where you can, keep track of which crews have boated from your raft.

---

<script setup>
// The boat check photos are from the previous marshal briefing's slides,
// which credited them to packer.dsl.pipex.com/rowing and the Janousek
// website; see the README. Replace them with our own photos when we can.
import heelPass from './media/heel-pass.jpg'
import heelFail from './media/heel-fail.jpg'
import bowPass from './media/bowball-pass.jpg'
import bowFail from './media/bowball-fail.jpg'
import pfdPass from './media/pfd-pass.jpg'
import pfdFail from './media/pfd-fail.jpg'
</script>

# Boat checks: pass or fail

<div class="checks">
  <div></div>
  <div class="checks-head">Heel restraints</div>
  <div class="checks-head">Bow ball</div>
  <div class="checks-head">Cox's PFD</div>

  <div class="checks-row pass">PASS</div>
  <img :src="heelPass" alt="Pass: heel restraints tied from the heels of a pair of rowing shoes to the footplate, so the heels cannot lift">
  <img :src="bowPass" alt="Pass: a moulded rubber bow ball, screwed firmly onto the bow">
  <img :src="pfdPass" alt="Pass: a cox in a boat at a raft, wearing a red lifejacket over all their clothing">

  <div class="checks-row fail">FAIL</div>
  <img :src="heelFail" alt="Fail: a hand lifting the heel of a rowing shoe well above the footplate">
  <img :src="bowFail" alt="Fail: a ball held onto the bow only with tape">
  <img :src="pfdFail" alt="Fail: a cox at racing, in a jacket, with no lifejacket visible over it">
</div>

<p class="checks-credit">Photos from the previous marshal briefing, credited there to packer.dsl.pipex.com/rowing and Janousek.</p>

<style>
.checks {
  display: grid;
  grid-template-columns: auto repeat(3, 1fr);
  gap: 0.5rem 1rem;
  align-items: center;
}

.checks-head {
  font-weight: 700;
  text-align: center;
}

.checks-row {
  font-weight: 800;
  letter-spacing: 0.06em;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  text-align: center;
  padding: 0.3rem;
  border-radius: 4px;
  color: white;
}

.checks-row.pass { background: #2e7d32; }
.checks-row.fail { background: #c62828; }

.slidev-layout .checks img {
  width: 100%;
  height: 165px;
  object-fit: cover;
  margin: 0;
  border-radius: 4px;
}

.slidev-layout .checks-credit {
  font-size: 0.7rem;
  color: var(--tamesis-muted);
  text-align: right;
}
</style>

---
class: dense
contingency: true
---

# If racing is stopped early

If Race Desk or the SU decides the river has become unsafe, in this order:

1. <span class="key">Raft marshals:</span> crews still on land must not boat; waiting crews take their boats off the water.
2. <span class="key">The SU</span> starts no more races.
3. <span class="key">The Head Marshal</span> tells finished crews to spin and land in normal circulation.
4. Once they have landed, and the Incident Controller says the top stretch is clear, <span class="key">the SU and marshals send crews in the Marshalling Zone home</span>, as quickly and safely as possible. This overrides normal circulation:
   - Boathouse Island: cross to the City side, go up the course, and land with bows pointing upstream.
   - Univ: land with bows pointing upstream, as the Univ Marshal directs.
   - Longbridges: land as usual, as the Longbridges Marshal directs.
   - Isis Boathouse: go through the Gut, as the Gut Marshal directs.

It should take under 20 minutes. Crews follow marshals, not their coaches.

---
contingency: true
---

# If the format changes

- <span v-if="regatta.amber_flag_racing"><span class="key">Low Amber Flag</span> (days 3 and 4 only): no crew goes through the Gut, and crews spin upstream of the Greenbanks Marshal (8), except those landing at Longbridges.</span>
- <span class="key">Time trials</span> (for example in high wind) always use the short course. Crews line up bow to stern in the Marshalling Zone, tucked in to the towpath bank, and the SU starts them one at a time. The SU's assistant times the start, and the Finish Timer (2A) backs up the finish.

The time trial map is on the next slide, and your position's slide says what changes for you.

---
layout: figure
contingency: true
---

<script setup>
import timeTrial from '../../docs/assets/img/circulation-time-trial.svg'
</script>

# Time trials: circulation and marshal positions

<img :src="timeTrial" alt="Time trial circulation and placement of marshals 1 to 10, with Boathouses B (5) as Crossing Marshal">

---
layout: section
---

# PART 2: POSITION BY POSITION

From the Head (1) down to Donnington Bridge (11)

---
layout: position
x: 0.180
y: 0.347
alt: "Map close-up: the Head Marshal (1) above the finish, near Folly Bridge, with Holding Point A"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 1st. You start it, after the SU's "GO!".
---

# (1) Head

At the Head of the River, upstream of the finish.

- <span class="key">Finished crews:</span> keep them going well clear of the finish, then tell them when and where to spin, so they don't build up by the finish. Send them back down the transit lane.
- <span class="key">River traffic from upstream:</span> ask it to wait at Holding Point A until the race in progress is over, and tell the SU. Downstream craft that fit use the transit lane, and must not leave it or cross the river without speaking to a marshal.
- Note any coxing protest, and pass it to Race Desk.
- Answer questions from the public.

<Contingency>
<ul>
<li><b>Racing stopped early:</b> tell finished crews to spin and land in normal circulation.</li>
<li><b>Time trials:</b> crews don't spin until you tell them.</li>
</ul>
</Contingency>

---
layout: position
x: 0.256
y: 0.360
alt: "Map close-up: the Finish Marshal (2) on the towpath side at the finish line"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 2nd, after the Head.
---

# (2) Finish

On the towpath side, at the finish line, near the Cox Stone.

- <span class="key">Decide who has won</span>: sound the clacker as the winning boat's bow crosses the line, however small the margin.
- Dead heat: tell both crews to go straight back to the start to re-row.
- <span class="key">Appeals:</span> a cox raises their arm as they cross the line. Note it, and pass it to Race Desk.
- Move crews on up to the Head Marshal, well clear of the line before they spin.
- Hold an N status crew whose bankrider has stopped for an incident, as Race Desk directs.
- Tell the SU about river traffic coming from upstream.

<Contingency>
<ul>
<li><b>Time trials:</b> you are also given a stopwatch. Time each crew across the line, with the Finish Timer (2A) as a backup.</li>
</ul>
</Contingency>

---
layout: position
tag: Not a safety marshal
x: 0.256
y: 0.360
alt: "Map close-up: the finish line on the towpath side, where the Results Marshal stands with the Finish Marshal (2)"
kit: Bib, radio (on its own channel to Race Desk), clipboard.
check: Not in the river check.
---

# Results Marshal

With the Finish Marshal (2), at the finish line.
Not one of the numbered safety marshals: <span class="key">your job is to get the results right</span>.

- Your radio is on <span class="key">a different channel</span> from the marshals', and you talk only to Race Desk.
- After each race, tell Race Desk <span class="key">the winner, the station it won on (City or County), and the verdict</span>: 6 inches, a canvas, 2 lengths, clear water, and so on.
- For example: "Race Desk, result: Linacre won on County, by a canvas."
- <span class="key">Appeals:</span> watch for a cox raising their arm as they cross the line, and note it. The Race Committee may ask you what you saw.
- You have no klaxon, but <span class="key">keep an eye out</span>: if you see danger, tell the Finish Marshal at once.

---
layout: position
x: 0.357
y: 0.243
alt: "Map close-up: the Meadow Marshal (3) on the City side, between the finish and the humpback bridge to Boathouse Island"
kit: Bib, radio, clipboard, klaxon.
check: 3rd, after the Finish.
---

# (3) Meadow

On the City side, by Christ Church Meadow, between the humpback bridge and the finish.

- <span class="key">Watch the top of the course</span>, and make sure it stays clear for racing.
- Direct crews coming away from the spinning area down the transit lane to land.
- River traffic coming down from upstream: direct it into the transit lane, and make sure it doesn't leave it or cross the river without speaking to a marshal. Keep the SU informed.
- Answer questions from the public: many walkers come along the meadow.

---
layout: position
x: 0.451
y: 0.232
alt: "Map close-up: the Boathouses A Marshal (4) at the upstream half of Boathouse Island, by the landing rafts"
kit: Bib, radio, clipboard, klaxon.
check: 4th, after Meadow.
---

# (4) Boathouses A

On Boathouse Island, at the upstream half, by the <span class="key">5 landing rafts</span>. A raft marshal (see the raft marshals slide).

- Crews land with <span class="key">bows pointing downstream</span>, and may need to walk their boat along the island to reach a free raft.
- Whoever holds a landing boat holds the blade of 6 or 8, <span class="key">never 2 or 4</span>, or the stream swings the stern out into the river.
- Identity checks on landing crews, when Race Desk asks.
- Talk to river traffic near you, and keep it in the transit lane. Keep the SU informed.
- Look out for boats being carried among the public, and warn both.

<Contingency>
<ul>
<li><b>Racing stopped early:</b> crews still on land don't boat. Boathouse Island crews come home up the course and land with bows pointing upstream.</li>
</ul>
</Contingency>

---
layout: position
x: 0.560
y: 0.225
alt: "Map close-up: the Boathouses B Marshal (5) at the downstream half of Boathouse Island, by the boating rafts"
kit: Bib, radio, clipboard, klaxon.
check: 5th, after Boathouses A.
---

# (5) Boathouses B

On Boathouse Island, at the downstream half, by the <span class="key">6 boating rafts</span>. A raft marshal (see the raft marshals slide).

- Check every boat before it pushes off.
- Crews boat with <span class="key">bows pointing downstream</span>, and stay in the transit lane past the start. Warn them that Univ crews cross into the transit lane near the Cherwell Cut.
- Help the Greenbanks Marshal get crews and river traffic across the racing lanes between races.
- Tell the SU about river traffic near you, and about any equipment failure (with how long it will take to fix).

<Contingency>
<ul>
<li><b>Racing stopped early:</b> crews still on land don't boat, and waiting crews take their boats off the water.</li>
<li><b>Time trials:</b> you are also the Crossing Marshal. Crews landing at Univ wait near St John's Boathouse, on the City side, and cross to land only when you tell them.</li>
</ul>
</Contingency>

---
layout: position
x: 0.576
y: 0.211
alt: "Map close-up: the Tower Marshal (6) on a boathouse roof at the downstream end of Boathouse Island"
kit: Radio, clipboard, klaxon, green flag.
check: 6th, after Boathouses B.
---

# (6) Tower

On the roof of a boathouse at the downstream end of Boathouse Island, with the best view of the racing.
<span class="key">No high-visibility bib</span>: wear dark clothing, so your green flag stands out against it.

- <span class="key">Watch every race for safety and fairness</span>: you are the first point of contact for appeals, and you liaise with the Race Committee about them.
- Work with the Univ Marshal: tell them when a race has gone far enough past for a Univ crew to boat, and help check a raft is clear for a Univ crew to land.
- Tell the SU about river traffic.
- The best view also means the best chance to see trouble coming: klaxon early.

---
layout: position
x: 0.576
y: 0.307
alt: "Map close-up: the Univ Marshal (7) on the towpath side at University College Boathouse, just above the start"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 7th, after the Tower.
---

# (7) Univ: boating

At the University College Boathouse raft, on the towpath side, just above the start. A raft marshal (see the raft marshals slide).

- <span class="key">Speak to the SU before any crew pushes off.</span> Univ crews boat only as you direct.
- Crews boat with <span class="key">bows pointing downstream</span>. With the Tower Marshal, hold them until the race in progress has gone past, and well past: the County crew might catch a crab. Then send them straight across into the transit lane.
- In exceptional cases a crew may boat with bows pointing upstream: it spins at once, and crosses into the transit lane only when you say.
- Crews must respond promptly: Univ boating must not delay racing.

<Contingency>
<ul>
<li><b>Time trials:</b> crews push off and cross to the City side between divisions, as you direct. Keep the raft clear for landing crews.</li>
</ul>
</Contingency>

---
layout: position
x: 0.576
y: 0.307
alt: "Map close-up: the Univ Marshal (7) on the towpath side at University College Boathouse, just above the start"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 7th, after the Tower.
---

# (7) Univ: landing

- A crew landing at Univ goes down the transit lane, spins into the Marshalling Zone, and makes clear to the marshals and the SU that it wants to land.
- The SU checks with you and the Tower Marshal that a raft is clear, and tells the crew to <span class="key">follow a race up the County Station</span>.
- The crew then lands with <span class="key">bows pointing upstream</span>; help it back down onto the raft.
- Tell the SU about river traffic near you, and any equipment failures.

<Contingency>
<ul>
<li><b>Racing stopped early:</b> crews still on land don't boat. Univ crews in the Marshalling Zone land with bows pointing upstream, as you direct.</li>
<li><b>Time trials:</b> landing crews wait near St John's Boathouse and cross when the Crossing Marshal (5) says.</li>
</ul>
</Contingency>

---
layout: position
x: 0.726
y: 0.378
alt: "Map close-up: the Greenbanks Marshal (8) on the towpath side, below the start, by the Marshalling Zone"
kit: Bib, radio, clipboard, klaxon.
check: 8th, after Univ.
---

# (8) Greenbanks

On the towpath side, below the start, by the Marshalling Zone.

- <span class="key">Help crews pair up</span> with their opposition, on the correct station (City or County). Unpaired crews tuck in on the towpath side and wait.
- Crews in transit to land at Univ: hold them back while a race is in progress.
- Watch the Cherwell Cut for new river traffic, and keep the SU informed.
- Help Univ crews across the racing lanes, with the Boathouses B Marshal.

<Contingency>
<ul>
<li v-if="regatta.amber_flag_racing"><b>Low Amber Flag:</b> stand exactly where the SU directs. All crews must spin upstream of you, except crews landing at Longbridges: move on any other crew you find below you.</li>
<li><b>Time trials:</b> keep crews in the Marshalling Zone tucked in to the towpath bank, bow to stern, in the correct order.</li>
</ul>
</Contingency>

---
layout: position
x: 0.890
y: 0.434
alt: "Map close-up: the Longbridges Marshal (9) at the Longbridges raft, at the bottom of the Marshalling Zone above the Gut"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 9th, after Greenbanks.
---

# (9) Longbridges: boating

At the Longbridges Boathouse raft, at the bottom of the Marshalling Zone. A raft marshal (see the raft marshals slide).

- Check every boat before it pushes off.
- Crews boat with <span class="key">bows pointing upstream</span>, straight into the Marshalling Zone.
- Keep crews pairing up and spinning well clear of the raft, and of the bridges.
- Crews in transit to land at Univ: advise them.
- <span class="key">Intermediate course, if crews are allowed through the Gut:</span> crews may instead boat with bows pointing downstream.

<Contingency>
<ul>
<li><b>Time trials:</b> show river traffic where Holding Point B is, and tell it when it may go on upstream.</li>
</ul>
</Contingency>

---
layout: position
x: 0.890
y: 0.434
alt: "Map close-up: the Longbridges Marshal (9) at the Longbridges raft, at the bottom of the Marshalling Zone above the Gut"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 9th, after Greenbanks.
---

# (9) Longbridges: landing

- Crews come back down the transit lane, then <span class="key">spin and land with bows pointing upstream</span>, without obstructing crews entering the Marshalling Zone.
- In high stream, crews may spin above the raft and drift back to land, still with bows pointing upstream.
- To keep the raft running, you may instead tell a crew to land with bows pointing downstream.
- Tell the SU about river traffic near you, and any equipment failures.

<Contingency>
<ul>
<li><b>Racing stopped early:</b> crews still on land don't boat. Longbridges crews land as usual, as you direct.</li>
<li v-if="regatta.amber_flag_racing"><b>Low Amber Flag:</b> crews always spin above the raft, as you direct, and drift back to land with bows pointing upstream. You may not tell them to land with bows pointing downstream.</li>
</ul>
</Contingency>

---
layout: position
class: dense
x: 0.9485
y: 0.396
alt: "Map close-up: the Gut Marshal (10) at Top Gut, just below Longbridges, at the top of the Gut"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 10th, after Longbridges.
---

# (10) Gut

At Top Gut, just below Longbridges.

- <span class="key">River traffic:</span> ask craft to wait at Holding Point B until the race in progress is over. Watch for kayaks from under the bridges.
- <span class="key">Isis Boathouse crews:</span> hold them coming up until it is safe to cross into reverse circulation; going down, see that they cross into standard circulation.
- <span class="key">Intermediate course, if crews are allowed through:</span> list the crews that go down, for the SU. Hold crews coming up until it is safe to cross into the Marshalling Zone, and tell any unsure crew its opposition and station.

<Contingency>
<ul>
<li><b>Racing stopped early:</b> Isis Boathouse crews go home through the Gut, as you direct.</li>
<li v-if="regatta.amber_flag_racing"><b>Low Amber Flag:</b> no crew goes through the Gut at all.</li>
<li><b>Time trials:</b> send crews up towards the start in the correct order, when it is clear.</li>
</ul>
</Contingency>

---
layout: position
map: intermediate
x: 0.335
y: 0.646
alt: "Map close-up: the Donnington Bridge Marshal (11) just above Donnington Bridge, on the intermediate course"
kit: Bib, radio, clipboard, klaxon, loudhailer.
check: 11th, after the Gut, on the intermediate course only.
---

# (11) Donnington Bridge

Just above Donnington Bridge, <span class="key">on the intermediate course only</span> (planned for Friday and Saturday, if conditions permit).

- <span class="key">No crew goes below Donnington Bridge</span>, unless it is landing at a boathouse below it.
- Tell crews where to spin, and help them find and pair up with their opposition.
- Keep a list of crews that have paired up and headed up to the start, and tell the SU if asked.
- Keep crews to the bank on their bow side, in standard circulation, while warming up and going back up through the Gut.
- River traffic heading upstream: ask it to wait, and tell the SU, who will say when it may follow a race up.
- Answer questions from the public and from crews.

---

# Contact

- <span class="key">On the day, Race Desk:</span> Merton Small Boats bay, on the radio, or the Race Desk phone (the number is on your clipboard).
- <span class="key">Email:</span> <a :href="'mailto:' + regatta.contact.email">{{ regatta.contact.email }}</a> (Event Organisers: {{ regatta.roles.regatta_captains.name }}).
- Event plan, rules and maps: <https://tamesisregatta.org/>.
- Watch the mailing lists for announcements if conditions change: the next day's format is confirmed by 5pm.

---
layout: section
---

# Any Questions?

---
layout: section
---

# Thank you for marshalling
