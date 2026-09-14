# Day 035 workbook: Encoding Fundamentals

Compare text vs binary encodings for size, speed, and evolution.

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

Serialize the same records as JSON, a compact binary (msgpack/protobuf), and maybe CSV. Measure size and encode/decode time.

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

Change a field type incompatibly. Which formats fail loudly vs silently?

- Expected:
- Observed:
- Why they differ:

**Numbers**

Bytes/record and encode µs.

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
