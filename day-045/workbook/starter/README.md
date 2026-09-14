# Starter: Day 045

Implement session-aware routing so users see their own writes. Without stickiness, violations appear when follower lags.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --sticky
python3 main.py --break
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
