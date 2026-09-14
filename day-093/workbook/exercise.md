# Day 093 workbook: Fault Tolerance in Streams

Restart a processor without corrupting derived state.

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

Processor updates local state + output; checkpoint offset+state together. Crash and restore.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Checkpoint state without offset (or the reverse). Show inconsistency.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Whether replay after crash yields the same derived state.

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
