# VASUKI ledger lab

An intentionally vulnerable public demonstration fixture. It is a standalone
SQLite query utility, separate from the Flask application in vasuki-security-lab.
All data is dummy data held in an in-memory database; it exposes no network service.

Submitting this repository to VASUKI should identify a dynamic SQL statement,
generate a parameterized query, preserve the seven normal behavior checks, and
make all three security checks pass. The quote-handling check also verifies
legitimate input containing an apostrophe. Keep this main branch vulnerable for
repeatable demos; inspect the pipeline's separate draft patch PRs.

The shared requirements allow the presentation's preloaded Docker test image.
Flask is not imported by this utility. Run the original tests with `pytest -q`;
three failures on this baseline are intentional.
