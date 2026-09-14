# Day 039 workbook: Dataflow Compatibility

Reason about producer/consumer deploy order.

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

Script a timeline: deploy consumers first, then producers (and the reverse) for a schema change. Mark when the pipeline is unsafe.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Roll back the producer after consumers expect the new field.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Safe deploy order written as a checklist.

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
