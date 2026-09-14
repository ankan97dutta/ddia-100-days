#!/usr/bin/env python3
"""Day 012: Load and capacity projection."""
from __future__ import annotations
import argparse

def main() -> None:
p = argparse.ArgumentParser(description="Capacity projection")
p.add_argument("--qps", type=int, default=1000)
p.add_argument("--growth", type=float, default=3.0, help="12-mo multiplier")
p.add_argument("--headroom", type=float, default=0.4)
p.add_argument("--break", dest="break_mode", action="store_true", help="10x spike for 1 hour")
args = p.parse_args()
base = args.qps
proj = base * args.growth
cap = proj / (1 - args.headroom)
spike = base * 10 if args.break_mode else proj
print(f"avg_qps={base} 12mo={proj:.0f} provision_for={cap:.0f} ({args.headroom:.0%} headroom)")
print(f" spike_qps={spike:.0f} first_to_shed={'rate_limiter' if args.break_mode else 'n/a'}")
if args.break_mode:
print("\n--break: 10x spike exceeds headroom -> shed load or queue")

if __name__ == "__main__":
main()
