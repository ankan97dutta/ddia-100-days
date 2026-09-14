#!/usr/bin/env python3
"""Day 086: mini MapReduce word count."""
from __future__ import annotations
from collections import defaultdict

DOCS = ["hello world", "hello mapreduce", "world of batch"]

def map_fn(doc: str) -> list[tuple[str, int]]:
return [(w, 1) for w in doc.split()]

def partition(key: str, n: int) -> int:
return hash(key) % n

def shuffle(pairs: list[tuple[str, int]], n: int) -> list[list[tuple[str, int]]]:
parts: list[list[tuple[str, int]]] = [[] for _ in range(n)]
for k, v in pairs:
parts[partition(k, n)].append((k, v))
return parts

def reduce_fn(pairs: list[tuple[str, int]]) -> dict[str, int]:
out: dict[str, int] = defaultdict(int)
for k, v in pairs:
out[k] += v
return dict(out)

def job(docs: list[str], parts: int = 2) -> dict[str, int]:
mapped = [p for d in docs for p in map_fn(d)]
shuffled = shuffle(mapped, parts)
merged: dict[str, int] = defaultdict(int)
for part in shuffled:
for k, v in reduce_fn(part).items():
merged[k] += v
return dict(merged)

def main() -> None:
r1 = job(DOCS)
r2 = job(DOCS[:2] + DOCS[2:]) # simulate retry of last split
print("=== MapReduce word count ===")
print(r1)
print(f"deterministic retry: {r1 == r2}")

if __name__ == "__main__":
main()
