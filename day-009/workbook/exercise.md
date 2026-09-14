# Day 009 workbook: Reliability and Faults

Separate component reliability from system reliability and graceful degradation.

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

Draw a fault tree for 'user cannot place an order'. Include deps (DB, payments, auth, CDN).

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Kill or mock-fail a non-critical dependency. Does the core path still work?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Estimated availability if each leaf has 99.9% and failures are independent vs correlated.

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
