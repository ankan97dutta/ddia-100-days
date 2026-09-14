#!/usr/bin/env python3
"""Day 054: Hot partition under Zipf traffic."""
import argparse
import hashlib
import random
from collections import Counter

def shard(key: str, n: int) -> int:
return int(hashlib.md5(key.encode()).hexdigest(), 16) % n

def zipf_keys(n: int, vocab: int, alpha: float, rng: random.Random):
weights = [1 / (i ** alpha) for i in range(1, vocab + 1)]
return rng.choices(range(vocab), weights=weights, k=n)

def main():
p = argparse.ArgumentParser()
p.add_argument("--requests", type=int, default=50000)
p.add_argument("--shards", type=int, default=8)
p.add_argument("--salt-hot", action="store_true")
p.add_argument("--salt-n", type=int, default=4)
args = p.parse_args()
rng = random.Random(42)
keys = zipf_keys(args.requests, 1000, 1.2, rng)
hot_key = 0
qps = Counter()
for k in keys:
logical = f"item:{k}"
if args.salt_hot and k == hot_key:
logical = f"item:{k}#salt{rng.randrange(args.salt_n)}"
qps[shard(logical, args.shards)] += 1
total = sum(qps.values())
print(f"Requests={total} shards={args.shards} salt_hot={args.salt_hot}")
for i in range(args.shards):
print(f" shard {i}: {qps[i]} ({100*qps[i]/total:.1f}%)")
mx, mn = max(qps.values()), min(qps.values())
print(f"hotspot ratio max/min: {mx/mn:.1f}x")

if __name__ == "__main__":
main()
