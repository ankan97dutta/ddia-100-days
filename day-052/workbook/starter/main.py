#!/usr/bin/env python3
"""Day 052: Hash partition load balance."""
import argparse
import hashlib
from collections import Counter

def shard(key: str, n: int) -> int:
h = int(hashlib.md5(key.encode()).hexdigest(), 16)
return h % n

def power_law_keys(count: int, alpha: float = 1.5):
weights = [1 / (i ** alpha) for i in range(1, count + 1)]
total = sum(weights)
return [f"user:{i}" for i, w in enumerate(weights, 1) for _ in range(max(1, int(w / total * 5000)))]

def main():
p = argparse.ArgumentParser()
p.add_argument("--shards", type=int, default=8)
p.add_argument("--skewed", action="store_true", help="Power-law key frequency")
p.add_argument("--keys", type=int, default=10000)
args = p.parse_args()
keys = power_law_keys(500) if args.skewed else [f"user:{i}" for i in range(args.keys)]
counts = Counter(shard(k, args.shards) for k in keys)
sizes = [counts[i] for i in range(args.shards)]
print(f"Keys={len(keys)} shards={args.shards} skewed={args.skewed}")
for i, c in enumerate(sizes):
print(f" shard {i}: {c} keys ({100*c/len(keys):.1f}%)")
ratio = max(sizes) / max(1, min(sizes))
print(f"max/min ratio: {ratio:.2f}")

if __name__ == "__main__":
main()
