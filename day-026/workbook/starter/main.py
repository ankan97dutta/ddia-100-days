#!/usr/bin/env python3
"""Day 026: append-only KV log (stdlib only)."""
from __future__ import annotations

import argparse
import time
from pathlib import Path

LOG = Path("data/kv.log")


def append_record(key: str, value: str | None) -> None:
LOG.parent.mkdir(parents=True, exist_ok=True)
line = f"{key}=\n" if value is None else f"{key}={value}\n"
with LOG.open("a", encoding="utf-8") as f:
f.write(line)


def load_latest(truncate_last: bool = False) -> dict[str, str | None]:
if not LOG.exists():
return {}
lines = LOG.read_text(encoding="utf-8").splitlines()
if truncate_last and lines:
lines = lines[:-1]
state: dict[str, str | None] = {}
for line in lines:
if "=" not in line:
continue
k, v = line.split("=", 1)
state[k] = v if v != "" else None
return state


def get(key: str, state: dict[str, str | None]) -> str | None:
if key not in state or state[key] is None:
return None
return state[key]


def main() -> None:
p = argparse.ArgumentParser(description="Append-only KV log lab")
p.add_argument("--keys", type=int, default=500, help="unique keys to write")
p.add_argument("--overwrites", type=int, default=3, help="overwrite passes")
p.add_argument("--break", dest="break_mode", action="store_true", help="simulate crash mid-append")
args = p.parse_args()

if LOG.exists():
LOG.unlink()

t0 = time.perf_counter()
for n in range(args.overwrites):
for i in range(args.keys):
append_record(f"k{i}", f"v{n}-{i}")
write_ms = (time.perf_counter() - t0) * 1000

if args.break_mode:
raw = LOG.read_text(encoding="utf-8")
last_nl = raw.rfind("\n")
if last_nl > 0:
LOG.write_text(raw[: last_nl + 1], encoding="utf-8")

state = load_latest(truncate_last=args.break_mode)
t1 = time.perf_counter()
hits = sum(1 for i in range(args.keys) if get(f"k{i}", state) is not None)
read_ms = (time.perf_counter() - t1) * 1000

file_bytes = LOG.stat().st_size if LOG.exists() else 0
logical = args.keys
amp = file_bytes / max(1, logical * 8)

print(f"records={LOG.read_text().count(chr(10)) if LOG.exists() else 0}")
print(f"unique_keys={len(state)} hits={hits}")
print(f"write_ms={write_ms:.2f} scan_read_ms={read_ms:.2f}")
print(f"file_bytes={file_bytes} space_amp_ratio~={amp:.1f}x")
if args.break_mode:
print("break_mode=truncated_last_line (check for partial record handling)")


if __name__ == "__main__":
main()
