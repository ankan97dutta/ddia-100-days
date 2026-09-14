#!/usr/bin/env python3
"""Day 096: unbundled stack ownership model."""
from __future__ import annotations

STACK = {
"event_log": {"owns": "immutable history", "rebuild": "restore from backup tape"},
"oltp_db": {"owns": "current row state", "rebuild": "replay log from offset 0"},
"search_index": {"owns": "inverted index", "rebuild": "reindex from log stream"},
"api": {"owns": "request routing", "rebuild": "redeploy container"},
}

def replace(component: str, new_impl: str) -> list[str]:
stable = [c for c in STACK if c != component]
return stable

def main() -> None:
print("=== Unbundled data systems ===")
for name, meta in STACK.items():
print(f"{name}: owns={meta['owns']} rebuild={meta['rebuild']}")
stable = replace("search_index", "typesense")
print(f"\nReplace search_index -> stable components: {stable}")

if __name__ == "__main__":
main()
