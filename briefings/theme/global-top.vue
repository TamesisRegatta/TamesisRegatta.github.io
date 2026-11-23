<script setup>
import logo from '../../docs/assets/img/tamesis_logo.svg'

// Layouts that fill the slide themselves, without the header bar.
const full = ['cover', 'section', 'alert']

// The header shows the slide's title as plain text, as written, so a
// {{ regatta.year }} in a heading would show unfilled. Fill in such simple
// references to event.yml (see setup/main.ts), leaving anything else as it is.
const event = __EVENT__
function fill(title) {
  return title.replace(/\{\{\s*regatta\.([\w.]+)\s*\}\}/g,
    (whole, path) => path.split('.').reduce((value, key) => value?.[key], event) ?? whole)
}

function tag(frontmatter) {
  return frontmatter?.tag || (frontmatter?.contingency ? 'Unlikely, but be ready' : '')
}
</script>

<!-- A slide with `contingency: true` in its frontmatter (one that applies only
     if something unusual happens; see components/Contingency.vue) gets a grey
     header bar, tagged as such. Any slide can instead give its own tag, such as
     `tag: Not a safety marshal`, which keeps the black bar. -->
<template>
  <div
    v-if="!full.includes($nav.currentLayout)"
    class="tamesis-header"
    :class="{ 'tamesis-header-contingency': $nav.currentSlideRoute.meta?.slide?.frontmatter?.contingency }"
  >
    <span class="tamesis-header-title">
      {{ fill($nav.currentSlideRoute.meta?.slide?.title || '') }}
    </span>
    <span v-if="tag($nav.currentSlideRoute.meta?.slide?.frontmatter)" class="tamesis-header-tag">{{ tag($nav.currentSlideRoute.meta?.slide?.frontmatter) }}</span>
    <img :src="logo" alt="Tamesis Regatta" class="tamesis-header-logo">
  </div>
</template>

<style>
.tamesis-header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: var(--tamesis-header-height);
  background: var(--tamesis-black);
  border-bottom: 4px solid var(--tamesis-yellow);
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0 2rem;
  z-index: 10;
}

.tamesis-header-title {
  color: var(--tamesis-yellow);
  font-size: 1.75rem;
  font-weight: 600;
  margin-right: auto;
}

.tamesis-header-logo {
  height: var(--tamesis-logo-height);
}

.tamesis-header-contingency {
  background: var(--tamesis-contingency-header);
  border-bottom-style: dashed;
}

.tamesis-header-contingency .tamesis-header-tag {
  border-style: dashed;
}

.tamesis-header-tag {
  color: white;
  border: 2px solid white;
  border-radius: 4px;
  padding: 0.1rem 0.6rem;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  white-space: nowrap;
}
</style>
