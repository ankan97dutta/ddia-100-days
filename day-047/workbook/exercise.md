# Day 047 workbook: Multi-Leader Replication

Simulate writes in two regions and reconcile.

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

Two leaders accept writes for the same key; replicate both ways. Log conflicts.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Concurrent updates to the same shopping cart. What merge policy do you pick?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Conflict rate and whether merges are automatic or need human rules.

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
