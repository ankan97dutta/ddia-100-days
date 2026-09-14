#!/usr/bin/env python3
"""Day 003: System of record vs derived lineage."""
from __future__ import annotations

import argparse
import json
import time

LINEAGE = {
"postgres": {"role": "system_of_record", "rebuildable": False, "rebuild_sec": None},
"redis_cache": {"role": "derived", "rebuildable": True, "rebuild_sec": 120},
"search_index": {"role": "derived", "rebuildable": True, "rebuild_sec": 900},
"analytics_warehouse": {"role": "derived", "rebuildable": True, "rebuild_sec": 3600},
}


def rebuild(name: str, meta: dict) -> dict:
if not meta["rebuildable"]:
return {"store": name, "status": "CANNOT_REBUILD", "note": "source of truth lost"}
time.sleep(0.01)
return {"store": name, "status": "rebuilt", "seconds": meta["rebuild_sec"]}


def main() -> None:
p = argparse.ArgumentParser(description="Data lineage and rebuild simulation")
p.add_argument("--break", dest="break_store", metavar="NAME", help="Simulate corrupting a derived store")
p.add_argument("--json", action="store_true")
args = p.parse_args()

print("=== Data lineage ===")
for name, meta in LINEAGE.items():
rb = "yes" if meta["rebuildable"] else "NO"
print(f" {name:22} role={meta['role']:18} rebuildable={rb}")

if args.break_store:
if args.break_store not in LINEAGE:
raise SystemExit(f"Unknown store: {args.break_store}")
meta = LINEAGE[args.break_store]
print(f"\n--break: corrupting {args.break_store!r}")
result = rebuild(args.break_store, meta)
if args.json:
print(json.dumps(result, indent=2))
else:
print(f" outcome: {result['status']}")
if result.get("seconds"):
print(f" rebuild_time_sec~={result['seconds']} staleness until users notice")
else:
print("\nTry --break search_index or --break postgres")


if __name__ == "__main__":
main()
