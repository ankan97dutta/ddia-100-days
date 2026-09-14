# Day 002 workbook: OLTP vs OLAP

Separate transactional and analytical work and see why storage/access patterns diverge.

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

Write 8 real queries/operations from a product (checkout, search, admin report, nightly export...). Label each OLTP or OLAP and note access pattern: point lookup, range, scan, aggregate.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Force one OLAP query onto the OLTP path (or the reverse). What contention or cost shows up?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Rows touched, latency class (ms vs seconds), and whether the query can tolerate staleness.

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
