# Day 016 workbook: Evolvability

Design so change does not require a synchronized rewrite.

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

Plan a backwards-compatible change (new field, new endpoint version). Sequence deploys for producer and consumer.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Deploy consumers first vs producers first. Which order breaks?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Compatibility matrix: old/new client × old/new server.

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
