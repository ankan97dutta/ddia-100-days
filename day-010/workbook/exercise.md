# Day 010 workbook: Hardware, Software, Human Faults

Model correlated vs independent failures.

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

List 10 failure modes across hardware, software, and humans (bad deploy, wrong config). Mark which ones share a root cause.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Simulate a correlated failure (shared disk, shared config, shared region).

- Expected:
- Observed:
- Why they differ:

**Numbers**

MTTR estimate and whether your runbook covers the correlated case.

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
