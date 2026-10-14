---
name: to-check-that-the-operant-dev
description: To check that the Operant dev app is up, run `npm run dev` in the background, then poll for a LISTEN on port 5199 with netstat in an until-loop rather than a chained sleep. The dev app runs on its own
---

# to-check-that-the-operant-dev

Drafted from a working procedure.

1. To check that the Operant dev app is up, run `npm run dev` in the background, then poll for a LISTEN on port 5199 with netstat in an until-loop rather than a chained sleep. The dev app runs on its own test profile at build/profiles/dev, so the real Operant data is untouched.
