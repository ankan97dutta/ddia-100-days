# Day 087 workbook: Joins and Grouping

Implement distributed-style joins and grouping.

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

Join clicks and users by user_id via partitioned hash join (partition both inputs the same way).

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Skewed join key (celebrity user). Show a hot reducer; propose a fix (salted join).

- Expected:
- Observed:
- Why they differ:

**Numbers**

Runtime with and without skew mitigation.

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
