# Day 045 workbook: Read-Your-Writes

Implement session-aware routing so users see their own writes.

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

After a write, sticky-route that session to the leader (or wait for lag < threshold) before reading.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Disable sticky routing. Capture a read-your-writes violation.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Violation count with and without the fix.

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
