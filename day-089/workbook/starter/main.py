#!/usr/bin/env python3
"""Day 089: partitioned append-only event log."""
from __future__ import annotations

class Log:
def __init__(self, n: int) -> None:
self.parts: list[list[tuple[str, str]]] = [[] for _ in range(n)]

def append(self, key: str, value: str) -> tuple[int, int]:
p = hash(key) % len(self.parts)
self.parts[p].append((key, value))
return p, len(self.parts[p]) - 1

def read(self, part: int, offset: int) -> list[tuple[str, str]]:
return self.parts[part][offset:]

def ordered_per_key(log: Log) -> bool:
seen: dict[str, list[str]] = {}
for part in log.parts:
for key, val in part:
seen.setdefault(key, []).append(val)
return all(vals == sorted(vals, key=lambda x: int(x.split("-")[1])) for vals in seen.values())

def main() -> None:
log = Log(3)
for i in range(6):
p, off = log.append("user-1", f"evt-{i}")
print(f"append user-1 evt-{i} -> partition={p} offset={off}")
print(f"per-key order preserved: {ordered_per_key(log)}")

if __name__ == "__main__":
main()
