#!/usr/bin/env bash
# Builds every briefing deck (<deck>/slides.md) into ../site/briefings/<deck>/,
# with its PDF, to be served at https://tamesisregatta.org/briefings/<deck>/.
# Run it after `mkdocs build`, which clears site/.

set -euo pipefail

cd "$(dirname "$0")"

out_root="../site/briefings"
mkdir -p "$out_root"

for slides in */slides.md; do
    deck="$(dirname "$slides")"
    echo "Building briefing deck: $deck"
    npx slidev build "$slides" --base "/briefings/${deck}/" --out "$(pwd)/${out_root}/${deck}"
    # Slidev leaves a cache next to the entry file
    rm -rf "${deck}/node_modules"
done
