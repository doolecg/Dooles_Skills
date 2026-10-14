---
name: to-give-opencode-the-addy-agent-skills
description: To give OpenCode the Addy agent-skills slash commands, copy each `.claude/commands/*.md` from the `addy-agent-skills` marketplace repo into `~/.config/opencode/commands/`, stripping the `agent-skills:
---

# to-give-opencode-the-addy-agent-skills

Drafted from a working procedure.

1. To give OpenCode the Addy agent-skills slash commands, copy each `.claude/commands/*.md` from the `addy-agent-skills` marketplace repo into `~/.config/opencode/commands/`, stripping the `agent-skills:` prefix with sed. The plugin's skills are already visible to OpenCode through `~/.claude/skills`, so no skill copy is needed.
