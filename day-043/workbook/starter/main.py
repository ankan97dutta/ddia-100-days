#!/usr/bin/env python3
"""Day 043: follower bootstrap via snapshot + log replay."""
from __future__ import annotations

import argparse
import json


def snapshot(state: dict, offset: int) -> dict:
return {"offset": offset, "data": dict(state)}


def replay(base: dict, entries: list[dict], min_offset: int) -> tuple[dict, int]:
st = dict(base)
rejected = 0
for e in entries:
if e["offset"] <= min_offset:
rejected += 1
continue
st.update(e["delta"])
return st, rejected


def main() -> None:
p = argparse.ArgumentParser(description="Follower bootstrap lab")
p.add_argument("--break", dest="break_mode", action="store_true", help="include pre-snapshot entries")
args = p.parse_args()

leader = {"balance": 100, "version": 3}
snap = snapshot(leader, offset=3)
log = [
{"offset": 2, "delta": {"balance": 999}},
{"offset": 4, "delta": {"balance": 110, "version": 4}},
{"offset": 5, "delta": {"balance": 120, "version": 5}},
]
if not args.break_mode:
log = [e for e in log if e["offset"] > snap["offset"]]

final, rej = replay(snap["data"], log, snap["offset"])
print(f"snapshot_offset={snap['offset']} replay_entries={len(log)} rejected={rej}")
print(f"follower_state={final} matches_leader={final['balance']==120}")


if __name__ == "__main__":
main()
