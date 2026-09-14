#!/usr/bin/env python3
"""Day 088: derived data ETL with versioned pointer."""
from __future__ import annotations
from collections import defaultdict

EVENTS = [
{"user": "u1", "type": "login", "ts": 1},
{"user": "u2", "type": "purchase", "ts": 2},
{"user": "u1", "type": "purchase", "ts": 3},
]

def build(events: list[dict]) -> dict[str, dict]:
profiles: dict[str, dict] = defaultdict(lambda: {"logins": 0, "purchases": 0})
for e in events:
p = profiles[e["user"]]
if e["type"] == "login":
p["logins"] += 1
else:
p["purchases"] += 1
return dict(profiles)

def validate(profiles: dict) -> bool:
return all(v["logins"] >= 0 and v["purchases"] >= 0 for v in profiles.values())

def main() -> None:
versions = {}
pointer = None
for ver in ("v1", "v2"):
data = build(EVENTS)
if ver == "v2":
data["u1"]["logins"] = -1 # bad deploy
versions[ver] = data
if validate(data):
pointer = ver
print(f"promoted {ver}: {data}")
else:
print(f"rejected {ver}: validation failed, pointer stays {pointer}")
print(f"\nactive pointer={pointer} serving={versions[pointer]}")

if __name__ == "__main__":
main()
