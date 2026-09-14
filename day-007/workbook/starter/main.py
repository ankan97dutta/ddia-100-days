#!/usr/bin/env python3
"""Day 007: Latency percentile lab."""
from __future__ import annotations
import argparse, random, statistics

def pct(data: list[float], p: float) -> float:
s = sorted(data)
k = (len(s) - 1) * p / 100
f, c = int(k), min(int(k) + 1, len(s) - 1)
return s[f] + (s[c] - s[f]) * (k - f)

def main() -> None:
p = argparse.ArgumentParser(description="Latency percentiles")
p.add_argument("-n", type=int, default=1000)
p.add_argument("--break", dest="break_mode", action="store_true", help="Add 1%% 500ms slow path")
args = p.parse_args()
slow = 0.01 if args.break_mode else 0.0
lat = [(500 + random.random() * 20) if random.random() < slow else 5 + random.random() * 10 for _ in range(args.n)]
print(f"samples={args.n} slow_pct={slow:.0%}")
print(f" mean={statistics.mean(lat):.1f}ms p50={pct(lat,50):.1f} p95={pct(lat,95):.1f} p99={pct(lat,99):.1f} max={max(lat):.1f}")
if args.break_mode:
print("\n--break: mean barely moved; p99 jumped")

if __name__ == "__main__":
main()
