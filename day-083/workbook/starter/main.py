#!/usr/bin/env python3
"""Day 083: architecture coordination scorer."""
from __future__ import annotations

COMPONENTS = {
"user_writes": {"needs_consensus": False, "reason": "Leader replication suffices"},
"shard_map": {"needs_consensus": True, "reason": "Split-brain routing is dangerous"},
"search_index": {"needs_consensus": False, "reason": "Derived, rebuildable"},
"leader_election": {"needs_consensus": True, "reason": "Exactly one writer required"},
"rate_limit_counters": {"needs_consensus": False, "reason": "Approximate OK"},
}

def score(design: dict[str, bool]) -> tuple[int, list[str]]:
pts, notes = 0, []
for comp, meta in COMPONENTS.items():
chosen = design.get(comp, False)
if chosen == meta["needs_consensus"]:
pts += 1
notes.append(f"OK {comp}: consensus={chosen}")
else:
notes.append(f"WARN {comp}: you={chosen} expected={meta['needs_consensus']} ({meta['reason']})")
return pts, notes

def main() -> None:
good = {k: v["needs_consensus"] for k, v in COMPONENTS.items()}
bad = dict(good, user_writes=True)
for label, d in [("good", good), ("over_coordination", bad)]:
pts, notes = score(d)
print(f"\n=== {label} design score {pts}/{len(COMPONENTS)} ===")
for n in notes:
print(n)

if __name__ == "__main__":
main()
