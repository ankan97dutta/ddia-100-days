#!/usr/bin/env python3
"""Day 051: When does one primary run out of headroom?"""
import argparse

def project_months(current, monthly_growth, limit):
v = current
m = 0
while v < limit and m < 120:
v *= 1 + monthly_growth
m += 1
return m, v

def main():
p = argparse.ArgumentParser(description="Shard threshold calculator")
p.add_argument("--storage-gb", type=float, default=400)
p.add_argument("--storage-limit-gb", type=float, default=2000)
p.add_argument("--qps", type=float, default=8000)
p.add_argument("--qps-limit", type=float, default=25000)
p.add_argument("--monthly-growth", type=float, default=0.08)
p.add_argument("--bad-shard-share", type=float, default=0.85,
help="Fraction of traffic on hottest shard with bad key")
args = p.parse_args()
sm, sf = project_months(args.storage_gb, args.monthly_growth, args.storage_limit_gb)
qm, qf = project_months(args.qps, args.monthly_growth, args.qps_limit)
bottleneck = "storage" if sm <= qm else "QPS"
months = min(sm, qm)
skew = args.bad_shard_share / (1.0 / 4) # vs 4 balanced shards
print(f"Storage headroom: {args.storage_gb:.0f} GB -> limit {args.storage_limit_gb:.0f} GB in ~{sm} mo")
print(f"QPS headroom: {args.qps:.0f} -> limit {args.qps_limit:.0f} in ~{qm} mo")
print(f"First bottleneck: {bottleneck} at ~{months} months (projected {min(sf,qf):.0f})")
print(f"Bad shard key: hottest shard gets {args.bad_shard_share:.0%} of load")
print(f"Skew ratio vs 4-way balance: {skew:.1f}x (max/min share)")

if __name__ == "__main__":
main()
