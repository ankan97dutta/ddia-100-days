# Day 034 workbook: Query Execution

Trace parse -> plan -> execute -> return.

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

Take 3 SQL queries; capture EXPLAIN (ANALYZE). Rewrite one to change the plan (index, rewrite JOIN order).

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Disable an index and re-run. What does the plan fall back to?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Actual rows vs estimated rows; time in each node.

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
