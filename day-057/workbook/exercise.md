# Day 057 workbook: Secondary Indexes on Shards

Compare local vs global secondary indexes when data is sharded.

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

For 'find user by email', design local index (scatter-gather) vs global index. Walk a write and a read for each.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Email changes on a user. What updates fan out in the global-index design?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Write path fan-out and read fan-out for both.

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
