#!/usr/bin/env python3
"""Day 091: CDC projection simulation."""
from __future__ import annotations

DB = {"1": {"name": "Ada", "score": 10}}

def apply_changelog(log: list[tuple[str, str, dict]], projection: dict) -> dict:
for op, key, val in log:
if op == "upsert":
projection[key] = {**projection.get(key, {}), **val}
elif op == "delete":
projection.pop(key, None)
return projection

def main() -> None:
log = [
("upsert", "1", {"score": 20}),
("upsert", "1", {"score": 99}),
("upsert", "2", {"name": "Lin", "score": 5}),
]
proj: dict = {}
for i, _ in enumerate(log, 1):
apply_changelog(log[:i], proj)
print(f"after {i} events: {proj}")
print(f"\nfinal score user-1={proj['1']['score']} (expect 99)")

if __name__ == "__main__":
main()
