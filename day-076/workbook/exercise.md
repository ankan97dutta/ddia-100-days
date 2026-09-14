# Day 076 workbook: System Models

State assumptions explicitly; test designs against them.

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

For your lease/lock design, write the system model: crash/recovery, network, timing. List which bugs are in-scope.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Change one assumption (e.g. allow arbitrary pause). Which proofs collapse?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Assumption checklist + out-of-scope failures.

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
