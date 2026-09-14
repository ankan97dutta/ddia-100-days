# Day 071 workbook: Synchronous vs Asynchronous Models

Show how timing assumptions change what you can guarantee.

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

Write two designs for leader election: one assuming bounded delay, one that does not. List guarantees each can claim.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Violate the synchronous assumption (long pause). Which design lies?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Guarantees table under sync vs partial sync vs async.

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
