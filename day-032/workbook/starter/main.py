#!/usr/bin/env python3
"""Day 032: index planner toy simulator."""
from __future__ import annotations

import argparse


def plan(query_cols: list[str], index_cols: list[str], include: list[str], select: list[str]) -> dict:
usable = all(c in index_cols[: len(query_cols)] or c in index_cols for c in query_cols)
prefix_ok = query_cols == index_cols[: len(query_cols)] or (
len(query_cols) == 1 and query_cols[0] == index_cols[0]
)
if len(query_cols) == 2:
prefix_ok = index_cols[:2] == query_cols
elif len(query_cols) == 1:
prefix_ok = query_cols[0] == index_cols[0]

covered = set(select).issubset(set(index_cols) | set(include))
return {
"uses_index": prefix_ok,
"index_only": prefix_ok and covered,
"heap_fetches": 0 if (prefix_ok and covered) else (100 if prefix_ok else 1000),
}


def main() -> None:
p = argparse.ArgumentParser(description="Multicolumn/covering index lab")
p.add_argument("--order", choices=["ab", "ba"], default="ab")
p.add_argument("--cover", action="store_true")
p.add_argument("--break", dest="break_mode", action="store_true", help="query filter on b only")
args = p.parse_args()

idx = ["a", "b"] if args.order == "ab" else ["b", "a"]
inc = ["c", "d"] if args.cover else []
qcols = ["b"] if args.break_mode else ["a", "b"]
sel = ["a", "b", "c"] if args.cover else ["a", "b", "c", "extra"]

r = plan(qcols, idx, inc, sel)
print(f"index={idx} include={inc} query_filter={qcols} select={sel}")
print(f"uses_index={r['uses_index']} index_only={r['index_only']} heap_fetches={r['heap_fetches']}")


if __name__ == "__main__":
main()
