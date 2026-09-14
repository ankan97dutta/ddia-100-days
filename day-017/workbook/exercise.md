# Day 017 workbook: Relational Modeling

Model a domain with normalized tables and real constraints.

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

Model orders + line items + customers in Postgres with PKs, FKs, and NOT NULL where it matters. Insert valid and invalid rows.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Try to insert orphan line items or negative quantities. Which constraints catch them?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Constraint list and one query that would be painful if denormalized early.

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
