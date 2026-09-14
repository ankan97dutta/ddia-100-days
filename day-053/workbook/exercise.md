# Day 053 workbook: Range Partitioning

Partition by key range; feel hot ranges.

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

Split a sorted keyspace into ranges. Insert sequential keys (time-based IDs).

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

All new writes hit the last range. Propose a split strategy.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Write share of the hottest range.

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
