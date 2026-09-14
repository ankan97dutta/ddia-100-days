# Day 064 workbook: Phantoms

Show predicate anomalies and what stronger isolation changes.

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

Transaction counts rows matching a predicate; another inserts a matching row; first re-reads. Observe phantoms.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Raise isolation / use locking so the phantom cannot appear. Note the cost.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Counts before/after and isolation level used.

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
