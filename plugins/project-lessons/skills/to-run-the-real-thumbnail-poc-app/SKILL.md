---
name: to-run-the-real-thumbnail-poc-app
description: To run the real thumbnail-poc app on port 8000, run `docker compose up -d --force-recreate` in thumbnail-poc, then confirm OPENAI_API_KEY and APP_PASSWORD are set and MOCK_MODE is false, using presenc
---

# to-run-the-real-thumbnail-poc-app

Drafted from a working procedure.

1. To run the real thumbnail-poc app on port 8000, run `docker compose up -d --force-recreate` in thumbnail-poc, then confirm OPENAI_API_KEY and APP_PASSWORD are set and MOCK_MODE is false, using presence-only checks that never print values. Check that /healthz returns ok and that a request with no login returns 401. In claude_code mode, also confirm the runner (runner/claude_runner.py) is alive.
