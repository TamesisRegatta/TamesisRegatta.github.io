// Race cycle for a crew from the Isis Boathouse on the short course, for
// RaceCycle, in Reuben's colours. Coordinates are those of
// docs/assets/map/print/course-short.svg (downstream is +x). Captions follow
// the event plan's Side-By-Side circulation for the Isis Boathouse, and the
// coxing briefing's slide on it. The start, race and spin at the Head are the
// same as in boathouse-island.js.
//
// Only the top stretch is shown, from coming up through the Gut to going back
// down into it: below Top Gut, crews follow standard OURCs circulation, which
// the map does not show (it ends at about x = 1702, below Longbridges).
// Standard circulation keeps right, so upstream on the City side (top of the
// map) and downstream on the County side; the event's reverse circulation is
// the other way round.
//
// Stage 0 is the starting picture; each later stage is one click. Each stage
// has one fixed view (camera: its centre, and its width in map units).

export default {
  title: 'Race cycle: Isis Boathouse',
  summary: 'Come up through the Gut in standard circulation, and cross to the County side when the Gut Marshal tells you (1), pair up and move up to the start (2), start and race, on past the finish line (3), spin at the Head under the marshals\' instruction (4), come all the way back down the transit lane (5), and cross to standard circulation as you enter the Gut (6).',
  // Where the Senior Umpire stands, for the starter's call.
  starter: [1134.6, 302.1],
  boats: {
    // Coming up from the Gut on the City side, in standard circulation.
    lin: { colours: 'reuben', start: { x: 1690, y: 352, h: 182 } },
    opp: { colours: 'plain', start: { x: 1440, y: 340, h: 190, opacity: 0 } },
  },
  stages: [
    {
      title: 'Isis Boathouse',
      text: 'Come up through the Gut in standard circulation, as for any outing: the event\'s area starts at Top Gut.',
      // The whole course, which is also the PDF's view of the route.
      camera: { at: [1010, 310], w: 1440 },
    },
    {
      title: 'Cross above the Gut',
      text: 'Wait for the Gut Marshal to tell you, then cross to the County side (reverse circulation), into the Marshalling Zone.',
      camera: { at: [1570, 360], w: 380 },
      moves: {
        lin: [
          { wait: 1 },
          { to: [[1660, 358], [1625, 369], [1590, 373], [1550, 370], [1510, 365], [1478, 362]], dur: 3.5 },
        ],
      },
    },
    {
      title: 'Pair up',
      text: 'Find your opposition, pair up, and move up the Marshalling Zone to the start together.',
      camera: { at: [1320, 312], w: 520 },
      moves: {
        lin: [
          { to: [[1445, 361], [1400, 352], [1350, 341], [1300, 327], [1250, 312], [1200, 295], [1165, 284]], dur: 3.5 },
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
      text: 'Come all the way back down in the TRANSIT LANE, past Boathouse Island, the start, the Marshalling Zone and Longbridges.',
      camera: { at: [1010, 305], w: 1440 },
      moves: {
        lin: [
          // The centre of the map's Transit Lane (as in longbridges.js), on
          // past Longbridges on the City side.
          { to: [[400, 297.5], [420, 294.6], [460, 290.5], [500, 286.4], [540, 282.3], [580, 275.8], [620, 266.7], [660, 259.4], [700, 253.8], [740, 248.9], [780, 244.4], [820, 241.5], [860, 238.7], [900, 236.2], [940, 234.1], [980, 232.8], [1020, 232.1], [1060, 232.1], [1100, 233.9], [1140, 239.2], [1180, 251.2], [1220, 266], [1260, 279.8], [1300, 291.4], [1340, 301.5], [1380, 311], [1420, 319.5], [1460, 323.1], [1490, 328.5], [1540, 339], [1590, 347], [1625, 352]], dur: 6.5 },
        ],
      },
    },
    {
      title: 'Into the Gut',
      text: 'Cross to standard circulation as you enter the Gut, keeping a good lookout for crews and boats coming up. Land at the Isis Boathouse in any safe manner.',
      camera: { at: [1600, 370], w: 300 },
      moves: {
        lin: [
          { to: [[1655, 360], [1680, 372], [1705, 388]], dur: 2.5 },
          { fade: 0, dur: 0.4 },
        ],
      },
    },
  ],
}
