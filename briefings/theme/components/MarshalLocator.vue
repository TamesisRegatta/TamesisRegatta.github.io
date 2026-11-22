<script setup>
// A close-up of one of the approved circulation maps (docs/assets/img/, the
// maps in the event plan's Appendix 3), centred on one marshal position and
// ringed, for the marshal briefing's position slides (layouts/position.vue).
// `x` and `y` give the marker's position as fractions of the whole map's width
// and height; `zoom` is how many frame widths wide the map is drawn. Near the
// map's edges the view stops at the edge, and the ring moves off centre.
import { computed } from 'vue'
import short from '../../../docs/assets/img/circulation-short.svg'
import intermediate from '../../../docs/assets/img/circulation-intermediate.svg'
import timeTrial from '../../../docs/assets/img/circulation-time-trial.svg'

// Height over width, from each SVG's viewBox
const maps = {
  'short': { src: short, aspect: 2922.296 / 5229.451 },
  'intermediate': { src: intermediate, aspect: 2922.296 / 5229.451 },
  'time-trial': { src: timeTrial, aspect: 2834.6458 / 5102.3625 },
}

const props = defineProps({
  map: { type: String, default: 'short' },
  x: { type: Number, required: true },
  y: { type: Number, required: true },
  zoom: { type: Number, default: 3 },
  alt: { type: String, required: true },
})

// The frame's height, in frame widths (4:3)
const FRAME = 0.75

// Everything in frame widths, shown as cqw (the frame is the container)
const view = computed(() => {
  const m = maps[props.map]
  if (!m)
    throw new Error(`[tamesis] MarshalLocator: no map "${props.map}"`)
  const w = props.zoom
  const h = props.zoom * m.aspect
  const clamp = (v, lo, hi) => Math.min(Math.max(v, lo), hi)
  const left = clamp(0.5 - props.x * w, 1 - w, 0)
  const top = clamp(FRAME / 2 - props.y * h, FRAME - h, 0)
  return { src: m.src, w, left, top, ringX: left + props.x * w, ringY: top + props.y * h }
})

const cqw = v => `${(v * 100).toFixed(3)}cqw`
</script>

<template>
  <div class="marshal-locator" role="img" :aria-label="alt">
    <img :src="view.src" alt="" :style="{ width: cqw(view.w), left: cqw(view.left), top: cqw(view.top) }">
    <span class="marshal-locator-ring" :style="{ left: cqw(view.ringX), top: cqw(view.ringY) }" />
  </div>
</template>

<style>
.marshal-locator {
  container-type: inline-size;
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  background: white;
  border: 2px solid var(--tamesis-black);
  border-radius: 4px;
}

.slidev-layout .marshal-locator img {
  position: absolute;
  max-width: none;
  margin: 0;
}

.marshal-locator-ring {
  position: absolute;
  width: 20cqw;
  height: 20cqw;
  transform: translate(-50%, -50%);
  border: 5px solid #c62828;
  border-radius: 50%;
}
</style>
