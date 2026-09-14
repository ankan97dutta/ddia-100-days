# Day 068 workbook: Partial Failure

Build something where pieces fail independently.

## Run

```bash
cd starter
python3 main.py
```

Paste interesting output below.

## Notes

**What I actually did**

> 

**Try this**

Client talks to two backends. Kill one mid-request. Observe retries, timeouts, and partial success.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Make the client assume 'both succeeded' after a timeout. Create a dual-write bug.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Outcomes: success, fail, ambiguous, and how you reconcile.

| Metric | Baseline | After change | What it means |
| --- | ---: | ---: | --- |
| | | | |

**Explanation**

> 

**Design call**

- Option A:
- Option B:
- I would ship: ___ because ___
- Evidence that would change my mind:

## Artifacts

```text
results/
├── measurements.txt
├── notes.md
└── ...
```

## Quick check

- [ ] Explained it without the book open
- [ ] Reproduced the important behavior
- [ ] Broke it on purpose
- [ ] Have at least one number or clear qualitative result
- [ ] Made a choice between alternatives
