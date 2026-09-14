# Day 051 workbook: Why Shard

Decide when a single primary is no longer enough.

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

Given growth curves for storage and QPS, calculate when one primary is out. List shard-key candidates.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Assume a bad shard key (all hot users on one shard). Quantify imbalance.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Storage/QPS headroom and skew ratio.

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
