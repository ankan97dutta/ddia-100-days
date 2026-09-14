#!/usr/bin/env python3
"""Day 008: Capacity model."""
from __future__ import annotations
import argparse
LIMITS = {"disk_mbps": 500, "net_mbps": 1000}

def main() -> None:
p = argparse.ArgumentParser(description="Capacity model")
p.add_argument("--rps", type=int, default=5000)
p.add_argument("--bytes", type=int, default=2048)
p.add_argument("--amp", type=float, default=3.0)
p.add_argument("--break", dest="break_mode", action="store_true", help="Double amplification")
args = p.parse_args()
amp = args.amp * (2 if args.break_mode else 1)
mbps = args.rps * args.bytes * amp * 8 / 1_000_000
sat = "disk" if mbps > LIMITS["disk_mbps"] else ("network" if mbps > LIMITS["net_mbps"] else "ok")
print(f"rps={args.rps} bytes={args.bytes} amp={amp} -> {mbps:.1f} Mbps")
print(f" limits disk={LIMITS['disk_mbps']} net={LIMITS['net_mbps']} saturated={sat}")
if args.break_mode:
print("\n--break: doubled amplification moves wall earlier")

if __name__ == "__main__":
main()
