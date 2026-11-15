"""Write the recipe for the time trial course map: the edits that
scripts/strip_map.py makes to a copy of the short course layer.

Usage, from the repo root:

    python scripts/time_trial_recipe.py scripts/courses/time-trial.svg

Time trials run on the short course, so the time trial map is the short
course without its racing lanes, plus what differs in a time trial, as the
published time trial circulation PDF (Appendix 3 of the event plan) shows it.
That PDF is drawn on an older version of Bernard Tao's map (October 2024),
which no longer lines up with the current one, so nothing is lifted from it:

  - Everything the time trial shares with the short course comes from the
    source's current short course layer: the Transit Lane, the Marshalling
    Zone (which Bernard has redrawn to end upstream of Longbridges House, as
    the event plan says), the arrows into the start, the Univ crews' crossing
    to the City side, the Gut note, and the marshals.
  - The crossing for crews landing at Univ is drawn here in the style of the
    current crossing arrow (LANDING): from the City side by St John's
    Boathouse, as the PDF's note says, to the Univ raft.
  - The PDF's notes are set as text (NOTES), in space the current map leaves
    free.
  - The PDF's arrows for Isis Boathouse crews are left out: they show those
    crews' ordinary transit, which the map does not need, and the Gut note
    already says who may go through the Gut.
"""
import sys
import xml.etree.ElementTree as ET

SVGNS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVGNS)

# Crews landing at Univ: from the City side by St John's Boathouse (the third
# boathouse on Boathouse Island) to the Univ raft, in the style of the source's
# "St John's Crossing" (Univ crews crossing to the City side).
LANDING = {
    'd': 'M 848,243 C 925,246 988,258 1026,280',
    'style': ('fill:none;stroke:#000fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:miter;'
              'stroke-dasharray:2, 4;marker-end:url(#marker19626-3-8)'),
}

# The PDF's notes, verbatim: label -> (x, y of the first baseline, lines);
# an empty line separates paragraphs.
NOTE_STYLE = "font-size:12px;line-height:1.25;font-family:'Noto Sans',sans-serif;fill:#800000"
NOTE_LINE = 15
NOTES = {
    'Note Marshalling Zone': (1372, 140, [
        'Crews should spin upstream of Longbridges house',
        'into the Marshalling Zone, and then tuck in to the',
        'towpath while waiting for the division to start.',
        '',
        'Crews must not obstruct Isis Boathouse or',
        'Longbridges crews returning to their boathouse.',
    ]),
    'Note Univ Boating': (690, 392, [
        'Crews from Univ Boathouse boat with bows pointing',
        'downstream, pushing off and crossing immediately',
        'between divisions under the direction of the Univ',
        'Marshal.',
    ]),
    'Note Univ Landing': (1110, 422, [
        "Crews landing at Univ Boathouse must wait near St",
        "John's Boathouse on the City side, and cross to land",
        'under instruction from the Crossing Marshal.',
        '',
        "Crews at Univ Boathouse must follow Marshal's",
        'directions when they are asked not to put their boat',
        'on the raft to make space for landing crews.',
    ]),
}

# Short course elements the time trial does without, by name path within the
# course layer: the racing lanes, their labels and arrows, and their key rows.
DROP = [
    'Lanes/Top Half/City Station',
    'Lanes/Top Half/County Station',
    'Lanes/Top Half/Lane Divider',
    'Lanes Labels/City Start',
    'Lanes Labels/County Start',
    'Lanes Labels/City Finish',
    'Lanes Labels/County Finish',
    'Circulation Arrows/City Racing 1',
    'Circulation Arrows/City Racing 2',
    'Circulation Arrows/City Racing 3',
    'Circulation Arrows/County Racing 1',
    'Circulation Arrows/County Racing 2',
    'Circulation Arrows/County Racing 3',
    'Circulation Arrows/City Station split',
    'Circulation Arrows/County Station Split',
    'Thamesis Key/City',
    'Thamesis Key/County',
]

# The key's right-hand column loses its first two rows (City and County
# Station), so the remaining symbols move up two rows: name path -> (dx, dy).
KEY_UP_RECT = (0, -39.1586)  # two rows of the filled squares
KEY_UP_LINE = (0, -40.3700)  # two rows of the line samples
MOVE = {
    'Thamesis Key/Transit': KEY_UP_RECT,
    'Thamesis Key/Marshalling': KEY_UP_RECT,
    'Thamesis Key/Crossing': KEY_UP_LINE,
    'Thamesis Key/Paired Crews': KEY_UP_LINE,
    'Thamesis Key/Isis BH Crews Only': KEY_UP_LINE,
}

# In order: each replacement must be the only match at the time, hence
# bottom row first.
RIGHT = 'Thamesis Key/Key Text/Right Text'
RETEXT = [
    ('Title/Short Course', 'Short Course', 'Time Trial'),
    (RIGHT, 'LB/Isis BH Landing Crews Only', ''),
    (RIGHT, 'Paired Crews proceeding to start', ''),
    (RIGHT, 'Crossing under Marshal direction', 'LB/Isis BH Landing Crews Only'),
    (RIGHT, 'Paired Crews Marshalling Zone', 'Crews heading to start, in order'),
    (RIGHT, 'Transit Lane', 'Crossing under Marshal direction'),
    (RIGHT, 'County Station', 'Marshalling Zone'),
    (RIGHT, 'City Station', 'Transit Lane'),
    # The event plan's Boathouses B marshal (5) is also the Crossing Marshal
    # in time trials.
    ('Thamesis Key/Key Text/Left Text', 'BH B: Boating Marshal', 'BH B: Boating & Crossing Marshal'),
]


def fmt(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)

    root = ET.Element(f'{{{SVGNS}}}svg')
    root.append(ET.Comment(
        ' Generated by scripts/time_trial_recipe.py, after the time trial circulation PDF by '
        'Bernard Tao (Oxford Isis Maps, CC BY 3.0); applied by scripts/strip_map.py. '
        'Do not edit by hand. '))
    arrows = ET.SubElement(root, f'{{{SVGNS}}}g', {'data-into': 'Circulation Arrows'})

    ET.SubElement(arrows, f'{{{SVGNS}}}path', dict(LANDING, **{'data-label': 'Univ Landing Crossing'}))

    for label, (x, y, text) in NOTES.items():
        t = ET.SubElement(arrows, f'{{{SVGNS}}}text', {'style': NOTE_STYLE, 'data-label': label})
        for i, s in enumerate(text):
            if s:
                ET.SubElement(t, f'{{{SVGNS}}}tspan', {'x': fmt(x), 'y': fmt(y + i * NOTE_LINE)}).text = s

    ops = ET.SubElement(root, f'{{{SVGNS}}}g', {'data-ops': 'true'})
    for path in DROP:
        ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'drop', 'data-path': path})
    for path, (dx, dy) in MOVE.items():
        ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'move', 'data-path': path,
                                              'data-dx': fmt(dx), 'data-dy': fmt(dy)})
    for path, old, new in RETEXT:
        ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'retext', 'data-path': path,
                                              'data-old': old, 'data-new': new})

    ET.indent(root)
    ET.ElementTree(root).write(sys.argv[1], xml_declaration=True, encoding='UTF-8')
    print(sys.argv[1], file=sys.stderr)


if __name__ == '__main__':
    main()
