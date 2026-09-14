#!/usr/bin/env python3
"""Day 087: partitioned hash join with skew demo."""
from __future__ import annotations
from collections import defaultdict

CLICKS = [(1, "p1"), (2, "p2"), (1, "p3"), (1, "p4"), (1, "p5")]
USERS = {1: "alice", 2: "bob"}

def partition(key: int, n: int) -> int:
return key % n

def hash_join(clicks, users, parts: int, salt: int = 1) -> list[tuple]:
buckets: list[list] = [[] for _ in range(parts)]
sizes = [0] * parts
for uid, page in clicks:
for s in range(salt):
k = (uid, s) if salt > 1 else uid
p = partition(uid if salt == 1 else hash(k) % 10_000, parts)
buckets[p].append((uid, page))
sizes[p] += 1
out = []
for part in buckets:
for uid, page in part:
out.append((users.get(uid, "?"), page))
return out, sizes

def main() -> None:
for salt in (1, 4):
joined, sizes = hash_join(CLICKS, USERS, 4, salt=salt)
print(f"\n=== salt={salt} partition sizes={sizes} max/min={max(sizes)/max(1,min(sizes)):.1f} ===")
print(f"rows={len(joined)}")

if __name__ == "__main__":
main()
