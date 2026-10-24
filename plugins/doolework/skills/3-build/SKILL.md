---
name: 3-build
description: Implement a plan, spec or ticket in code. Use when the design is settled and it's time to write the code.
---

Input is a plan from `2-plan`, a spec, or a ticket. Fetch it, state its title and the outcome in one line, then build. Ambiguous reference: ask.

**Order.** Tasks in plan order unless independent (independent ones can go to `8-autoagents`). One task at a time, to done, before the next.

**Per task.**
1. Confirm the seams the plan names. Build test-first at them with `4-testing`; one slice per cycle.
2. Run the typecheck and the single test file often; the full suite once per task, not per edit.
3. Compare every expected output in the plan against real output. Deviation: fix the code, or if the plan is wrong (contradicts the code or spec) stop and say so; don't improvise around it. Keep a short ledger of deviations.
4. Broken and not obvious in two looks: switch to `5-bug`. No guess-fixes.
5. `6-check` before marking the task done. Commit with a short plain message.

**Scope.** Only what the plan says. New need discovered mid-build: two lines on what grew and why, one recommendation, wait.

**Antislop per task, before commit.** Diff the task: no abstraction, helper, flag or interface the plan didn't name; no try/catch, fallback or null check for impossible states; no comments restating code; no TODO, stub, mock data or hardcoded value standing in for real work; no test edited or weakened to pass; no file touched the task doesn't own; style matches the surrounding code. Anything found: delete it, don't justify it.

**End.** Full suite green, `7-review` on the whole change, fix Critical and Important, then `9-push`.
