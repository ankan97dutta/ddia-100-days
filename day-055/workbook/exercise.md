# Day 055 workbook: Rebalancing

Move partitions while traffic is still flowing.

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

Migrate one partition to a new node with a dual-write or copy+catch-up approach. Keep serving reads.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Fail the migration halfway. Can you abort cleanly without split brain?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Migration duration and error rate during move.

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
