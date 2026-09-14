# Day 001 workbook: Architecture Trade-offs

Map a system you know into workloads, constraints, and the choices it made.

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

Pick an app you have shipped or used heavily. List its data stores, queues, caches, and batch jobs. For each, write one sentence: what problem it solves and what it costs.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Remove one component on paper (cache, replica, queue). What breaks first for users?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Rough order-of-magnitude: QPS, data size, p99 latency budget, and how many people operate it.

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
