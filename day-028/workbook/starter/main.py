#!/usr/bin/env python3
"""Day 028: LSM-style compaction simulator."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

DIR = Path("data/segments")


def write_seg(name: str, data: dict[str, str]) -> None:
DIR.mkdir(parents=True, exist_ok=True)
(DIR / name).write_text(json.dumps(dict(sorted(data.items()))), encoding="utf-8")


def list_segs() -> list[Path]:
return sorted(DIR.glob("*.json"))


def get(key: str) -> tuple[str | None, int]:
val, touched = None, 0
for p in list_segs():
touched += 1
data = json.loads(p.read_text(encoding="utf-8"))
if key in data:
val = data[key]
return val, touched


def compact() -> float:
merged: dict[str, str] = {}
for p in list_segs():
merged.update(json.loads(p.read_text(encoding="utf-8")))
p.unlink()
write_seg("compact.json", merged)
return sum(len(json.dumps(json.loads(p.read_text()))) for p in list_segs()) if list_segs() else len(json.dumps(merged))


def main() -> None:
p = argparse.ArgumentParser(description="Compaction lab")
p.add_argument("--flushes", type=int, default=6)
p.add_argument("--compact", action="store_true")
p.add_argument("--break", dest="skip", action="store_true", help="skip compaction")
args = p.parse_args()

if DIR.exists():
for f in DIR.glob("*.json"):
f.unlink()

keys = [f"k{i}" for i in range(100)]
for i in range(args.flushes):
batch = {k: f"v{i}" for k in keys[i * 10 : (i + 1) * 10]}
write_seg(f"seg{i}.json", batch)

t0 = time.perf_counter()
if args.compact and not args.skip:
compact()
compact_ms = (time.perf_counter() - t0) * 1000

_, fanout = get("k55")
segs = len(list_segs())
total_bytes = sum(p.stat().st_size for p in list_segs())

print(f"segments={segs} read_fanout={fanout} total_bytes={total_bytes}")
print(f"compact_ran={args.compact and not args.skip} compact_ms={compact_ms:.2f}")


if __name__ == "__main__":
main()
