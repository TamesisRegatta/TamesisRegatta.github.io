// Race cycle for a Longbridges crew on the short course, for RaceCycle, in
// Mansfield's colours. Coordinates are those of
// docs/assets/map/print/course-short.svg (downstream is +x). Captions follow
// the event plan's Side-By-Side circulation for Longbridges, and "Boating and
// landing at Longbridges". The start, race and spin at the Head are the same
// as in boathouse-island.js.
//
// Stage 0 is the starting picture; each later stage is one click. Each stage
// has one fixed view (camera: its centre, and its width in map units).

export default {
  title: 'Race cycle: Longbridges',
  summary: 'Boat bows pointing upstream, straight into the Marshalling Zone (1), pair up and move up to the start (2), start and race, on past the finish line (3), spin at the Head under the marshals\' instruction (4), come back down the transit lane (5), and spin to land bows pointing upstream (6).',
  // Where the Senior Umpire stands, for the starter's call.
  starter: [1134.6, 302.1],
  boats: {
    // On the Longbridges raft, bows pointing upstream.
    lin: { colours: 'mansfield', start: { x: 1644, y: 404, h: 193 } },
    opp: { colours: 'plain', start: { x: 1440, y: 340, h: 190, opacity: 0 } },
  },
  stages: [
    {
      title: 'Longbridges',
      text: 'Boat with bows pointing upstream. After racing, land with bows pointing upstream too.',
      // The whole course, which is also the PDF's view of the route.
      camera: { at: [1010, 310], w: 1440 },
    },
    {
      title: 'Into the Marshalling Zone',
      text: 'Push off bows pointing upstream, straight into the Marshalling Zone.',
      camera: { at: [1545, 372], w: 460 },
      moves: {
        lin: [
          { to: [[1600, 396], [1550, 384], [1500, 372], [1470, 365]], dur: 3.5 },
        ],
      },
    },
    {
      title: 'Pair up',
      text: 'Pair up with your opponent, and move up the Marshalling Zone to the start together.',
      camera: { at: [1320, 312], w: 520 },
      moves: {
        lin: [
          { to: [[1445, 359], [1400, 352], [1350, 341], [1300, 327], [1250, 312], [1200, 295], [1165, 284]], dur: 3.5 },
        ],
        opp: [
          { fade: 1, dur: 0.3 },
          { to: [[1395, 331], [1345, 320], [1295, 306], [1245, 291], [1195, 275], [1160, 264]], dur: 3.4 },
        ],
      },
    },
    {
      title: 'Start and race',
      text: 'Line up in your lane and keep the stagger the Senior Umpire sets. Go on "Go!", stay in your own lane, and keep going past the finish line.',
      camera: { at: [765, 292], w: 940 },
      moves: {
        lin: [
          { to: [[1150, 279], [1137, 276]], dur: 0.8, heading: 180 },
          { wait: 0.4 },
          { to: [[1100, 274], [1050, 270.8], [1000, 269.5], [950, 269.2], [900, 269.8], [850, 271.5], [800, 276.2], [750, 283], [700, 294], [650, 306], [600, 318.8], [550, 328], [500, 333.8], [450, 338.2], [430, 340], [405, 341], [380, 339.5]], dur: 3.9, stroke: 'race', ease: 'start' },
        ],
        opp: [
          { to: [[1152, 258], [1141, 255]], dur: 0.8, heading: 180 },
          { wait: 0.4 },
          { to: [[1100, 253], [1050, 251], [1000, 250.8], [950, 251.5], [900, 253], [850, 255.5], [800, 259.8], [750, 265.8], [700, 273.8], [650, 283.2], [600, 295.2], [550, 304.8], [500, 310.2], [450, 315], [432, 317], [410, 318.5], [384, 318.2]], dur: 4.15, stroke: 'race', ease: 'start' },
        ],
      },
      cues: [
        { at: 1.2, set: { call: 'Go!' } },
        { at: 2.6, set: { call: '' } },
      ],
    },
    {
      title: 'Spin at the Head',
      text: 'Spin at the Head under instruction from the marshals.',
      camera: { at: [420, 318], w: 450 },
      moves: {
        lin: [
          { to: [[362, 338.5]], dur: 0.8, ease: 'end' },
          { spin: 176, to: [366, 314], dur: 2 },
        ],
        opp: [
          { to: [[370, 318]], dur: 0.8, ease: 'end' },
          { fade: 0, dur: 0.3 },
        ],
      },
    },
    {
      title: 'Down the transit lane',
      text: 'Come back down the TRANSIT LANE all the way, past Boathouse Island, the start and the Marshalling Zone. Don\'t get in the way of crews entering the zone.',
      camera: { at: [1010, 305], w: 1440 },
      moves: {
        lin: [
          { to: [[400, 300], [450, 292], [500, 287], [550, 281.5], [600, 271.5], [650, 262], [700, 256], [750, 252], [800, 249.5], [850, 247.5], [900, 246], [950, 245.5], [1000, 245.5], [1050, 246.5], [1100, 248.5], [1150, 253], [1200, 263], [1250, 278], [1300, 292], [1350, 304], [1400, 315.5], [1450, 323.5], [1490, 330], [1540, 339], [1590, 348]], dur: 6, heading: 12 },
        ],
      },
    },
    {
      title: 'Spin and land',
      text: 'Spin, and land with bows pointing upstream, as the Longbridges Marshal directs.',
      camera: { at: [1610, 378], w: 440 },
      moves: {
        lin: [
          { to: [[1630, 357], [1668, 368]], dur: 1.5, ease: 'end' },
          { spin: 180, to: [1680, 382], dur: 2 },
          { to: [[1662, 400], [1644, 404]], dur: 1.5, heading: 193, ease: 'end' },
        ],
      },
    },
  ],
}
