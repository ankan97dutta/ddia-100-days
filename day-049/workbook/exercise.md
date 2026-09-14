# Day 049 workbook: Leaderless Replication

Implement quorum reads/writes (W + R > N).

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

N=3 replicas; try W=2,R=2 and W=1,R=1. Show stale reads with weak quorums.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

One replica permanently stale. Do strong quorums still protect you?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Stale-read frequency vs W/R settings.

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
