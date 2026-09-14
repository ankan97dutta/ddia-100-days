#!/usr/bin/env python3
"""Day 073: Clock uncertainty intervals."""
import argparse

def order(a: float, b: float, uncertainty: float) -> str:
if a + uncertainty < b - uncertainty:
return "A before B"
if b + uncertainty < a - uncertainty:
return "B before A"
return "unorderable (intervals overlap)"

def main():
p = argparse.ArgumentParser()
p.add_argument("--offset-ms", type=float, default=15)
p.add_argument("--uncertainty-ms", type=float, default=10)
args = p.parse_args()
a_local, b_local = 1000.0, 1012.0
a_true = a_local
b_true = b_local + args.offset_ms
print(f"A={a_local} B={b_local} true_offset={args.offset_ms} ±{args.uncertainty_ms}ms")
print("order by local stamps:", order(a_local, b_local, args.uncertainty_ms))
print("order with corrected B:", order(a_local, b_true, args.uncertainty_ms))

if __name__ == "__main__":
main()
