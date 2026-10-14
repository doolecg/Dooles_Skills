---
name: to-run-the-learn-check-against
description: To run the learn check against a made-up transcript, create a Claude tile on claude-haiku-5-5, then point its scratch session_id at the fake session in operant.db. Set PRAGMA busy_timeout first, becau
---

# to-run-the-learn-check-against

Drafted from a working procedure.

1. To run the learn check against a made-up transcript, create a Claude tile on claude-haiku-5-5, then point its scratch session_id at the fake session in operant.db. Set PRAGMA busy_timeout first, because the live tile may write its own session id.
