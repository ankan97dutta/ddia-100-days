# Day 025 workbook: Storage Engine Basics

Trace a write from API call to durable bytes.

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

Diagram: client -> API -> WAL/fsync -> pages/files. Annotate when the write is 'safe' after a crash.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Kill the process between ACK and fsync (or skip fsync). What is lost?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Durability guarantee you actually have, in one sentence.

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
