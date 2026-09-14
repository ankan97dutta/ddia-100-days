#!/usr/bin/env python3
"""Day 099: capstone architecture checklist scorer."""
from __future__ import annotations
import json
import sys

DEFAULT = {
"product": "collaborative_notes",
"multi_region": True,
"consistency_model": "per-document linearizable",
"has_change_log": True,
"derived_views": ["search", "analytics"],
"backup_restore_tested": False,
"privacy_retention_days": 30,
"hot_key_plan": True,
"consumer_offset_mgmt": True,
}

REQUIRED = [
"multi_region", "consistency_model", "has_change_log", "derived_views",
"backup_restore_tested", "privacy_retention_days", "hot_key_plan", "consumer_offset_mgmt",
]

def score(design: dict) -> None:
print(f"=== Capstone checklist: {design.get('product', '?')} ===")
missing = [k for k in REQUIRED if k not in design]
for k in missing:
print(f"[MISSING] {k}")
pts = 0
if design.get("has_change_log"):
pts += 1
print("[OK] change log for derived rebuild")
else:
print("[FAIL] no change log")
if design.get("backup_restore_tested"):
pts += 1
print("[OK] backup/restore tested")
else:
print("[WARN] backup/restore not tested")
if design.get("hot_key_plan"):
pts += 1
print("[OK] hot key mitigation documented")
if design.get("privacy_retention_days", 0) <= 90:
pts += 1
print(f"[OK] retention {design.get('privacy_retention_days')}d")
else:
print("[WARN] long retention - justify")
views = design.get("derived_views", [])
print(f"[INFO] derived_views={views} consistency={design.get('consistency_model')}")
print(f"\nChecklist score: {pts}/4 critical (+ {len(REQUIRED)-len(missing)} fields present)")

def main() -> None:
raw = sys.argv[1] if len(sys.argv) > 1 else json.dumps(DEFAULT)
score(json.loads(raw))

if __name__ == "__main__":
main()
