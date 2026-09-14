# Day 074 workbook: Process Pauses

Simulate stop-the-world pauses and stale heartbeats.

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

Node sends heartbeats; freeze it (sleep/SIGSTOP) without killing it. Watch peers declare it dead while it is 'alive'.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Paused node wakes and keeps acting as leader. Create a split-brain moment.

- Expected:
- Observed:
- Why they differ:

**Numbers**

False-positive death detections; split-brain duration.

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
