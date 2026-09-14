# Day 060 workbook: Read Committed

Reproduce dirty and non-repeatable read boundaries in Postgres.

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

Two sessions: try to read uncommitted data; then commit and re-read. Use READ COMMITTED.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Hold an open transaction that updates a row; show what others see mid-flight.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Exact SQL + observed rows for each step.

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
