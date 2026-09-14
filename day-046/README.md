# Day 046: Monotonic Reads

Chapter 6 | Replica-routing lab

Create, and then eliminate, reads that go backwards in time.

## Summary

Monotonic reads promise a user never sees newer data followed by older data in the same session. Bouncing reads across followers with different lag can violate this even when each read alone is acceptable. Pinning a session to one replica preserves a consistent timeline for that user. Monotonic reads are weaker than linearizability but cheap compared to always reading the leader.

> These notes and diagrams are original study aids for this repo, not copies of DDIA figures or prose. Read the matching section in your own copy of the book.

## Key points

- Time appears to go backward when switching to a laggier replica.
- Session replica pinning prevents cross-replica timeline jumps.
- Monotonic reads do not guarantee seeing latest global writes.
- Load balancers must respect session affinity for this guarantee.

## Diagram

switching followers can show older state after a newer read.

```mermaid
flowchart LR
F1[Follower A newer] -->|switch| F2[Follower B older]
F2 --> X[Time goes backward]
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

Two followers with different lag; bounce a client between them to see older state after newer state.

### Break it

Pin a session to one follower (or require monotonically increasing version).

### Measure

Whether you can still reproduce going-backwards reads.

## Done when

- [ ] You can explain the idea simply
- [ ] You ran the starter and captured output
- [ ] You changed one variable or failure mode and noted what happened
- [ ] You wrote one trade-off you would defend in a design review

Workbook: [workbook/exercise.md](./workbook/exercise.md)
