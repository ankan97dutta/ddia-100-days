#!/usr/bin/env python3
"""Day 077: linearizability history checker for a single register."""
from __future__ import annotations
from itertools import permutations

def check(ops: list) -> bool:
writes = [(v, inv, ok) for _, k, v, inv, ok in ops if k == "write"]
reads = [(exp, inv, ok) for _, k, exp, inv, ok in ops if k == "read"]
for perm in permutations(writes):
val = 0
timeline = sorted(
[(inv, "w", v) for v, inv, _ in perm] + [(inv, "r", exp) for exp, inv, _ in reads],
key=lambda x: x[0],
)
ok_all = True
for _, kind, payload in timeline:
if kind == "w":
val = payload
elif payload != val:
ok_all = False
break
if ok_all:
return True
return False

def main() -> None:
good = [("A", "write", 1, 0, 2), ("B", "read", 1, 3, 5), ("A", "write", 2, 6, 8), ("B", "read", 2, 9, 11)]
bad = [("A", "write", 1, 0, 2), ("B", "read", 0, 3, 5), ("A", "write", 2, 6, 8)]
print("=== Linearizability checker ===")
for label, hist in [("good_history", good), ("stale_read", bad)]:
ok = check(hist)
print(f"{label}: {'LINEARIZABLE' if ok else 'NOT LINEARIZABLE'}")

if __name__ == "__main__":
main()
