---
name: before-relying-on-a-module-that
description: Before relying on a module that reads an external SQLite database, open the real database read-only with node:sqlite (DatabaseSync with readOnly: true) and check the table, column and JSON key names t
---

# before-relying-on-a-module-that

Drafted from a working procedure.

1. Before relying on a module that reads an external SQLite database, open the real database read-only with node:sqlite (DatabaseSync with readOnly: true) and check the table, column and JSON key names the queries use. Only then treat the reader as verified.
