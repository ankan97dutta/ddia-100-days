#!/usr/bin/env python3
"""Day 050: replication architecture decision scorer."""
from __future__ import annotations

import argparse


def score(req: dict) -> dict[str, float]:
s = {
"single_leader": 50,
"multi_leader": 50,
"leaderless": 50,
}
if req["read_heavy"]:
s["single_leader"] += 15
s["leaderless"] += 5
if req["multi_region_writes"]:
s["multi_leader"] += 25
s["leaderless"] += 10
s["single_leader"] -= 20
if req["low_ops"]:
s["single_leader"] += 20
s["leaderless"] -= 15
if req["strong_consistency"]:
s["single_leader"] += 10
s["leaderless"] -= 10
if req["conflict_tolerance"]:
s["multi_leader"] += 10
return s


def main() -> None:
p = argparse.ArgumentParser(description="Replication design review scorer")
p.add_argument("--multi-write", action="store_true")
p.add_argument("--break", dest="break_mode", action="store_true", help="strict strong consistency + multi-write")
args = p.parse_args()

req = {
"read_heavy": True,
"multi_region_writes": args.multi_write or args.break_mode,
"low_ops": True,
"strong_consistency": args.break_mode,
"conflict_tolerance": not args.break_mode,
}
scores = score(req)
pick = max(scores, key=scores.get)
print(f"requirements={req}")
for k, v in sorted(scores.items(), key=lambda x: -x[1]):
print(f" {k}: {v:.0f}")
print(f"recommendation={pick}")


if __name__ == "__main__":
main()
