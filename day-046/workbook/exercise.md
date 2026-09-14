# Day 046 workbook: Monotonic Reads

Create, and then eliminate, reads that go backwards in time.

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

Two followers with different lag; bounce a client between them to see older state after newer state.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Pin a session to one follower (or require monotonically increasing version).

- Expected:
- Observed:
- Why they differ:

**Numbers**

Whether you can still reproduce going-backwards reads.

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
