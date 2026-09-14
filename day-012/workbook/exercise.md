# Day 012 workbook: Load and Capacity Modeling

Estimate capacity under growth and how much headroom you need.

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

Assume 3× traffic in 12 months. Project storage, QPS, and connection counts. Decide headroom policy (e.g. 40% unused).

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Spike to 10× for one hour (launch/event). What sheds load first?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Peak vs average ratio and the first resource that runs out.

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
