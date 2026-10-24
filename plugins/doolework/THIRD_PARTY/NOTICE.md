# Third-party sources

Skills in this plugin are condensed from two MIT-licensed repos. Nothing is copied verbatim beyond `1-qa` and the HITL script; the rest is rewritten and merged for size.

## mattpocock/skills
https://github.com/mattpocock/skills, commit `5beb35b040e3de97e54fa9e386d7e42d15c295c2`. Licence: `mattpocock-skills-LICENSE`.
- `1-qa`: copied from `grilling`.
- `5-bug`: condensed; `scripts/hitl-loop.template.sh` copied.
- `4-testing`: seams, anti-patterns, one-slice rule.
- `7-review`: two-axis review and smell baseline.
- `8-autoagents`: frontier/task-graph execution.
- `3-build`: implement, implement-spec.

## obra/superpowers
https://github.com/obra/superpowers, commit `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. Licence: `superpowers-LICENSE`.
- `4-testing`: red-green cycle, delete-code-written-first rule.
- `6-check`: verification-before-completion.
- `5-bug`: root-cause-first, two-strikes rule.
- `2-plan`, `3-build`: writing-plans and executing-plans.
- `7-review`: receiving-code-review.
- `8-autoagents`: dispatching-parallel-agents, subagent-driven-development.
- `9-push`: finishing-a-development-branch.
