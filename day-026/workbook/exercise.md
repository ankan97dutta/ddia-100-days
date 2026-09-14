# Day 026 workbook: Log-Structured Storage

Implement a tiny append-only key-value store.

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

Append `key=value\n` to a file; on read, scan from the end for the latest key. Support overwrite and crude delete.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Crash mid-append (truncate the last line). Does startup recover cleanly?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Read latency vs file size; space amplification after many overwrites.

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
