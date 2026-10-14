---
name: in-thumbnail-poc-run-docker-compose-up
description: In thumbnail-poc, run `docker compose up -d --build` after changing app code. `--force-recreate` alone restarts the existing image, so code changes such as checks.py do not reach port 8000 until the i
---

# in-thumbnail-poc-run-docker-compose-up

Drafted from a working procedure.

1. In thumbnail-poc, run `docker compose up -d --build` after changing app code. `--force-recreate` alone restarts the existing image, so code changes such as checks.py do not reach port 8000 until the image is rebuilt.
