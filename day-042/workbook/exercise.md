# Day 042 workbook: Synchronous vs Asynchronous Replication

Measure latency vs durability when followers are slow.

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

ACK after local write (async) vs ACK after follower confirm (sync). Inject follower delay.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Lose the leader after async ACK. Prove data loss is possible.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Write latency and durability outcome for both modes.

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
