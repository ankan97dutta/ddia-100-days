# Day 003 workbook: Systems of Record and Derived Data

Trace what is authoritative vs what is derived.

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

Draw a lineage from write -> system of record -> caches/search indexes/analytics. Mark which copies can be rebuilt and which cannot.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Corrupt or delete a derived store. How do you rebuild? How long until users notice?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Rebuild time, staleness window, and blast radius if the source of truth is wrong.

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
