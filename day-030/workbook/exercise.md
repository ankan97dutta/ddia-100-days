# Day 030 workbook: B-Tree vs LSM

Benchmark read-heavy and write-heavy workloads on both styles.

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

Compare Postgres (B-tree-ish) vs an LSM (RocksDB/LevelDB) or your toy LSM, for write-heavy then read-heavy loads.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Create update-heavy keys (read-modify-write). Which engine suffers more?

- Expected:
- Observed:
- Why they differ:

**Numbers**

ops/s and space amplification for each workload.

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
