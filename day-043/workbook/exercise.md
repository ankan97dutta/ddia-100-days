# Day 043 workbook: Follower Bootstrap

Simulate snapshot + log catch-up for a new follower.

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

Take a snapshot of leader state, then replay log entries after the snapshot LSN/offset.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Apply log entries from before the snapshot. Detect and reject them.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Bootstrap time and correctness check (follower == leader).

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
