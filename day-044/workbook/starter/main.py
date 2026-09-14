#!/usr/bin/env python3
"""Day 044: replication lag and stale reads."""
from __future__ import annotations

import argparse
import random
import time


def main() -> None:
p = argparse.ArgumentParser(description="Replication lag lab")
p.add_argument("--lag-entries", type=int, default=3)
p.add_argument("--reads", type=int, default=50)
p.add_argument("--break", dest="break_mode", action="store_true", help="read follower immediately after write")
args = p.parse_args()

leader = {}
follower = {}
stale = 0
rng = random.Random(0)

for i in range(args.reads):
k = f"k{i%10}"
leader[k] = i
if not args.break_mode:
follower[k] = i
else:
if i >= args.lag_entries:
follower[k] = i - args.lag_entries

time.sleep(0.001 * args.lag_entries)
rk = f"k{rng.randrange(10)}"
if rk in leader and (rk not in follower or follower[rk] != leader[rk]):
stale += 1

print(f"leader_keys={len(leader)} follower_keys={len(follower)} stale_reads={stale}/{args.reads}")
print(f"lag_entries={args.lag_entries} immediate_read={args.break_mode}")


if __name__ == "__main__":
main()
