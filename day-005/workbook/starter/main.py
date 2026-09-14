#!/usr/bin/env python3
"""Day 005: Single node vs distributed failure modes."""
from __future__ import annotations

import argparse

SINGLE = ["disk full", "process crash", "bad deploy"]
DISTRIBUTED = SINGLE + ["network partition", "split brain", "partial timeout", "clock skew", "cascade retry storm"]


def main() -> None:
p = argparse.ArgumentParser(description="Compare failure modes: single vs distributed")
p.add_argument("--break", dest="break_mode", action="store_true", help="Simulate network partition")
args = p.parse_args()

print("=== Failure mode inventory ===")
print(f" single_node count={len(SINGLE)}")
for f in SINGLE:
print(f" - {f}")
print(f" distributed count={len(DISTRIBUTED)}")
for f in DISTRIBUTED:
print(f" - {f}")
print(f"\n extra failure cases from distribution: {len(DISTRIBUTED) - len(SINGLE)}")
print(" typical added latency per hop: ~0.5-2ms LAN, 20-100ms cross-region")
if args.break_mode:
print("\n--break: partition between auth and orders -> stale cart, duplicate charges, hung checkout")


if __name__ == "__main__":
main()
