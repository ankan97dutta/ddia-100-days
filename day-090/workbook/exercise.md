# Day 090 workbook: Consumer Groups

Assign partitions and track offsets.

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

N partitions, M consumers in a group; rebalance when a consumer joins/leaves. Persist offsets.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Crash after process but before offset commit. Show at-least-once redelivery.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Duplicate processing count; time to rebalance.

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
