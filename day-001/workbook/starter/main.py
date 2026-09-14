#!/usr/bin/env python3
"""Day 001: Architecture trade-off inventory (study starter)."""
from __future__ import annotations

import argparse
import json

DEFAULT_STACK = {
"api": {"purpose": "request handling", "cost_ops": 2, "user_impact_if_removed": "total outage"},
"postgres": {"purpose": "system of record", "cost_ops": 4, "user_impact_if_removed": "data loss risk"},
"redis_cache": {"purpose": "hot read acceleration", "cost_ops": 3, "user_impact_if_removed": "slow pages"},
"queue": {"purpose": "async work", "cost_ops": 3, "user_impact_if_removed": "stale side effects"},
"search_index": {"purpose": "full-text search", "cost_ops": 4, "user_impact_if_removed": "search broken"},
}

IMPACT_ORDER = {"total outage": 0, "data loss risk": 1, "search broken": 2, "slow pages": 3, "stale side effects": 4}


def inventory(stack: dict) -> list[dict]:
rows = []
for name, meta in stack.items():
rows.append({"component": name, **meta, "ops_score": meta["cost_ops"]})
rows.sort(key=lambda r: (-r["ops_score"], r["component"]))
return rows


def simulate_removal(stack: dict, component: str) -> dict:
if component not in stack:
raise SystemExit(f"Unknown component: {component}")
remaining = {k: v for k, v in stack.items() if k != component}
impact = stack[component]["user_impact_if_removed"]
return {"removed": component, "first_user_pain": impact, "remaining_components": list(remaining)}


def main() -> None:
p = argparse.ArgumentParser(description="Architecture trade-off inventory")
p.add_argument("--break", dest="break_component", metavar="NAME", help="Simulate removing a component")
p.add_argument("--json", action="store_true", help="Emit JSON")
args = p.parse_args()

rows = inventory(DEFAULT_STACK)
if args.break_component:
result = simulate_removal(DEFAULT_STACK, args.break_component)
payload = {"inventory": rows, "removal_simulation": result}
else:
payload = {"inventory": rows, "hint": "Try --break redis_cache"}

if args.json:
print(json.dumps(payload, indent=2))
else:
print("=== Architecture inventory (higher ops_score = more operational cost) ===")
for r in rows:
print(f" {r['component']:14} ops={r['ops_score']} purpose={r['purpose']}")
if args.break_component:
sim = payload["removal_simulation"]
print(f"\nRemoved {sim['removed']!r} -> first user pain: {sim['first_user_pain']}")
else:
print("\nRun with --break <component> to simulate removal.")


if __name__ == "__main__":
main()
