# Day 050 workbook: Replication Design Review

Choose a replication architecture for a multi-region workload.

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

Requirements: mostly reads, rare cross-region writes, low ops complexity. Pick single-leader, multi-leader, or leaderless, and defend it.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Add a hard requirement for multi-region writes with low conflict. Does your choice hold?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Decision table: consistency, lag, ops burden, conflict handling.

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
