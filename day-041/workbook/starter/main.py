#!/usr/bin/env python3
"""Day 041: leader/follower log replication."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

LOG = Path("data/repl.log")
STATE = Path("data/state.json")


def leader_append(op: dict) -> int:
LOG.parent.mkdir(parents=True, exist_ok=True)
entries = []
if LOG.exists():
entries = [json.loads(x) for x in LOG.read_text().splitlines() if x]
entries.append(op)
LOG.write_text("\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8")
return len(entries)


def follower_apply(up_to: int | None = None) -> dict:
state = {"k": {}}
if not LOG.exists():
return state
lines = [json.loads(x) for x in LOG.read_text().splitlines() if x]
if up_to is not None:
lines = lines[:up_to]
for e in lines:
if e["op"] == "put":
state["k"][e["key"]] = e["val"]
elif e["op"] == "del":
state["k"].pop(e["key"], None)
STATE.write_text(json.dumps(state), encoding="utf-8")
return state


def main() -> None:
p = argparse.ArgumentParser(description="Leader-follower replication lab")
p.add_argument("--ops", type=int, default=5)
p.add_argument("--break", dest="break_mode", action="store_true", help="follower stops mid-stream")
args = p.parse_args()

if LOG.exists():
LOG.unlink()

for i in range(args.ops):
leader_append({"op": "put", "key": f"k{i}", "val": i})

applied = args.ops - 1 if args.break_mode else args.ops
st = follower_apply(applied)
lag = args.ops - applied

print(f"leader_entries={args.ops} follower_applied={applied} lag_entries={lag}")
print(f"follower_keys={len(st['k'])} state={st['k']}")


if __name__ == "__main__":
main()
