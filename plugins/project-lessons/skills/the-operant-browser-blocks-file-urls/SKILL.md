---
name: the-operant-browser-blocks-file-urls
description: The Operant Browser blocks file: URLs, so to render-check docs/tracker.html, navigate to about:blank, inject its HTML and script with browser_evaluate, and take a screenshot. The injected copy can dri
---

# the-operant-browser-blocks-file-urls

Drafted from a working procedure.

1. The Operant Browser blocks file: URLs, so to render-check docs/tracker.html, navigate to about:blank, inject its HTML and script with browser_evaluate, and take a screenshot. The injected copy can drift from the file, so say what was not checked.

## Learned correction

- To view a generated HTML file in the Operant browser, navigate to the local URL the browser serves for that file. The file: scheme is blocked, and injecting a copy with browser_evaluate drifts from the real file, so use it only as a last resort.

## Learned correction

- The skill the-operant-browser-blocks-file-urls says to inject the HTML with browser_evaluate. This session showed that is the wrong first step: navigate to the local URL the Operant browser serves for the file instead.

## Learned correction

- The the-operant-browser-blocks-file-urls skill tells you to inject a copy of an HTML file with browser_evaluate. This session showed that serving the real file and navigating to its local URL in the Operant browser works, so the injection step is outdated and drifts from the file.
