#!/usr/bin/env python3
"""Day 009: Fault tree availability estimate."""
from __future__ import annotations
import argparse

LEAVES = {"db": 0.999, "payments": 0.999, "auth": 0.999, "cdn": 0.995}

def series(avail: list[float]) -> float:
p = 1.0
for a in avail:
p *= a
return p

def main() -> None:
p = argparse.ArgumentParser(description="Fault tree availability")
p.add_argument("--break", dest="break_mode", action="store_true", help="Correlate failures: shared region")
args = p.parse_args()
vals = list(LEAVES.values())
indep = series(vals)
print("=== Leaf availability ===")
for name, a in LEAVES.items():
print(f" {name}: {a:.3%}")
print(f"\n system (independent series): {indep:.3%} (~{(1-indep)*525600:.0f} min/yr down)")
if args.break_mode:
corr = min(vals) # all fail together
print(f" system (correlated/shared region): {corr:.3%}")
print("\n--break: correlated failures erase independence gains")

if __name__ == "__main__":
main()
