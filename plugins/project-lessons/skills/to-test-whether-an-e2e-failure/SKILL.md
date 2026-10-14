---
name: to-test-whether-an-e2e-failure
description: To test whether an e2e failure predates your change, create a git worktree at HEAD, link node_modules into it with `cmd //c mklink /J` on Windows, build, and run the same script there. Afterwards remo
---

# to-test-whether-an-e2e-failure

Drafted from a working procedure.

1. To test whether an e2e failure predates your change, create a git worktree at HEAD, link node_modules into it with `cmd //c mklink /J` on Windows, build, and run the same script there. Afterwards remove it with `git worktree remove --force` and run `git worktree prune`.
2. To check whether an e2e failure predates your change, run `git worktree add ../<name>-base HEAD`, link node_modules into it with `cmd //c mklink /J`, build and run the test there. Then remove it with `git worktree remove --force` and `git worktree prune`.
