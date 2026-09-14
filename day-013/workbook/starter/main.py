#!/usr/bin/env python3
"""Day 013: Runbook completeness checker."""
from __future__ import annotations
import argparse

SECTIONS = ["deploy", "rollback", "logs", "metrics", "on_call", "dependencies"]

def main() -> None:
p = argparse.ArgumentParser(description="Runbook completeness")
p.add_argument("--have", action="append", default=[], help="Sections present")
p.add_argument("--break", dest="break_mode", action="store_true", help="Simulate author on vacation")
args = p.parse_args()
have = set(args.have or ["deploy", "logs"])
missing = [s for s in SECTIONS if s not in have]
score = len(have) / len(SECTIONS)
print(f"runbook completeness: {score:.0%} ({len(have)}/{len(SECTIONS)} sections)")
for s in SECTIONS:
print(f" [{'x' if s in have else ' '}] {s}")
if missing:
print(f"\n missing: {', '.join(missing)}")
if args.break_mode and missing:
print("\n--break: author away + missing rollback -> longer MTTR")

if __name__ == "__main__":
main()
