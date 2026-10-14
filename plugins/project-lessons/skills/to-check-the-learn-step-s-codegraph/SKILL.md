---
name: to-check-the-learn-step-s-codegraph
description: To check the learn step's CodeGraph MCP access against the real CLI, run `claude -p` with an --mcp-config that starts `codegraph serve --mcp`, --strict-mcp-config, --allowedTools mcp__codegraph__codeg
---

# to-check-the-learn-step-s-codegraph

Drafted from a working procedure.

1. To check the learn step's CodeGraph MCP access against the real CLI, run `claude -p` with an --mcp-config that starts `codegraph serve --mcp`, --strict-mcp-config, --allowedTools mcp__codegraph__codegraph_explore, and --output-format stream-json --verbose. A working run shows that tool as allowed and the server as connected.
