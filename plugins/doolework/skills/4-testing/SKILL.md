---
name: 4-testing
description: Test-first implementation for features and bug fixes. Use when building or fixing anything with testable behaviour, or the user says TDD / red-green.
---

Red before green: a failing test first, then only enough code to pass it. If you wrote code before the test, delete it and start from the test.

**Seams.** Tests live at public boundaries, never against internals. Before the first test, name the seams you will test and what each catches and misses; confirm them with the user. Prefer the highest existing seam; the fewer seams, the better.

**One slice per cycle.** One seam, one test, one minimal implementation. Never write all tests first (that tests imagined shape, not behaviour).

**Cycle.**
1. Write one test showing the behaviour. Run it. Watch it fail for the right reason; a wrong failure means fix the test.
2. Write the minimum to pass. Run. Green.
3. Run the whole suite. Still green, commit.
4. Refactor only when green, and only if asked or clearly needed; it is review work, not loop work.

**Anti-patterns to reject.**
- Implementation-coupled: mocks internal collaborators, tests private methods, asserts via a side channel. Tell: breaks on refactor with no behaviour change.
- Tautological: the assertion recomputes the expected value the way the code does. Expected values come from a known-good literal, spec or worked example.
- Regression test never seen red: write it, run it, revert the fix, confirm it fails, restore.

Exceptions need the user's say: throwaway prototypes, generated code, config.
