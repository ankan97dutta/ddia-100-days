# Day 059: ACID

Chapter 8 | Failure scenarios

Make A/C/I/D concrete with failure stories.

## Summary

ACID names four guarantees relational databases aim for: Atomicity (all-or-nothing), Consistency (constraints hold), Isolation (concurrent txs don't step on each other), Durability (committed survives crash). Each letter maps to a different failure class, crashes, constraint violations, races, and lost fsyncs.

> These notes and diagrams are original study aids for this repo, not copies of DDIA figures or prose. Read the matching section in your own copy of the book.

## Key points

- Atomicity: partial work rolls back on error or crash before commit.
- Consistency: CHECK/FK/UNIQUE constraints reject illegal states.
- Isolation: isolation level defines which anomalies remain possible.
- Durability: commit survives process crash after ACK (not every media failure).
- ACID scope is usually one database instance, not your whole microservice graph.

## Diagram

Four properties address different failure modes in one database.

```mermaid
mindmap
root((ACID))
Atomicity
all or nothing
Consistency
constraints
Isolation
concurrency
Durability
survive crash
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

Write one scenario each for atomicity, consistency (constraints), isolation, durability, using a bank transfer or inventory example.

### Break it

Crash after commit is acknowledged. Which property did you rely on?

### Measure

Four short failure stories tied to each letter.

## Done when

- [ ] You can explain the idea simply
- [ ] You ran the starter and captured output
- [ ] You changed one variable or failure mode and noted what happened
- [ ] You wrote one trade-off you would defend in a design review

Workbook: [workbook/exercise.md](./workbook/exercise.md)
