---
name: when-several-subagents-edit-overlapping
description: When several subagents edit overlapping code in parallel, one agent's half-finished test file can make `npm run typecheck` fail in another agent's run. Run typecheck and the full vitest suite once, af
---

# when-several-subagents-edit-overlapping

Drafted from a working procedure.

1. When several subagents edit overlapping code in parallel, one agent's half-finished test file can make `npm run typecheck` fail in another agent's run. Run typecheck and the full vitest suite once, after every worker has reported, instead of trusting each worker's own check.
