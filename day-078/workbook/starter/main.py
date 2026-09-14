#!/usr/bin/env python3
"""Day 078: compare linearizable vs eventual write latency."""
from __future__ import annotations
import random
import statistics

def simulate(mode: str, n: int, rtt_ms: float, partitioned: bool) -> list[float]:
lat = []
for _ in range(n):
base = random.uniform(0.5, 2.0)
if mode == "linearizable":
if partitioned:
continue
lat.append(base + rtt_ms * 2)
else:
lat.append(base + rtt_ms * 0.1)
return lat

def main() -> None:
random.seed(42)
rtt = 5.0
for part in (False, True):
print(f"\n=== partition={part} ===")
for mode in ("linearizable", "eventual"):
samples = simulate(mode, 200, rtt, part)
if not samples:
print(f"{mode}: UNAVAILABLE")
else:
p95 = sorted(samples)[190]
print(f"{mode}: mean={statistics.mean(samples):.2f}ms p95={p95:.2f}ms n={len(samples)}")

if __name__ == "__main__":
main()
