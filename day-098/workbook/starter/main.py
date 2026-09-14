#!/usr/bin/env python3
"""Day 098: privacy checklist scorer."""
from __future__ import annotations
import json
import sys

DEFAULT = {
"feature": "location_history",
"fields": ["lat", "lon", "timestamp"],
"retention_days": 365,
"rbac": True,
"audit_log": False,
"purpose_documented": True,
"deletion_on_request": True,
}

def score(inv: dict) -> None:
print(f"=== Privacy review: {inv.get('feature', '?')} ===")
issues = []
if inv.get("retention_days", 0) > 90:
issues.append("WARN retention > 90d increases subpoena/breach exposure")
if not inv.get("audit_log"):
issues.append("FAIL missing audit_log for sensitive access")
if not inv.get("deletion_on_request"):
issues.append("FAIL no user deletion path")
if len(inv.get("fields", [])) > 5:
issues.append("WARN many fields - justify each")
print(f"fields={inv.get('fields')} retention={inv.get('retention_days')}d rbac={inv.get('rbac')}")
if issues:
for i in issues:
print(i)
else:
print("PASS no critical issues")
print(f"\nRisk count: {len(issues)}")

def main() -> None:
raw = sys.argv[1] if len(sys.argv) > 1 else json.dumps(DEFAULT)
score(json.loads(raw))

if __name__ == "__main__":
main()
