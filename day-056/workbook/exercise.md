# Day 056 workbook: Request Routing

Route with metadata and handle stale routing info.

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

Client asks a coordinator/lookup for partition -> node. Cache the answer. Then move a partition.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Serve with a stale route. Detect and refresh (redirect/error).

- Expected:
- Observed:
- Why they differ:

**Numbers**

Stale-route errors and time-to-correct.

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
