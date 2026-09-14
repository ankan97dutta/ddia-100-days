#!/usr/bin/env python3
"""Day 079: Lamport logical clock simulation."""
from __future__ import annotations

class Lamport:
def __init__(self, name: str) -> None:
self.name = name
self.t = 0
self.log: list[tuple[int, str]] = []

def local(self, label: str) -> None:
self.t += 1
self.log.append((self.t, f"{self.name} local {label}"))

def send(self, label: str) -> int:
self.t += 1
self.log.append((self.t, f"{self.name} send {label}"))
return self.t

def receive(self, ts: int, label: str) -> None:
self.t = max(self.t, ts) + 1
self.log.append((self.t, f"{self.name} recv {label}"))

def main() -> None:
a, b, c = Lamport("A"), Lamport("B"), Lamport("C")
a.local("start")
ts1 = a.send("to B")
b.receive(ts1, "from A")
b.local("work")
ts2 = b.send("to C")
c.receive(ts2, "from B")
c.local("finish")
print("=== Lamport event log ===")
for proc in (a, b, c):
for t, msg in proc.log:
print(f"L={t:2d} {msg}")

if __name__ == "__main__":
main()
