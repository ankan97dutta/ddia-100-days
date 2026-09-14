#!/usr/bin/env python3
"""Day 015: Complexity budget inventory."""
from __future__ import annotations
import argparse

STACK = {
"api": ("essential", 2),
"postgres": ("essential", 4),
"legacy_etl": ("historical", 6),
"experimental_ml": ("speculative", 8),
"redis": ("essential", 3),
}

def main() -> None:
p = argparse.ArgumentParser(description="Complexity budget")
p.add_argument("--cut", metavar="NAME", help="Remove a component")
p.add_argument("--break", dest="break_mode", action="store_true", help="Cut speculative without checking users")
args = p.parse_args()
cut = args.cut or ("experimental_ml" if args.break_mode else None)
total = sum(v[1] for v in STACK.values())
print(f"ops_toil_hours/week total={total}")
for name, (tag, hrs) in STACK.items():
mark = " REMOVE" if name == cut else ""
print(f" {name:16} {tag:12} {hrs}h/wk{mark}")
if cut and cut in STACK:
saved = STACK[cut][1]
print(f"\n saved ~{saved}h/wk toil; users affected if {STACK[cut][0]}==essential")

if __name__ == "__main__":
main()
