# Day 019 workbook: Normalization vs Denormalization

Measure the read/write trade-off of duplicated data.

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

Implement both a normalized schema and a denormalized 'order summary' field/table. Benchmark a hot read and a write that invalidates the copy.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Forget to update the denormalized copy. How do you detect drift?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Read latency and write latency for both designs.

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
