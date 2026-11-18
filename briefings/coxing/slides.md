---
theme: ../theme
title: Coxing briefing
layout: cover
draft: true
presenters:
  - Fergus Cooper
  - Sydney Rose
when: coxing_briefing
venue: Gulbenkian Lecture Theatre
download: true
exportFilename: tamesis-coxing-briefing
favicon: /assets/img/favicon.svg
transition: fade
drawings:
  persist: false
---

Have you handed your coxing card or other photo ID in at the front?

---

# The Essentials: make sure you know...

- <span class="key">The circulation pattern: it's essential you get this right.</span>
- <span class="key">What to do in emergencies.</span>
- <span class="key">The rules of the regatta.</span>
- <span class="key">Whom to contact for issues.</span>
- Your schedule and warm-up plans.
- Who you're racing: <span v-if="regatta.draw_url">the draw is out at <a href="https://tamesisregatta.org/draw/" target="_blank" rel="noopener">tamesisregatta.org/draw</a></span><span v-else>the draw is not out yet, so watch the mailing lists for it</span>.

<br>

- <span class="key">Please read the rules and the event plan</span>: everyone on the water is expected to know them.
- All info is available at <https://tamesisregatta.org/>.

---

# This briefing will cover...

1. **Tamesis {{ regatta.year }}:** what you must know for this regatta: key information, safety, circulation and race day.
2. **Racing on the Isis:** safety and rules for any outing or event on the river.
3. **Coxing well:** general advice for preparing and racing.

---
layout: section
---

# PART 1: TAMESIS {{ regatta.year }}

What you must know for this regatta

---

# Format of the regatta

- Racing runs from noon Wednesday to Friday, and from 11am on Saturday, until half an hour before sunset.
- Every crew races a side-by-side heat on the first day.
- Lose your heat, and you race a repechage, normally the next day.
- Win your heat or repechage, and you go on to a side-by-side knock-out, up to the final.
- Unless conditions require changes, every crew gets at least two races.
- Friendly crews: in the repechage and later rounds, a competitive crew racing a friendly crew always wins.
- Conditions may change the format, and the draw, at short notice.

---

# Tamesis {{ regatta.year }} Advice

- All crews must be safe to race, and the Tamesis organisers recommend novices have been on the water at least 5 times. Crews the Senior Umpires or Event Committee judge unsafe may be asked to land, withdrawn, or disqualified.
- Only coxes that have been briefed here, or otherwise exempted may cox.
- No one may row in, or cox, more than one crew.
- If conditions dictate a change to X/S only, there may be an additional online briefing.

---

# Checks on the day

- A raft marshal checks your boat before you push off: any problems need fixing before you can boat.
- Photo ID for every member of your crew, including you: a printout of their University card or coxing licence. You may have to prove the identity of your crew and/or cox before racing or when you return.

<br>

<p class="text-center key">Lights are required on the water after 15:00 each day: crews without them will be disqualified.</p>

<p class="text-center mt-8 key">Every cox must wear a lifejacket to race</p>

---

# Safety: First priority

- Risk assessment: please read it (<https://tamesisregatta.org/risk-assessment/>).
- Medics at all times, at Race Desk and on the medical launch: find any marshal.
- If you have equipment problems, talk to a marshal as soon as possible.
- Klaxons: <span class="key">always follow marshals' instructions</span>.

---

# Race week forecast

<div class="grid grid-cols-4 gap-6 text-center text-base">
  <div>
    <p class="font-700 !mb-1">Wednesday</p>
    <ph-cloud-rain class="text-5xl mx-auto" aria-hidden="true" />
    <p class="!mt-1">Drizzle from 1pm<br>8-9&deg;C, feels like 5&deg;C<br>Gusts to 20 mph</p>
  </div>
  <div>
    <p class="font-700 !mb-1">Thursday</p>
    <ph-cloud-sun class="text-5xl mx-auto" aria-hidden="true" />
    <p class="!mt-1">Drizzle, then brighter<br>3-5&deg;C, feels like 0&deg;C<br>Gusts to 17 mph</p>
  </div>
  <div>
    <p class="font-700 !mb-1">Friday</p>
    <ph-cloud-rain class="text-5xl mx-auto" aria-hidden="true" />
    <p class="!mt-1">Drizzle all day<br>6-9&deg;C, feels like 2-5&deg;C<br>Windy, gusts to 30 mph</p>
  </div>
  <div>
    <p class="font-700 !mb-1">Saturday</p>
    <ph-cloud class="text-5xl mx-auto" aria-hidden="true" />
    <p class="!mt-1">Cloudy and dry<br>9-10&deg;C, feels like 5&deg;C<br>Breezy, gusts to 30 mph</p>
  </div>
</div>

- <span class="key">Cold all week</span>, especially on Thursday: wear warm kit, bring a dry change, and watch for hypothermia.
- Breezy on Friday and Saturday: expect crosswinds at the start.
- No thunderstorms forecast, so lightning looks unlikely.

<p class="text-sm" style="color: var(--tamesis-muted)">Our best guess a week ahead: Open-Meteo forecast for Oxford, 11:00-16:00, taken 18 November. Check again the night before you race.</p>

---

# Lightning at Tamesis

- Not yet boated: don't push off, and seek shelter.
- On the water: land as the marshals and umpires direct.
- Mid-race: the Senior Umpire decides whether you stop or finish.
- Once landed, shelter in a boathouse; no one boats again until the Senior Umpire says it is safe.

<br>

Instructions will be given by marshals if required.

---

# The river flag

- <span class="key">Red Flag: no racing.</span>
- <span v-if="regatta.amber_flag_racing" class="key">Amber Flag: no racing, except on Low Amber Flag on the last two days (next slide).</span><span v-else class="key">Amber Flag: no racing.</span>
- Dark Blue Flag: racing may continue, with S and X status coxes only, and possibly on a changed course.
- The format for the next day's racing is confirmed by 5pm each day, but racing can be called off at shorter notice if conditions get worse.
- In adverse conditions the Event Committee may let S and X coxes cox more than one crew.

---

# Low Amber Flag

<div v-if="regatta.amber_flag_racing">

- Racing may continue only on Days 3 and 4, only if there was racing on both Days 1 and 2, and only on the short course. It is never guaranteed: we will tell you by 5pm the day before.
- Coxes must be S status, or X status upgraded more than 12 months before the day.
- Every crew must have senior rowers (at least 3 full terms of rowing) at bow and 2.
- No crew may boat from or land at a boathouse below the Gut, or go through the Gut.
- All crews spin upstream of the Greenbanks Marshal, as race officials direct.
- Longbridges crews spin above their raft, as the Longbridges Marshal directs, and drift back to land with bows pointing upstream.

</div>

<div v-else>

- Racing is suspended on Amber Flag, as on Red Flag.

</div>

---

# If racing is stopped early

- Crews still in their boathouses will not boat.
- No more races are started; crews that have finished spin and land in normal circulation.
- Then the Senior Umpire and marshals send crews in the Marshalling Zone home, as quickly and safely as possible. <span class="key">This overrides normal circulation</span>:
  - Boathouse Island: cross to the City side, go up the course, and land with bows pointing upstream.
  - Univ: land with bows pointing upstream, as the Univ Marshal directs.
  - Longbridges: land as usual, as the Longbridges Marshal directs.
  - Isis Boathouse: go through the Gut as the Gut Marshal directs.
- Stay calm, and follow the marshals' instructions rather than your coach's.

---

# Circulation

- The course is the same every day with a start somewhere on the Greenbank, at or below Univ, and a finish near the Cox Stone.
- The start may move up or down the Greenbank, depending on factors such as stream and time constraints.
- Earlier rounds will be a short course, and if conditions permit we will lengthen the course in later rounds.
- Reverse circulation above the Gut: the transit lane is on the City side for the whole course, and never crosses the racing lanes.

---
layout: figure
---

<script setup>
import shortCourse from '../../docs/assets/img/circulation-short.svg'
</script>

# Short course: circulation, marshals and defibrillators

<img :src="shortCourse" alt="Short course circulation and placement of marshals, with defibrillator locations">

---

# Spinning for the regatta

- Spin where the marshals direct you.
- Nearly all your spins will be the other way to usual: row on with stroke side.
- After the race, spin where you are told, and row back close to the Meadows bank.

---

<script setup>
import rafts from '../../docs/assets/map/print/boathouse-rafts.svg'
</script>

# Boating and Landing for Boathouse Island

<div class="grid grid-cols-2 font-600">
  <div>&larr; UPSTREAM (TOWARDS HEAD)</div>
  <div class="text-right">DOWNSTREAM (TOWARDS GUT) &rarr;</div>
</div>

<img :src="rafts" alt="Boathouse Island rafts: landing on the top 5 rafts, boating from the bottom 6" class="w-full my-2">

<div class="grid grid-cols-2">
  <ul><li>You <span class="key">land</span> on the upstream 5 rafts.</li></ul>
  <ul><li>You <span class="key">boat</span> on the downstream 6 rafts.</li></ul>
</div>

<p class="text-center key">Both boating and landing, your bows point downstream.</p>

---

# Circulation (Boathouse Island)

- Boat (from downstream rafts) pointing towards the Gut and go down in the <span class="key">transit lane</span>. Be aware that there may be crews joining the transit lane near the Cherwell cut who have crossed after boating from Univ.
- <span class="key">Stay above the Gut.</span>
- Spin into the Marshalling Zone as the marshals direct, without obstructing other crews, and pair up to await racing.
- After the race, return beside the Meadow to the landing rafts, and land with bows pointing downstream.

---
clicks: 5
---

<script setup>
import boathouseIsland from './race-cycles/boathouse-island.js'
</script>

# Race cycle: Boathouse Island

<RaceCycle :route="boathouseIsland" />

---

# Circulation (Longbridges)

- Boat with your bow ball pointing upstream towards the head, directly into the Marshalling Zone.
- Pair up, and proceed upstream towards the start waiting to race.
- After the race, spin at the Head, come down by the Meadows then the boathouses, and stay in the <span class="key">transit lane</span>. Take care not to obstruct crews entering the Marshalling Zone.
- To land: spin and land with bows pointing upstream. In high stream, spin above the raft and drift back to land.
- The Longbridges Marshal may tell you to land with bows pointing downstream instead: please follow their instructions.

---
clicks: 6
---

<script setup>
import longbridges from './race-cycles/longbridges.js'
</script>

# Race cycle: Longbridges

<RaceCycle :route="longbridges" />

---

# Circulation (Univ Raft)

- Boat bow ball pointing towards the Gut. Only push off when instructed to by the Univ Marshal. Cross immediately into the <span class="key">transit lane</span>, proceed downstream along the Greenbank.
- Crews should be in their boat ready to push off before requesting permission from the Univ Marshal, who will then coordinate with the SU so that you can safely push off after a race comes past.
- Spin as the marshals direct, and pair up to await racing.
- After the race, spin at the Head, come down beside the Meadows and then the boathouses in the <span class="key">transit lane</span>, then spin into the Marshalling Zone (never through the Gut).
- Make it clear to the Marshals/Senior Umpire that you wish to land, and they will instruct you to follow a race in the County Station back to Univ, and land bows upstream.

---
clicks: 6
---

<script setup>
import univ from './race-cycles/univ.js'
</script>

# Race cycle: Univ raft

<RaceCycle :route="univ" />

---

# Circulation (Isis Boathouse)

- The event managed area runs from the Head down to Top Gut on the short course, and to Donnington Bridge on the intermediate course.
- Below that, crews must follow the OURCs rules for a standard outing.
- Head upstream in standard circulation through the Gut, and wait for the Gut Marshal's instruction before crossing to reverse circulation above it. Then find your opposition, pair up, and continue upstream towards the start.
- After the race, spin at the Head, and continue all the way downstream in the <span class="key">transit lane</span>.
- Cross to standard circulation as you enter the Gut, keeping a good lookout for crews and boats coming upstream. Land at the Isis Boathouse in any safe manner.

<p v-if="regatta.amber_flag_racing" class="key">When racing on Low Amber Flag, no crew may boat from or land at a boathouse below the Gut.</p>

---
clicks: 6
---

<script setup>
import isisBoathouse from './race-cycles/isis-boathouse.js'
</script>

# Race cycle: Isis Boathouse

<RaceCycle :route="isisBoathouse" />

---

# Transit through the Gut

- Crews based below the Gut, such as at the Isis Boathouse, may always go through the Gut, as the Gut Marshal directs<span v-if="regatta.amber_flag_racing">, except when racing on Low Amber Flag, when no crew may go through the Gut</span>.
- <span class="key">On the short course, which all time trials use, no other crew may go through the Gut.</span>
- On the intermediate course, the Senior Umpires and Race Committee may also allow other crews through the Gut, as far as Donnington Bridge. This will be made clear before each day's racing: if it isn't, you may not go through.
- When they are allowed through:
  - Any crews heading downstream along the Greenbank cross <span class="key">carefully</span> to standard circulation when entering the Gut.
  - Longbridges crews may boat with bows pointing downstream.

---
layout: figure
---

<script setup>
import intermediateCourse from '../../docs/assets/img/circulation-intermediate.svg'
</script>

# Intermediate course circulation

<img :src="intermediateCourse" alt="Intermediate course circulation and placement of marshals">

---

# Obeying the rules

- Keep clear of other crews, both while racing and while warming up.
- Please be on time for your race: late crews risk penalties or disqualification (DQ), and the Senior Umpire may award a row-over if your opponents are late. Races are timed in blocks: aim to be at the start line when your block is set to start.
- Any appeals need to follow the procedure in the rules.

---

# Side-by-side racing

Side-by-side: 'enough' buoys marking the mid-race area, and more buoys marking off the transit lane.

- County Station: along the towpath side; City Station: the middle of the river; transit lane: on the City side.

<ol type="a">
  <li>Stay <span class="key">completely</span> out of the <span class="key">transit lane</span> when racing, including blades.</li>
  <li>Stay in your lane, and don't hit the other crew, including blades.</li>
</ol>

<p class="text-center mt-8 key">Fouling (hitting another crew), interference (going into another crew's lane) or safety infringements (going into the transit lane) can result in a DQ.</p>

---

# The start

- The stagger is set by the Senior Umpire, not by you or your coach: please don't try to change it.
- Not ready? Raise your arm, and lower it as soon as you are.
- We <span class="key">will not</span> start a race if you are clearly not straight or ready, or the stagger is not right, so there's no need to panic.
- We <span class="key">will</span> start a race if you look ready and are not actively adjusting, even with a hand up, so be ready.
- The starter names the two crews, then says "Attention" and raises a red flag, then says "Go!" and drops the flag.
- If the stream is strong, the command will be shorter: listen to the SU for instructions.
- False start, or a collision straight off the start: the starter stops you both and restarts the race. Repeated false starts can mean a DQ.

---

# Let's look at the start

<div class="text-center text-2xl mt-24">

<https://www.youtube.com/watch?v=VgSArFfquNk>

</div>

---
layout: alert
class: text-center
---

<script setup>
// The klaxon sound is a file in coxing/public/media/, served from the deck's
// own base URL (see the README for its source and licence). The PDF can't
// play it, so it links to the published file instead. The exporter loads the
// deck with ?print, which with hash routing Slidev's own isPrintMode does not
// see.
const klaxon = import.meta.env.BASE_URL + 'media/klaxon.mp3'
const klaxonUrl = 'https://tamesisregatta.org' + klaxon
const inPdf = new URLSearchParams(window.location.search).has('print')
</script>

If a marshal needs to stop your race, they will fire a loud

<div class="text-8xl font-800 leading-tight my-6">KLAXON</div>

<p class="font-700">All crews on the water stop immediately, and wait for marshals' instructions.</p>

<audio v-if="!inPdf" controls preload="none" :src="klaxon" class="mx-auto mt-4"></audio>
<p v-if="inPdf" class="text-base">Listen to it: <a :href="klaxonUrl">{{ klaxonUrl }}</a></p>

---

# At the finish line

- Row through the finish line, and keep paddling until you are fully clear of it.
- It's a straight finish, with no stagger.
- The race is decided by the bows: the finish is a white post, the clacker, which clacks as each crew crosses.
- If you wish to appeal the race, raise your hand at the finish.
- Dead heat: the finish marshal tells you, and you go straight back to the start to re-row.
- Listen to marshals and stop as soon as you're asked.
- Make sure the whole crew knows when your next race is before leaving the river.

---

# Landing

- Stay upstream until a raft is free.
- Don't drift: You can back down if needed.
- If landing the wrong way from training:
  - Blades on the raft get out first.
  - Then they hold the boat for the others.

---

# Race Desk and problems

- Blade clashes in races may lead to appeals.
- Equipment failure: discuss with Racedesk as soon as possible. They may not be able to reschedule, though.
- Equipment conflicts (adjacent races): also discuss with Racedesk.
- Register <span class="key">all substitutions</span> before you boat: on the entry system up to the online deadline, then in person at Racedesk.
- A crew that races as a friendly crew stays friendly from then on.
- Racedesk is in the Merton Small Boats bay.
  - For problems on the day, try to go in person: they may not see emails in time.

---
layout: section
---

# PART 2: RACING ON THE ISIS

Safety and rules for any outing or event on the river

---

# Cold and water

- Race week looks cold: keep a lookout for hypothermia.
  - Signs: shivering; pale, cold and dry skin; slurred speech; slow breathing; tiredness or confusion.
  - Move them indoors, get them into dry clothing, and contact the medics.
  - NHS advice: <https://www.nhs.uk/conditions/hypothermia/>.
- Every crew should bring a dry change of kit for after racing.
- Coxes sit still in the cold for a long time: wear warm, waterproof layers, with your lifejacket over the top.
- Water hygiene.

---

# Lightning: 30/30 rule

- Seek shelter if the time between seeing a lightning flash and hearing thunder is 30 seconds or less.
- Shelter for 30 minutes after the last clap of thunder.
- Take care with anything long and pointy, such as blades.

---

# Lifejackets

<span class="key">Coxes lacking lifejackets:</span>

- <span class="key">£50 fine.</span>
- <span class="key">Club Safety Review.</span>

<p class="text-center mt-8">Always do your lifejacket up properly (including crotch strap) and wear it <span class="key">over</span> your coat, in line with the OURCs Code of Conduct.</p>

---

# Boat safety checks

- Bow ball: firmly attached (not just taped).
- Heel restraints and quick release: heels released before they come above horizontal, and shoes can be undone with one hand.
- Boat lights: charged.
- Hatch covers: present.
- Backstays: present.
- Bolts and fittings: tight.

---

# Bankriders

- N status coxes must have a bankrider at all times on the water. X and S status coxes may have one if they wish.
- Only one bankrider may follow each crew.
- Bankriders need a roadworthy bike with working brakes, and lights when appropriate.
- Bankriders must not hold cameras or other devices while cycling, and must give way to pedestrians.

---

# Keep to bowside

- <span class="key">Stick closely to bowside</span> in training unless overtaking: this is an existing rule. This includes entry to/exit from the Gut. Tuck back in quickly after overtaking. Practise steering close to the bank.

---
layout: section
---

# PART 3: COXING WELL

General advice for preparing and racing

---

# Getting ready to race

### The week before

- Decide warm-up plan, the start commands, and a race plan (with your coach).

### The night before

- Racing equipment (small bag of tools: adjustable spanner, screwdriver, roll of electrical tape, watch).
- Know your opposition: who are they? What do their blades look like? Are you on City or County station?
- Check the weather, and wear appropriate kit.
- Double-check timings.

---

# Race day timing

- About 3 hours before: make sure your crew has eaten.
- Agree a meeting time and place with your crew.
- About an hour before: arrive at the boathouse.
- About 30-40 minutes before: hands on (if there is space on the raft).
- 20-25 minutes before, and no earlier: push off.
- A few minutes to go: be queuing for the start and ready.
- Race time: Go!

<br>

- Aim to reach the start in good time.

---

# Warming your crew up to race

- Assume there will be no warm-up on the water.
- The crew should warm up well on land: there is no guarantee of any time to warm up on the water.
- Make sure you have practised this beforehand, and that your crew gets properly warm:
  - High heart rate.
  - Sweating.

---

# Lining up well

- Listen for the SU's instructions. Decide beforehand whether your crew will follow the SU directly or you will relay the instructions, and make sure the whole crew knows which.
- Aim for center of lane well before you get to the start line.
- Wind may push you sideways: Go to upwind side of your lane if crosswinds.
- Remember you can back down to straighten as well as row on. Please only use 1 rower at a time to adjust position.
- You may have to wait for river traffic: keep on top of position.

---

# During the race

- Your main job is steering.
- A good line can easily win you the race.
- Crashing or clashing will likely mean you lose the race.
- Look down your lane and focus on steering. Don't look directly at the next-door crew (you may veer towards them). Sneak peeks briefly.

<br>

- The next slide has some pointers on calls... this comes <span class="key">second</span> to good steering.

---

# Racing Calls

- You can prep and practice a race plan beforehand:
  - Plan a few technique points to make calls on.
  - Use a few landmarks: "passing our raft", "end of boathouses".
  - Think about what would motivate you to pull harder! Ask your crew what they would like to hear. Sound confident: rehearse before hand if you need to.
- Tell your rowers where you are: be honest but sound positive. Anyone can catch a sudden crab! Remember, in novice racing the winner is often the one who <span class="key">doesn't</span> make a mistake: see Somerville in the 2022 W final: <https://youtu.be/qIXQKo3uhL8?t=120>.

---

# After the finish

- Wind down: don't call 'easy there' or 'hold it' or say 'we've won'.
- Please don't lie down in the boat unless you are unwell: marshals may mistake it for a medical emergency.

---

# Spinning and crabs

- Row on with stroke side and back down with bow side.
- Make sure your bowsiders know how to back down!
- You may not always need to back down, especially if you are trying to cross the river while spinning.

<br>

- If you catch a crab, start rowing again asap: make sure you talk through with your crew what you are going to do if this happens.

---

# Final Training Advice

- Practice your warm-up and remember it won't be very long on water for the short course.
- Practice starts, but be careful to do them safely including stopping safely (check behind you first) and not obstructing other crews.
- Practice bursts of pressure, with pushes in.
- Practice the crew catching a crab and what you will call if it happens.

---

# Contact

- Email <a :href="'mailto:' + regatta.contact.email">{{ regatta.contact.email }}</a> (Event Organisers: {{ regatta.roles.regatta_captains.name }}).
- Race Desk: Merton Small Boats bay (please leave the SU to run the racing: appeals go through Race Desk).
- Marshals: along the racing course (see maps). Note that they may need to get permission to change race times from the Senior Umpire.
- First Aid: at Race Desk, and with all medics and medical launches.
- Rules, event plan and maps: <https://tamesisregatta.org/>.
- Keep an eye on the mailing lists for announcements if weather or conditions change: the next day's format is confirmed by 5pm.

---
layout: section
---

# Any Questions?

---
layout: section
---

# Good luck and have fun
