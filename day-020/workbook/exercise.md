# Day 020 workbook: Joins

Compare application-side joins with database joins.

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

Same data: join in SQL vs fetch + join in Python/Go. Compare latency and correctness under concurrent updates.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Under concurrent writes, does the app-side join see a torn read the DB join would not?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Latency and number of round-trips.

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
