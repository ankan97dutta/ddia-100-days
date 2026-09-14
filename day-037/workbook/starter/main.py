#!/usr/bin/env python3
"""Day 037: DIY protobuf-style tagged encoding (stdlib only)."""
from __future__ import annotations

import argparse
import struct

# field_number -> (wire_type, name) wire_type 0=varint 2=length-delimited
SCHEMA_V1 = {1: (0, "id"), 2: (2, "name")}
SCHEMA_V2 = {1: (0, "id"), 2: (2, "name"), 3: (2, "email")}


def encode_varint(n: int) -> bytes:
out = bytearray()
while True:
b = n & 0x7F
n >>= 7
out.append(b | (0x80 if n else 0))
if not n:
break
return bytes(out)


def tag(field: int, wire: int) -> bytes:
return encode_varint((field << 3) | wire)


def encode_v1(rec: dict) -> bytes:
out = bytearray()
out += tag(1, 0) + encode_varint(rec["id"])
name = rec["name"].encode()
out += tag(2, 2) + encode_varint(len(name)) + name
return bytes(out)


def decode(blob: bytes, schema: dict) -> dict:
i, out = 0, {}
while i < len(blob):
key, i = _varint(blob, i)
field, wire = key >> 3, key & 7
if field not in schema:
i = _skip(wire, blob, i)
continue
exp_wire, name = schema[field]
if wire == 0:
val, i = _varint(blob, i)
elif wire == 2:
ln, i = _varint(blob, i)
val = blob[i:i+ln].decode(); i += ln
else:
i = _skip(wire, blob, i); continue
out[name] = val
return out


def _varint(blob: bytes, i: int) -> tuple[int, int]:
shift = n = 0
while True:
b = blob[i]; i += 1
n |= (b & 0x7F) << shift
if not (b & 0x80):
return n, i
shift += 7


def _skip(wire: int, blob: bytes, i: int) -> int:
if wire == 0:
_, i = _varint(blob, i)
elif wire == 2:
ln, i = _varint(blob, i); i += ln
return i


def main() -> None:
p = argparse.ArgumentParser(description="DIY protobuf lab")
p.add_argument("--break", dest="break_mode", action="store_true", help="recycle field 2 for int age")
args = p.parse_args()

rec = {"id": 42, "name": "ada", "email": "a@x.com"}
v1_bytes = encode_v1(rec)
print(f"v1_bytes_len={len(v1_bytes)} v2_reader_on_v1={decode(v1_bytes, SCHEMA_V2)}")

v2_bytes = encode_v1(rec) + tag(3, 2) + encode_varint(len(rec["email"])) + rec["email"].encode()
print(f"v1_reader_on_v2={decode(v2_bytes, SCHEMA_V1)}")

if args.break_mode:
poison = tag(2, 0) + encode_varint(99)
mis = decode(v1_bytes + poison, SCHEMA_V2)
print(f"break_recycled_field2={mis}")


if __name__ == "__main__":
main()
