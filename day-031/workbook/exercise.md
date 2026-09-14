# Day 031 workbook: Secondary Indexes

Build and compare a secondary-index approach.

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

Primary key lookup vs secondary index on email/status. Measure write cost with and without the secondary index.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Update the indexed field on hot rows. Quantify write amplification.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Write latency delta; read latency for filtered queries.

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
