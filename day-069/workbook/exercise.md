# Day 069 workbook: Unreliable Networks

Inject latency, drops, duplicates, and reordering.

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

Add a thin proxy or mock transport that delays/drops/duplicates messages between two nodes.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Send a non-idempotent operation twice. Fix with idempotency keys.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Success rate and duplicate side effects before/after idempotency.

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
