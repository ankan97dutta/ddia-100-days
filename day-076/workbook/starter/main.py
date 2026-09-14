#!/usr/bin/env python3
"""Day 076: system model assumption checker."""
from __future__ import annotations

MODELS = {
"crash_stop": "Process halts permanently; no recovery.",
"crash_recovery": "Process may restart and replay durable state.",
"async_network": "Messages may delay, drop, duplicate, reorder.",
"sync_timing": "Delays bounded by known Delta.",
}

SCENARIOS = [
("lease_ttl", "crash_stop", True, "TTL lease safe if holder never resumes after crash."),
("lease_ttl", "crash_recovery", False, "Paused holder can resume after TTL expires."),
("leader_election", "sync_timing", True, "Timeouts can distinguish crash from slow."),
("leader_election", "async_network", False, "Ambiguous timeouts without timing bounds."),
]

def main() -> None:
print("=== System model assumption checker ===")
for name, assumption, holds, note in SCENARIOS:
status = "HOLDS" if holds else "BREAKS"
print(f"[{status}] {name} under {assumption}: {note}")
print("\nDeclared model axes:")
for k, v in MODELS.items():
print(f" {k}: {v}")

if __name__ == "__main__":
main()
