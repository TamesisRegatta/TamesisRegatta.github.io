// True while the deck is being exported to PDF. The exporter loads the deck
// with ?print, which with hash routing Slidev's own isPrintMode does not see.
export function inPdf() {
  return typeof window !== 'undefined' && new URLSearchParams(window.location.search).has('print')
}
