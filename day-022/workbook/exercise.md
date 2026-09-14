# Day 022 workbook: Graph Modeling

Model relationships and traverse them without melting down.

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

Model users↔users follows (or parts↔BOM) in tables or a graph store. Implement friends-of-friends or transitive deps with a depth limit.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Remove the depth limit on a dense graph. What happens to runtime/memory?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Nodes/edges visited and latency vs depth.

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
