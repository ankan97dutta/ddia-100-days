#!/usr/bin/env python3
"""Day 070: Timeout ambiguity simulator."""
import argparse
import random

def run(timeout_ms: float, latencies: list[float]):
ambiguous = 0
duplicates = 0
for lat in latencies:
if lat > timeout_ms:
ambiguous += 1
if random.random() < 0.8: # server still completes
duplicates += 1
print(f"timeout={timeout_ms}ms requests={len(latencies)}")
print(f"ambiguous={ambiguous} likely_duplicate_retries={duplicates}")

def main():
p = argparse.ArgumentParser()
p.add_argument("--timeout", type=float, default=50.0)
p.add_argument("--aggressive", action="store_true")
args = p.parse_args()
rng = random.Random(3)
lats = [rng.expovariate(1 / 40) for _ in range(500)]
if args.aggressive:
args.timeout = 20.0
run(args.timeout, lats)

if __name__ == "__main__":
main()
