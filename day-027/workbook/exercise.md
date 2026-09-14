# Day 027 workbook: SSTables

Build immutable sorted segments and lookups.

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

Flush a memtable to a sorted file with a sparse index. Implement get() using the index + scan.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Lookup a missing key in a large segment. How much I/O did you do?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Bytes read per get; flush size vs lookup cost.

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
