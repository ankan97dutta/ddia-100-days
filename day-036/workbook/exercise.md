# Day 036 workbook: Schema Evolution

Evolve a schema while old readers/writers keep working.

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

Define v1 and v2 of a record (add optional field, rename carefully). Test old reader + new writer and the reverse.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Make a breaking change on purpose. Document the migration bridge you need.

- Expected:
- Observed:
- Why they differ:

**Numbers**

Pass/fail matrix for forward and backward compatibility.

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
