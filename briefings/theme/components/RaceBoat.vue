<script setup>
// A top-down schematic of an eight, for RaceCycle. The hull is drawn larger
// than true size against the course map (SCALE), and the oars shorter with
// bigger spoons, so the blades can be seen while two boats still fit side by
// side in the racing lanes. The bow points along +x before the pose's
// rotation.
import { computed } from 'vue'
import { bladeAt } from '../utils/race-cycle.js'

const props = defineProps({
  pose: { type: Object, required: true }, // { x, y, h, opacity }
  stroke: { type: String, default: 'none' }, // paddle, race, spin or none
  phase: { type: Number, default: 0 }, // stroke cycle, 0 to 1
  colours: { type: String, default: 'linacre' }, // linacre or plain
})

// Seats 1 (bow) to 8 (stroke). Stroke side is port, which is the -y side when
// the boat points along +x; stroke's blade is on stroke side, and the rest
// alternate.
const SEATS = Array.from({ length: 8 }, (_, i) => {
  const seat = i + 1
  return { seat, x: 8.4 - i * 2.25, side: seat % 2 === 0 ? 'stroke' : 'bow' }
})

const oars = computed(() => SEATS.map((s) => {
  const { angle, open } = bladeAt(props.stroke, props.phase, s.side)
  // Oars are drawn outward along -y (stroke side) or +y (bow side). A sweep
  // toward the stern (-x) is then an anticlockwise turn on stroke side and a
  // clockwise one on bow side, which is dir * angle either way.
  const dir = s.side === 'stroke' ? -1 : 1
  return { ...s, dir, rot: dir * angle, open }
}))

const SCALE = 1.25
const transform = computed(() => `translate(${props.pose.x} ${props.pose.y}) rotate(${props.pose.h}) scale(${SCALE})`)
</script>

<template>
  <g :transform="transform" :opacity="pose.opacity ?? 1" class="race-boat" :class="colours">
    <g v-for="o in oars" :key="o.seat" :transform="`translate(${o.x} ${o.dir * 1.1}) rotate(${o.rot})`">
      <line class="rigger" x1="0" :y1="0" x2="0" :y2="o.dir * 1.6" />
      <line class="shaft" x1="0" :y1="o.dir * 1.6" x2="0" :y2="o.dir * 5.2" />
      <g :transform="`translate(0 ${o.dir * 6.8}) scale(${o.open} 1)`">
        <rect class="spoon" x="-0.85" y="-1.6" width="1.7" height="3.2" rx="0.35" />
        <template v-if="colours === 'linacre'">
          <line class="saltire" x1="-0.85" y1="-1.6" x2="0.85" y2="1.6" />
          <line class="saltire" x1="0.85" y1="-1.6" x2="-0.85" y2="1.6" />
        </template>
      </g>
    </g>
    <path class="hull" d="M 12.5 0 Q 7 -1.25 -9 -1.25 Q -11.5 -1.1 -12 0 Q -11.5 1.1 -9 1.25 Q 7 1.25 12.5 0 Z" />
    <circle v-for="s in SEATS" :key="`r${s.seat}`" class="rower" :cx="s.x" cy="0" r="0.6" />
    <circle class="cox" cx="-10" cy="0" r="0.75" />
    <circle class="bow-ball" cx="12.7" cy="0" r="0.55" />
  </g>
</template>

<style>
.race-boat .hull { fill: #1a1a1a; stroke: #fff; stroke-width: 0.35; }
.race-boat .rower { fill: #8a8a8a; }
.race-boat .cox { fill: var(--tamesis-yellow); stroke: #1a1a1a; stroke-width: 0.25; }
.race-boat.plain .cox { fill: #d0d0d0; }
.race-boat .bow-ball { fill: #fff; stroke: #1a1a1a; stroke-width: 0.25; }
.race-boat .rigger { stroke: #6b6b6b; stroke-width: 0.35; }
.race-boat .shaft { stroke: #3a3a3a; stroke-width: 0.35; }
.race-boat .spoon { fill: var(--tamesis-yellow); stroke: #1a1a1a; stroke-width: 0.2; }
.race-boat .saltire { stroke: #000; stroke-width: 0.38; }
.race-boat.plain .spoon { fill: #9e9e9e; stroke: #555; }
</style>
