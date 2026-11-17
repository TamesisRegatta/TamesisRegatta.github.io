---
# Not in the nav: linked from the footer of every page.
pdf: false
---

# Analytics

A transparent view of the statistics available to us: these are the same numbers we see.
Our [privacy policy](privacy.md) explains how they are collected.

{% if config.extra.plausible.dashboard %}
If they do not show below, [open them on their own page]({{ config.extra.plausible.dashboard }}){ target="_blank" rel="noopener" }.

{# As Plausible's own embed code has it: plausible-embed lets its embed script
   fit the frame's height to the dashboard, 1600 px until then; a 1 px width
   stretched by min-width keeps it from overflowing on iOS. docs/assets/analytics.js
   sets the src, so the dashboard matches the site's light or dark mode. #}
<iframe plausible-embed class="tr-analytics" data-src="{{ config.extra.plausible.dashboard }}" title="Visit statistics for tamesisregatta.org" loading="lazy"></iframe>
<script async src="{{ config.extra.plausible.embed_script }}"></script>

Stats powered by [Plausible Analytics](https://plausible.io/){ target="_blank" rel="noopener" }.
{% else %}
The statistics will be shown here soon.
{% endif %}
