# Day 066 workbook: Two-Phase Locking

Watch lock acquisition and deadlocks.

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

Two transactions lock rows in opposite order. Capture a deadlock. Inspect lock waits if available.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Impose a lock ordering convention. Confirm deadlocks disappear.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Deadlock frequency and wait time.

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
