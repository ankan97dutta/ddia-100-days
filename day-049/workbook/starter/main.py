#!/usr/bin/env python3
"""Day 049: leaderless quorum read/write simulator."""
from __future__ import annotations

import argparse
import random


def write_quorum(replicas: list[dict], key: str, val: int, w: int) -> None:
chosen = random.sample(replicas, w)
for r in chosen:
r[key] = val


def read_quorum(replicas: list[dict], key: str, r: int) -> int | None:
chosen = random.sample(replicas, r)
vals = [c.get(key) for c in chosen if key in c]
return max(vals) if vals else None


def main() -> None:
p = argparse.ArgumentParser(description="Quorum replication lab")
p.add_argument("--n", type=int, default=3)
p.add_argument("--w", type=int, default=2)
p.add_argument("--r", type=int, default=2)
p.add_argument("--trials", type=int, default=200)
p.add_argument("--break", dest="break_mode", action="store_true", help="one stale replica stuck at 0")
args = p.parse_args()

rng = random.Random(0)
random.seed(0)
replicas = [{ "k": 0 } for _ in range(args.n)]
if args.break_mode:
replicas[0]["k"] = 0
for i in range(1, args.n):
replicas[i]["k"] = 10

stale_reads = 0
for t in range(1, args.trials + 1):
write_quorum(replicas, "k", t, args.w)
if args.break_mode:
replicas[0]["k"] = 0
v = read_quorum(replicas, "k", args.r)
if v is not None and v < t:
stale_reads += 1

overlap = args.w + args.r > args.n
print(f"N={args.n} W={args.w} R={args.r} overlap={overlap} stale_reads={stale_reads}/{args.trials}")


if __name__ == "__main__":
main()
