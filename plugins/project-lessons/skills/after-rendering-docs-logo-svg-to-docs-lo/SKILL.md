---
name: after-rendering-docs-logo-svg-to-docs-lo
description: After rendering docs/logo.svg to docs/logo.png, docs/logo_icon.png and build/icon.png, check with PIL that the corner alpha is 0. Then composite build/icon.png on a dark background, save a temporary p
---

# after-rendering-docs-logo-svg-to-docs-lo

Drafted from a working procedure.

1. After rendering docs/logo.svg to docs/logo.png, docs/logo_icon.png and build/icon.png, check with PIL that the corner alpha is 0. Then composite build/icon.png on a dark background, save a temporary preview, view it, and delete the preview before finishing.
