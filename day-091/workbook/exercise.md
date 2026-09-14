# Day 091 workbook: CDC

Capture DB changes into a derived view.

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

Tail a logical log or poll `updated_at` to stream changes into a projection (e.g. search document).

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Update a row twice quickly. Ensure the projection converges to the latest.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Lag and eventual consistency of the projection.

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
