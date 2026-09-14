# Day 058 workbook: Transaction Boundaries

Decide what must sit inside one transaction, and what must not.

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

For checkout: inventory decrement, payment charge, order insert. Mark transaction boundaries and cross-service gaps.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Put payment and inventory in one DB transaction vs saga. What failure looks like either way?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Invariants that must never break, and where you enforce them.

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
