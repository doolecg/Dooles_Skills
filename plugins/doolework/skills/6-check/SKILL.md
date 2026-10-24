---
name: 6-check
description: Gate before claiming anything is done, fixed, passing or complete, and before committing or opening a PR. Evidence first.
---

No completion claim without fresh evidence from this turn.

Before any "done", "fixed", "passes", "works", or wording that implies it:
1. Name the command that proves the claim.
2. Run it in full. Read the whole output and the exit code.
3. State the claim with the evidence, or state the real status.

| Claim | Needs | Not enough |
|---|---|---|
| Tests pass | test run, 0 failures | earlier run, "should pass" |
| Build ok | build exit 0 | linter clean |
| Bug fixed | original symptom re-run, now clean | code changed |
| Regression test works | seen red, then green | passed once |
| Subagent done | VCS diff checked | agent said so |
| Requirements met | checklist against the spec, line by line | tests green |

Red flags: "should", "probably", "seems"; a cheerful word before the check; "just this once"; a partial check standing in for the full one. Spirit over letter: rephrasing the claim doesn't exempt it.
