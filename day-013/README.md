# Day 013: Maintainability and Operability

Chapter 2 | Runbook

Design for debugging, deploys, rollbacks, and boring weekday ops.

## Summary

Maintainable systems are boring on weekdays: deploys are repeatable, rollbacks are tested, logs are findable. Operability means someone other than the author can ship a hotfix from the runbook. Missing dashboards and tribal knowledge are operational debt.

> These notes and diagrams are original study aids for this repo, not copies of DDIA figures or prose. Read the matching section in your own copy of the book.

## Key points

- Runbooks cover deploy, rollback, logs, metrics, and paging paths.
- Idempotent deploy scripts beat heroics during incidents.
- Bus factor: can a teammate fix production without calling you?
- Measure time-to-rollback, not only time-to-deploy.

## Diagram

operability loop from deploy through runbook-driven rollback.

```mermaid
flowchart LR
 DEP[Deploy] --> MON[Monitor]
 MON --> INC[Incident]
 INC --> RB[Runbook]
 RB --> ROLL[Rollback]
```

## Today

1. Read the matching DDIA section in your own copy of the book.
2. Skim [WORKFLOW.md](../WORKFLOW.md) if you need the shared checklist.
3. Run the starter, then do Try this / Break it / Measure.

### Run the starter

```bash
cd workbook/starter
python3 main.py --help
python3 main.py
```

See [workbook/starter/README.md](./workbook/starter/README.md).

### Try this

Write a one-page runbook for a service: how to deploy, roll back, find logs, and page the right person.

### Break it

Assume the primary author is on vacation. Can someone else ship a hotfix from your runbook alone?

### Measure

Time-to-rollback drill (even if only on paper) and missing dashboards.

## Done when

- [ ] You can explain the idea simply
- [ ] You ran the starter and captured output
- [ ] You changed one variable or failure mode and noted what happened
- [ ] You wrote one trade-off you would defend in a design review

Workbook: [workbook/exercise.md](./workbook/exercise.md)
