# Day 004 workbook: Cloud vs Self-Hosted

Compare control, cost, failure domains, and managed-service trade-offs.

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

Write a one-page ADR for Postgres: managed vs self-hosted for a mid-size product. Include failure domains and who gets paged.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Assume a region outage or a noisy-neighbor incident. Who owns recovery in each option?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Monthly cost ballpark, RTO/RPO, and ops hours/week.

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
