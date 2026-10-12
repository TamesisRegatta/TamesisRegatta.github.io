"""Replace the course map page's PDF with one page per map, each page the size
of its map.

mkdocs-exporter prints every page through Paged.js, which allows one page size
per document, but the maps have very different shapes. So, after the exporter
has written site/map/index.pdf, this renders each map image listed in the
page's print section (.tamesis-map-print in map.md) to its own page with
headless Chromium, as the exporter does, and joins them with pypdf. Both come
with mkdocs-exporter. The page's "Download as PDF" button is unchanged.

Does nothing when PDF export is off (no PDF to replace).
"""
import io
import logging
import os
import re
import tempfile
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urljoin
from urllib.request import pathname2url

from mkdocs.plugins import event_priority

log = logging.getLogger('mkdocs.hooks.map_pdf')

PAGE = 'map/index.html'
PDF = 'map/index.pdf'
WIDTH_MM = 297  # every page this wide (A4's long side); height follows the map
IMAGES = re.compile(r'<div class="tamesis-map-print">(.*?)</div>', re.S)
SRC = re.compile(r'<img[^>]*\ssrc="([^"]+)"')


def aspect(svg_path):
    """Width over height, from the SVG's viewBox."""
    x, y, w, h = (float(v) for v in ET.parse(svg_path).getroot().get('viewBox').split())
    return w / h


# After the exporter has written its PDFs (it does so at priority -90).
@event_priority(-110)
def on_post_build(config, **kwargs):
    site = config['site_dir']
    pdf_path = os.path.join(site, PDF)
    if not os.path.exists(pdf_path):
        return

    html = open(os.path.join(site, PAGE), encoding='utf-8').read()
    section = IMAGES.search(html)
    if not section:
        log.warning('map_pdf: no .tamesis-map-print section in %s', PAGE)
        return
    page_url = 'file:' + pathname2url(os.path.join(site, PAGE))
    images = [unquote(urljoin(page_url, src))[len('file:'):] for src in SRC.findall(section.group(1))]

    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader, PdfWriter

    writer = PdfWriter()
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--allow-file-access-from-files', '--font-render-hinting=none'])
        page = browser.new_page()
        for image in images:
            height_mm = WIDTH_MM / aspect(image)
            # A file: page beside the image, since about:blank (set_content)
            # may not load file: images.
            with tempfile.NamedTemporaryFile('w', suffix='.html', dir=os.path.dirname(image),
                                             delete=False, encoding='utf-8') as wrapper:
                wrapper.write(
                    '<!doctype html><html><body style="margin:0;background:#fff">'
                    f'<img src="{pathname2url(os.path.basename(image))}" style="display:block;'
                    f'width:{WIDTH_MM}mm;height:{height_mm:.3f}mm"></body></html>')
            try:
                page.goto('file:' + pathname2url(wrapper.name), wait_until='load')
                pdf = page.pdf(width=f'{WIDTH_MM}mm', height=f'{height_mm:.3f}mm',
                               print_background=True, page_ranges='1')
            finally:
                os.unlink(wrapper.name)
            writer.append(PdfReader(io.BytesIO(pdf)))
        browser.close()

    writer.add_metadata({'/Title': 'Tamesis Regatta course maps'})
    with open(pdf_path, 'wb') as f:
        writer.write(f)
    log.info('map_pdf: wrote %s, %d page(s) sized to their maps', PDF, len(images))
