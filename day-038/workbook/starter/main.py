#!/usr/bin/env python3
"""Day 038: Avro-style writer/reader schema resolution (stdlib)."""
from __future__ import annotations

import argparse
import json


WRITER = {"fields": ["id", "name"]}
READER = {"fields": ["id", "name", "tier"], "defaults": {"tier": "free"}}


def write(rec: dict, schema: dict) -> list:
return [rec.get(f) for f in schema["fields"]]


def resolve(payload: list, writer: dict, reader: dict) -> dict:
wmap = {f: payload[i] for i, f in enumerate(writer["fields"]) if i < len(payload)}
out = {}
defaults = reader.get("defaults", {})
for f in reader["fields"]:
if f in wmap:
out[f] = wmap[f]
elif f in defaults:
out[f] = defaults[f]
else:
raise KeyError(f"missing required field {f} with no default")
return out


def main() -> None:
p = argparse.ArgumentParser(description="Avro-style schema lab")
p.add_argument("--break", dest="break_mode", action="store_true", help="reader drops field without default")
args = p.parse_args()

rec = {"id": 3, "name": "bob"}
blob = write(rec, WRITER)
ok = resolve(blob, WRITER, READER)
print(f"forward_ok={ok}")

if args.break_mode:
bad_reader = {"fields": ["id", "tier"]}
try:
resolve(blob, WRITER, bad_reader)
except KeyError as e:
print(f"break_error={e}")


if __name__ == "__main__":
main()
