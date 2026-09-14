# Day 006 workbook: Architecture Review

Turn requirements into an explicit decision with assumptions written down.

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

Given: 5k writes/s, 50k reads/s, multi-region users, strong preference for simple ops. Propose one architecture and list assumptions that would invalidate it.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Change one requirement (e.g. multi-region writes). How much of the design survives?

- Expected:
- Observed:
- Why they differ:

**Numbers**

A short risk list ranked by likelihood × impact.

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
