# Day 037 workbook: Protocol Buffers

Version messages and test compatibility with field numbers.

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

Write a `.proto`, generate code, add a field with a new number. Decode old bytes with new code and new bytes with old code.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Reuse a field number for a different meaning. Observe the footgun.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Compatibility results and a rule you will follow for field numbers.

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
