#!/usr/bin/env python3
"""Day 039: dataflow deploy-order simulator."""
from __future__ import annotations

import argparse


def step(producer: str, consumer: str, change: str) -> tuple[bool, str]:
if change == "add_field":
if consumer == "old" and producer == "new":
return False, "consumer cannot read new field"
return True, "ok"
if change == "remove_field":
if consumer == "new" and producer == "old":
return False, "consumer expects field producer no longer sends"
return True, "ok"
return False, "unknown change"


def timeline(order: list[str], change: str) -> None:
prod, cons = "old", "old"
for action in order:
if action == "upgrade_consumer":
cons = "new"
elif action == "upgrade_producer":
prod = "new"
safe, msg = step(prod, cons, change)
print(f"{action:20} producer={prod} consumer={cons} safe={safe} note={msg}")


def main() -> None:
p = argparse.ArgumentParser(description="Dataflow compatibility lab")
p.add_argument("--change", choices=["add_field", "remove_field"], default="add_field")
p.add_argument("--break", dest="break_mode", action="store_true", help="producer first (unsafe for add)")
args = p.parse_args()

if args.break_mode:
timeline(["upgrade_producer", "upgrade_consumer"], args.change)
else:
timeline(["upgrade_consumer", "upgrade_producer"], args.change)


if __name__ == "__main__":
main()
