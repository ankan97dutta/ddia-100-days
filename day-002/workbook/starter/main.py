#!/usr/bin/env python3
"""Day 002: OLTP vs OLAP workload classifier."""
from __future__ import annotations

import argparse
import json

SAMPLES = [
{"name": "checkout_charge", "rows": 3, "latency_ms": 40, "aggregate": False, "pattern": "point lookup"},
{"name": "update_inventory", "rows": 2, "latency_ms": 25, "aggregate": False, "pattern": "point lookup"},
{"name": "monthly_revenue_report", "rows": 5_000_000, "latency_ms": 45_000, "aggregate": True, "pattern": "scan + aggregate"},
{"name": "user_profile_fetch", "rows": 1, "latency_ms": 8, "aggregate": False, "pattern": "point lookup"},
{"name": "cohort_retention", "rows": 2_000_000, "latency_ms": 120_000, "aggregate": True, "pattern": "scan + aggregate"},
{"name": "nightly_csv_export", "rows": 10_000_000, "latency_ms": 300_000, "aggregate": False, "pattern": "full scan"},
]


def classify(op: dict) -> str:
if op["aggregate"] or op["rows"] > 100_000 or op["latency_ms"] > 5_000:
return "OLAP"
return "OLTP"


def main() -> None:
p = argparse.ArgumentParser(description="Classify sample workloads as OLTP or OLAP")
p.add_argument("--break", dest="break_mode", action="store_true", help="Simulate running OLAP on OLTP path")
args = p.parse_args()

results = []
for op in SAMPLES:
label = classify(op)
results.append({**op, "label": label})

print("=== Workload classification ===")
for r in results:
print(f" {r['name']:22} {r['label']:4} rows={r['rows']:>10} pattern={r['pattern']}")

if args.break_mode:
heavy = [r for r in results if r["label"] == "OLAP"]
total_rows = sum(r["rows"] for r in heavy)
print(f"\n--break: forcing {len(heavy)} OLAP jobs onto OLTP DB")
print(f" extra rows scanned on hot path: {total_rows:,}")
print(" expected: p99 latency spikes, lock contention, replica lag")


if __name__ == "__main__":
main()
