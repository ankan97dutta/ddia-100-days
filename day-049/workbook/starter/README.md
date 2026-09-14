# Starter: Day 049

Implement quorum reads/writes (W + R > N). Weak quorums + stale replica increase stale read rate.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --w 2 --r 2
python3 main.py --w 1 --r 1 --break
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
