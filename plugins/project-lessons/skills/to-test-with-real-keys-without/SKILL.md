---
name: to-test-with-real-keys-without
description: To test with real keys without touching the port 8000 app, start a second compose project on port 8002 from an override file in the scratchpad. Use `ports: !override` and a separate data volume, then 
---

# to-test-with-real-keys-without

Drafted from a working procedure.

1. To test with real keys without touching the port 8000 app, start a second compose project on port 8002 from an override file in the scratchpad. Use `ports: !override` and a separate data volume, then check /healthz on both ports. Reference secrets from .env rather than writing their values into the override file.
