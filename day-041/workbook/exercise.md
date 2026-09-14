# Day 041 workbook: Leader-Follower Replication

Build a tiny leader/follower replication log.

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

Leader appends to a log file; follower tails and applies. Client writes go to leader only.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Kill the leader mid-replicate. What is on the follower? Who becomes writable?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Lag in entries and time-to-catch-up.

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
