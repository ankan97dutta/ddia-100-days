# Day 077 workbook: Linearizability

Build operation histories; spot linearizable vs not.

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

Record client ops with invoke/ok times for a register. Draw a linearization or show why none exists.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Add a stale read that crosses a concurrent write. Fail the checker.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Pass/fail on 3 hand-written histories.

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
