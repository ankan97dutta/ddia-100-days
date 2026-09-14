# Day 067 workbook: Two-Phase Commit

Toy coordinator + participants; then kill the coordinator.

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

Implement prepare/commit/abort across two resource managers in process. Persist votes.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Crash the coordinator after prepare. Participants are blocked, show it.

- Expected:
- Observed:
- Why they differ:

**Numbers**

States of each participant after the crash; recovery strategy.

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
