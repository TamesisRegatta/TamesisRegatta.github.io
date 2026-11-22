<script setup>
// Information that applies only if something unusual happens (time trials,
// Low Amber Flag, the intermediate course, racing stopped early), set apart
// from a slide's main content in a grey dashed box, last on the slide, so the
// everyday instructions stand out. Write a list inside it as HTML (<ul><li>),
// so an item can take a v-if. A slide that is all contingency takes
// `contingency: true` in its frontmatter instead, which greys its header bar
// (global-top.vue).
defineProps({
  label: { type: String, default: 'Unlikely, but be ready' },
})
</script>

<template>
  <div class="tamesis-contingency">
    <div class="tamesis-contingency-label">{{ label }}</div>
    <slot />
  </div>
</template>

<style>
.slidev-layout .tamesis-contingency {
  margin-top: var(--flow-gap);
  padding: 0.35rem 0.8rem 0.45rem;
  background: var(--tamesis-contingency-bg);
  border: 2px dashed var(--tamesis-contingency-border);
  border-radius: 4px;
  color: var(--tamesis-contingency-text);
  font-size: 0.92em;
  line-height: 1.35;
}

.slidev-layout .tamesis-contingency-label {
  font-size: 0.72em;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.slidev-layout .tamesis-contingency :is(p, ul, ol) {
  margin: 0.15rem 0 0;
}

.slidev-layout .tamesis-contingency li + li {
  margin-top: 0.1rem;
}

.slidev-layout .tamesis-contingency li::marker {
  color: var(--tamesis-contingency-text);
}

.slidev-layout .tamesis-contingency :is(.key, b) {
  color: var(--tamesis-text);
  font-weight: 700;
}
</style>
