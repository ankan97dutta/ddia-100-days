# Day 032 workbook: Multicolumn and Covering Indexes

See how column order and covering indexes change plans.

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

In Postgres, create `(a,b)` vs `(b,a)` indexes. Run queries that filter on a, on b, and on both. Read EXPLAIN.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Add INCLUDE columns (or select-only indexed cols) and check for index-only scans.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Whether the planner uses your index; heap fetches avoided.

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
