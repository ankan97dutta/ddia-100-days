# Day 096 workbook: Unbundled Data Systems

Compose log, storage, indexes, and serving on purpose.

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

Sketch (or stub) an unbundled stack: event log -> derived DB -> search index -> API. Show what each owns.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Replace the search index implementation. What stays stable (the log)?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Ownership diagram and rebuild instructions for each derived piece.

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
