#!/usr/bin/env python3
"""Day 027: toy SSTable with sparse index."""
from __future__ import annotations

import argparse
import bisect
import json
import random
import struct
import time
from pathlib import Path

DATA = Path("data/sstable.bin")
IDX = Path("data/sstable.idx")


def flush(keys: dict[str, str], stride: int) -> None:
DATA.parent.mkdir(parents=True, exist_ok=True)
index: list[tuple[str, int]] = []
with DATA.open("wb") as f:
for i, (k, v) in enumerate(sorted(keys.items())):
off = f.tell()
if i % stride == 0:
index.append((k, off))
payload = json.dumps([k, v]).encode()
f.write(struct.pack(">I", len(payload)) + payload)
IDX.write_text(json.dumps(index), encoding="utf-8")


def get(key: str) -> tuple[str | None, int]:
index = json.loads(IDX.read_text(encoding="utf-8"))
keys = [k for k, _ in index]
pos = bisect.bisect_right(keys, key) - 1
start = index[max(0, pos)][1]
bytes_read = 0
with DATA.open("rb") as f:
f.seek(start)
while True:
hdr = f.read(4)
if len(hdr) < 4:
break
nbytes = struct.unpack(">I", hdr)[0]
chunk = f.read(nbytes)
bytes_read += 4 + nbytes
k, v = json.loads(chunk)
if k == key:
return v, bytes_read
if k > key:
break
return None, bytes_read


def main() -> None:
p = argparse.ArgumentParser(description="SSTable lookup lab")
p.add_argument("--n", type=int, default=2000)
p.add_argument("--stride", type=int, default=50)
p.add_argument("--miss", action="store_true", help="lookup missing key")
args = p.parse_args()

rng = random.Random(7)
mem = {f"k{i:05d}": f"v{i}" for i in range(args.n)}
flush(mem, args.stride)

target = "missing-key" if args.miss else "k01000"
t0 = time.perf_counter()
val, bread = get(target)
ms = (time.perf_counter() - t0) * 1000

print(f"segment_bytes={DATA.stat().st_size} index_entries={len(json.loads(IDX.read_text()))}")
print(f"lookup={target} hit={val is not None} bytes_read={bread} latency_ms={ms:.3f}")


if __name__ == "__main__":
main()
