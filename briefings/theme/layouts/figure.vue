<script setup>
// One image (or component, in the default slot) filling the slide under the
// header bar, for maps and diagrams. `image` is a URL; import local files in
// the slide instead, so Vite bundles them. An `aside` slot (::aside:: in the
// slide's Markdown) puts a narrow text column beside the figure.
defineProps({
  image: { type: String, default: '' },
  alt: { type: String, default: '' },
})
</script>

<template>
  <div class="slidev-layout figure tamesis-figure">
    <div class="tamesis-figure-main">
      <img v-if="image" :src="image" :alt="alt">
      <slot />
    </div>
    <div v-if="$slots.aside" class="tamesis-figure-aside">
      <slot name="aside" />
    </div>
  </div>
</template>

<style>
.slidev-layout.tamesis-figure {
  display: flex;
  gap: 1.5rem;
  height: 100%;
  padding-bottom: 1rem;
}

.tamesis-figure-main {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.tamesis-figure-main img,
.tamesis-figure-main svg,
.tamesis-figure-main video {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.tamesis-figure-aside {
  flex: 0 0 30%;
  font-size: 1rem;
  align-self: center;
}
</style>
