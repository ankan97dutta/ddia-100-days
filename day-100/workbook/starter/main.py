#!/usr/bin/env python3
"""Day 100: adversarial scenario runner against design JSON."""
from __future__ import annotations
import json
import sys

DEFAULT = {
"product": "collaborative_notes",
"multi_region_failover": False,
"hot_key_plan": True,
"poison_event_quarantine": False,
"privacy_incident_runbook": True,
"thundering_herd_cache": False,
}

SCENARIOS = [
("region_loss", "multi_region_failover", "Enable automated failover + tested restore."),
("hot_key", "hot_key_plan", "Document detection, cache, or salting for skewed keys."),
("poison_event", "poison_event_quarantine", "Validate and quarantine bad events before sinks."),
("privacy_incident", "privacy_incident_runbook", "Runbook for breach/subpoena with retention limits."),
("thundering_herd", "thundering_herd_cache", "Cache stampede protection on cold keys."),
]

def run_scenarios(design: dict) -> None:
print(f"=== Capstone defense: {design.get('product', '?')} ===")
passed = 0
for name, key, fix in SCENARIOS:
ok = bool(design.get(key))
passed += int(ok)
print(f"[{'PASS' if ok else 'FAIL'}] {name}: {key}={design.get(key)}")
if not ok:
print(f" mitigation: {fix}")
print(f"\nDefense score: {passed}/{len(SCENARIOS)}")
if passed < len(SCENARIOS):
print("Revise design JSON and rerun until critical scenarios pass.")

def main() -> None:
raw = sys.argv[1] if len(sys.argv) > 1 else json.dumps(DEFAULT)
run_scenarios(json.loads(raw))

if __name__ == "__main__":
main()
