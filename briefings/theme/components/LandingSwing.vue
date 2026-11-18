<script setup>
// Landing at Boathouse Island, bows pointing downstream, seen from above: why
// whoever is on the raft should hold the blades of 6 or 8 rather than 2 or 4.
// Held by the bow pair's blades (held: 'bow'), the boat pivots near its bow
// and the stream swings its stern out into the river; held by 6's and 8's
// (held: 'stern'), it stays alongside. Rafts are coloured as on the course
// map: landing orange, boating blue. Downstream is +x.
import { REST } from '../utils/race-cycle.js'
import RaceBoat from './RaceBoat.vue'

const props = defineProps({
  held: { type: String, default: 'bow' }, // bow or stern
  label: { type: String, required: true }, // the figure's accessible name
})

// Marker ids must be unique on the page, which may show both panels
const id = `landing-${props.held}`

// The boat is drawn larger than RaceBoat draws it on the course map
const ZOOM = 1.4
const BOAT_SCALE = 1.25 // RaceBoat's own SCALE

// Each pose's boat centre and heading, the seats whose blades are held, and
// where "held here" is written (on the island, above the rafts)
const POSES = {
  // Pivoting near the bow, at the raft, with the stern swung out
  bow: { at: [59.3, 27.9], h: -22, seats: [2, 4], label: [56.5, -1] },
  // Alongside the raft, parallel to it
  stern: { at: [60, 20], h: 0, seats: [6, 8], label: [46, -1] },
}
const { at, h, seats, label: tag } = POSES[props.held]

// Where a stroke-side seat's spoon lies at rest, as RaceBoat draws it: the
// oar leaves the rigger (seat x, -0.8) along -y, swept REST degrees toward
// the stern, with the spoon's middle 6.8 along it.
function spoon(seat) {
  const r = REST * Math.PI / 180
  const local = [8.4 - (seat - 1) * 2.25 - 6.8 * Math.sin(r), -0.8 - 6.8 * Math.cos(r)]
  const k = ZOOM * BOAT_SCALE
  const t = h * Math.PI / 180
  return [
    at[0] + k * (local[0] * Math.cos(t) - local[1] * Math.sin(t)),
    at[1] + k * (local[0] * Math.sin(t) + local[1] * Math.cos(t)),
  ]
}
const holds = seats.map(spoon)
const RING = 3.8
</script>

<template>
  <svg class="landing-swing" viewBox="2 -6 104 66" role="img" :aria-label="label">
    <defs>
      <marker :id="`${id}-stream`" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 Z" class="stream-head" />
      </marker>
      <marker :id="`${id}-swing`" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 Z" class="swing-head" />
      </marker>
    </defs>

    <!-- Boathouse Island, with its bank and rafts -->
    <rect class="land" x="0" y="-6" width="120" height="10" />
    <line class="bank" x1="0" y1="4" x2="120" y2="4" />
    <rect class="raft landing" x="-2" y="4" width="16" height="14" />
    <rect class="raft landing" x="26" y="4" width="56" height="14" />
    <rect class="raft boating" x="96" y="4" width="26" height="14" />

    <!-- The stream, flowing downstream -->
    <text class="stream-label" x="6" y="47">Stream</text>
    <line class="stream" x1="6" y1="52" x2="28" y2="52" :marker-end="`url(#${id}-stream)`" />

    <g :transform="`translate(${at[0]} ${at[1]}) scale(${ZOOM})`">
      <RaceBoat :pose="{ x: 0, y: 0, h }" stroke="none" :phase="0" colours="linacre" />
    </g>

    <!-- How the stern swings out, pivoting near the bow -->
    <path v-if="held === 'bow'" class="swing" d="M 39.3 43 A 47 47 0 0 0 53 58" :marker-end="`url(#${id}-swing)`" />

    <!-- The blades held from the raft -->
    <circle v-for="(p, i) in holds" :key="i" class="hold" :cx="p[0]" :cy="p[1]" :r="RING" />
    <text class="hold-label" :x="tag[0]" :y="tag[1]" text-anchor="middle">held here</text>
    <line
      v-for="(p, i) in holds" :key="`l${i}`" class="hold-pointer"
      :x1="tag[0]" :y1="tag[1] + 1" :x2="p[0]" :y2="p[1] - RING"
    />
  </svg>
</template>

<style>
.landing-swing { width: 100%; height: auto; display: block; }
.landing-swing .land { fill: #f2f2f2; }
.landing-swing .bank { stroke: #1a1a1a; stroke-width: 0.6; }
.landing-swing .raft { stroke: #1a1a1a; stroke-width: 0.5; }
.landing-swing .raft.landing { fill: #ffa500; }
.landing-swing .raft.boating { fill: #1f3fe0; }
.landing-swing .stream { stroke: #2f55d4; stroke-width: 1.6; }
.landing-swing .stream-head { fill: #2f55d4; }
.landing-swing .stream-label { fill: #2f55d4; font-size: 6px; font-weight: 600; }
.landing-swing .swing { fill: none; stroke: #1a1a1a; stroke-width: 1.2; }
.landing-swing .swing-head { fill: #1a1a1a; }
.landing-swing .hold { fill: none; stroke: #1a1a1a; stroke-width: 0.8; }
.landing-swing .hold-label { fill: #1a1a1a; font-size: 4.5px; font-weight: 600; }
.landing-swing .hold-pointer { stroke: #1a1a1a; stroke-width: 0.4; }
</style>
