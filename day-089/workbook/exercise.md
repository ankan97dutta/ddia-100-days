# Day 089 workbook: Event Streams

Build a partitioned append-only event log.

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

Append events to partition files by key hash. Consumers read with an offset.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Two producers write the same key. Preserve per-key order within a partition.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Throughput and per-partition ordering check.

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
