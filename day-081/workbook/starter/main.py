#!/usr/bin/env python3
"""Day 081: compare ID generation strategies."""
from __future__ import annotations
import time
import uuid

_seq = 0
_node = 42

def db_sequence() -> int:
global _seq
_seq += 1
return _seq

def snowflake(clock_ms: int, seq: int) -> int:
return (clock_ms << 22) | (_node << 12) | (seq & 0xFFF)

def main() -> None:
print("=== ID strategy comparison ===")
ids = [db_sequence() for _ in range(3)]
print(f"DB sequence: {ids} monotonic={ids == sorted(ids)}")
uuids = {uuid.uuid4().hex for _ in range(1000)}
print(f"UUID v4: unique={len(uuids)==1000}, sortable=False")
t = int(time.time() * 1000)
normal = [snowflake(t + i, i) for i in range(3)]
skewed = [snowflake(t - 5000 + i, i) for i in range(3)]
print(f"Snowflake normal: {normal}")
print(f"Snowflake after clock skew: {skewed} backwards={skewed[0] > skewed[-1]}")

if __name__ == "__main__":
main()
