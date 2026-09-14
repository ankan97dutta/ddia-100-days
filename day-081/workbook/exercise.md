# Day 081 workbook: Linearizable IDs

Design an ID service and name its consistency needs.

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

Requirements: unique IDs, roughly time-ordered, multi-region. Compare Snowflake-style vs DB sequence vs UUID.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Clock skew in Snowflake-style IDs. Can IDs go backwards?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Uniqueness proof sketch and ordering guarantees.

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
