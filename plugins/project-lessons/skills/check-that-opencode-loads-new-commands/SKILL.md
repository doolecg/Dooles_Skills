---
name: check-that-opencode-loads-new-commands
description: Check that OpenCode loads new commands with `opencode debug config` before reporting done, and grep its output for `command`. Use the `timeout` flag, because the command can hang.
---

# check-that-opencode-loads-new-commands

Drafted from a working procedure.

1. Check that OpenCode loads new commands with `opencode debug config` before reporting done, and grep its output for `command`. Use the `timeout` flag, because the command can hang.

## Learned correction

- Grepping `opencode debug config` for `command` only matched generic config keys and never showed the new command names, so it did not confirm the commands loaded. Verify by listing the commands folder or by opening OpenCode and typing `/` to see them.
