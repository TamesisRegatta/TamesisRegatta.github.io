<script setup>
// A top-down schematic of an eight, for RaceCycle, after the usual pictogram
// (as on Wikipedia's "Eight (rowing)"): a slim hull, parallel-sided through
// the middle and tapering evenly to both ends, with the cox in the stern.
// The oars sweep and feather as the crew rows (utils/race-cycle.js, bladeAt),
// and lie angled back toward the stern at rest, as in the pictogram. The hull
// is drawn larger than true size against the course map (SCALE), and wider
// than a real eight's 30:1, so that it stays visible zoomed out; the oars are
// shorter, with bigger spoons. The bow points along +x before the pose's
// rotation.
import { computed } from 'vue'
import { bladeAt } from '../utils/race-cycle.js'

const props = defineProps({
  pose: { type: Object, required: true }, // { x, y, h, opacity }
  stroke: { type: String, default: 'none' }, // paddle, race or none
  phase: { type: Number, default: 0 }, // stroke cycle, 0 to 1
  colours: { type: String, default: 'linacre' }, // a key of BLADES
})

// Blade designs (from OURCs's blade colours chart), simplified to what shows
// on a small spoon: its colour, and a mark across it. The cox wears the
// club's colour too.
const BLADES = {
  linacre: { spoon: 'var(--tamesis-yellow)', edge: '#1a1a1a', mark: 'saltire', markColour: '#000', cox: 'var(--tamesis-yellow)' },
  mansfield: { spoon: '#eb1c24', edge: '#1a1a1a', mark: 'cross', markColour: '#fff000', cox: '#eb1c24' },
  plain: { spoon: '#9e9e9e', edge: '#555', mark: null, cox: '#d0d0d0' },
}
const blade = computed(() => BLADES[props.colours] || BLADES.plain)

// Seats 1 (bow) to 8 (stroke). Stroke side is port, which is the -y side when
// the boat points along +x; stroke's blade is on stroke side, and the rest
// alternate.
const SEATS = Array.from({ length: 8 }, (_, i) => {
  const seat = i + 1
  return { seat, x: 8.4 - i * 2.25, side: seat % 2 === 0 ? 'stroke' : 'bow' }
})

const HALF_BEAM = 0.8

const oars = computed(() => SEATS.map((s) => {
  const { angle, open } = bladeAt(props.stroke, props.phase)
  // Oars are drawn outward along -y (stroke side) or +y (bow side). A sweep
  // toward the stern (-x) is then an anticlockwise turn on stroke side and a
  // clockwise one on bow side, which is dir * angle either way.
  const dir = s.side === 'stroke' ? -1 : 1
  return { ...s, dir, rot: dir * angle, open }
}))

const SCALE = 1.25
const transform = computed(() => `translate(${props.pose.x} ${props.pose.y}) rotate(${props.pose.h}) scale(${SCALE})`)

// Parallel-sided from -6 to 6, tapering to small rounded ends at +-12.5.
const HULL = 'M 6 -0.8 L -6 -0.8 C -9.5 -0.8 -12.2 -0.45 -12.5 -0.2 Q -12.75 0 -12.5 0.2 '
  + 'C -12.2 0.45 -9.5 0.8 -6 0.8 L 6 0.8 C 9.5 0.8 12.2 0.45 12.5 0.2 Q 12.75 0 12.5 -0.2 '
  + 'C 12.2 -0.45 9.5 -0.8 6 -0.8 Z'
</script>

<template>
  <g :transform="transform" :opacity="pose.opacity ?? 1" class="race-boat" :class="colours">
    <g v-for="o in oars" :key="o.seat" :transform="`translate(${o.x} ${o.dir * HALF_BEAM}) rotate(${o.rot})`">
      <line class="shaft" x1="0" y1="0" :x2="0" :y2="o.dir * 5.2" />
      <g :transform="`translate(0 ${o.dir * 6.8}) scale(${o.open} 1)`">
        <rect class="spoon" x="-0.85" y="-1.6" width="1.7" height="3.2" rx="0.35" :fill="blade.spoon" :stroke="blade.edge" />
        <g v-if="blade.mark" class="mark" :stroke="blade.markColour">
          <template v-if="blade.mark === 'saltire'">
            <line x1="-0.85" y1="-1.6" x2="0.85" y2="1.6" />
            <line x1="0.85" y1="-1.6" x2="-0.85" y2="1.6" />
          </template>
          <template v-else-if="blade.mark === 'cross'">
            <line x1="0" y1="-1.05" x2="0" y2="1.05" />
            <line x1="-0.55" :y1="o.dir * 0.35" x2="0.55" :y2="o.dir * 0.35" />
          </template>
        </g>
      </g>
    </g>
    <path class="hull" :d="HULL" />
    <circle v-for="s in SEATS" :key="`r${s.seat}`" class="rower" :cx="s.x" cy="0" r="0.5" />
    <circle class="cox" cx="-10" cy="0" r="0.55" :fill="blade.cox" />
    <circle class="bow-ball" cx="12.75" cy="0" r="0.45" />
  </g>
</template>

<style>
.race-boat .hull { fill: #1a1a1a; stroke: #fff; stroke-width: 0.3; }
.race-boat .rower { fill: #8a8a8a; }
.race-boat .cox { stroke: #1a1a1a; stroke-width: 0.2; }
.race-boat .bow-ball { fill: #fff; stroke: #1a1a1a; stroke-width: 0.2; }
.race-boat .shaft { stroke: #3a3a3a; stroke-width: 0.35; }
.race-boat .spoon { stroke-width: 0.2; }
.race-boat .mark { stroke-width: 0.38; }
</style>
