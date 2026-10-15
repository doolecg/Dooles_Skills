---
name: to-build-the-github-release-body
description: To build the GitHub release body, print RELEASE_NOTES.md from the top up to the line before the previous version heading (awk with an exit on that heading), then trim trailing blank lines and pass the
---

# to-build-the-github-release-body

Drafted from a working procedure.

1. To build the GitHub release body, print RELEASE_NOTES.md from the top up to the line before the previous version heading (awk with an exit on that heading), then trim trailing blank lines and pass the file to `gh release create --notes-file`. Confirm the body contains only the new version's section before publishing.
2. The top section runs from its `# <App> <version>` heading up to the next `# <App>` heading.
