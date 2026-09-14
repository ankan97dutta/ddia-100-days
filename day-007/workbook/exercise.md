# Day 007 workbook: Latency and Percentiles

Measure latency distributions instead of hiding behind averages.

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

Hit a tiny HTTP or local function under load. Record mean, p50, p95, p99. Plot or print a histogram.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Add a 1% slow path (sleep/GC/lock). Watch how averages lie and tails move.

- Expected:
- Observed:
- Why they differ:

**Numbers**

p50/p95/p99 before and after; max observed latency.

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
