// Date formatting matching the ukdate / ukdatetime filters in main.py, so a
// date reads the same on the slides as on the site.
//
// event.yml is parsed as YAML 1.2 (see setup/vite-plugins.ts), so its dates
// arrive as strings such as "2026-11-18" or "2026-11-18 18:30:00". They are
// UK local times, so they are split into fields here rather than handed to
// Date, which would shift them by the viewer's time zone.

const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

function parse(value) {
  const match = /^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}):(\d{2}))?/.exec(String(value ?? ''))
  if (!match)
    throw new Error(`[tamesis] not an ISO date: ${JSON.stringify(value)}`)
  const [, year, month, day, hour, minute] = match
  const weekday = new Date(Date.UTC(+year, +month - 1, +day)).getUTCDay()
  return { year: +year, month: +month, day: +day, weekday, hour, minute }
}

// "Wed 18 Nov 2026"
export function ukdate(value) {
  const d = parse(value)
  return `${DAYS[d.weekday]} ${d.day} ${MONTHS[d.month - 1]} ${d.year}`
}

// "Wed 18 Nov 2026, 18:30"
export function ukdatetime(value) {
  const d = parse(value)
  if (d.hour === undefined)
    throw new Error(`[tamesis] date has no time: ${JSON.stringify(value)}`)
  return `${ukdate(value)}, ${d.hour}:${d.minute}`
}

// "18:30"
export function uktime(value) {
  const d = parse(value)
  if (d.hour === undefined)
    throw new Error(`[tamesis] date has no time: ${JSON.stringify(value)}`)
  return `${d.hour}:${d.minute}`
}
