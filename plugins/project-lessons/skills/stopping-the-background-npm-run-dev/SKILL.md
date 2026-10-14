---
name: stopping-the-background-npm-run-dev
description: Stopping the background `npm run dev` task does not stop its Vite server, which keeps port 5199 and makes the next start fail. Find the owner with `Get-NetTCPConnection -LocalPort 5199`, confirm it is
---

# stopping-the-background-npm-run-dev

Drafted from a working procedure.

1. Stopping the background `npm run dev` task does not stop its Vite server, which keeps port 5199 and makes the next start fail. Find the owner with `Get-NetTCPConnection -LocalPort 5199`, confirm it is `node scripts/dev.mjs` under the dev shell, then stop that PID and its parent by ID.
