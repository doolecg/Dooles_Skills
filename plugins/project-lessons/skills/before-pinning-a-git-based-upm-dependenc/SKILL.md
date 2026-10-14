---
name: before-pinning-a-git-based-upm-dependenc
description: Before pinning a Git-based UPM dependency to a tag, confirm the tag exists with `git ls-remote --tags <url> <tag>`. When editing Packages/manifest.json, do not rewrite it with json.dump, because that 
---

# before-pinning-a-git-based-upm-dependenc

Drafted from a working procedure.

1. Before pinning a Git-based UPM dependency to a tag, confirm the tag exists with `git ls-remote --tags <url> <tag>`. When editing Packages/manifest.json, do not rewrite it with json.dump, because that re-sorts the dependency list. Make a minimal text edit so Unity-added entries such as com.unity.ai.* stay as they are.
