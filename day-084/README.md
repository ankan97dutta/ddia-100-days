# Day 084: Batch Processing

Chapter 11 | Batch pipeline

Build a log-analysis pipeline with boring tools.

## Summary

Batch jobs consume immutable input files, transform them deterministically, and write outputs you can rerun. Idempotence and loud failure on bad input beat silent partial results when pipelines grow.

> These notes and diagrams are original study aids for this repo, not copies of DDIA figures or prose. Read the matching section in your own copy of the book.

## Key points

- Immutable inputs make reruns and debugging tractable.
- Unix-style composable filters still power many production pipelines.
- Checksum outputs to verify two runs match.
- Corrupt inputs should fail the job, not skew metrics quietly.

## Diagram

Batch pipelines chain deterministic transforms over immutable inputs.

```mermaid
flowchart LR
L[Raw logs] --> P[Parse]
P --> F[Filter errors]
F --> A[Aggregate]
A --> O[Output report]
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

Given sample logs, use sort/uniq/awk or Python to compute top endpoints and error rates. Make it rerunnable.

### Break it

Corrupt one input file mid-directory. Does the job fail loud or silently wrong?

### Measure

Runtime and output checksum for two runs (idempotent).

## Done when

- [ ] You can explain the idea simply
- [ ] You ran the starter and captured output
- [ ] You changed one variable or failure mode and noted what happened
- [ ] You wrote one trade-off you would defend in a design review

Workbook: [workbook/exercise.md](./workbook/exercise.md)
