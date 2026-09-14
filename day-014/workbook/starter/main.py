#!/usr/bin/env python3
"""Day 014: SLO error budget calculator."""
from __future__ import annotations
import argparse

def main() -> None:
p = argparse.ArgumentParser(description="SLO error budget")
p.add_argument("--target", type=float, default=99.9, help="SLO percent")
p.add_argument("--window-min", type=int, default=43200, help="30d in minutes")
p.add_argument("--bad-min", type=int, default=0, help="bad minutes this window")
p.add_argument("--break", dest="break_mode", action="store_true", help="Burn 50%% budget in one week")
args = p.parse_args()
allowed = args.window_min * (1 - args.target / 100)
bad = args.bad_min or (allowed * 0.5 if args.break_mode else allowed * 0.1)
remaining = max(0, allowed - bad)
burn = bad / allowed if allowed else 0
print(f"SLO={args.target}% window={args.window_min}min allowed_bad={allowed:.1f}min")
print(f" consumed={bad:.1f}min remaining={remaining:.1f}min burn={burn:.0%}")
if burn >= 0.5:
print(" policy: pause risky launches; focus reliability")
if args.break_mode:
print("\n--break: 50% budget burned in a week")

if __name__ == "__main__":
main()
