#!/usr/bin/env python3
"""Day 016: Evolvability deploy order matrix."""
from __future__ import annotations
import argparse

def compatible(client_new: bool, server_new: bool, order: str) -> bool:
if order == "consumers_first":
return not (client_new and not server_new)
return not (server_new and not client_new)

def main() -> None:
p = argparse.ArgumentParser(description="Deploy order compatibility")
p.add_argument("--order", choices=["consumers_first", "producers_first"], default="consumers_first")
p.add_argument("--break", dest="break_mode", action="store_true", help="Deploy in wrong order")
args = p.parse_args()
order = "producers_first" if args.break_mode else args.order
print(f"deploy order: {order}")
cases = [(False, False), (False, True), (True, False), (True, True)]
for c, s in cases:
ok = compatible(c, s, order)
print(f" client_new={c} server_new={s} -> {'OK' if ok else 'BREAK'}")
if args.break_mode:
print("\n--break: producers_first with new server/old client breaks reads")

if __name__ == "__main__":
main()
