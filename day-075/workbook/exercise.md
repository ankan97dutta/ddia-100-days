# Day 075 workbook: Leases and Locks

Design a lease and attack it with pauses and partitions.

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

Implement a lock with a TTL lease. Renew periodically. Fence tokens on write.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Pause the holder past TTL; let a new holder take the lock; old holder resumes writing without a fence.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Whether fencing prevents the stale writer's writes.

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
