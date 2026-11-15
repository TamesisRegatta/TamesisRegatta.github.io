<script setup>
import { computed } from 'vue'
import logo from '../../../docs/assets/img/tamesis_logo.svg'
import { ukdatetime } from '../utils/dates.js'

const event = __EVENT__

// `when` names a key in event.yml's dates (e.g. coxing_briefing), and `venue`
// is free text; both are shown under the title when set. `draft: true` puts
// a "not for circulation" band across the top, on screen and in the PDF.
const props = defineProps({
  presenters: { type: Array, default: null },
  when: { type: String, default: '' },
  venue: { type: String, default: '' },
  draft: { type: Boolean, default: false },
})

const presenters = computed(() => (props.presenters || []).join(' and '))

const when = computed(() => {
  if (!props.when)
    return ''
  if (!(props.when in event.dates))
    throw new Error(`[tamesis] cover: no date "${props.when}" in event.yml`)
  return ukdatetime(event.dates[props.when])
})
</script>

<template>
  <div class="slidev-layout cover tamesis-cover">
    <p v-if="draft" class="tamesis-cover-draft" role="note">
      Draft: not yet final and not for circulation
    </p>
    <img :src="logo" alt="Tamesis Regatta" class="tamesis-cover-logo">
    <div class="tamesis-cover-content">
      <p class="tamesis-cover-event">Tamesis Regatta {{ event.year }}</p>
      <h1>{{ $slidev.configs.title }}</h1>
      <p v-if="presenters" class="tamesis-cover-presenters">{{ presenters }}</p>
      <p v-if="when || venue" class="tamesis-cover-when">
        {{ [when, venue].filter(Boolean).join(', ') }}
      </p>
      <slot />
    </div>
  </div>
</template>

<style>
.tamesis-cover {
  background: var(--tamesis-black);
  color: white;
  display: grid;
  grid-template-columns: auto 1fr;
  column-gap: 3rem;
  align-items: center;
  padding: 3rem 3.5rem;
  height: 100%;
  position: relative;
}

.tamesis-cover-draft {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  margin: 0;
  padding: 0.6rem 1rem;
  background: #c62828;
  color: white;
  font-size: 1.3rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-align: center;
  text-transform: uppercase;
}

.tamesis-cover-logo {
  height: 260px;
}

.tamesis-cover-content {
  border-left: 4px solid var(--tamesis-yellow);
  padding-left: 2rem;
}

.tamesis-cover-event {
  color: var(--tamesis-yellow);
  font-size: 1.4rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.tamesis-cover h1 {
  color: white;
  font-size: 3.2rem;
  font-weight: 700;
  line-height: 1.15;
  margin: 0.4rem 0 1rem;
}

.tamesis-cover-presenters {
  font-size: 1.25rem;
}

.tamesis-cover-when {
  font-size: 1.1rem;
  opacity: 0.8;
}

/* Anything in the cover slide's own Markdown, such as a reminder for the
   audience, shown in yellow under the title block. */
.tamesis-cover-content p:not([class]) {
  color: var(--tamesis-yellow);
  font-size: 1.2rem;
  font-weight: 600;
  margin-top: 1.5rem;
}
</style>
