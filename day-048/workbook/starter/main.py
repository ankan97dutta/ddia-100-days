#!/usr/bin/env python3
"""Day 048: conflict resolution: LWW vs set-union merge."""
from __future__ import annotations

import argparse


def lww(a: dict, b: dict) -> dict:
return a if a["ts"] >= b["ts"] else b


def merge_tags(a: dict, b: dict) -> dict:
tags = set(a["tags"]) | set(b["tags"])
ts = max(a["ts"], b["ts"])
return {"tags": sorted(tags), "ts": ts}


def main() -> None:
p = argparse.ArgumentParser(description="Conflict resolution lab")
p.add_argument("--skew", action="store_true", help="clock skew favors wrong write")
p.add_argument("--break", dest="break_mode", action="store_true", help="use LWW on tag sets")
args = p.parse_args()

left = {"tags": ["a", "b"], "ts": 100}
right = {"tags": ["b", "c"], "ts": 90 if args.skew else 110}

if args.break_mode:
winner = lww(left, right)
print(f"strategy=lww winner_tags={winner['tags']} lost_tags={set(left['tags'])|set(right['tags']) - set(winner['tags'])}")
else:
merged = merge_tags(left, right)
print(f"strategy=union merged_tags={merged['tags']}")


if __name__ == "__main__":
main()
