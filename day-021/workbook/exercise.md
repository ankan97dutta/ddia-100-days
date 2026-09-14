# Day 021 workbook: Analytical Schemas

Build a small star schema from operational data.

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

Export a few fact/dimension tables (orders, date, product). Run 3 analytical queries.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Add a slowly changing dimension (product rename). Do historical reports stay correct?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Query time and row counts scanned.

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
