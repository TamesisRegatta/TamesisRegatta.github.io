"""Derive the time trial course for the course map from the published time
trial circulation PDF, as a recipe that scripts/strip_map.py applies to a copy
of the short course layer.

Usage, from the repo root (needs PyMuPDF, which the site does not use:
pip install pymupdf):

    python scripts/lift_time_trial.py \\
        "Tamesis 2026 Circulation Short Course Time Trial.pdf" \\
        scripts/courses/time-trial.svg

Time trials run on the short course, so the time trial map is the short
course without its racing lanes, plus the time trial's own circulation. The
published PDF is drawn on an older version of Bernard Tao's map (October
2024) than the short course one, and only its bottom half still lines up with
the current map. So:

  - The Isis Boathouse crews' arrows, all in the bottom half, are lifted from
    the PDF as vectors (ISIS).
  - Everything the time trial shares with the short course comes from the
    source's current short course layer: the Transit Lane, the Marshalling
    Zone (which Bernard has redrawn to end upstream of Longbridges House, as
    the event plan says), the arrows into the start, the Univ crews' crossing
    to the City side, and the marshals.
  - The crossing for crews landing at Univ, which in the PDF is drawn against
    the older Boathouse Island, is redrawn here in the style of the current
    crossing arrow (LANDING): from the City side by St John's Boathouse, as
    the PDF's note says, to the Univ raft.
  - The PDF's notes are set as text (NOTES), in space the current map leaves
    free.
"""
import os
import sys
import xml.etree.ElementTree as ET

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lift_course import SVGNS, drawing_style, fmt, path_d  # noqa: E402

# PDF points -> map units for the bottom half of this PDF (registered on the
# river outline, which is unchanged there since 2024).
BOTTOM = (0.352778, 17.0, -4.0)

# The Isis Boathouse crews' arrows: this colour, above the key at the bottom
# of the page (y < KEY_TOP).
ISIS_COLOUR = (0.588, 0.141, 0.184)
KEY_TOP = 2380
ISIS_COUNT = 20  # ten lines, each with a head
LINE_STYLE = ('fill:none;stroke:#962430;stroke-width:2;stroke-linecap:butt;'
              'stroke-linejoin:miter;stroke-dasharray:2,4,6,2')

# The PDF key's sample of that arrow (line, head), redrawn in the course key
# in the row the short course uses for paired crews (KEY_ROW: where its line
# starts, and its length).
KEY_SAMPLE = ((1488.2, 2666.0, 1565.9, 2666.5), (1559.3, 2654.7, 1579.0, 2677.4))
KEY_ROW = ((1010.6015, 919.4777), 17.8782)

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
    'Note Isis Boathouse': (786, 718, [
        'Crews from Isis Boathouse carefully cross',
        'under the direction of Top Gut Marshal',
        'While downstream of Top Gut Marshal, they are outside the event',
        'managed area, and must follow OURCs rules for a standard outing.',
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
# Station), so the remaining symbols move up two rows, and the Isis
# Boathouse crews' arrow takes the sixth. Elements moved: name path -> (dx, dy).
KEY_UP_RECT = (0, -39.1586)  # two rows of the filled squares
KEY_UP_LINE = (0, -40.3700)  # two rows of the line samples
MOVE = {
    'Thamesis Key/Transit': KEY_UP_RECT,
    'Thamesis Key/Marshalling': KEY_UP_RECT,
    'Thamesis Key/Crossing': KEY_UP_LINE,
    'Thamesis Key/Paired Crews': KEY_UP_LINE,
    'Thamesis Key/Isis BH Crews Only': KEY_UP_LINE,
    # The Gut note ("Only crews boating or landing downstream are allowed to
    # go through the Gut") sits in the Gut, where the lifted Isis Boathouse
    # arrows now run; it moves out onto the open ground above the Gut.
    'Circulation Arrows/Isis Boathouse Crews Only': (-84, -62),
}

# In order: each replacement must be the only match at the time, hence
# bottom row first.
RIGHT = 'Thamesis Key/Key Text/Right Text'
RETEXT = [
    ('Title/Short Course', 'Short Course', 'Time Trial'),
    (RIGHT, 'LB/Isis BH Landing Crews Only', ''),
    (RIGHT, 'Paired Crews proceeding to start', 'Isis BH Crews'),
    (RIGHT, 'Crossing under Marshal direction', 'LB/Isis BH Landing Crews Only'),
    (RIGHT, 'Paired Crews Marshalling Zone', 'Crews heading to start, in order'),
    (RIGHT, 'Transit Lane', 'Crossing under Marshal direction'),
    (RIGHT, 'County Station', 'Marshalling Zone'),
    (RIGHT, 'City Station', 'Transit Lane'),
    # The event plan's Boathouses B marshal (5) is also the Crossing Marshal
    # in time trials.
    ('Thamesis Key/Key Text/Left Text', 'BH B: Boating Marshal', 'BH B: Boating & Crossing Marshal'),
]


def near(c, want):
    return c is not None and all(abs(a - b) < 0.005 for a, b in zip(c, want))


def box(r):
    return tuple(round(v, 1) for v in r)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    page = pymupdf.open(sys.argv[1])[0]
    drawings = page.get_drawings()

    root = ET.Element(f'{{{SVGNS}}}svg')
    root.append(ET.Comment(
        ' Generated by scripts/lift_time_trial.py from the time trial circulation PDF by '
        'Bernard Tao (Oxford Isis Maps, CC BY 3.0); applied by scripts/strip_map.py. '
        'Do not edit by hand. '))
    arrows = ET.SubElement(root, f'{{{SVGNS}}}g', {'data-into': 'Circulation Arrows'})
    key = ET.SubElement(root, f'{{{SVGNS}}}g', {'data-into': 'Thamesis Key'})

    isis = [d for d in drawings if near(d.get('color'), ISIS_COLOUR) and d['rect'].y1 < KEY_TOP]
    if len(isis) != ISIS_COUNT:
        sys.exit(f'lift_time_trial: {len(isis)} Isis Boathouse arrow parts in the PDF; expected {ISIS_COUNT}')
    lines = sorted((d for d in isis if not near(d.get('fill'), ISIS_COLOUR)), key=lambda d: d['rect'].x0)
    heads = [d for d in isis if near(d.get('fill'), ISIS_COLOUR)]
    for n, line in enumerate(lines, 1):
        # Some lines carry a stray fill in the PDF; draw them as open strokes.
        ET.SubElement(arrows, f'{{{SVGNS}}}path', {
            'd': path_d(dict(line, type='s', closePath=False), BOTTOM),
            'style': LINE_STYLE, 'data-label': f'Isis BH Crews {n}'})
        # Its head: the one nearest the line's end.
        end = line['items'][-1][-1]
        head = min(heads, key=lambda h: abs(h['rect'].x0 + h['rect'].width / 2 - end.x)
                   + abs(h['rect'].y0 + h['rect'].height / 2 - end.y))
        heads.remove(head)
        ET.SubElement(arrows, f'{{{SVGNS}}}path', {
            'd': path_d(head, BOTTOM), 'style': drawing_style(head, BOTTOM),
            'data-label': f'Isis BH Crews {n} Head'})
        print(f'lifted Isis BH Crews {n}: {box(line["rect"])}', file=sys.stderr)

    ET.SubElement(arrows, f'{{{SVGNS}}}path', dict(LANDING, **{'data-label': 'Univ Landing Crossing'}))

    for label, (x, y, text) in NOTES.items():
        t = ET.SubElement(arrows, f'{{{SVGNS}}}text', {'style': NOTE_STYLE, 'data-label': label})
        for i, s in enumerate(text):
            if s:
                ET.SubElement(t, f'{{{SVGNS}}}tspan', {'x': fmt(x), 'y': fmt(y + i * NOTE_LINE)}).text = s

    # The key sample, scaled so its line matches the other key lines.
    by_box = {box(d['rect']): d for d in drawings}
    line, head = (by_box[b] for b in KEY_SAMPLE)
    (x0, y0), length = KEY_ROW
    s = length / (KEY_SAMPLE[0][2] - KEY_SAMPLE[0][0])
    mid = (KEY_SAMPLE[0][1] + KEY_SAMPLE[0][3]) / 2
    scaled = (s, x0 - s * KEY_SAMPLE[0][0], y0 - s * mid)
    ET.SubElement(key, f'{{{SVGNS}}}path', {
        'd': path_d(dict(line, type='s', closePath=False), scaled),
        'style': LINE_STYLE, 'data-label': 'Isis BH Crews'})
    ET.SubElement(key, f'{{{SVGNS}}}path', {
        'd': path_d(head, scaled), 'style': drawing_style(head, scaled), 'data-label': 'Isis BH Crews Head'})

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
    ET.ElementTree(root).write(sys.argv[2], xml_declaration=True, encoding='UTF-8')
    print(sys.argv[2], file=sys.stderr)


if __name__ == '__main__':
    main()
