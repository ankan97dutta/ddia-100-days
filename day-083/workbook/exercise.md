# Day 083 workbook: Consensus in Practice

Decide where coordination belongs, and where it is waste.

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

For a multi-region app, list decisions that need consensus (config, leader) vs those that need only replication.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Put consensus on the application write path. Quantify the latency/availability hit.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Coordination points diagram with justification.

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
