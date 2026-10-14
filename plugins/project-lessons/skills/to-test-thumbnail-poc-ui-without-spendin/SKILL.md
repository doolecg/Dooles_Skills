---
name: to-test-thumbnail-poc-ui-without-spendin
description: To test thumbnail-poc UI without spending OpenAI money, run a second compose project on port 8001 with MOCK_MODE set to true, CLAUDE_MODE set to api, and a separate data volume. Take APP_PASSWORD from
---

# to-test-thumbnail-poc-ui-without-spendin

Drafted from a working procedure.

1. To test thumbnail-poc UI without spending OpenAI money, run a second compose project on port 8001 with MOCK_MODE set to true, CLAUDE_MODE set to api, and a separate data volume. Take APP_PASSWORD from .env without printing it, and never put credentials in browser URLs.
