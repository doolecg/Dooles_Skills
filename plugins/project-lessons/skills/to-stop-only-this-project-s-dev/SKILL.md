---
name: to-stop-only-this-project-s-dev
description: To stop only this project's dev run, find the process listening on port 5199 with Get-NetTCPConnection, confirm its command line is `node scripts/dev.mjs`, and stop it along with its cmd.exe parent by
---

# to-stop-only-this-project-s-dev

Drafted from a working procedure.

1. To stop only this project's dev run, find the process listening on port 5199 with Get-NetTCPConnection, confirm its command line is `node scripts/dev.mjs`, and stop it along with its cmd.exe parent by PID. Do this in addition to finding the electron.exe processes by profile path, because the Vite server is not an electron.exe process.
