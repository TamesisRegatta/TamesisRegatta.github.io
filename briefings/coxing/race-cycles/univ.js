// Race cycle for a crew boating from the Univ raft on the short course, for
// RaceCycle, in Wolfson M2's colours. Coordinates are those of
// docs/assets/map/print/course-short.svg (downstream is +x). Captions follow
// the event plan's Side-By-Side circulation for University Boathouse, and the
// coxing briefing's slide on it. The start, race and spin at the Head are the
// same as in boathouse-island.js.
//
// Stage 0 is the starting picture; each later stage is one click. Each stage
// has one fixed view (camera: its centre, and its width in map units).

export default {
  title: 'Race cycle: Univ raft',
  summary: 'Boat bows pointing downstream and cross straight to the transit lane (1), spin into the Marshalling Zone and pair up (2), start and race, on past the finish line (3), spin at the Head under the marshals\' instruction (4), come back down the transit lane and spin into the Marshalling Zone (5), and follow a race up the County Station to land at Univ bows pointing upstream (6).',
  // Where the Senior Umpire stands, for the starter's call.
  starter: [1134.6, 302.1],
  boats: {
    // On the Univ raft, bows pointing downstream.
    lin: { colours: 'wolfsonM2', start: { x: 1048, y: 278, h: 3 } },
    opp: { colours: 'plain', start: { x: 1440, y: 340, h: 190, opacity: 0 } },
  },
  stages: [
    {
      title: 'Univ raft',
      text: 'Boat with bows pointing downstream. After racing, land with bows pointing upstream.',
      // The whole course, which is also the PDF's view of the route.
      camera: { at: [1010, 310], w: 1440 },
    },
    {
      title: 'Cross to the transit lane',
      text: 'Push off only when the Univ Marshal tells you, after a race has passed. Cross straight to the TRANSIT LANE, and go down it along the Greenbank.',
      camera: { at: [1285, 290], w: 600 },
      moves: {
        lin: [
          { to: [[1075, 272], [1100, 258], [1125, 246], [1150, 242], [1180, 251.2], [1220, 266], [1260, 279.8], [1300, 291.4], [1340, 301.5], [1380, 311], [1420, 319.5], [1460, 323.1], [1490, 328.5], [1515, 334]], dur: 4.5 },
        ],
      },
    },
    {
      title: 'Spin and pair up',
      text: 'Spin where the marshals tell you, into the Marshalling Zone (never through the Gut), then pair up and move up to the start.',
      camera: { at: [1320, 312], w: 520 },
      moves: {
        lin: [
          // Round in a clockwise arc (rowing on with stroke side), then up
          // the Marshalling Zone.
          { to: [[1532, 339], [1543, 349], [1539, 360], [1522, 365], [1500, 364], [1478, 362], [1445, 361], [1400, 352], [1350, 341], [1300, 327], [1250, 312], [1200, 295], [1165, 284]], dur: 4 },
        ],
        opp: [
          { fade: 1, dur: 0.3 },
          { to: [[1395, 331], [1345, 320], [1295, 306], [1245, 291], [1195, 275], [1160, 264]], dur: 3.7 },
        ],
      },
    },
    {
      title: 'Start and race',
      text: 'Line up in your lane and keep the stagger the Senior Umpire sets. Go on "Go!", stay in your own lane, and keep going past the finish line.',
      camera: { at: [765, 292], w: 940 },
      moves: {
        // The City station (opp) starts slightly ahead, as in
        // boathouse-island.js.
        lin: [
          { to: [[1153, 279], [1141, 276]], dur: 0.8, heading: 180 },
          { wait: 0.4 },
          { to: [[1100, 274], [1050, 270.8], [1000, 269.5], [950, 269.2], [900, 269.8], [850, 271.5], [800, 276.2], [750, 283], [700, 294], [650, 306], [600, 318.8], [550, 328], [500, 333.8], [450, 338.2], [430, 340], [405, 341], [380, 339.5]], dur: 3.9, stroke: 'race', ease: 'start' },
        ],
        opp: [
          { to: [[1149, 258], [1137, 255]], dur: 0.8, heading: 180 },
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
          // On past the finish, and round in a clockwise arc.
          { to: [[362, 338.5], [349, 332], [344, 321], [349, 310], [362, 303], [380, 300]], dur: 2.8 },
        ],
        opp: [
          { to: [[370, 318]], dur: 0.8, ease: 'end' },
          { fade: 0, dur: 0.3 },
        ],
      },
    },
    {
      title: 'Down the transit lane',
      text: 'Come back down beside the Meadow and the boathouses in the TRANSIT LANE, then spin into the Marshalling Zone (never through the Gut).',
      camera: { at: [1010, 305], w: 1440 },
      moves: {
        lin: [
          // The centre of the map's Transit Lane (as in longbridges.js),
          // then the spin into the Marshalling Zone.
          { to: [[400, 297.5], [420, 294.6], [460, 290.5], [500, 286.4], [540, 282.3], [580, 275.8], [620, 266.7], [660, 259.4], [700, 253.8], [740, 248.9], [780, 244.4], [820, 241.5], [860, 238.7], [900, 236.2], [940, 234.1], [980, 232.8], [1020, 232.1], [1060, 232.1], [1100, 233.9], [1140, 239.2], [1180, 251.2], [1220, 266], [1260, 279.8], [1300, 291.4], [1340, 301.5], [1380, 311], [1420, 319.5], [1460, 323.1], [1490, 328.5], [1515, 334], [1532, 339], [1543, 349], [1539, 360], [1522, 365], [1500, 364], [1478, 362]], dur: 8 },
        ],
      },
    },
    {
      title: 'Follow a race and land',
      text: 'Make it clear you want to land. When the Senior Umpire tells you, follow a race up the County Station, and land at Univ with bows pointing upstream.',
      camera: { at: [1255, 315], w: 560 },
      moves: {
        lin: [
          { to: [[1445, 361], [1400, 352], [1350, 341], [1300, 327], [1250, 312], [1200, 295], [1165, 284], [1130, 279], [1100, 277.5], [1070, 278], [1048, 278]], dur: 5, heading: 183 },
        ],
      },
    },
  ],
}
