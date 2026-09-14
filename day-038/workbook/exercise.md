# Day 038 workbook: Avro

Use writer/reader schemas to evolve records safely.

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

Write Avro with schema A; read with schema B (added field with default). Then try a conflicting change.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Drop a field without a default on the reader. What error do you get?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Which evolutions Avro accepts vs rejects in your tests.

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
