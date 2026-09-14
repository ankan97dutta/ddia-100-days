# Day 048 workbook: Conflict Resolution

Implement deterministic conflict resolution (and know its limits).

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

Implement last-write-wins (timestamp) and a simple merge (e.g. set-union for tags). Show a case LWW gets wrong.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Clock skew makes the 'losing' write look newer. What breaks?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Examples where your resolver is wrong for the product.

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
