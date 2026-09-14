# Day 008 workbook: Throughput and Capacity

Build a simple capacity model from rate, payload, and limits.

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

Model: requests/s × bytes × amplification = disk/network needed. Sanity-check against one machine's limits.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Double write amplification (indexing, replication). Where do you hit the wall first?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Sustained ops/s and the first saturated resource.

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
