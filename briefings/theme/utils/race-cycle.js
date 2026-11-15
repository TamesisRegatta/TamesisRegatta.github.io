// Timeline maths for RaceCycle.vue: turns a route (stages of moves per boat)
// into poses at any stage and time, so the animation can play a stage or
// jump straight to its end with the same result.
//
// Map coordinates are the course map's viewBox units (about a metre each).
// Headings are degrees, measured as on screen: 0 points along +x (downstream
// on this map) and positive turns are clockwise.

export const ease = u => (u <= 0 ? 0 : u >= 1 ? 1 : 0.5 - 0.5 * Math.cos(Math.PI * u))

// Distance covered by time u of a move whose speed ramps up over the first
// a0 and down over the last a1 of it (both fractions of the move), steady in
// between.
function ramp(u, a0, a1) {
  u = Math.max(0, Math.min(1, u))
  const total = 1 - a0 / 2 - a1 / 2
  let s
  if (u < a0)
    s = (u * u) / (2 * a0)
  else if (u <= 1 - a1)
    s = a0 / 2 + (u - a0)
  else
    s = a0 / 2 + (1 - a1 - a0) + (a1 / 2 - ((1 - u) ** 2) / (2 * a1))
  return s / total
}

// Speed profiles for a move: default starts and stops gently; 'start' only
// pulls away (for a race start), 'end' only winds down, 'linear' neither.
const PROFILES = { default: [0.35, 0.35], start: [0.12, 0], end: [0, 0.6], linear: [0, 0] }
const smooth = u => (u <= 0 ? 0 : u >= 1 ? 1 : u * u * (3 - 2 * u))
const lerp = (a, b, u) => a + (b - a) * u
const deg = Math.PI / 180

// Shortest signed turn from a to b, in degrees.
export function turn(a, b) {
  return ((((b - a) % 360) + 540) % 360) - 180
}

// A Catmull-Rom curve through points, as a dense polyline with arc lengths.
function curve(points) {
  const pts = [points[0], ...points, points[points.length - 1]]
  const out = []
  for (let i = 1; i < pts.length - 2; i++) {
    const [p0, p1, p2, p3] = [pts[i - 1], pts[i], pts[i + 1], pts[i + 2]]
    for (let k = 0; k < 24; k++) {
      const t = k / 24
      const t2 = t * t
      const t3 = t2 * t
      out.push([0, 1].map(j => 0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t
        + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
        + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3)))
    }
  }
  out.push(points[points.length - 1])
  const len = [0]
  for (let i = 1; i < out.length; i++)
    len.push(len[i - 1] + Math.hypot(out[i][0] - out[i - 1][0], out[i][1] - out[i - 1][1]))
  return { pts: out, len, total: len[len.length - 1] }
}

function along(c, s) {
  s = Math.max(0, Math.min(c.total, s))
  let i = 1
  while (i < c.len.length - 1 && c.len[i] < s) i++
  const u = (s - c.len[i - 1]) / (c.len[i] - c.len[i - 1] || 1)
  const [a, b] = [c.pts[i - 1], c.pts[i]]
  return { x: lerp(a[0], b[0], u), y: lerp(a[1], b[1], u), h: Math.atan2(b[1] - a[1], b[0] - a[0]) / deg }
}

// One move, starting from pose p, as a function of u in [0, 1].
//   { to: [[x, y], ...], dur, stroke?, heading?, ease? }   row along a smooth
//       path (stroke: 'paddle', the default, or 'race'); heading: a final
//       heading to turn to over the last part of the path.
//   { spin: degrees, dur, to?: [x, y] }   spin in place (clockwise positive),
//       drifting to `to`; rows on stroke side and backs down bow side.
//   { wait: dur }   sit still, blades resting.
//   { fade: opacity, dur }   fade in or out where it is.
function build(move, p) {
  if (move.to && !move.spin) {
    const c = curve([[p.x, p.y], ...move.to])
    const h0 = p.h
    const [a0, a1] = PROFILES[move.ease || 'default']
    return {
      dur: move.dur,
      stroke: move.stroke || 'paddle',
      at(u) {
        const q = along(c, ramp(u, a0, a1) * c.total)
        // Ease out of the starting heading over the first fifth of the path,
        // and into a requested final heading over the last fifth.
        let h = q.h
        if (u < 0.2)
          h = q.h + turn(q.h, h0) * (1 - smooth(u / 0.2))
        if (move.heading !== undefined && u > 0.8)
          h = h + turn(h, move.heading) * smooth((u - 0.8) / 0.2)
        return { ...p, x: q.x, y: q.y, h }
      },
    }
  }
  if (move.spin) {
    const [x1, y1] = move.to || [p.x, p.y]
    return {
      dur: move.dur,
      stroke: 'spin',
      at(u) {
        const e = ease(u)
        return { ...p, x: lerp(p.x, x1, e), y: lerp(p.y, y1, e), h: p.h + move.spin * e }
      },
    }
  }
  if (move.fade !== undefined) {
    return { dur: move.dur, stroke: 'none', at: u => ({ ...p, opacity: lerp(p.opacity, move.fade, ease(u)) }) }
  }
  return { dur: move.wait, stroke: 'none', at: () => ({ ...p }) }
}

// Precompute every stage: for each boat, its timed segments and end pose.
export function compile(route) {
  const poses = {}
  for (const [name, boat] of Object.entries(route.boats))
    poses[name] = { opacity: 1, ...boat.start }
  return route.stages.map((stage) => {
    const boats = {}
    let dur = 0
    for (const name of Object.keys(route.boats)) {
      let t = 0
      let p = poses[name]
      const segs = []
      for (const move of stage.moves?.[name] || []) {
        const seg = build(move, p)
        segs.push({ ...seg, t0: t })
        t += seg.dur
        p = seg.at(1)
      }
      boats[name] = { segs, start: poses[name], end: p }
      poses[name] = p
      dur = Math.max(dur, t)
    }
    for (const cue of stage.cues || [])
      dur = Math.max(dur, cue.at)
    return { ...stage, boats, dur: Math.max(dur, stage.dur || 0) }
  })
}

// A boat's pose and stroke at time t in a compiled stage (segT: time into
// the current move, for the stroke cycle).
export function poseAt(stage, name, t) {
  const b = stage.boats[name]
  for (const seg of b.segs) {
    if (t < seg.t0 + seg.dur)
      return { ...seg.at(Math.max(0, (t - seg.t0) / seg.dur)), stroke: seg.stroke, segT: t - seg.t0 }
  }
  return { ...b.end, stroke: 'none', segT: 0 }
}

// Cue state (the starter's call) at time t: the latest cue of each kind.
export function cuesAt(stage, t) {
  const out = {}
  for (const cue of stage.cues || []) {
    if (cue.at <= t)
      Object.assign(out, cue.set)
  }
  return out
}

// Blade sweep for a stroke phase in [0, 1): degrees toward the stern from
// square, and how much of the spoon's face shows from above. A feathered
// blade lies flat, so its whole face (and colours) shows; a squared blade is
// on edge, so it looks narrow. At rest ('none') the blades lie back at REST,
// as in the usual pictogram of an eight.
const SQUARE = 0.4
export const REST = 25
export function bladeAt(mode, phase, side) {
  if (mode === 'none')
    return { angle: REST, open: 1 }
  const catchA = -38
  const finishA = 30
  const drive = 0.4
  let angle
  let open
  if (phase < drive) {
    angle = lerp(catchA, finishA, ease(phase / drive))
    open = SQUARE
  }
  else {
    const u = (phase - drive) / (1 - drive)
    angle = lerp(finishA, catchA, ease(u))
    // Feathered for the middle of the recovery, squaring up for the catch.
    open = u < 0.15 ? lerp(SQUARE, 1, u / 0.15) : u > 0.8 ? lerp(1, SQUARE, (u - 0.8) / 0.2) : 1
  }
  // Spinning: bow side backs down, which is the stroke played backwards.
  if (mode === 'spin' && side === 'bow')
    angle = -angle
  return { angle, open }
}

// Strokes per second for each kind of rowing.
export const RATES = { paddle: 0.8, race: 1.25, spin: 0.7, none: 0 }
