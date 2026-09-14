# Day 094 workbook: Data Integration

Fan one event log out into multiple derived views.

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

From one order-events log, build (a) analytics counts and (b) a customer notification feed. Share the log, not the DB.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Rewrite one consumer's schema. Confirm the other is unaffected.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Consumer independence: deploy one without touching the other.

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
