---
name: to-expose-a-claude-code-plugin-s
description: To expose a Claude Code plugin's slash commands in OpenCode, copy each `.claude/commands/*.md` file into `~/.config/opencode/commands/`. Strip the `agent-skills:` prefix with sed, because OpenCode doe
---

# to-expose-a-claude-code-plugin-s

Drafted from a working procedure.

1. To expose a Claude Code plugin's slash commands in OpenCode, copy each `.claude/commands/*.md` file into `~/.config/opencode/commands/`. Strip the `agent-skills:` prefix with sed, because OpenCode does not use the plugin namespace.
