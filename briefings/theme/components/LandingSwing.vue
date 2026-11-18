<script setup>
// Landing at Boathouse Island, bows pointing downstream, seen from above: why
// to hold the boat from the middle or stern. Held by a bow-seat blade (held:
// 'bow'), the boat pivots on its bow and the stream swings its stern out
// into the river; held from the middle or stern (held: 'stern'), it stays
// alongside. Rafts are coloured as on the course map: landing orange,
// boating blue. Downstream is +x.
import RaceBoat from './RaceBoat.vue'

const props = defineProps({
  held: { type: String, default: 'bow' }, // bow or stern
  label: { type: String, required: true }, // the figure's accessible name
})

// Marker ids must be unique on the page, which may show both panels
const id = `landing-${props.held}`

// The boat is drawn larger than RaceBoat draws it on the course map
const ZOOM = 1.4

// Each pose's boat centre and heading, where it is held, and where that is
// labelled (clear of the blades lying on the raft)
const POSES = {
  // Pivoting on the bow, at the raft, with the stern swung out
  bow: { at: [59.3, 29.4], h: -22, hold: [68, 17.5], label: [68, 7.5] },
  // Alongside the raft, parallel to it
  stern: { at: [60, 20], h: 0, hold: [43, 17.5], label: [22, 7.5] },
}
const { at, h, hold, label: tag } = POSES[props.held]
</script>

<template>
  <svg class="landing-swing" viewBox="2 2 104 60" role="img" :aria-label="label">
    <defs>
      <marker :id="`${id}-stream`" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 Z" class="stream-head" />
      </marker>
      <marker :id="`${id}-swing`" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 Z" class="swing-head" />
      </marker>
    </defs>

    <!-- Boathouse Island, with its bank and rafts -->
    <rect class="land" x="0" y="0" width="120" height="12" />
    <line class="bank" x1="0" y1="12" x2="120" y2="12" />
    <rect class="raft landing" x="-2" y="12" width="16" height="6" />
    <rect class="raft landing" x="26" y="12" width="56" height="6" />
    <rect class="raft boating" x="96" y="12" width="26" height="6" />

    <!-- The stream, flowing downstream -->
    <text class="stream-label" x="6" y="47">Stream</text>
    <line class="stream" x1="6" y1="52" x2="28" y2="52" :marker-end="`url(#${id}-stream)`" />

    <g :transform="`translate(${at[0]} ${at[1]}) scale(${ZOOM})`">
      <RaceBoat :pose="{ x: 0, y: 0, h }" stroke="none" :phase="0" colours="linacre" />
    </g>

    <!-- How the stern swings out, pivoting on the bow -->
    <path v-if="held === 'bow'" class="swing" d="M 39.3 44.5 A 47 47 0 0 0 53 59.5" :marker-end="`url(#${id}-swing)`" />

    <!-- Where the boat is held -->
    <circle class="hold" :cx="hold[0]" :cy="hold[1]" r="2.2" />
    <text class="hold-label" :x="tag[0]" :y="tag[1]" text-anchor="middle">held here</text>
    <line class="hold-pointer" :x1="tag[0]" :y1="tag[1] + 1.5" :x2="hold[0]" :y2="hold[1] - 2.4" />
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
.landing-swing .hold { fill: var(--tamesis-yellow); stroke: #1a1a1a; stroke-width: 0.5; }
.landing-swing .hold-label { fill: #1a1a1a; font-size: 4.5px; font-weight: 600; }
.landing-swing .hold-pointer { stroke: #1a1a1a; stroke-width: 0.4; }
</style>
