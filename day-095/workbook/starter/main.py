#!/usr/bin/env python3
"""Day 095: batch vs stream daily active users."""
from __future__ import annotations

EVENTS = [("u1", 1), ("u2", 1), ("u1", 2), ("u3", 2), ("u2", 2)]

def batch_dau(events: list[tuple[str, int]]) -> dict[int, set[str]]:
days: dict[int, set[str]] = {}
for user, day in events:
days.setdefault(day, set()).add(user)
return days

def stream_dau(events: list[tuple[str, int]], bug: bool = False) -> dict[int, set[str]]:
days: dict[int, set[str]] = {}
for user, day in events:
if bug and user == "u2" and day == 2:
continue # simulated stream bug
days.setdefault(day, set()).add(user)
return days

def main() -> None:
b = batch_dau(EVENTS)
s_good = stream_dau(EVENTS, bug=False)
s_bad = stream_dau(EVENTS, bug=True)
print("=== Batch vs stream DAU ===")
print(f"batch day2={len(b[2])} users={sorted(b[2])}")
print(f"stream ok day2={len(s_good[2])} drift={b[2]!=s_good[2]}")
print(f"stream bug day2={len(s_bad[2])} drift={b[2]!=s_bad[2]} users={sorted(s_bad[2])}")

if __name__ == "__main__":
main()
