# Starter: Day 055

Move partitions while traffic is still flowing. Try `--fail-at 0.6` and `--dual-write` to see abort vs divergence.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --fail-at
python3 main.py --dual-write
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
