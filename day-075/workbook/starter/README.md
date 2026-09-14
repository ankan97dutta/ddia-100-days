# Starter: Day 075

Design a lease and attack it with pauses and partitions. Without `--fence`, stale A may corrupt; with `--fence`, storage rejects stale token.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --fence
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
