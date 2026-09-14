# Day 080 workbook: Ordering

Use logical time to order concurrent events.

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

Build a simple causal broadcast or ordered log using Lamport/vector clocks.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Deliver a message out of causal order on purpose; detect the violation.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Whether consumers can see causally inconsistent state.

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
