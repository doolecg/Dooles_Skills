---
name: 7-review
description: Review a change since a fixed point on two axes, standards and spec, and handle incoming review feedback. Use when asked to review a branch, PR or diff, or when review comments arrive.
---

## Giving a review

Pin the base: `git diff <base>...HEAD`, `git log <base>..HEAD --oneline`. Confirm the ref resolves and the diff is non-empty. No base given: ask.

Two axes, kept separate so one can't mask the other:
- **Standards**: the repo's documented conventions (CONTRIBUTING, CODING_STANDARDS, CLAUDE.md), plus a smell baseline as judgement calls, never hard violations: mysterious name, duplicated code, feature envy, data clumps, primitive obsession, repeated switches, shotgun surgery, speculative generality, message chain, middle man. Repo rules override the baseline. Skip anything tooling enforces.
- **Spec**: against the issue or spec. Report missing or partial requirements, scope creep, and implemented-but-wrong. Quote the spec line. No spec: say so and skip the axis.

For a large diff run each axis in its own subagent (give it the diff command, the standards files, the smell list, and "under 400 words"). Report under `## Standards` and `## Spec`; do not merge or rerank across axes. Rate each finding Critical / Important / Minor.

## Receiving a review

Read the whole comment. Verify the claim against the code before acting. Then either implement it, or push back with technical reasoning (breaks behaviour, reviewer lacks context, violates YAGNI, wrong for this stack). No "You're absolutely right", no performative thanks; action or a technical reply. Fix Critical now, Important before moving on, note Minor. Architectural disagreements go to the user.
