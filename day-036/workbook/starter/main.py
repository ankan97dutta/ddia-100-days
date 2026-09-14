#!/usr/bin/env python3
"""Day 036: schema evolution compatibility matrix."""
from __future__ import annotations

import argparse
import json


V1 = {"fields": ["id", "name"]}
V2 = {"fields": ["id", "name", "nickname"], "defaults": {"nickname": "anon"}}


def write_v1(rec: dict) -> bytes:
return json.dumps({k: rec[k] for k in V1["fields"]}).encode()


def write_v2(rec: dict) -> bytes:
payload = {k: rec.get(k, V2["defaults"].get(k)) for k in V2["fields"]}
return json.dumps(payload).encode()


def read_v1(blob: bytes) -> dict:
data = json.loads(blob)
return {k: data[k] for k in V1["fields"] if k in data}


def read_v2(blob: bytes) -> dict:
data = json.loads(blob)
out = {}
for k in V2["fields"]:
out[k] = data.get(k, V2["defaults"].get(k))
return out


def cell(r: str, w: str, rec: dict) -> bool:
writer = write_v1 if w == "v1" else write_v2
reader = read_v1 if r == "v1" else read_v2
try:
back = reader(writer(rec))
return back["id"] == rec["id"] and back["name"] == rec["name"]
except Exception:
return False


def main() -> None:
p = argparse.ArgumentParser(description="Schema evolution lab")
p.add_argument("--break", dest="break_mode", action="store_true", help="rename id without bridge")
args = p.parse_args()

rec = {"id": 7, "name": "ada", "nickname": "ad"}
if args.break_mode:
bad = json.dumps({"user_id": 7, "name": "ada"}).encode()
ok = "user_id" in json.loads(bad.decode())
print(f"breaking_rename_detected={ok}")
return

for r in ("v1", "v2"):
for w in ("v1", "v2"):
print(f"reader={r} writer={w} ok={cell(r, w, rec)}")


if __name__ == "__main__":
main()
