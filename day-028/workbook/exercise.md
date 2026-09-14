# Day 028 workbook: Compaction

Measure how compaction strategy affects space and reads.

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

Keep multiple overlapping segments; implement a simple compaction that merges and drops old keys.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Delay compaction until you have many segments. Watch read fan-out explode.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Space used, segments touched per read, compaction CPU time.

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
