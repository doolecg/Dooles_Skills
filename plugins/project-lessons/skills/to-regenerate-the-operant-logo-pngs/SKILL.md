---
name: to-regenerate-the-operant-logo-pngs
description: To regenerate the Operant logo PNGs, render docs/logo.svg with headless Chromium through playwright-core at about 815 px wide with a transparent background, and make docs/logo_icon.png 64 px and build
---

# to-regenerate-the-operant-logo-pngs

Drafted from a working procedure.

1. To regenerate the Operant logo PNGs, render docs/logo.svg with headless Chromium through playwright-core at about 815 px wide with a transparent background, and make docs/logo_icon.png 64 px and build/icon.png 512 px. Then regenerate build/icon.ico and build/icon.icns, check that the corner alpha is 0, and inspect a copy composited on a dark background before reporting it done.
2. To regenerate the logo from the vector source, render docs/logo.svg with headless Chromium through playwright-core at about 815 px wide with a transparent background. Derive the 64 px in-app icon and the 512 px program icon from that render, then regenerate build/icon.ico and build/icon.icns with build/icon.py. Check that the corner pixels have alpha 0.
