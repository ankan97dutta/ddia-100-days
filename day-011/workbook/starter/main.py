#!/usr/bin/env python3
"""Day 011: Scale-out efficiency simulator."""
from __future__ import annotations
import argparse

def throughput(workers: int, shared: bool) -> float:
per = 100.0
if shared:
return per # serialized on shared lock
return per * workers * 0.9 # 90% parallel efficiency

def main() -> None:
p = argparse.ArgumentParser(description="Scale-out experiment")
p.add_argument("--break", dest="break_mode", action="store_true", help="Enable shared lock bottleneck")
args = p.parse_args()
print("=== Throughput vs workers ===")
for w in [1, 2, 4, 8]:
tp = throughput(w, args.break_mode)
eff = tp / w
print(f" workers={w} throughput={tp:.0f}/s efficiency={eff:.0%}")
if args.break_mode:
print("\n--break: shared lock -> scaling plateaus at ~100/s")

if __name__ == "__main__":
main()
