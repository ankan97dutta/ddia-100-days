#!/usr/bin/env python3
"""Day 006: Mini architecture review."""
from __future__ import annotations
import argparse
BASE_REQ = {"writes_s": 5000, "reads_s": 50000, "multi_region": True, "simple_ops": True}
DESIGN = {"pattern": "Postgres leader + replicas + CDN", "assumptions": ["reads >> writes", "no multi-region writes", "eventual OK on replicas"], "risks": [("replica lag", 0.6), ("leader failover", 0.5)]}

def main() -> None:
p = argparse.ArgumentParser(description="Mini design review")
p.add_argument("--break", dest="break_mode", action="store_true", help="Enable multi-region writes requirement")
args = p.parse_args()
print("=== Requirements ===")
for k, v in BASE_REQ.items():
print(f" {k}={v}")
if args.break_mode:
print(" multi_region_writes=True # requirement changed")
print(f"\n=== Design: {DESIGN['pattern']} ===")
for a in DESIGN["assumptions"]:
broken = args.break_mode and "no multi-region writes" in a
print(f" [{'BROKEN' if broken else 'OK'}] {a}")
print("\n=== Risks ===")
for name, s in DESIGN["risks"]:
print(f" {s:.1f} {name}")

if __name__ == "__main__":
main()
