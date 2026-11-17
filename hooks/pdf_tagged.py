"""Make the PDFs accessible: tagged, with bookmarks.

mkdocs-exporter (6.2) prints each page with Playwright's page.pdf() but does
not ask for a tagged PDF or an outline, both off by default. Untagged, a PDF
has no structure for screen readers (headings, lists, tables, reading order)
and no language; without an outline, it has no bookmarks. This sets both on
every PDF Playwright makes during the build, unless the caller sets them:
Chromium then tags the PDF, gives it the page's language (lang="en") and
builds its bookmarks from the headings. The pages look exactly the same
(checked by rendering them before and after).

hooks/map_pdf.py's per-map pages go through here too, though joining them
with pypdf keeps neither tags nor bookmarks; they are images of the maps.
"""
from playwright.async_api._generated import Page as AsyncPage
from playwright.sync_api._generated import Page as SyncPage

_async_pdf = AsyncPage.pdf
_sync_pdf = SyncPage.pdf


async def async_pdf(self, *args, **kwargs):
    kwargs.setdefault('tagged', True)
    kwargs.setdefault('outline', True)
    return await _async_pdf(self, *args, **kwargs)


def sync_pdf(self, *args, **kwargs):
    kwargs.setdefault('tagged', True)
    kwargs.setdefault('outline', True)
    return _sync_pdf(self, *args, **kwargs)


AsyncPage.pdf = async_pdf
SyncPage.pdf = sync_pdf
