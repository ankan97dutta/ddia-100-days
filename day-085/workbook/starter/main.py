#!/usr/bin/env python3
"""Day 085: streaming vs sort-then-aggregate."""
from __future__ import annotations
import random
import tracemalloc
from collections import Counter

def stream_count(keys: list[str]) -> Counter:
return Counter(keys)

def sort_count(keys: list[str]) -> Counter:
return Counter(sorted(keys))

def bench(name: str, fn, keys: list[str]) -> None:
tracemalloc.start()
result = fn(keys)
_, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"{name}: distinct={len(result)} peak_kb={peak/1024:.1f}")

def main() -> None:
random.seed(0)
small = [str(random.randint(0, 50)) for _ in range(10_000)]
huge = [str(random.randint(0, 500_000)) for _ in range(10_000)]
print("=== Low cardinality ===")
bench("stream", stream_count, small)
bench("sort", sort_count, small)
print("\n=== High cardinality ===")
bench("stream", stream_count, huge)
bench("sort", sort_count, huge)

if __name__ == "__main__":
main()
