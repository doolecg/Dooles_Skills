---
name: 9-push
description: Close out a development branch: verify, then merge locally, open a PR, or hand back. Use when work on a branch is complete.
---

1. Run the full test suite and build. Not green: stop and fix; don't finish.
2. Find the base branch (`git merge-base`, or ask). Confirm no uncommitted changes, debug logging, temp files or stray worktrees.
3. Offer one choice: merge locally into base, push and open a PR, or leave the branch for the user. Recommend one.
4. Merge: merge or fast-forward into base, re-run tests on the result, delete the branch (local, and remote if pushed) once merged.
   PR: push the branch, open it with a short description (what changed, how verified), link the issue.
5. Report the result with the command output that proves it.

Commit and PR messages: short, plain, no AI attribution lines.
