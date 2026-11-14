<script setup>
// An animated race cycle on the short course map: one boathouse's crew from
// pushing off to landing, one stage per click. See coxing/race-cycles/ for
// the routes, and utils/race-cycle.js for the timeline maths.
//
// Each click plays the next stage; any other jump (back, or straight to a
// slide part-way through) shows the end of that stage at once, as does
// everything when the viewer prefers reduced motion. The PDF shows the whole
// route, with stage numbers, on the overview.
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import mapSource from '../../../docs/assets/map/print/course-short.svg?raw'
import RaceBoat from './RaceBoat.vue'
import { compile, cuesAt, poseAt, RATES } from '../utils/race-cycle.js'
import { inPdf } from '../utils/print.js'

const props = defineProps({
  route: { type: Object, required: true },
})

// The map's contents without its outer <svg>, to sit in ours, whose viewBox
// is the camera.
const mapInner = mapSource.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '')

const stages = compile(props.route)
const boatNames = Object.keys(props.route.boats)
const lead = boatNames[0]
const last = stages.length - 1
const pdf = inPdf()

const { $clicks, $renderContext } = useSlideContext()

const stageIdx = ref(0)
const t = ref(0)
const box = ref(null)
const aspect = ref(2.3)
const cam = ref({ x: 0, y: 0, w: 1000 })

const stage = computed(() => stages[stageIdx.value])

const boats = computed(() => boatNames.map((name) => {
  const p = poseAt(stage.value, name, t.value)
  const rate = RATES[p.stroke] || 0
  return { name, pose: p, stroke: p.stroke, phase: (p.segT * rate) % 1, colours: props.route.boats[name].colours }
}))

const cues = computed(() => cuesAt(stage.value, t.value))

function cameraAt(i, time) {
  const c = stages[i].camera
  if (c.follow) {
    const p = poseAt(stages[i], c.follow, time)
    return { x: p.x + (c.offset?.[0] || 0), y: p.y + (c.offset?.[1] || 0), w: c.w }
  }
  return { x: c.at[0], y: c.at[1], w: c.w }
}

const viewBox = computed(() => {
  const { x, y, w } = cam.value
  const h = w / aspect.value
  return `${x - w / 2} ${y - h / 2} ${w} ${h}`
})

// The lead crew's route, sampled once, for the trail behind it and the PDF.
const samples = []
for (let i = 1; i <= last; i++) {
  for (let tt = 0; tt <= stages[i].dur + 1e-9; tt += 0.1) {
    const p = poseAt(stages[i], lead, tt)
    samples.push({ i, t: tt, x: p.x, y: p.y })
  }
}
const trail = computed(() => samples
  .filter(s => pdf || s.i < stageIdx.value || (s.i === stageIdx.value && s.t <= t.value))
  .map(s => `${s.x.toFixed(1)},${s.y.toFixed(1)}`).join(' '))
const markers = stages.slice(1).map((s, k) => ({ n: k + 1, ...s.boats[lead].start }))

let raf = 0
let lastTs = 0
function stop() {
  cancelAnimationFrame(raf)
  raf = 0
}

function frame(ts) {
  const dt = Math.min(0.1, (ts - lastTs) / 1000)
  lastTs = ts
  const dur = stage.value.dur
  t.value = Math.min(dur, t.value + dt)
  // The camera eases toward where it should be, so cuts between stages and
  // changes of zoom glide rather than jump.
  const want = cameraAt(stageIdx.value, t.value)
  const k = 1 - Math.exp(-dt / 0.45)
  const c = cam.value
  const w = Math.exp(Math.log(c.w) + (Math.log(want.w) - Math.log(c.w)) * k)
  cam.value = { x: c.x + (want.x - c.x) * k, y: c.y + (want.y - c.y) * k, w }
  const settled = Math.abs(want.x - c.x) < 0.5 && Math.abs(want.y - c.y) < 0.5 && Math.abs(want.w / c.w - 1) < 0.005
  if (t.value >= dur && settled)
    raf = 0
  else
    raf = requestAnimationFrame(frame)
}

function show(i, play) {
  stop()
  stageIdx.value = Math.max(0, Math.min(last, i))
  if (play) {
    t.value = 0
    lastTs = performance.now()
    raf = requestAnimationFrame(frame)
  }
  else {
    t.value = stage.value.dur
    cam.value = cameraAt(stageIdx.value, t.value)
  }
}

const reduced = typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches

// Slidev can step the click count up one at a time when a slide is opened
// part-way through (from a URL, or the overview), so only a single step
// forward once the slide has been showing for a moment counts as a click.
let settledAt = Infinity
function animates() {
  return !pdf && !reduced && ['slide', 'presenter'].includes($renderContext.value)
    && performance.now() > settledAt
}

let pending = 0
watch($clicks, (n, old) => {
  clearTimeout(pending)
  if (animates() && n === old + 1) {
    show(n, true)
  }
  else {
    show(n, false)
    settledAt = Infinity
    pending = setTimeout(() => (settledAt = performance.now()), 400)
  }
})

let observer
onMounted(() => {
  observer = new ResizeObserver(([entry]) => {
    const { width, height } = entry.contentRect
    if (width && height)
      aspect.value = width / height
  })
  observer.observe(box.value)
  if (pdf)
    cam.value = cameraAt(0, 0)
  show(pdf ? 0 : $clicks.value, false)
  pending = setTimeout(() => (settledAt = performance.now()), 400)
})
onBeforeUnmount(() => {
  clearTimeout(pending)
  stop()
  observer?.disconnect()
})

const caption = computed(() => stages[pdf ? 0 : stageIdx.value])
const su = props.route.starter
</script>

<template>
  <div class="race-cycle">
    <div ref="box" class="race-cycle-frame">
      <svg class="race-cycle-map" :viewBox="viewBox" preserveAspectRatio="xMidYMid slice" role="img" :aria-label="route.title">
        <g class="race-cycle-base" v-html="mapInner" />
        <polyline class="race-cycle-trail" :points="trail" />
        <g v-if="su && cues.flag" class="race-cycle-flag" :transform="`translate(${su[0] + 6} ${su[1] - 2})`">
          <line x1="0" y1="0" x2="0" y2="-10" />
          <rect v-if="cues.flag === 'raised'" x="0" y="-10" width="6" height="4" />
          <rect v-else x="-0.4" y="-4" width="4" height="6" transform="rotate(30 0 -4)" />
        </g>
        <text v-if="su && cues.call" class="race-cycle-call" :x="su[0] + 13" :y="su[1] + 3">{{ cues.call }}</text>
        <RaceBoat
          v-for="b in boats" :key="b.name"
          :pose="b.pose" :stroke="b.stroke" :phase="b.phase" :colours="b.colours"
        />
        <g v-if="pdf" class="race-cycle-markers">
          <g v-for="m in markers" :key="m.n" :transform="`translate(${m.x} ${m.y - 16})`">
            <circle r="10" />
            <text y="4">{{ m.n }}</text>
          </g>
        </g>
      </svg>
      <div class="race-cycle-credit">Map adapted from Oxford Isis Maps by Bernard Tao, CC BY 3.0</div>
    </div>
    <div class="race-cycle-caption">
      <template v-if="pdf">
        <strong>{{ route.title }}.</strong> {{ route.summary }}
      </template>
      <template v-else>
        <span class="race-cycle-step">{{ stageIdx }}/{{ last }}</span>
        <strong>{{ caption.title }}:</strong> {{ caption.text }}
      </template>
    </div>
  </div>
</template>

<style>
.race-cycle {
  position: absolute;
  top: var(--tamesis-header-height);
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  background: var(--tamesis-bg);
}

.race-cycle-frame {
  position: relative;
  flex: 1;
  min-height: 0;
  overflow: hidden;
}

.race-cycle-map {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

/* Parts of the printed map that the animation doesn't need: its title, keys,
   attribution box (credited below the map instead), and the inset of the
   river below the Gut. (No "&" in these selectors, even quoted: the CSS
   nesting step reads it as the parent selector and drops the rule.) */
.race-cycle :is([data-label="Title"], [data-label="Tamesis Key"], [data-label="AED Key Both"],
  [data-label^="Disclaimer"], [data-label="Bottom Half"], [data-label="AED Bottom Half"],
  [data-label="Riverside-AED"], [data-label="Falcon-AED"], [data-label="LB-AED-Bottom"],
  [data-label="10 Top Gut"], [data-label="09 Longbridges (bottom half)"],
  [data-label="Isis Boathouse Crews Only"], [data-label="Mooring Point B"], [data-label="Mooring Point B Circle"]),
.race-cycle #g443, .race-cycle #text412, .race-cycle #text413 {
  /* !important, as many of the map's groups set display:inline in a style
     attribute, which would win otherwise. */
  display: none !important;
}

/* The map's own arrows stay as a faint guide under the moving boats. */
.race-cycle [data-label="Circulation Arrows"] > path {
  opacity: 0.35;
}

.race-cycle-trail {
  fill: none;
  stroke: var(--tamesis-black);
  stroke-width: 1;
  stroke-dasharray: 2.5 2;
  opacity: 0.55;
}

.race-cycle-flag line { stroke: #333; stroke-width: 0.6; }
.race-cycle-flag rect { fill: #d32f2f; }

.race-cycle-call {
  font-size: 7px;
  font-weight: 800;
  fill: #b71c1c;
  stroke: #fff;
  stroke-width: 1.6px;
  paint-order: stroke;
}

.race-cycle-markers circle { fill: var(--tamesis-black); stroke: var(--tamesis-yellow); stroke-width: 1.2; }
.race-cycle-markers text { fill: var(--tamesis-yellow); font-size: 12px; font-weight: 800; text-anchor: middle; }

.race-cycle-credit {
  position: absolute;
  right: 0.5rem;
  bottom: 0.3rem;
  font-size: 0.6rem;
  color: var(--tamesis-muted);
  background: rgb(255 255 255 / 0.85);
  padding: 0 0.3rem;
}

.race-cycle-caption {
  min-height: 3.6rem;
  padding: 0.55rem 1.5rem;
  background: var(--tamesis-tint);
  border-top: 3px solid var(--tamesis-yellow);
  font-size: 1.05rem;
  line-height: 1.35;
}

.race-cycle-step {
  display: inline-block;
  margin-right: 0.6rem;
  padding: 0 0.45rem;
  background: var(--tamesis-black);
  color: var(--tamesis-yellow);
  font-weight: 700;
  border-radius: 3px;
}
</style>
