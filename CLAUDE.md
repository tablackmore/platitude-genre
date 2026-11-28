# stemulous-genre: agent notes

Workspace conventions live in ~/aurum/CLAUDE.md on Tom's Mac; this file carries the rules every machine (incl. the Windows laptop) must follow.

## Flaky tests are release blockers (Tom, 2026-11-22)

A flaky test (fails, then passes on re-run) is a bug. Re-running until green is not a fix.

- **Every time** you see one, open an issue right away with the labels `flaky` + `kind:bug`. Include the test name, the failure output, how often it fails, and the context (machine, load, what else was running). Put it at the **top of Ready** on board #2: high priority.
- **Fix it deterministically:** fake timers, awaited conditions instead of sleeps, injected clocks, simulated time, per-test temp dirs. Retries, longer timeouts and sleeps don't count as fixes. Quarantine (skip) only with a linked open issue.
- **No release** of this repo while any `flaky` issue is open in it. Check it in the pre-release steps.
