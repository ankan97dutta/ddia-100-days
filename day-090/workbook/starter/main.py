#!/usr/bin/env python3
"""Day 090: consumer group assignment and offset commit."""
from __future__ import annotations

def assign(partitions: list[int], consumers: list[str]) -> dict[str, list[int]]:
mapping: dict[str, list[int]] = {c: [] for c in consumers}
for i, p in enumerate(partitions):
mapping[consumers[i % len(consumers)]].append(p)
return mapping

def process_with_crash(records: list[int], commit_at: int | None) -> tuple[list[int], int]:
processed = records[:commit_at] if commit_at is not None else records
committed = commit_at or 0
return processed, committed

def main() -> None:
parts = list(range(6))
print("=== Initial assign ===", assign(parts, ["c0", "c1"]))
print("=== After join c2 ===", assign(parts, ["c0", "c1", "c2"]))
records = [1, 2, 3, 4]
seen, committed = process_with_crash(records, commit_at=2) # crash before commit
redelivered = records[committed:]
print(f"processed={seen} committed={committed} redelivered={redelivered} duplicates={len(seen)}")

if __name__ == "__main__":
main()
