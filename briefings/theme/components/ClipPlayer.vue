<script setup>
// A video clip from the deck's public/media/, with its poster frame (the same
// name, as .jpg) shown until it plays. Nothing loads until someone presses
// play. The PDF can't play it, so it shows the poster frame and links to the
// published clip instead.
import { inPdf } from '../utils/print.js'

const props = defineProps({
  name: { type: String, required: true }, // file name in public/media/, without .mp4
  alt: { type: String, required: true }, // what the poster frame shows, for the PDF
})

const base = import.meta.env.BASE_URL + 'media/' + props.name
const published = 'https://tamesisregatta.org' + base + '.mp4'
const pdf = inPdf()
</script>

<template>
  <div class="clip-player">
    <video v-if="!pdf" controls preload="none" :poster="base + '.jpg'" :src="base + '.mp4'" />
    <template v-else>
      <img :src="base + '.jpg'" :alt="alt">
      <p class="text-base">Watch it: <a :href="published">{{ published }}</a></p>
    </template>
  </div>
</template>

<style>
.clip-player { text-align: center; }
.slidev-layout .clip-player video,
.slidev-layout .clip-player img {
  display: block;
  margin: 0 auto;
  /* As tall as fits under the header bar with a one-line caption below, in
     the slide's 980 by 552 canvas */
  height: 375px;
  width: auto;
  max-width: 100%;
  aspect-ratio: 16 / 9;
  background: #000;
}
</style>
