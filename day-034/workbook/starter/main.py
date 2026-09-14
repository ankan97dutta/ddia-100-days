#!/usr/bin/env python3
"""Day 034: toy query planner + executor."""
from __future__ import annotations

import argparse
import json
import time


def execute(plan: dict, rows: list[dict]) -> tuple[list[dict], dict]:
stats = {"ops": 0, "rows_in": len(rows), "rows_out": 0}
cur = rows
for step in plan["steps"]:
stats["ops"] += 1
if step["op"] == "seq_scan":
cur = [r for r in cur if step.get("filter")(r)]
elif step["op"] == "index_scan":
key, val = step["eq"]
cur = [r for r in cur if r.get(key) == val]
elif step["op"] == "project":
cols = step["cols"]
cur = [{c: r[c] for c in cols} for r in cur]
stats["rows_out"] = len(cur)
return cur, stats


def main() -> None:
p = argparse.ArgumentParser(description="Query execution lab")
p.add_argument("--no-index", action="store_true")
args = p.parse_args()

rows = [{"id": i, "status": "active" if i % 3 else "paused"} for i in range(5000)]

if args.no_index:
plan = {"steps": [{"op": "seq_scan", "filter": lambda r: r["status"] == "active"}]}
else:
plan = {"steps": [{"op": "index_scan", "eq": ("status", "active")}]}

t0 = time.perf_counter()
out, stats = execute(plan, rows)
ms = (time.perf_counter() - t0) * 1000

print(f"plan={json.dumps(plan['steps'], default=str)}")
print(f"result_rows={len(out)} ops={stats['ops']} elapsed_ms={ms:.3f}")


if __name__ == "__main__":
main()
