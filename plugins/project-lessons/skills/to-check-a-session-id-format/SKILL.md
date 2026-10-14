---
name: to-check-a-session-id-format
description: To check a session id format, run `opencode run --session <id> -m opencode/big-pickle "Reply with only ok"` and read the last line. An id with 26 characters after `ses_` answers ok, and one with 32 ch
---

# to-check-a-session-id-format

Drafted from a working procedure.

1. To check a session id format, run `opencode run --session <id> -m opencode/big-pickle "Reply with only ok"` and read the last line. An id with 26 characters after `ses_` answers ok, and one with 32 characters gets the free-tier error.
