"""Derive the intermediate course for the course map from the published
circulation PDFs, as a recipe that scripts/strip_map.py applies to a copy of
the short course layer.

Usage, from the repo root (needs PyMuPDF, which the site does not use:
pip install pymupdf):

    python scripts/lift_course.py \\
        "Tamesis 2026 Circulation Intermediate Course.pdf" \\
        "Tamesis 2026 Circulation Short Course.pdf" \\
        scripts/courses/intermediate.svg

Bernard Tao's source map has a short course layer but no intermediate one.
The two PDFs are exports of the same document (October 2025), so whatever is
in the intermediate PDF and not in the short one is what makes the intermediate
course. This script lifts those items out of the PDF as vectors, moves them
onto the current map, and writes them out with the edits to make to a copy of
the short course: elements to drop, elements to move, and so on. Everything
the two courses share comes from the source's own short course layer, which
Bernard has redrawn since 2025.

Placement: the 2025 PDFs line up with the current map with one scale and
offset for each half of the map (measured by registering the river outlines).
The parts lifted here are all where that registration is exact: between the
Cherwell Cut and Longbridges, and the bottom half. The upstream end around
Folly Bridge has been redrawn, and nothing is lifted from there.
"""
import math
import sys
import xml.etree.ElementTree as ET

import pymupdf

SVGNS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVGNS)

# PDF points -> map units, for each half of the PDF page (split at y = SPLIT).
SPLIT = 1600
TOP = (0.342194, 28.5, -19.5)
BOTTOM = (0.352778, -8.0, -11.5)

# Intermediate-only drawings to lift, by the box they occupy in the PDF
# (rounded to 0.1 pt, as printed when this script runs) and what they become.
# The rest of the intermediate-only drawings are left out:
#   - the yellow Marshalling Zone: the short course's zone is reused, cut off
#     at the intermediate start, so its upstream end and the Greenbank spin
#     stay where Bernard has since moved them;
#   - the black arrows beyond Longbridges at the right edge of the top half,
#     which fall off the current map; its Longbridges arrows are kept instead;
#   - the Senior Umpire and marshal 8 icons, which are moved instead (MOVE).
#   - the City and County Station lanes themselves: Bernard has since
#     redrawn the lanes, so the 2025 shapes no longer meet the current
#     Transit Lane and bank. The lanes from the short course start to the
#     intermediate start are instead the current Marshalling Zone shape (which
#     fills that stretch below the Transit Lane), split along the lifted lane
#     divider (CLONE).
LIFT = {
    # The lane divider from the short course start to the intermediate start,
    # moved slightly to meet the current one (DIVIDER_END).
    (1334.3, 790.7, 4001.4, 1063.3): ('lanes', 'Lane Divider',
                                      'fill:none;stroke:#808080;stroke-width:1;stroke-linecap:round;'
                                      'stroke-linejoin:round;stroke-dasharray:2, 2', 'between'),
    (3979.5, 904.5, 4038.0, 1158.0): ('lanes', 'Start Line', 'fill:none;stroke:#000000;stroke-width:2', None),
    # Racing arrows between the two starts.
    (3504.3, 885.8, 3695.6, 948.9): ('arrows', 'City Racing 4', None, None),
    (3491.8, 877.0, 3514.0, 898.6): ('arrows', 'City Racing 4 Head', None, None),
    (3484.6, 938.1, 3675.9, 1001.3): ('arrows', 'County Racing 4', None, None),
    (3472.2, 929.4, 3494.4, 951.0): ('arrows', 'County Racing 4 Head', None, None),
    # Paired crews going to the start.
    (4049.9, 1057.9, 4107.9, 1109.9): ('arrows', 'City Station split', None, None),
    (4040.1, 1049.1, 4062.3, 1070.7): ('arrows', 'City Station split Head', None, None),
    (4041.6, 1102.5, 4107.9, 1109.9): ('arrows', 'County Station Split', None, None),
    (4028.6, 1091.9, 4049.4, 1114.5): ('arrows', 'County Station Split Head', None, None),
    # Univ crews crossing to the Transit Lane under the marshal's direction.
    (3039.2, 748.4, 3204.3, 860.6): ('arrows', 'Univ Crossing', None, None),
    (3192.6, 741.1, 3215.2, 761.5): ('arrows', 'Univ Crossing Head', None, None),
    # Through the Gut to Donnington Bridge, and the spin there.
    (409.5, 2381.5, 554.0, 2411.1): ('arrows', 'Gut Downstream 1', None, None),
    (545.4, 2371.7, 566.9, 2393.9): ('arrows', 'Gut Downstream 1 Head', None, None),
    (626.2, 2229.8, 708.3, 2352.4): ('arrows', 'Gut Downstream 2', None, None),
    (695.2, 2218.9, 715.6, 2241.5): ('arrows', 'Gut Downstream 2 Head', None, None),
    (955.8, 2051.2, 1099.0, 2086.9): ('arrows', 'Gut Downstream 3', None, None),
    (1089.9, 2041.8, 1111.7, 2063.8): ('arrows', 'Gut Downstream 3 Head', None, None),
    (1518.3, 1856.5, 1663.7, 1882.0): ('arrows', 'Donnington Downstream', None, None),
    (1655.3, 1846.4, 1676.5, 1868.8): ('arrows', 'Donnington Downstream Head', None, None),
    (603.0, 2128.0, 692.1, 2245.6): ('arrows', 'Gut Upstream 1', None, None),
    (595.1, 2233.6, 616.0, 2256.0): ('arrows', 'Gut Upstream 1 Head', None, None),
    (942.9, 1972.1, 1084.6, 2013.1): ('arrows', 'Gut Upstream 3', None, None),
    (930.3, 2000.4, 952.3, 2022.2): ('arrows', 'Gut Upstream 3 Head', None, None),
    (1517.1, 1757.7, 1662.9, 1780.7): ('arrows', 'Donnington Upstream', None, None),
    (1504.2, 1768.5, 1525.3, 1790.9): ('arrows', 'Donnington Upstream Head', None, None),
    (1887.3, 1738.9, 1972.8, 1836.4): ('arrows', 'Donnington Spinning', None, None),
    (1874.3, 1735.3, 1895.0, 1757.9): ('arrows', 'Donnington Spinning Head', None, None),
    # Marshal 11 at Donnington Bridge: Bernard's marshal icon, as drawn.
    (1732.7, 1883.4, 1770.2, 1909.6): ('marshals', '11 Donnington Bridge', None, None),
    (1740.2, 1872.1, 1762.7, 1894.6): ('marshals', '11 Donnington Bridge Head', None, None),
}

# Intermediate-only text to lift: text -> (group, label, style).
LABEL_STYLE = 'font-size:10.5833px;line-height:1.25;font-family:sans-serif'
NUMBER_STYLE = 'font-size:16.9333px;line-height:1.25;font-family:sans-serif'
TEXTS = {
    'Start': ('labels', 'Start', LABEL_STYLE),
    'City Station': ('labels', 'City Start', LABEL_STYLE),
    'County Station': ('labels', 'County Start', LABEL_STYLE),
    '11': ('marshals', '11', NUMBER_STYLE),
}

# Where each kind of lifted item goes in the course layer: (group, after).
INTO = {
    'lanes': ('Lanes/Top Half', 'Lanes/Top Half/Lane Divider'),
    'arrows': ('Circulation Arrows', None),
    'labels': ('Lanes Labels', None),
    'marshals': ('Marshals', None),
}

# Short course elements the intermediate course does without, by name path
# within the course layer.
DROP = [
    'Lanes/Top Half/Start Line',
    'Lanes Labels/Start',
    'Lanes Labels/City Start',
    'Lanes Labels/County Start',
    'Circulation Arrows/City Station split',
    'Circulation Arrows/County Station Split',
    # The paired crews arrows in the short course's Marshalling Zone, which
    # is racing water on the intermediate course; the lifted arrows into the
    # start replace them.
    'Circulation Arrows/Gut Upstream 4',
    'Circulation Arrows/Gut Upstream 2',
    # Replaced by the published intermediate crossing (Univ Crossing above).
    "Circulation Arrows/St John's Crossing",
    # "Only crews boating or landing downstream are allowed to go through the
    # Gut": on the intermediate course others may be allowed through too.
    'Circulation Arrows/Isis Boathouse Crews Only',
    # The zone left between the intermediate start and the current zone end
    # is too short for its label beside the arrows into the start; the key
    # still names it.
    'Lanes Labels/Marshalling Area',
]

# Short course elements moved for the intermediate course, by the distance
# the same thing moved between the two PDFs: name paths -> (PDF box in the
# short course, PDF box in the intermediate course). Moving Bernard's current
# icons, rather than lifting the 2025 ones, keeps his later adjustments.
MOVE = {
    ('Marshals/Senior Umpire', 'Marshals/SU'): ((3191.0, 888.8), (3938.0, 1116.8)),
    ('Marshals/08 Greenbank', 'Marshals/08'): ((3780.9, 1086.6), (4206.9, 1189.3)),
}

# The short course's Marshalling Zone, cut off at the intermediate start.
CLIP = {
    'Lanes/Top Half/Marshalling Zone': 'upstream',
}

# The short course start line in the current source ('Lanes/Top Half/Start
# Line'), City end first: where the lifted lanes take over from its lanes.
SHORT_START = ((1127.4704, 212.77628), (1119.4126, 308.22367))
# Where the current lane divider meets that start line (the first point of
# 'Lanes/Top Half/County Station').
DIVIDER_END = (1122.9609, 266.19357)

# New lanes cut from a copy of a short course element: label -> (copy of,
# style, clip regions it is cut to).
CLONE = {
    'City Station Extension': ('Lanes/Top Half/Marshalling Zone',
                               'fill:#33ff33;fill-opacity:0.501961', ('between', 'city')),
    'County Station Extension': ('Lanes/Top Half/Marshalling Zone',
                                 'fill:#ff3333;fill-opacity:0.501961', ('between', 'county')),
}

RETEXT = {
    'Title/Short Course': ('Short Course', 'Intermediate Course'),
}


def to_map(x, y, half, shift=(0, 0)):
    s, tx, ty = half
    return s * x + tx + shift[0], s * y + ty + shift[1]


def sample(drawing, half, n=20):
    """Points along a drawing's lines and curves, in map units."""
    pts = []
    for it in drawing['items']:
        op, ps = it[0], [to_map(p.x, p.y, half) for p in it[1:]]
        if op == 'l':
            pts += [ps[0], ps[1]]
        elif op == 'c':
            for i in range(n + 1):
                t = i / n
                a = [(1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3]
                pts.append((sum(w * p[0] for w, p in zip(a, ps)), sum(w * p[1] for w, p in zip(a, ps))))
    return pts


def half_of(rect):
    return TOP if rect.y0 < SPLIT else BOTTOM


def fmt(v):
    return f'{v:.3f}'.rstrip('0').rstrip('.')


def path_d(drawing, half, shift=(0, 0)):
    def xy(p):
        return ' '.join(fmt(c) for c in to_map(p.x, p.y, half, shift))
    d, cur = [], None
    for it in drawing['items']:
        op, pts = it[0], it[1:]
        if op == 're':
            r = pts[0]
            pts, op = (r.tl, r.tr, r.br, r.bl, r.tl), 'poly'
        elif op == 'qu':
            q = pts[0]
            pts, op = (q.ul, q.ur, q.lr, q.ll, q.ul), 'poly'
        if cur is None or abs(pts[0].x - cur.x) > 1e-3 or abs(pts[0].y - cur.y) > 1e-3:
            d.append('M ' + xy(pts[0]))
        if op == 'l':
            d.append('L ' + xy(pts[1]))
        elif op == 'c':
            d.append('C ' + ' '.join(xy(p) for p in pts[1:]))
        elif op == 'poly':
            d.append('L ' + ' '.join(xy(p) for p in pts[1:]))
        cur = pts[-1]
    if drawing.get('closePath') or 'f' in drawing['type']:
        d.append('Z')
    return ' '.join(d)


def colour(rgb):
    return '#%02x%02x%02x' % tuple(round(c * 255) for c in rgb)


def drawing_style(drawing, half):
    s = half[0]
    st = []
    st.append('fill:' + (colour(drawing['fill']) if drawing.get('fill') and 'f' in drawing['type'] else 'none'))
    if 's' in drawing['type'] and drawing.get('color'):
        st.append('stroke:' + colour(drawing['color']))
        st.append('stroke-width:' + fmt(drawing['width'] * s))
        dashes = (drawing.get('dashes') or '').strip()
        nums = dashes[dashes.find('[') + 1:dashes.find(']')].split() if '[' in dashes else []
        if nums:
            st.append('stroke-dasharray:' + ','.join(fmt(float(n) * s) for n in nums))
        st.append('stroke-linecap:butt;stroke-linejoin:miter')
    return ';'.join(st)


def key(d):
    return (d.get('fill'), d.get('color'), tuple(round(v, 1) for v in d['rect']))


def extend(p, q, by):
    """The line through p and q, extended by `by` map units past each end."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    ux, uy = dx / n * by, dy / n * by
    return (p[0] - ux, p[1] - uy), (q[0] + ux, q[1] + uy)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    inter, short = pymupdf.open(sys.argv[1])[0], pymupdf.open(sys.argv[2])[0]

    # Intermediate-only drawings: a multiset difference, as identical items in
    # the two exports have identical boxes and colours.
    left = {}
    for d in short.get_drawings():
        left[key(d)] = left.get(key(d), 0) + 1
    only = []
    for d in inter.get_drawings():
        if left.get(key(d)):
            left[key(d)] -= 1
        else:
            only.append(d)
    found = {}
    for d in only:
        box = tuple(round(v, 1) for v in d['rect'])
        print('intermediate only:', box, '(lifted)' if box in LIFT else '(left out)', file=sys.stderr)
        if box in LIFT:
            found[box] = d
    missing = set(LIFT) - set(found)
    if missing:
        sys.exit(f'lift_course: not found in the PDF: {sorted(missing)}')

    root = ET.Element(f'{{{SVGNS}}}svg')
    root.append(ET.Comment(
        ' Generated by scripts/lift_course.py from the 2025 circulation PDFs by '
        'Bernard Tao (Oxford Isis Maps, CC BY 3.0); applied by scripts/strip_map.py. '
        'Do not edit by hand. '))
    groups = {}
    for kind, (into, after) in INTO.items():
        g = ET.SubElement(root, f'{{{SVGNS}}}g', {'data-into': into})
        if after:
            g.set('data-after', after)
        groups[kind] = g

    # Clip regions either side of the intermediate start line, which runs
    # from the City side to the County side like the short course one.
    start = found[(3979.5, 904.5, 4038.0, 1158.0)]['items'][0]
    a, b = to_map(start[1].x, start[1].y, TOP), to_map(start[2].x, start[2].y, TOP)
    if a[1] > b[1]:
        a, b = b, a
    i0, i1 = extend(a, b, 150)
    s0, s1 = extend(*SHORT_START, 150)
    far = 1000

    # The lifted divider, moved to meet the current one where the short
    # course lanes end, and the regions either side of it.
    divider_box = (1334.3, 790.7, 4001.4, 1063.3)
    pts = sample(found[divider_box], TOP)
    near = min(pts, key=lambda p: abs(p[0] - DIVIDER_END[0]))
    shift = (0, DIVIDER_END[1] - near[1])
    print(f'lane divider moved {shift[1]:.2f} map units to meet the current one', file=sys.stderr)
    pts = sorted(((x, y + shift[1]) for x, y in pts), key=lambda p: p[0])
    a0, a1 = extend(pts[0], pts[1], 30)[0], extend(pts[-2], pts[-1], 30)[1]
    line = [a0] + pts + [a1]
    regions = {
        'between': [s0, i0, i1, s1],
        'upstream': [i0, (i0[0] + far, i0[1]), (i1[0] + far, i1[1]), i1],
        'city': line + [(a1[0], a1[1] - far), (a0[0], a0[1] - far)],
        'county': line + [(a1[0], a1[1] + far), (a0[0], a0[1] + far)],
    }
    for name, pts in regions.items():
        cp = ET.SubElement(groups['lanes'], f'{{{SVGNS}}}clipPath', {'id': 'intermediate-' + name})
        ET.SubElement(cp, f'{{{SVGNS}}}path', {'d': 'M ' + ' L '.join(f'{fmt(x)} {fmt(y)}' for x, y in pts) + ' Z'})

    for box, (kind, label, style, clip) in LIFT.items():
        d = found[box]
        half = half_of(d['rect'])
        attrs = {'d': path_d(d, half, shift if box == divider_box else (0, 0)),
                 'style': style or drawing_style(d, half), 'data-label': label}
        if clip:
            attrs['clip-path'] = f'url(#intermediate-{clip})'
        ET.SubElement(groups[kind], f'{{{SVGNS}}}path', attrs)

    spans = {}
    for blk in inter.get_text('rawdict')['blocks']:
        for line in blk.get('lines', []):
            for sp in line['spans']:
                t = ''.join(c['c'] for c in sp['chars']).strip()
                spans.setdefault(t, []).append((sp, line['dir']))
    for text, (kind, label, style) in TEXTS.items():
        # The intermediate copy of the text: the one not at the same place in
        # the short course PDF.
        short_boxes = [tuple(round(v, 1) for v in sp['bbox'])
                       for blk in short.get_text('rawdict')['blocks'] for line in blk.get('lines', [])
                       for sp in line['spans'] if ''.join(c['c'] for c in sp['chars']).strip() == text]
        cands = [(sp, dr) for sp, dr in spans.get(text, []) if tuple(round(v, 1) for v in sp['bbox']) not in short_boxes]
        if len(cands) != 1:
            sys.exit(f'lift_course: {len(cands)} intermediate-only copies of {text!r}; expected 1')
        sp, (dx, dy) = cands[0]
        half = TOP if sp['origin'][1] < SPLIT else BOTTOM
        x, y = to_map(*sp['origin'], half)
        angle = math.degrees(math.atan2(dy, dx))
        t = ET.SubElement(groups[kind], f'{{{SVGNS}}}text', {
            'transform': f'translate({fmt(x)},{fmt(y)}) rotate({fmt(angle)})' if abs(angle) > 0.01 else f'translate({fmt(x)},{fmt(y)})',
            'style': style, 'data-label': label})
        t.text = text

    ops = ET.SubElement(root, f'{{{SVGNS}}}g', {'data-ops': 'true'})
    into, after = INTO['lanes']
    for label, (path, style, (outer, inner)) in CLONE.items():
        ET.SubElement(ops, f'{{{SVGNS}}}g', {
            'data-op': 'clone', 'data-path': path, 'data-label': label, 'data-style': style,
            'data-into': into, 'data-after': after,
            'data-clip-outer': f'url(#intermediate-{outer})', 'data-clip': f'url(#intermediate-{inner})'})
    for path in DROP:
        ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'drop', 'data-path': path})
    for paths, (frm, to) in MOVE.items():
        dx, dy = (TOP[0] * (to[0] - frm[0]), TOP[0] * (to[1] - frm[1]))
        for path in paths:
            ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'move', 'data-path': path,
                                                  'data-dx': fmt(dx), 'data-dy': fmt(dy)})
    for path, region in CLIP.items():
        ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'clip', 'data-path': path,
                                              'data-clip': f'url(#intermediate-{region})'})
    for path, (old, new) in RETEXT.items():
        ET.SubElement(ops, f'{{{SVGNS}}}g', {'data-op': 'retext', 'data-path': path,
                                              'data-old': old, 'data-new': new})

    ET.indent(root)
    ET.ElementTree(root).write(sys.argv[3], xml_declaration=True, encoding='UTF-8')
    print(sys.argv[3], file=sys.stderr)


if __name__ == '__main__':
    main()
