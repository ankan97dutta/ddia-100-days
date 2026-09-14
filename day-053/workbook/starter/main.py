#!/usr/bin/env python3
"""Day 053: Range partitioning and trailing hot range."""
import argparse
from collections import defaultdict

def find_shard(key: int, bounds: list[tuple[int, int]]) -> int:
for i, (lo, hi) in enumerate(bounds):
if lo <= key < hi:
return i
return len(bounds) - 1

def main():
p = argparse.ArgumentParser()
p.add_argument("--writes", type=int, default=10000)
p.add_argument("--split-at", type=int, default=0, help="Split last range at this key (0=none)")
args = p.parse_args()
bounds = [(0, 2500), (2500, 5000), (5000, 7500), (7500, 10**9)]
if args.split_at:
bounds = [(0, 2500), (2500, 5000), (5000, 7500), (7500, args.split_at), (args.split_at, 10**9)]
writes = defaultdict(int)
for i in range(args.writes):
key = 8000 + i # time-ordered IDs in hot tail
writes[find_shard(key, bounds)] += 1
total = sum(writes.values())
print(f"Sequential writes={total} ranges={len(bounds)}")
for i in range(len(bounds)):
c = writes.get(i, 0)
print(f" range {i} [{bounds[i][0]},{bounds[i][1]}): {c} writes ({100*c/total:.1f}%)")
hot = max(writes.values()) / total
print(f"Hottest range write share: {hot:.1%}")

if __name__ == "__main__":
main()
