# Day 086 workbook: MapReduce

Implement map -> shuffle -> reduce locally.

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

Word count (or URL count) with map workers writing partitions, shuffle by key hash, reduce merge.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Kill a map worker; rerun only that partition. Confirm final output identical.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Task retries and whether output is deterministic.

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
