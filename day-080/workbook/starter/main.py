#!/usr/bin/env python3
"""Day 080: vector clock causal ordering."""
from __future__ import annotations

def dominates(a: list[int], b: list[int]) -> bool:
return all(x >= y for x, y in zip(a, b)) and any(x > y for x, y in zip(a, b))

def concurrent(a: list[int], b: list[int]) -> bool:
return not dominates(a, b) and not dominates(b, a)

def main() -> None:
v0, v1, v2 = [1, 0, 0], [1, 1, 0], [0, 0, 1]
print("=== Vector clock relations ===")
print(f"v0={v0} -> v1={v1} causal={dominates(v0, v1)}")
print(f"v0={v0} vs v2={v2} concurrent={concurrent(v0, v2)}")
buffer = [("m1", v1), ("m2", v2)]
seen = [0, 0, 0]
delivered = []
for msg, vec in buffer:
if dominates(vec, seen) or vec == seen:
seen = [max(seen[i], vec[i]) for i in range(3)]
delivered.append(msg)
else:
print(f"BLOCKED {msg} vec={vec} seen={seen}")
print("Delivered:", delivered)

if __name__ == "__main__":
main()
