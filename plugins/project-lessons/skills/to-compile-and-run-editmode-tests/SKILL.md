---
name: to-compile-and-run-editmode-tests
description: To compile and run EditMode tests in Big Haul through UnityMCP: call refresh_unity with compile set to request and scope all, poll until the editor is idle, then read_console for errors and warnings. 
---

# to-compile-and-run-editmode-tests

Drafted from a working procedure.

1. To compile and run EditMode tests in Big Haul through UnityMCP: call refresh_unity with compile set to request and scope all, poll until the editor is idle, then read_console for errors and warnings. Next call run_tests with mode EditMode and include_failed_tests true, and poll get_test_job with its job_id until the status is succeeded.
