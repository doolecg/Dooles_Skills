---
name: 8-autoagents
description: Delegate work to subagents. Use when 2+ independent tasks can run in parallel, or a plan's tasks should each get a fresh context.
---

Subagents start with no context; you build exactly what they need. One task per agent, small enough to finish in one run, with a checkable outcome.

**When.** Independent problems (different test files, subsystems, tickets) with no shared state. Not when failures are likely related, or agents would edit the same files. Under about 10 tool calls: do it yourself.

**Task card** (the whole brief):
```
TASK: one sentence
CONTEXT: why, relevant files, decisions already made (pointers, not dumps)
FILES ALLOWED / FILES FORBIDDEN
STEPS: numbered
EXPECTED OUTCOME: test passes, file exists, output equals X
IF STUCK: return BLOCKED (expected / got / tried / suspect / need); don't improvise
```
Put the standing rules in the brief: no scope creep, no weakening tests, no faking success.

**Plan execution.** Treat tasks as a graph; dispatch the frontier (tasks whose prerequisites are done). When one finishes, verify it yourself (`6-check`: read the diff, run the check), review it (`7-review`), then dispatch what it unblocked. Same approach failing twice: stop and rewrite the card, not a third try.

**Reports back.** `DONE / CHANGED (file: what) / VERIFIED (command, result) / NOTES`, short. Integration is where multi-agent work breaks: after the last agent, run the full suite and the whole-change review yourself.
