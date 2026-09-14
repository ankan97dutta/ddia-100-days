#!/usr/bin/env python3
"""Day 046: monotonic reads replica routing."""
from __future__ import annotations

import argparse
import random


def main() -> None:
p = argparse.ArgumentParser(description="Monotonic reads lab")
p.add_argument("--pin", action="store_true")
p.add_argument("--reads", type=int, default=30)
p.add_argument("--break", dest="break_mode", action="store_true", help="random replica each read")
args = p.parse_args()

replicas = [{"v": i * 2} for i in range(3)] # different lag => different version
last_seen = {}
violations = 0
pin_map: dict[str, int] = {}
rng = random.Random(2)

for i in range(args.reads):
sess = "u1"
if args.pin and not args.break_mode:
if sess not in pin_map:
pin_map[sess] = 1
rid = pin_map[sess]
else:
rid = rng.randrange(len(replicas))
v = replicas[rid]["v"]
prev = last_seen.get(sess)
if prev is not None and v < prev:
violations += 1
last_seen[sess] = max(prev or 0, v)

print(f"pin={args.pin and not args.break_mode} reads={args.reads} monotonic_violations={violations}")


if __name__ == "__main__":
main()
