# Day 065 workbook: Serializability

Compare serial execution with concurrent serializable transactions.

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

Run the write-skew workload under SI vs SERIALIZABLE (or serial queue). Compare correctness and throughput.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Under SERIALIZABLE, force aborts; measure retry overhead.

- Expected:
- Observed:
- Why they differ:

**Numbers**

abort rate and throughput.

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
