# Day 011 workbook: Scalability

Find bottlenecks and test whether 'just add nodes' actually helps.

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

Run a simple service with 1 worker, then 2-4. Measure throughput. Note what does not scale linearly.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Make the bottleneck a shared lock or single DB connection. Confirm scaling plateaus.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Throughput vs workers curve; efficiency = total_throughput / workers.

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
