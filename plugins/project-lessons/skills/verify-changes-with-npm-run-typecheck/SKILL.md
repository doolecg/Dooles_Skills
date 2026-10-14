---
name: verify-changes-with-npm-run-typecheck
description: Verify changes with `npm run typecheck` and then `npx vitest run` (90 files, 1014 tests at the time) before reporting done. Re-run both after any later edit to a file.
---

# verify-changes-with-npm-run-typecheck

Drafted from a working procedure.

1. Verify changes with `npm run typecheck` and then `npx vitest run` (90 files, 1014 tests at the time) before reporting done. Re-run both after any later edit to a file.
2. After Operant changes, run `npm run typecheck` and then `npx vitest run` over the full suite. Both must pass before reporting done.
