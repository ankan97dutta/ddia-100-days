# Starter: Day 044

Inject lag and reproduce stale reads. Higher `--lag-entries` increases stale read count.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --break
python3 main.py --lag-entries
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
