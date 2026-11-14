---
theme: ../theme
title: Coxing briefing
layout: cover
presenters:
  - Fergus Cooper
  - Sydney Rose
when: coxing_briefing
venue: Gulbenkian Lecture Theatre
download: true
exportFilename: tamesis-coxing-briefing
favicon: /assets/img/favicon.svg
transition: fade
drawings:
  persist: false
---

---
layout: section
---

# Placeholder

The 2026 briefing will be ported here.

---

# Key facts

- The coxing briefing is on {{ ukdatetime(regatta.dates.coxing_briefing) }}.
- Racing is from {{ ukdate(regatta.dates.regatta_start) }} to {{ ukdate(regatta.dates.regatta_end) }}.
- The {{ regatta.roles.captain_of_coxes.title }} is {{ regatta.roles.captain_of_coxes.name }}.
- Contact: <a :href="'mailto:' + regatta.contact.email">{{ regatta.contact.email }}</a>
- <span v-if="regatta.amber_flag_racing">Racing may continue on Low Amber Flag.</span><span v-else>Racing is suspended on Amber Flag.</span>

---
layout: figure
---

<script setup>
import circulation from '../../docs/assets/img/circulation-short.svg'
</script>

# Circulation: short course

<img :src="circulation" alt="Circulation pattern for the short course">

::aside::

This map is the website's own file, so the deck and the event plan show the same thing.

---
layout: alert
---

# Lifejackets

- Wear it over your coat, done up properly, crotch strap included.
- No lifejacket, no racing.
