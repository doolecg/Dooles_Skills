---
name: team-work
description: How Dayle wants multi-part jobs run in Claude Code and OpenCode - split into tasks, give each to the cheapest model tier as a subagent (Agent tool with `model`, or the OpenCode worker agents), run independent ones in parallel, keep only the hard parts on the main model, verify results. Use when a job has several parts, big features, or the user says "use agents", "split this up", "team mode", "in parallel", "hand this out", or "get workers on it".
---

# Team work

The lead (you, the main model) designs, delegates, reviews and verifies. Workers build. This skill is the working method.

- Claude Code: workers are subagents started with the Agent tool; pick the tier with its `model` param.
- OpenCode: workers are the agents `worker-small` (Haiku), `worker-medium` (Sonnet) and `worker-hard` (Opus), defined in `Dooles_Skills/opencode/agent` and linked into `~/.config/opencode/agent`.

## 1. Settle the design first
Before spawning anything, decide yourself:
- The split: tasks that can run in parallel, and what must come first.
- The shared contracts: interfaces, stubs, data formats, names. Write the stubs or skeleton into the repo yourself so every worker builds against the same thing.
- File ownership: each worker gets exclusive files or folders. Two workers never own the same file. Shared files (build scripts, registries, config) are yours or go to exactly one worker.
If the design is genuinely hard or unclear, ask the user (or take the design yourself on the main model); do not let workers invent the contracts.

## 2. Size each task to a tier
Say the tier in one line when spawning ("Spawning 3 workers: 2 opus, 1 haiku"). No need to ask for haiku, sonnet, or opus on medium work.
- haiku, Haiku 5.5 (OpenCode: `worker-small`): very small jobs: commit and push, look-ups, researching folders, reading and summarising files, running builds and tests, renames, screenshots.
- sonnet, Sonnet 5.5, the default (`worker-medium`): small jobs: simple edits, docs tweaks, a small fix in one file, tests for existing code.
- opus (`worker-hard`): medium jobs by default (a feature across a few files, a normal bug fix, a UI change, asset generation), and the hard part (architecture, big migration, tricky debugging, security work) only with the user's OK. Split it out so the follow-up (tests, docs, screenshots) goes to a smaller tier.
- Judgement calls, design decisions and anything touching the user's intent stay with you.
Cheapest tier that fits. In Claude Code, use the Agent tool with `model` set (`run_in_background` for work you do not need to wait on). Forks run on the main model, so prefer a fresh small-model agent.
Independent tasks go in one message, in parallel (6 parallel workers on separate folders has worked well).

## 3. Write a self-contained brief
A worker knows only its brief. Include:
- Goal, in one or two sentences.
- Files it owns; "do not edit anything outside these; report needed changes instead".
- Exact reference files and paths to read first (existing patterns to copy, the contract stubs).
- Verified API facts it needs (versions, signatures, gotchas you already checked). Don't make it rediscover them.
- The user's rules that apply (style, no extra features, no commits unless asked, test-run setup, no AI attribution, max 3 test/verify passes per problem).
- What "done" means: the build or test command, and what a pass looks like.
- What to report: files changed (one line each), how it checked, concerns, and verbatim error text for any failure. Keep it short.
Template:
```
Task: <one-line goal>
Context: <why, what exists, the contract in <path>>
You own: <files/folders>. Do not edit outside these; report needed changes instead.
Read first: <exact paths>
Facts: <verified API/version facts>
Rules: <user rules that apply; no commit/push; max 3 test passes>
Done when: <command> passes.
Report: Status DONE|DONE_WITH_CONCERNS|BLOCKED|NEEDS_CONTEXT, files changed, how checked, verbatim failures. Max 100 words.
```

## 4. While workers run
- Do non-overlapping work yourself (the shared files, docs, the next stage's design) or review finished parts.
- Never touch a file a running worker owns.
- Don't poll in a loop; wait for reports.
- Parallel Gradle or other builds share locks. That is fine, but expect slower runs.

## 5. Review and verify
Treat every report as a claim.
- Read the diff (`git diff`, the files). Check it matches the contract and stayed in its files.
- Build and run the tests yourself. For UI or game work, run it and look at a screenshot.
- Small revision: send it back to the same worker with SendMessage, which keeps its context. A new worker is for new work.
- A wrong or half-done result: say exactly what failed, send it back once; if it still fails, take it over or re-split.
- Tell the user only what you verified, and say what you did not.

## 6. Wrap up
Integrate, run the full build and tests once more, then give the user a short result: what was done, what was verified, anything open. Commit, push or release only if the user asked in that turn.
