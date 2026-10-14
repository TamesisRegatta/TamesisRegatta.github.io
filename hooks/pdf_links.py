"""Keep mailto: and tel: links working in the PDFs.

mkdocs-exporter (6.2) turns every link without a host into a full URL on the
site, so that relative links work from a downloaded PDF. It treats mailto:
and tel: as relative too, so mailto:regatta@linacre.ox.ac.uk becomes
https://tamesisregatta.org/event-plan/regatta@linacre.ox.ac.uk. This wraps
its link rewriting to leave any link with a scheme (mailto:, tel:, ...) as it
was, and rewrite the rest exactly as before.
"""
from urllib.parse import urlparse

from mkdocs_exporter.formats.pdf.preprocessor import Preprocessor

_rewrite_links = Preprocessor.rewrite_links


def rewrite_links(self, base, root):
    kept = [(a, a['href']) for a in self.html.find_all('a', href=True)
            if urlparse(a['href']).scheme and not urlparse(a['href']).netloc]
    _rewrite_links(self, base, root)
    for a, href in kept:
        a['href'] = href


Preprocessor.rewrite_links = rewrite_links
