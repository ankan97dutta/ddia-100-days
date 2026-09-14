# Day 063 workbook: Write Skew

Reproduce write skew under snapshot isolation.

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

Classic doctors-on-call or similar: two transactions each think one remains on duty. Demonstrate skew under SI.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Fix with explicit locking, constraints, or serializable. Re-test.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Whether the invariant holds under concurrency.

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
