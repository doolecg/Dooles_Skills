---
name: after-operant-changes-run-npm-run
description: After Operant changes, run `npm run typecheck` and then `npx vitest run` over the full suite. Both must pass before reporting done.
---

# after-operant-changes-run-npm-run

Drafted from a working procedure.

1. After Operant changes, run `npm run typecheck` and then `npx vitest run` over the full suite. Both must pass before reporting done.

## Learned correction

- Full Operant verification is npm run typecheck, then npx vitest run, then npm run build. The skill lists only the first two, so add the build step.

## Learned correction

- When the user asks for quick checks and then to run the app, run `npm run typecheck` and the full `npx vitest run`, then tell the user to start the Dev Run themselves. Do not launch the app. If typecheck fails only in files a subagent is still editing, say so and name those files.
