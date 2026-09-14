#!/usr/bin/env python3
"""Day 024: Model selection from access patterns."""
from __future__ import annotations
import argparse

QUERIES = [
("feed_by_user", "document", {"relational": 2, "document": 5, "graph": 3}),
("friends_of_friends", "graph", {"relational": 2, "document": 1, "graph": 5}),
("order_history_join", "relational", {"relational": 5, "document": 3, "graph": 2}),
("search_by_tag", "document", {"relational": 3, "document": 4, "graph": 3}),
("revenue_aggregate", "relational", {"relational": 5, "document": 2, "graph": 1}),
]

def score(model: str) -> int:
return sum(m[2][model] for m in QUERIES)

def main() -> None:
p = argparse.ArgumentParser(description="Model selection scorer")
p.add_argument("--break", dest="break_query", metavar="QUERY", help="Add adversarial access pattern")
args = p.parse_args()
qs = list(QUERIES)
if args.break_query:
qs.append(("live_recommendations", "graph", {"relational": 1, "document": 2, "graph": 5}))
print("=== Query × model fit (1-5) ===")
for name, best, scores in qs:
print(f" {name:22} best={best:10} scores={scores}")
for model in ("relational", "document", "graph"):
print(f" total_{model}={score(model)}")
if args.break_query:
print("\n--break: new graph-heavy query shifts winner")

if __name__ == "__main__":
main()
