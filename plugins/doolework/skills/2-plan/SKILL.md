---
name: 2-plan
description: Write the spec and implementation plan for multi-step work. Use when a task spans several files or tasks, or the user asks for a plan.
---

Settle the design first (use `1-qa` if anything is still assumed). Then write the plan. Building it is `3-build`.

## Spec (top of the plan)

Problem (from the user's view), solution (same view), numbered user stories ("as X I want Y so that Z"), implementation decisions (modules, interfaces, schema, contracts; no file paths or code, they date fast), testing decisions (which seams, prior art in the repo), out of scope. Use the repo's own vocabulary (GLOSSARY, ADRs if present).

## Plan

Global constraints: test command, style rules, what is out of scope.

Each task:
- Files: create / modify (with line ranges) / test, exact paths.
- Consumes / Produces: exact names and signatures other tasks rely on.
- Steps, each small and checkable:
  1. write the failing test (name + assertions)
  2. run it, expect failure
  3. implement (exact signature, where)
  4. run tests, expect pass
  5. commit
- Verification: the command and the output that means success.

Sizing: a task fits one fresh context. Split by responsibility, not layer; follow the codebase's existing file patterns. Self-review the plan: every Consumes has a Produces, no step says "handle appropriately" or similar hand-waving.

## Antislop check before hand-off

Strike from the spec and plan: any module, flag, option, interface or abstraction with one caller and no story behind it; "future-proofing", "extensible", "configurable" without a named need; error handling for states that can't happen; any task that is only a refactor or tidy of code the stories don't touch; any step that says "handle", "appropriately", "as needed", "robust". Every remaining item must trace to a user story. Fewer tasks is better.

Hand off: the plan goes to `3-build` (or `8-autoagents` for independent tasks).
