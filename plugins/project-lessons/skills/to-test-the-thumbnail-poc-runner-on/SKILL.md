---
name: to-test-the-thumbnail-poc-runner-on
description: To test the thumbnail-poc runner on a real failed job without spending OpenAI credits, copy that job's task.json into a scratch jobs/<id> folder and run `python -I runner/claude_runner.py --data-dir "
---

# to-test-the-thumbnail-poc-runner-on

Drafted from a working procedure.

1. To test the thumbnail-poc runner on a real failed job without spending OpenAI credits, copy that job's task.json into a scratch jobs/<id> folder and run `python -I runner/claude_runner.py --data-dir "<scratch>"` with the path quoted. Read result.json, then stop the runner by PID and delete the scratch folder.
