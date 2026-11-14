import { defineVitePluginsSetup } from '@slidev/types'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { parse as parseYaml } from 'yaml'

// The repository root, two levels up from briefings/theme/setup/.
const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..')

// Defines __EVENT__ for layouts, components and slides: the public parts of
// event.yml, the same file the website is built from, so dates, roles and the
// regatta mailbox can't drift apart between the site and the slides.
//
// Only public data is passed on. Personal contact details live in
// contacts.local.yml, which is never read here: the decks are always public.
export default defineVitePluginsSetup(() => {
  const file = path.join(repoRoot, 'event.yml')
  // YAML 1.2 (the default) leaves dates as strings; see utils/dates.js.
  const event = parseYaml(fs.readFileSync(file, 'utf-8'))

  const exposed = {
    year: Number(String(event.dates.regatta_start).slice(0, 4)),
    dates: event.dates,
    amber_flag_racing: event.amber_flag_racing,
    public_phones: event.public_phones,
    entry_fee: event.entry_fee,
    contact: { email: event.contact.email },
    roles: event.roles,
  }

  return [{
    name: 'tamesis-event',
    config() {
      return {
        define: {
          __EVENT__: JSON.stringify(exposed),
        },
        server: {
          // Let decks use the site's own assets (logo, maps, diagrams) from
          // docs/assets/ instead of keeping copies.
          fs: { allow: [repoRoot] },
        },
      }
    },
    configureServer(server) {
      // Reload the deck when event.yml changes during `slidev` dev.
      server.watcher.add(file)
      server.watcher.on('change', (changed) => {
        if (path.resolve(changed) === file)
          server.restart()
      })
    },
  }]
})
