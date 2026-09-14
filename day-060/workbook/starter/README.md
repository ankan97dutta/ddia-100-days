# Starter: Day 060

Reproduce dirty and non-repeatable read boundaries in Postgres. Leaves B uncommitted to inspect visibility.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --break
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
