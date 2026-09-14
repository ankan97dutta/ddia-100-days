# Day 005 workbook: Distributed vs Single Node

Find where distribution helps and where it mostly adds failure modes.

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

Take a single-node design that fits on one beefy machine. List three reasons to distribute and three reasons not to.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Add a network partition between two pieces that used to be local calls. What new user-visible bugs appear?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Latency added by the network hop, and number of new failure cases you can name.

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
