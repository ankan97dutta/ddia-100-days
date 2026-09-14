# Day 095 workbook: Batch + Stream

Same output via batch recompute and incremental stream.

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

Compute daily active users with a batch job and with a streaming aggregator. Compare results.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Introduce a bug in streaming; use batch as the source of truth to detect drift.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Drift between pipelines; time-to-detect.

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
