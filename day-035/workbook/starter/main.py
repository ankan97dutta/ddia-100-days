#!/usr/bin/env python3
"""Day 035: JSON vs DIY binary encoding benchmark."""
from __future__ import annotations

import argparse
import json
import struct
import time


def records(n: int) -> list[dict]:
return [{"id": i, "name": f"user{i}", "score": i % 100, "active": i % 2 == 0} for i in range(n)]


def encode_binary(rows: list[dict]) -> bytes:
out = bytearray()
for r in rows:
name = r["name"].encode()
out += struct.pack(">I", r["id"])
out += struct.pack(">H", len(name))
out += name
out += struct.pack(">H", r["score"])
out += b"\x01" if r["active"] else b"\x00"
return bytes(out)


def decode_binary(blob: bytes) -> list[dict]:
rows, i = [], 0
while i < len(blob):
rid, = struct.unpack_from(">I", blob, i); i += 4
(nlen,) = struct.unpack_from(">H", blob, i); i += 2
name = blob[i:i+nlen].decode(); i += nlen
score, = struct.unpack_from(">H", blob, i); i += 2
active = blob[i] == 1; i += 1
rows.append({"id": rid, "name": name, "score": score, "active": active})
return rows


def bench(label: str, enc_fn, dec_fn, rows: list[dict]) -> None:
t0 = time.perf_counter(); blob = enc_fn(rows); enc_ms = (time.perf_counter() - t0) * 1000
t1 = time.perf_counter(); back = dec_fn(blob); dec_ms = (time.perf_counter() - t1) * 1000
print(f"[{label}] bytes={len(blob)} enc_ms={enc_ms:.2f} dec_ms={dec_ms:.2f} roundtrip_ok={back[:3]==rows[:3]}")


def main() -> None:
p = argparse.ArgumentParser(description="Encoding benchmark")
p.add_argument("--n", type=int, default=5000)
p.add_argument("--break", dest="break_mode", action="store_true", help="decode binary with wrong int width")
args = p.parse_args()

rows = records(args.n)
bench("json", lambda r: json.dumps(r).encode(), lambda b: json.loads(b.decode()), rows)
bench("binary", encode_binary, decode_binary, rows)
if args.break_mode:
blob = encode_binary(rows[:1])
try:
struct.unpack_from(">H", blob, 0)
print("break=expected_type_mismatch (manual inspect wrong schema)")
except struct.error as e:
print(f"break_error={e}")


if __name__ == "__main__":
main()
