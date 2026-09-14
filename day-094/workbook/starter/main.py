#!/usr/bin/env python3
"""Day 094: multi-view fan-out from one event log."""
from __future__ import annotations
from collections import Counter

LOG = [
{"order": 1, "user": "u1", "amount": 50},
{"order": 2, "user": "u2", "amount": 120},
{"order": 3, "user": "u1", "amount": 30},
]

def analytics(events: list[dict]) -> dict:
return {"orders": len(events), "revenue": sum(e["amount"] for e in events)}

def notifications(events: list[dict]) -> list[str]:
return [f"notify {e['user']}: order {e['order']} shipped" for e in events]

def main() -> None:
a1 = analytics(LOG)
n1 = notifications(LOG)
# consumer B schema change: add emoji - consumer A untouched
n2 = [m + " 🎉" for m in notifications(LOG)]
print("=== Multi-view integration ===")
print(f"analytics unchanged: {a1}")
print(f"notifications v1={n1[0]}")
print(f"notifications v2={n2[0]}")

if __name__ == "__main__":
main()
