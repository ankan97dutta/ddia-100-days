# Day 013 workbook: Maintainability and Operability

Design for debugging, deploys, rollbacks, and boring weekday ops.

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

Write a one-page runbook for a service: how to deploy, roll back, find logs, and page the right person.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Assume the primary author is on vacation. Can someone else ship a hotfix from your runbook alone?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Time-to-rollback drill (even if only on paper) and missing dashboards.

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
