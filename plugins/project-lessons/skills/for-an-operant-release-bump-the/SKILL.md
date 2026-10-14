---
name: for-an-operant-release-bump-the
description: For an Operant release, bump the version in package.json and package-lock.json, put the new top section in RELEASE_NOTES.md, and use that section as the GitHub release body (`gh release create <versio
---

# for-an-operant-release-bump-the

Drafted from a working procedure.

1. For an Operant release, bump the version in package.json and package-lock.json, put the new top section in RELEASE_NOTES.md, and use that section as the GitHub release body (`gh release create <version> --notes-file`). After fast-forwarding main, delete the dev branch locally and on origin.

## Learned correction

- Stage Operant release commits by naming the files (package.json, package-lock.json, RELEASE_NOTES.md). Never use git add -A, because the working tree holds untracked stray files such as .playwright-mcp/, docs/design/ and a loose .py file that must not be committed.

## Learned correction

- After an Operant release, delete all stale dev-<version> branches, not only the one just released. Before deleting each one, check that it has no commits missing from origin/main, then delete it on origin.
