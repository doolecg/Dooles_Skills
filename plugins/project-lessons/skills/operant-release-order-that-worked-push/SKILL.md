---
name: operant-release-order-that-worked-push
description: Operant release order that worked: push dev-<version> and wait for its CI to go green, then fast-forward main and push it, then create the GitHub release and tag from RELEASE_NOTES.md. Tag builds atta
---

# operant-release-order-that-worked-push

Drafted from a working procedure.

1. Operant release order that worked: push dev-<version> and wait for its CI to go green, then fast-forward main and push it, then create the GitHub release and tag from RELEASE_NOTES.md. Tag builds attach installers to the release, while branch builds keep artifacts for only 3 days, so check the release has its installer assets once the tag CI run finishes.

## Learned correction

- For an Operant release, bump the version in package.json and package-lock.json, put the new top section in RELEASE_NOTES.md, and use that section as the GitHub release body (`gh release create <version> --notes-file`). After fast-forwarding main, delete the dev branch locally and on origin.

## Learned correction

- After publishing a release, find the tag build with `gh run list --branch <version>` (the tag name is the branch name), wait with `gh run watch <id> --exit-status`, then list `gh release view <version> --json assets`. The release is incomplete until the installers are attached, because the in-app updater downloads them from there.
