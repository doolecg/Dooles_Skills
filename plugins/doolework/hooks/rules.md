Standing coding rules (doolework plugin):

Scope: only what was asked, smallest diff that works, extend existing code before adding files. No new deps, features, refactors or renames without asking. Scope grows: stop, say so in two lines, wait.
Antislop: no speculative abstractions, flags, or one-implementation interfaces. No defensive try/catch, fallbacks or null checks for impossible states. No comments restating code. No stubs, TODOs, mock data or hardcoded values passed off as done. Never edit, skip or weaken a test to pass it. Match the file's style.
Bugs: root cause before any fix. Build a repro that goes red first; no repro, no hypothesis. Two failed fixes means stop and rethink, not a third variation.
Verify: run build/tests/lint this turn and quote the result before saying done. Unverifiable: say so. Never trust a subagent's "success"; check the diff.
Ask: unclear intent means one question, not a guess. Facts you can look up yourself: look them up.
Output: terse, no preamble, recap or summary docs. Don't re-read files already in context.
