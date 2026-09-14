# Starter: Day 030

Benchmark read-heavy and write-heavy workloads on both styles. Watch LSM read fan-out grow without compaction.

## Run

```bash
python3 main.py --help
python3 main.py
python3 main.py --keys 2000 --updates 1000
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
