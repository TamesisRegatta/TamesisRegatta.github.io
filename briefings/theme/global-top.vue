<script setup>
import logo from '../../docs/assets/img/tamesis_logo.svg'

// Layouts that fill the slide themselves, without the header bar.
const full = ['cover', 'section', 'alert']
</script>

<template>
  <div v-if="!full.includes($nav.currentLayout)" class="tamesis-header">
    <span class="tamesis-header-title">
      {{ $nav.currentSlideRoute.meta?.slide?.title || '' }}
    </span>
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
  justify-content: space-between;
  padding: 0 2rem;
  z-index: 10;
}

.tamesis-header-title {
  color: var(--tamesis-yellow);
  font-size: 1.75rem;
  font-weight: 600;
}

.tamesis-header-logo {
  height: var(--tamesis-logo-height);
}
</style>
