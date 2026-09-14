# Day 044 workbook: Replication Lag

Inject lag and reproduce stale reads.

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

Read from follower while artificial delay is applied. Show a write that is missing on the follower for N seconds.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Route a user to a lagging follower after they wrote on the leader.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Lag seconds and stale-read rate under your workload.

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
