// Race cycle for a Boathouse Island crew on the short course, for RaceCycle.
// Coordinates are those of docs/assets/map/print/course-short.svg (downstream
// is +x); the paths follow the centrelines of the map's lanes. Captions
// follow the event plan's Side-By-Side circulation for Boathouse Island.
//
// Stage 0 is the starting picture; each later stage is one click. Each stage
// has one fixed view (camera: its centre, and its width in map units).

export default {
  title: 'Race cycle: Boathouse Island',
  summary: 'Boat from the downstream rafts and go down the transit lane (1), spin into the Marshalling Zone and pair up (2), start and race (3), spin at the Head (4), and come back down the transit lane to land on the upstream rafts (5).',
  // Where the Senior Umpire stands, for the starter's call.
  starter: [1134.6, 302.1],
  boats: {
    lin: { colours: 'linacre', start: { x: 1048, y: 229.5, h: 0 } },
    opp: { colours: 'plain', start: { x: 1440, y: 340, h: 190, opacity: 0 } },
  },
  stages: [
    {
      title: 'Boathouse Island',
      text: 'Boat from the downstream rafts, bows pointing downstream. Land, after racing, on the upstream rafts.',
      camera: { at: [910, 300], w: 1320 },
    },
    {
      title: 'Down the transit lane',
      text: 'Push off into the TRANSIT LANE and stay in it, past the start and down the Greenbank.',
      camera: { at: [1285, 285], w: 600 },
      moves: {
        lin: [
          { to: [[1075, 232.5], [1110, 236], [1150, 242.5], [1200, 259], [1250, 277], [1300, 291.5], [1350, 304], [1400, 315.5], [1450, 322.5], [1490, 329], [1515, 334]], dur: 4 },
        ],
      },
    },
    {
      title: 'Spin and pair up',
      text: 'Spin where the marshals tell you, into the Marshalling Zone (never through the Gut), then pair up and move up to the start.',
      camera: { at: [1320, 312], w: 520 },
      moves: {
        lin: [
          { spin: 180, to: [1508, 357], dur: 1.5 },
          { to: [[1478, 362], [1445, 361], [1400, 352], [1350, 341], [1300, 327], [1250, 312], [1200, 295], [1165, 284]], dur: 2.5 },
        ],
        opp: [
          { fade: 1, dur: 0.3 },
          { to: [[1395, 331], [1345, 320], [1295, 306], [1245, 291], [1195, 275], [1160, 264]], dur: 3.7 },
        ],
      },
    },
    {
      title: 'Start and race',
      text: 'Line up in your lane and keep the stagger the Senior Umpire sets. Go on "Go!", and stay in your own lane.',
      camera: { at: [790, 290], w: 900 },
      moves: {
        lin: [
          { to: [[1150, 279], [1137, 276]], dur: 0.8, heading: 180 },
          { wait: 0.4 },
          { to: [[1100, 274], [1050, 270.8], [1000, 269.5], [950, 269.2], [900, 269.8], [850, 271.5], [800, 276.2], [750, 283], [700, 294], [650, 306], [600, 318.8], [550, 328], [500, 333.8], [450, 338.2], [430, 340]], dur: 3.6, ease: 'start' },
        ],
        opp: [
          { to: [[1152, 258], [1141, 255]], dur: 0.8, heading: 180 },
          { wait: 0.4 },
          { to: [[1100, 253], [1050, 251], [1000, 250.8], [950, 251.5], [900, 253], [850, 255.5], [800, 259.8], [750, 265.8], [700, 273.8], [650, 283.2], [600, 295.2], [550, 304.8], [500, 310.2], [450, 315], [432, 317]], dur: 3.8, ease: 'start' },
        ],
      },
      cues: [
        { at: 1.2, set: { call: 'Go!' } },
        { at: 2.6, set: { call: '' } },
      ],
    },
    {
      title: 'Finish and spin',
      text: 'Keep paddling until you are clear of the finish, then spin at the Head where the marshal tells you.',
      camera: { at: [420, 318], w: 450 },
      moves: {
        lin: [
          { to: [[400, 341], [372, 339]], dur: 1, ease: 'end' },
          { spin: 176, to: [368, 314], dur: 2 },
        ],
        opp: [
          { to: [[405, 319], [385, 318]], dur: 1, ease: 'end' },
          { fade: 0, dur: 0.3 },
        ],
      },
    },
    {
      title: 'Return and land',
      text: 'Come back down beside the Meadow in the TRANSIT LANE, and land on the upstream rafts, bows pointing downstream.',
      camera: { at: [625, 275], w: 620 },
      moves: {
        lin: [
          { to: [[400, 300], [450, 292], [500, 287], [550, 281.5], [600, 271.5], [650, 261], [700, 254], [750, 248], [800, 243], [835, 238], [852, 236.5]], dur: 4, heading: 0 },
        ],
      },
    },
  ],
}
