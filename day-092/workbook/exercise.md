# Day 092 workbook: Stream Joins and Time

Window by event time; handle late data.

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

Join clicks and impressions on a time window using event timestamps. Inject late events.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Watermark passes; late event arrives. Document drop vs update policy.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Late-arrival rate and incorrect join count if ignored.

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
