#!/usr/bin/env python3
"""Day 082: simple majority consensus simulator."""
from __future__ import annotations

def round_vote(proposals: dict[int, str], alive: set[int]) -> str | None:
votes: dict[str, int] = {}
for node, val in proposals.items():
if node in alive:
votes[val] = votes.get(val, 0) + 1
if not votes:
return None
winner, count = max(votes.items(), key=lambda x: x[1])
return winner if count > len(alive) / 2 else None

def main() -> None:
nodes = {0, 1, 2}
scenarios = [
("clean majority", {0: "A", 1: "A", 2: "B"}, nodes),
("split vote", {0: "A", 1: "B", 2: "C"}, nodes),
("lost minority", {0: "A", 1: "A"}, nodes - {2}),
("lost quorum", {0: "A"}, {0}),
]
print("=== Consensus simulator ===")
for label, props, alive in scenarios:
decision = round_vote(props, alive)
print(f"{label}: alive={sorted(alive)} -> {decision or 'NO DECISION'}")

if __name__ == "__main__":
main()
