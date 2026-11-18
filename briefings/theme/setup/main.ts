import { defineAppSetup } from '@slidev/types'
import { ukdate, ukdatetime, uktime } from '../utils/dates.js'
import { startFlowGap } from '../utils/flow-gap.js'

declare const __EVENT__: Record<string, any>

// Makes event.yml and the date formats available in slide Markdown, e.g.
// {{ ukdatetime(regatta.dates.coxing_briefing) }} or
// <div v-if="regatta.amber_flag_racing">...</div>
// The names have no leading $ because two $ on one line of Markdown are read
// as inline LaTeX.
export default defineAppSetup(({ app }) => {
  app.config.globalProperties.regatta = __EVENT__
  app.config.globalProperties.ukdate = ukdate
  app.config.globalProperties.ukdatetime = ukdatetime
  app.config.globalProperties.uktime = uktime

  // Spreads each slide's content down the slide; see utils/flow-gap.js
  if (typeof window !== 'undefined')
    startFlowGap()
})
