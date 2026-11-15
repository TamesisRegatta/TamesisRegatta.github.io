<script setup>
// A top-down schematic of an eight, for RaceCycle, after the usual pictogram
// (as on Wikipedia's "Eight (rowing)"): a slim hull, parallel-sided through
// the middle and tapering evenly to both ends, with the oars angled back
// toward the stern in alternate pairs and the cox in the stern. The hull is
// drawn larger than true size against the course map (SCALE), and wider than
// a real eight's 30:1, so that it stays visible zoomed out; the oars are
// shorter, with bigger spoons. The bow points along +x before the pose's
// rotation.
import { computed } from 'vue'

const props = defineProps({
  pose: { type: Object, required: true }, // { x, y, h, opacity }
  colours: { type: String, default: 'linacre' }, // linacre or plain
})

// Seats 1 (bow) to 8 (stroke). Stroke side is port, which is the -y side when
// the boat points along +x; stroke's blade is on stroke side, and the rest
// alternate.
const SEATS = Array.from({ length: 8 }, (_, i) => {
  const seat = i + 1
  return { seat, x: 8.4 - i * 2.25, dir: seat % 2 === 0 ? -1 : 1 }
})

const HALF_BEAM = 0.8
// How far each oar is angled back from square, toward the stern.
const BACK = 25

const SCALE = 1.25
const transform = computed(() => `translate(${props.pose.x} ${props.pose.y}) rotate(${props.pose.h}) scale(${SCALE})`)

// Parallel-sided from -6 to 6, tapering to small rounded ends at +-12.5.
const HULL = 'M 6 -0.8 L -6 -0.8 C -9.5 -0.8 -12.2 -0.45 -12.5 -0.2 Q -12.75 0 -12.5 0.2 '
  + 'C -12.2 0.45 -9.5 0.8 -6 0.8 L 6 0.8 C 9.5 0.8 12.2 0.45 12.5 0.2 Q 12.75 0 12.5 -0.2 '
  + 'C 12.2 -0.45 9.5 -0.8 6 -0.8 Z'
</script>

<template>
  <g :transform="transform" :opacity="pose.opacity ?? 1" class="race-boat" :class="colours">
    <g v-for="s in SEATS" :key="s.seat" :transform="`translate(${s.x} ${s.dir * HALF_BEAM}) rotate(${s.dir * BACK})`">
      <line class="shaft" x1="0" y1="0" :x2="0" :y2="s.dir * 5.2" />
      <g :transform="`translate(0 ${s.dir * 6.8})`">
        <rect class="spoon" x="-0.85" y="-1.6" width="1.7" height="3.2" rx="0.35" />
        <template v-if="colours === 'linacre'">
          <line class="saltire" x1="-0.85" y1="-1.6" x2="0.85" y2="1.6" />
          <line class="saltire" x1="0.85" y1="-1.6" x2="-0.85" y2="1.6" />
        </template>
      </g>
    </g>
    <path class="hull" :d="HULL" />
    <circle v-for="s in SEATS" :key="`r${s.seat}`" class="rower" :cx="s.x" cy="0" r="0.5" />
    <circle class="cox" cx="-10" cy="0" r="0.55" />
    <circle class="bow-ball" cx="12.75" cy="0" r="0.45" />
  </g>
</template>

<style>
.race-boat .hull { fill: #1a1a1a; stroke: #fff; stroke-width: 0.3; }
.race-boat .rower { fill: #8a8a8a; }
.race-boat .cox { fill: var(--tamesis-yellow); stroke: #1a1a1a; stroke-width: 0.2; }
.race-boat.plain .cox { fill: #d0d0d0; }
.race-boat .bow-ball { fill: #fff; stroke: #1a1a1a; stroke-width: 0.2; }
.race-boat .shaft { stroke: #3a3a3a; stroke-width: 0.35; }
.race-boat .spoon { fill: var(--tamesis-yellow); stroke: #1a1a1a; stroke-width: 0.2; }
.race-boat .saltire { stroke: #000; stroke-width: 0.38; }
.race-boat.plain .spoon { fill: #9e9e9e; stroke: #555; }
</style>
