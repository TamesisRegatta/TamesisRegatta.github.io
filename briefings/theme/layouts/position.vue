<script setup>
// One marshal position, for the marshal briefing: the slide's Markdown (the
// position's duties) on the left; on the right, where the position is on the
// approved map (components/MarshalLocator.vue), the kit it is given and its
// place in the river check, all from the slide's frontmatter. An `aside` slot
// (::aside:: in the slide's Markdown) adds more under them. The map's
// magnification is `mapZoom`: Slidev itself reads `zoom` in a slide's
// frontmatter, and scales the whole slide by it.
defineProps({
  map: { type: String, default: 'short' },
  x: { type: Number, required: true },
  y: { type: Number, required: true },
  mapZoom: { type: Number, default: 2.5 },
  alt: { type: String, required: true },
  kit: { type: String, default: '' },
  check: { type: String, default: '' },
})
</script>

<template>
  <div class="slidev-layout position tamesis-position">
    <div class="tamesis-position-main">
      <slot />
    </div>
    <div class="tamesis-position-aside">
      <MarshalLocator :map="map" :x="x" :y="y" :zoom="mapZoom" :alt="alt" />
      <dl class="tamesis-position-facts">
        <template v-if="kit">
          <dt>Kit</dt>
          <dd>{{ kit }}</dd>
        </template>
        <template v-if="check">
          <dt>River check</dt>
          <dd>{{ check }}</dd>
        </template>
      </dl>
      <slot name="aside" />
    </div>
  </div>
</template>

<style>
.slidev-layout.tamesis-position {
  display: grid;
  grid-template-columns: 1fr 34%;
  column-gap: 1.5rem;
  align-items: start;
  font-size: 1rem;
  line-height: 1.4;
}

.slidev-layout.tamesis-position :is(p, li) {
  line-height: 1.4;
}

.tamesis-position-main > :first-child,
.tamesis-position-main > h1:first-child + * {
  margin-top: 0;
}

.tamesis-position-facts {
  margin: 0.6rem 0 0;
  padding: 0.5rem 0.75rem;
  background: var(--tamesis-tint);
  border-left: 4px solid var(--tamesis-yellow);
  font-size: 0.9rem;
}

.tamesis-position-facts dt {
  font-weight: 700;
}

.tamesis-position-facts dd {
  margin: 0 0 0.3rem;
}
</style>
