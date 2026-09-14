# Starter: Day 063

Reproduce write skew under snapshot isolation. Adds row lock to reduce skew (may still race, experiment).

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --fix-lock
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
