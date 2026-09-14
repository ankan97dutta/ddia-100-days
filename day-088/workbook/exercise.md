# Day 088 workbook: Derived Data

Batch-build a serving-oriented derived dataset.

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

From raw events, build a daily 'user profile' table/file used by an API. Version the output path.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Bad deploy writes corrupt derived data. Roll back by switching a pointer/version.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Build time and a validation query on the output.

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
