# Day 070 workbook: Timeouts

Show that a timeout is a guess, not proof of failure.

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

Server sometimes slow, sometimes dead. Client times out and retries. Log cases where the first request still succeeded.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Too-aggressive timeout under load. Measure false failure rate.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Ambiguous outcomes count; chosen timeout vs p99 latency.

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
