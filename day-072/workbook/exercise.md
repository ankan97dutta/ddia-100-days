# Day 072 workbook: Monotonic and Wall Clocks

Simulate skew and backwards wall-clock jumps.

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

Stamp events with wall clock vs monotonic. Force NTP step-back on wall clock.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Order events using wall clock under skew; show incorrect order vs Lamport/monotonic.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Mis-order count when relying on wall time.

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
