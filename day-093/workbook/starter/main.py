#!/usr/bin/env python3
"""Day 093: stream processor checkpoint recovery."""
from __future__ import annotations

EVENTS = [("a", 1), ("b", 2), ("a", 3), ("c", 1)]

def fold(events: list[tuple[str, int]], start: int = 0) -> tuple[dict, int]:
state: dict[str, int] = {}
for i, (k, v) in enumerate(events[start:], start):
state[k] = state.get(k, 0) + v
return state, len(events)

def checkpoint(state: dict, offset: int, match: bool) -> dict:
return {"state": state, "offset": offset if match else offset - 1}

def restore(cp: dict, events: list) -> dict:
return fold(events, cp["offset"])[0] if cp["offset"] <= len(events) else {}

def main() -> None:
full, off = fold(EVENTS)
crash_at = 2
partial, _ = fold(EVENTS[:crash_at])
good = checkpoint(partial, crash_at, match=True)
bad = checkpoint(partial, crash_at, match=False)
print("=== Fault tolerance ===")
print(f"full state={full}")
print(f"restore good cp -> {restore(good, EVENTS)} match={restore(good, EVENTS)==full}")
print(f"restore bad cp -> {restore(bad, EVENTS)} match={restore(bad, EVENTS)==full}")

if __name__ == "__main__":
main()
