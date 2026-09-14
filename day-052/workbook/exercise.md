# Day 052 workbook: Hash Partitioning

Partition by hash and watch key distribution.

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

Hash keys into N buckets; load a realistic key set. Plot counts per partition.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Use a non-uniform keyspace (power-law user ids). How bad is balance?

- Expected:
- Observed:
- Why they differ:

**Numbers**

max/min partition size ratio.

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
