"""Strip Bernard Tao's Oxford Isis Maps SVG down to the SVGs the course map
page (docs/map.md) uses.

Usage, from the repo root (Playwright comes with the site's requirements):

    .venv/bin/python scripts/strip_map.py path/to/IsisMap.svg docs/assets/map

The source SVG is the full Inkscape document with every event's layers; it is
not kept in this repository. This script writes:

    tamesis-map.svg          the interactive map: base map, overlays, courses
    boathouse-rafts.svg      the Boathouse Island raft plan, cropped
    print/course-<id>.svg    per course: base map, overlays and that course
    print/boathouse-rafts.svg
                             the print/ files have Noto Sans embedded, since
                             an SVG shown as an <img> cannot use the page's
                             fonts; they are the pages of the map PDF
                             (hooks/map_pdf.py)

Layers and elements are found by their Inkscape names (the label shown in the
Layers panel) as a path through the named layers and groups above them, e.g.
'Regattas/Thamesis Short Course'. A path that matches nothing or more than one
element is an error, so a renamed layer in a new version of the source fails
loudly rather than silently dropping out.

To add a course: add its layer to OUTPUTS['tamesis-map.svg']['keep'] with
data-course and data-title, exclude anything inside it that belongs elsewhere
(like the raft inset), rerun, and add a <figure> for print/course-<id>.svg to
the print section of docs/map.md.
"""
import base64
import os
import re
import sys
import xml.etree.ElementTree as ET

SVGNS = 'http://www.w3.org/2000/svg'
INKNS = 'http://www.inkscape.org/namespaces/inkscape'
SODNS = 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd'
XLNS = 'http://www.w3.org/1999/xlink'
SVG, INK = f'{{{SVGNS}}}', f'{{{INKNS}}}'
LABEL = INK + 'label'
ET.register_namespace('', SVGNS)
ET.register_namespace('xlink', XLNS)

COURSE = 'Regattas/Thamesis Short Course'
RAFTS = COURSE + '/Boathouse Island'

# Per output: the layers to keep, by name path, and the attributes that tell
# docs/assets/map.js what each one is. Nested layers are lifted to the top
# level, so the stacking order follows the source.
#   data-layer="base"   always shown
#   data-course="x"     one of a mutually exclusive set (plus "None"); the
#                       one with data-default="true" is selected initially
#   data-overlay="x"    independent on/off, initially on
# data-title is the label of its control. 'exclude' removes elements that live
# inside a kept layer but belong in another output. 'crop' cuts the viewBox
# down to the content.
OUTPUTS = {
    'tamesis-map.svg': {
        'keep': {
            'Logo & Disclaimer/Disclaimer & License': {'data-layer': 'base'},  # CC-BY attribution
            'Bottom Half': {'data-layer': 'base'},  # river outline, buildings, labels
            'Top Half': {'data-layer': 'base'},
            'AEDs': {'data-overlay': 'aed', 'data-title': 'AEDs'},
            COURSE: {'data-course': 'short', 'data-title': 'Short course', 'data-default': 'true'},
        },
        'exclude': [RAFTS],  # its own file below
    },
    'boathouse-rafts.svg': {
        'keep': {
            RAFTS: {'data-layer': 'base'},
        },
        'crop': True,
    },
}

# Elements not wanted in any output. Hidden elements inside kept layers are
# dropped as well.
DROP = [
    COURSE + '/Title/Linacre',  # club logo, linked to a file outside the SVG
]

# Links to keep. Every other <a> becomes a plain <g>: the AED and course keys
# are wrapped in leftover copies of the licence link, which made them
# clickable and put them in the keyboard tab order.
KEEP_LINKS = [
    'Logo & Disclaimer/Disclaimer & License/License Text',  # "licensed under CC-BY 3.0"
]


# Map items that can be clicked or tapped for information (map.js):
# data-select is the kind, data-name the popup heading; the other data-*
# fields are shown in the popup (data-w3w: a what3words address, from the AED
# key drawn on the map). Items that are the same real thing drawn more than
# once share a data-id, and selecting one marks them all.
def aed(name, w3w, ident):
    return {'data-select': 'aed', 'data-id': 'aed-' + ident, 'data-name': 'AED: ' + name, 'data-w3w': w3w}


SELECTABLE = {
    'AEDs/AED Top Half/PMB-AED': aed('Pembroke Boat House', 'glitz.actual.horn', 'pembroke'),
    'AEDs/AED Top Half/Balliol-AED': aed('Balliol Boat House', 'speech.gums.stocks', 'balliol'),
    'AEDs/AED Top Half/Univ-AED': aed('University College Boat House', 'nation.bunks.levels', 'univ'),
    # Longbridges is at both ends of the map: the end of the top half and the
    # start of the bottom half.
    'AEDs/AED Top Half/LB-AED-Top': aed('Longbridges Boat House', 'normal.when.sings', 'longbridges'),
    'AEDs/AED Bottom Half/LB-AED-Bottom': aed('Longbridges Boat House', 'normal.when.sings', 'longbridges'),
    'AEDs/AED Bottom Half/Falcon-AED': aed('Falcon Boat House', 'margin.rating.votes', 'falcon'),
    'AEDs/AED Bottom Half/Riverside-AED': aed('The Riverside Centre', 'rider.burst.vouch', 'riverside'),
}

# Colours that change between light and dark (docs/assets/extra.css);
# everything else keeps its value but is still routed through a variable,
# --map-c-RRGGBB, so it can be tuned later.
NAMED = {
    '#000000': 'ink',
    '#ffffff': 'paper',
    '#ffffcc': 'building',
    '#ffffc8': 'building',
    '#ffdd99': 'building-alt',
}
CROP_MARGIN = 2  # map units around cropped content
PRINT_FONTS = [  # (file in docs/assets/fonts, font-style), embedded in print/
    ('noto-sans-latin-wght-normal.woff2', 'normal'),
    ('noto-sans-latin-wght-italic.woff2', 'italic'),
]
REF = re.compile(r'url\(#([^)]+)\)|^#(.+)$')
WARNED = set()


class Source:
    """A parsed copy of the source SVG, with name-path lookup."""

    def __init__(self, path):
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        self.parent = {c: p for p in self.root.iter() for c in p}
        self.paths = {}
        self._index(self.root, [])

    def _index(self, e, prefix):
        for c in e:
            label = c.get(LABEL)
            path = prefix + [label] if label else prefix
            if label:
                self.paths.setdefault('/'.join(path), []).append(c)
            self._index(c, path)

    def optional(self, paths):
        """The paths that exist; warn about the others, which may be gone or
        renamed in a new version of the source."""
        present = [p for p in paths if p in self.paths]
        for p in paths:
            if p not in self.paths and p not in WARNED:
                WARNED.add(p)
                print(f'strip_map: warning: nothing named {p!r} in the source; skipped', file=sys.stderr)
        return present

    def find(self, path):
        found = self.paths.get(path, [])
        if len(found) != 1:
            sys.exit(f'strip_map: {len(found)} elements named {path!r} in the source; expected exactly 1')
        return found[0]


def colour_var(m):
    prop, val = m.group(1), m.group(2).lower()
    name = NAMED.get(val, 'c-' + val[1:])
    return f'{prop}:var(--map-{name},{val})'


def clean(e):
    """Drop editor-only attributes, keep labels as data-label, theme colours."""
    for k in list(e.attrib):
        if k == LABEL:
            e.set('data-label', e.attrib.pop(k).replace('Thamesis', 'Tamesis'))
        elif k.startswith(INK) or k.startswith(f'{{{SODNS}}}'):
            del e.attrib[k]
    st = e.get('style')
    if st:
        st = re.sub(r'-inkscape-font-specification:[^;]+;?', '', st)
        # The site self-hosts Noto Sans (extra.css); use it for all map text.
        st = re.sub(r'font-family:[^;]+', "font-family:'Noto Sans',sans-serif", st)
        st = re.sub(r'(fill|stroke|stop-color):(#[0-9a-fA-F]{6})\b', colour_var, st)
        e.set('style', st)
    if e.tag == SVG + 'text':
        for t in e.iter():
            if t.text:
                t.text = t.text.replace('Thamesis', 'Tamesis')


def refs(el):
    found = set()
    for x in el.iter():
        for v in x.attrib.values():
            for a, b in REF.findall(v):
                found.add(a or b)
    return found


def build(src_path, keep, exclude=()):
    src = Source(src_path)
    root, parent = src.root, src.parent
    kept = {src.find(path): attrs for path, attrs in keep.items()}
    unwanted = {src.find(path) for path in exclude} | {src.find(path) for path in src.optional(DROP)}
    links = {src.find(path) for path in src.optional(KEEP_LINKS)}
    selectable = {src.find(path): SELECTABLE[path] for path in src.optional(SELECTABLE)}

    # Lift nested kept layers to the top level, in document order so stacking
    # is unchanged: straight after a kept ancestor (it was drawn over that
    # ancestor's earlier children), otherwise in the ancestor's place. Their
    # ancestors must not carry a transform. Dict order matters: list a layer
    # after any kept layer that contains it.
    for e in kept:
        p = parent[e]
        if p is root:
            continue
        top, a = p, p
        while a is not root:
            if a.get('transform'):
                sys.exit(f'strip_map: {e.get(LABEL)!r} is inside {a.get(LABEL) or a.get("id")!r}, '
                         'which is moved or scaled; lifting it out would misplace it')
            top, a = a, parent[a]
        p.remove(e)
        i = list(root).index(top)
        root.insert(i + 1 if top in kept else i, e)
        parent[e] = root

    # Remove everything at the top level except kept layers and defs.
    for c in list(root):
        if c.tag != SVG + 'defs' and c not in kept:
            root.remove(c)
    for c, attrs in kept.items():
        for k, v in attrs.items():
            c.set(k, v)
        # No display on kept layers: Inkscape's display:none/inline would
        # override the stylesheet that map.js uses to show and hide them.
        st = re.sub(r'display:[^;]+;?', '', c.get('style') or '').strip(';')
        if st:
            c.set('style', st)
        else:
            c.attrib.pop('style', None)
    for e in list(root.iter()):
        if e in unwanted or 'display:none' in (e.get('style') or ''):
            parent[e].remove(e)

    # Keep only the defs that kept content references (markers, text shapes),
    # following references inside defs too.
    defs = root.find(SVG + 'defs')
    by_id = {d.get('id'): d for d in defs}
    wanted, todo = set(), set()
    for c in root:
        if c is not defs:
            todo |= refs(c)
    while todo:
        i = todo.pop()
        if i in wanted or i not in by_id:
            continue
        wanted.add(i)
        todo |= refs(by_id[i])
    for d in list(defs):
        if d.get('id') not in wanted:
            defs.remove(d)

    for e in root.iter():
        if e.tag == SVG + 'a' and e not in links:
            e.tag = SVG + 'g'
            for k in [k for k in e.attrib if k.endswith('href')]:
                del e.attrib[k]
        clean(e)
        for k, v in selectable.get(e, {}).items():
            e.set(k, v)

    # Responsive: size from the viewBox only.
    for k in ('width', 'height', 'version', 'xml:space', 'id'):
        root.attrib.pop(k, None)
    root.set('class', 'tamesis-map')
    return src.tree


def crop(path):
    """Cut the viewBox down to the drawn content, plus a small margin."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto('file://' + os.path.abspath(path))
        box = pg.evaluate('(() => { const b = document.documentElement.getBBox();'
                          ' return [b.x, b.y, b.width, b.height]; })()')
        b.close()
    x, y, w, h = box
    m = CROP_MARGIN
    tree = ET.parse(path)
    tree.getroot().set('viewBox', f'{x - m:.3f} {y - m:.3f} {w + 2 * m:.3f} {h + 2 * m:.3f}')
    tree.write(path, xml_declaration=True, encoding='UTF-8')


def embed_fonts(path, fonts_dir):
    """Add Noto Sans to an SVG as data URIs, for use as an <img>."""
    css = ''
    for name, style in PRINT_FONTS:
        data = base64.b64encode(open(os.path.join(fonts_dir, name), 'rb').read()).decode()
        css += ("@font-face{font-family:'Noto Sans';font-style:%s;font-weight:100 900;"
                "src:url(data:font/woff2;base64,%s) format('woff2')}" % (style, data))
    tree = ET.parse(path)
    style = ET.SubElement(tree.getroot().find(SVG + 'defs'), SVG + 'style')
    style.text = css
    tree.write(path, xml_declaration=True, encoding='UTF-8')


def write(src, path, keep, exclude=(), do_crop=False, fonts_dir=None):
    build(src, keep, exclude).write(path, xml_declaration=True, encoding='UTF-8')
    if do_crop:
        crop(path)
    if fonts_dir:
        embed_fonts(path, fonts_dir)
    print(path, os.path.getsize(path), 'bytes, viewBox', ET.parse(path).getroot().get('viewBox'))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, outdir = sys.argv[1], sys.argv[2]
    fonts_dir = os.path.join(os.path.dirname(os.path.abspath(outdir)), 'fonts')
    os.makedirs(os.path.join(outdir, 'print'), exist_ok=True)
    for name, cfg in OUTPUTS.items():
        keep, exclude, do_crop = cfg['keep'], cfg.get('exclude', ()), cfg.get('crop', False)
        write(src, os.path.join(outdir, name), keep, exclude, do_crop)
        courses = [k for k, v in keep.items() if 'data-course' in v]
        if not courses:
            write(src, os.path.join(outdir, 'print', name), keep, exclude, do_crop, fonts_dir)
        for c in courses:
            only = {k: v for k, v in keep.items() if k == c or k not in courses}
            write(src, os.path.join(outdir, 'print', 'course-%s.svg' % keep[c]['data-course']),
                  only, exclude, do_crop, fonts_dir)


if __name__ == '__main__':
    main()
