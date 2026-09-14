#!/usr/bin/env python3
"""Day 010: Failure mode taxonomy."""
from __future__ import annotations
import argparse

MODES = [
("disk_failure", "hardware", "az-a"),
("bad_deploy", "human", "deploy-pipeline"),
("config_typo", "human", "config-repo"),
("memory_leak", "software", "api-v2"),
("retry_storm", "software", "api-v2"),
("region_loss", "hardware", "az-a"),
]

def main() -> None:
p = argparse.ArgumentParser(description="Failure mode taxonomy")
p.add_argument("--break", dest="break_root", metavar="ROOT", help="Simulate correlated failure by root cause")
args = p.parse_args()
print("=== Failure modes ===")
for name, kind, root in MODES:
print(f" {name:16} type={kind:8} root={root}")
if args.break_root:
hit = [m for m in MODES if m[2] == args.break_root]
print(f"\n--break: correlated root={args.break_root!r} -> {len(hit)} modes fire together")
for m in hit:
print(f" - {m[0]}")
else:
print("\nTry --break az-a or --break api-v2")

if __name__ == "__main__":
main()
