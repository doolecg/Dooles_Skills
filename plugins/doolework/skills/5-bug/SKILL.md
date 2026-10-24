---
name: 5-bug
description: Root-cause loop for bugs, failing tests and performance regressions. Use when the user says "diagnose"/"debug", or reports something broken, throwing, failing or slow.
---

Root cause before any fix. Symptom fixes are failures. Skip a phase only with a stated reason.

Redact every secret in anything you show (`<REDACTED>`); build loops against env vars. If redacted output isn't enough, say so.

## 1. Feedback loop (this is the skill)

A tight pass/fail signal that goes red on *this* bug. Without one, no amount of code reading helps. Spend disproportionate effort here.

Ways to build one, roughly in order: failing test at the nearest seam; curl/HTTP script against a dev server; CLI run with a fixture, diffed against known-good; headless browser script; replay a captured trace; throwaway harness around the one code path; property/fuzz loop for "sometimes wrong"; bisection harness (`git bisect run`); differential run old vs new; last resort a human-in-the-loop script (`scripts/hitl-loop.template.sh`).

Tighten it: faster (skip unrelated setup), sharper (assert the exact symptom, not "didn't crash"), deterministic (pin time, seed RNG, isolate FS). Flaky bugs: raise the reproduction rate (loop 100x, parallelise, stress) until it's debuggable.

Done when you can name one command you have already run (show invocation and output) that is red-capable, deterministic, fast and agent-runnable. Can't build one: stop, list what you tried, ask for an environment, a redacted artifact (HAR, log, recording) or permission to add instrumentation. **No red command, no hypothesis.**

## 2. Reproduce and minimise

Run it red. Confirm it's the user's symptom, not a nearby one. Then cut inputs, callers, config and steps one at a time, re-running after each cut, until every remaining element is load-bearing.

## 3. Hypothesise

3 to 5 ranked, falsifiable hypotheses before testing any: "if X is the cause, changing Y makes it disappear". Can't state the prediction: it's a vibe, drop it. Show the list to the user (they often re-rank instantly); don't block on them.

## 4. Instrument

One probe per prediction, one variable at a time. Debugger or REPL over logs; targeted logs over "log everything". Tag every debug log with a unique prefix like `[DEBUG-a4f2]` so cleanup is one grep. Performance: measure a baseline first, then bisect; logs are usually the wrong tool.

## 5. Fix and lock down

Regression test before the fix, at a seam that exercises the real bug pattern. If no correct seam exists, that is a finding; note it. Watch the test fail, apply the fix, watch it pass, re-run the original un-minimised loop.

Two fixes failed: stop. Return to phase 1; don't try a third variation. Three or more: question the architecture, not the line.

## 6. Cleanup

Original repro clean; regression test green (or missing seam documented); `grep` the debug prefix, all gone; throwaway harnesses deleted; the confirmed hypothesis stated in the commit message.
