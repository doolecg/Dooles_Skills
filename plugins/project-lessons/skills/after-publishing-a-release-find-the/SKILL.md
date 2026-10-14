---
name: after-publishing-a-release-find-the
description: After publishing a release, find the tag build with `gh run list --branch <version>` (the tag name is the branch name), wait with `gh run watch <id> --exit-status`, then list `gh release view <version
---

# after-publishing-a-release-find-the

Drafted from a working procedure.

1. After publishing a release, find the tag build with `gh run list --branch <version>` (the tag name is the branch name), wait with `gh run watch <id> --exit-status`, then list `gh release view <version> --json assets`. The release is incomplete until the installers are attached, because the in-app updater downloads them from there.
