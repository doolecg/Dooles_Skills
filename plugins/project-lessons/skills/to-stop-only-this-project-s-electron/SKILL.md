---
name: to-stop-only-this-project-s-electron
description: To stop only this project's Electron dev run, list electron.exe processes whose command line contains the build\profiles\dev user-data path, then stop those PIDs. Stopping by image name would also kil
---

# to-stop-only-this-project-s-electron

Drafted from a working procedure.

1. To stop only this project's Electron dev run, list electron.exe processes whose command line contains the build\profiles\dev user-data path, then stop those PIDs. Stopping by image name would also kill the user's own Operant copy.

## Learned correction

- Stopping the background `npm run dev` task does not stop its Vite server, which keeps port 5199 and makes the next start fail. Find the owner with `Get-NetTCPConnection -LocalPort 5199`, confirm it is `node scripts/dev.mjs` under the dev shell, then stop that PID and its parent by ID.
