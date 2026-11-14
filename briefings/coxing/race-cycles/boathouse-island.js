// Race cycle for a Boathouse Island crew on the short course, for RaceCycle.
// Coordinates are those of docs/assets/map/print/course-short.svg (downstream
// is +x); the paths follow the centrelines of the map's lanes. Captions
// follow the event plan's Side-By-Side circulation for Boathouse Island.
//
// Stage 0 is the starting picture; each later stage is one click.

export default {
  title: 'Race cycle: Boathouse Island',
  summary: 'Boat from the downstream rafts (1), down the transit lane (2), spin into the Marshalling Zone (3), pair up and go up to the start (4, 5), race (6), spin at the Head (7), and back down the transit lane to land on the upstream rafts (8).',
  // Where the Senior Umpire stands, for the flag and the starter's call.
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
      title: 'Push off',
      text: 'The raft marshal checks your boat first. Push off bows pointing downstream, into the TRANSIT LANE.',
      camera: { follow: 'lin', w: 230, offset: [10, 8] },
      moves: {
        lin: [
          { wait: 1.2 },
          { to: [[1075, 232.5], [1110, 236]], dur: 3.5 },
        ],
      },
    },
    {
      title: 'Down the transit lane',
      text: 'Stay in the TRANSIT LANE past the start and down the Greenbank. Watch for Univ crews crossing at the Cherwell Cut.',
      camera: { follow: 'lin', w: 380, offset: [40, 0] },
      moves: {
        lin: [
          { to: [[1150, 242.5], [1200, 259], [1250, 277], [1300, 291.5], [1350, 304], [1400, 315.5], [1450, 322.5], [1490, 329], [1515, 334]], dur: 10 },
        ],
      },
    },
    {
      title: 'Spin',
      text: 'Spin where the marshals tell you, into the Marshalling Zone: row on stroke side, back down bow side. Never go through the Gut.',
      camera: { at: [1500, 343], w: 190 },
      moves: {
        lin: [
          { spin: 180, to: [1508, 357], dur: 5 },
        ],
      },
    },
    {
      title: 'Pair up',
      text: 'Find your opponent and pair up, then move up the Marshalling Zone towards the start together.',
      camera: { follow: 'lin', w: 360, offset: [-30, -12] },
      moves: {
        opp: [
          { fade: 1, dur: 1 },
          { wait: 2.5 },
          { to: [[1395, 331], [1345, 320], [1295, 306], [1245, 291], [1195, 275], [1160, 264]], dur: 8 },
        ],
        lin: [
          { to: [[1478, 362], [1445, 361]], dur: 3, heading: 190 },
          { wait: 0.5 },
          { to: [[1400, 352], [1350, 341], [1300, 327], [1250, 312], [1200, 295], [1165, 284]], dur: 8 },
        ],
      },
    },
    {
      title: 'The start',
      text: 'Line up in your lane. The Senior Umpire sets the stagger: don\'t change it. "Attention!" with the red flag up; "Go!" as it drops.',
      camera: { at: [1142, 276], w: 190 },
      moves: {
        lin: [{ to: [[1150, 279], [1137, 276]], dur: 3, heading: 180 }, { wait: 3.2 }],
        opp: [{ to: [[1152, 258], [1141, 255]], dur: 3, heading: 180 }, { wait: 3.2 }],
      },
      cues: [
        { at: 3.8, set: { flag: 'raised', call: 'Attention!' } },
        { at: 5.6, set: { flag: 'dropped', call: 'Go!' } },
      ],
    },
    {
      title: 'Race',
      text: 'Stay in your own lane, and out of the transit lane. Steering comes first: a good line wins races.',
      camera: { at: [770, 290], w: 760 },
      moves: {
        lin: [
          { to: [[1100, 274], [1050, 270.8], [1000, 269.5], [950, 269.2], [900, 269.8], [850, 271.5], [800, 276.2], [750, 283], [700, 294], [650, 306], [600, 318.8], [550, 328], [500, 333.8], [450, 338.2], [430, 340]], dur: 9, stroke: 'race', ease: 'start' },
        ],
        opp: [
          { to: [[1100, 253], [1050, 251], [1000, 250.8], [950, 251.5], [900, 253], [850, 255.5], [800, 259.8], [750, 265.8], [700, 273.8], [650, 283.2], [600, 295.2], [550, 304.8], [500, 310.2], [450, 315], [432, 317]], dur: 9.6, stroke: 'race', ease: 'start' },
        ],
      },
    },
    {
      title: 'Finish and spin',
      text: 'Keep paddling until you are clear of the finish, then wind down. Spin at the Head where the marshal tells you.',
      camera: { at: [385, 322], w: 230 },
      moves: {
        lin: [
          { to: [[400, 341], [372, 339]], dur: 3, ease: 'end' },
          { spin: 176, to: [368, 314], dur: 5 },
        ],
        opp: [
          { to: [[405, 319], [385, 318]], dur: 3, ease: 'end' },
          { fade: 0, dur: 1.5 },
        ],
      },
    },
    {
      title: 'Return and land',
      text: 'Come back down beside the Meadow in the TRANSIT LANE, and land on the upstream rafts with bows pointing downstream.',
      camera: { follow: 'lin', w: 380, offset: [30, 10] },
      moves: {
        lin: [
          { to: [[400, 300], [450, 292], [500, 287], [550, 281.5], [600, 271.5], [650, 261], [700, 254], [750, 248], [800, 243], [835, 238], [852, 236.5]], dur: 11, heading: 0 },
        ],
      },
    },
  ],
}
