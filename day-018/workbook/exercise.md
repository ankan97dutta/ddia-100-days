# Day 018 workbook: Document Modeling

Model the same domain as documents and find aggregate boundaries.

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

Store an order as a document (JSON file or Mongo/SQLite JSON). Decide what is embedded vs referenced.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Update one line item across 10k orders. Painful? That is your boundary signal.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Read amplification for common queries; write cost for partial updates.

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
