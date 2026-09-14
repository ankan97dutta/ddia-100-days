#!/usr/bin/env python3
"""Day 055: Online rebalance with optional failure."""
import argparse
import random
import time

def main():
p = argparse.ArgumentParser()
p.add_argument("--keys", type=int, default=1000)
p.add_argument("--fail-at", type=float, default=0.0, help="Fail migration at fraction 0-1")
p.add_argument("--dual-write", action="store_true")
args = p.parse_args()
rng = random.Random(1)
old = {f"k{i}": i for i in range(args.keys)}
new = {}
copied = 0
errors = 0
t0 = time.perf_counter()
for i, (k, v) in enumerate(old.items()):
frac = (i + 1) / args.keys
if args.fail_at and frac >= args.fail_at:
print(f"FAIL at {frac:.0%}: copied={copied} new={len(new)} - abort, router stays on OLD")
print(f"split-brain risk if router flipped early: {args.dual_write and frac > 0.5}")
return
new[k] = v
if args.dual_write:
old[k] = v + 1 # concurrent updates during migration
copied += 1
dt = time.perf_counter() - t0
mism = sum(1 for k in old if old[k] != new.get(k))
print(f"OK migrated {copied} keys in {dt:.3f}s dual_write={args.dual_write}")
print(f"divergent keys after dual-write period: {mism}")
print(f"errors (simulated): {errors}")

if __name__ == "__main__":
main()
