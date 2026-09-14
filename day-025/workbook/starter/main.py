#!/usr/bin/env python3
"""Day 025: Write path / WAL durability simulator."""
from __future__ import annotations
import argparse
from pathlib import Path

WAL = Path("data/wal.log")

def write_record(key: str, val: str, fsync: bool, ack_early: bool) -> str:
WAL.parent.mkdir(parents=True, exist_ok=True)
with WAL.open("a", encoding="utf-8") as f:
f.write(f"{key}={val}\n")
if ack_early:
return "ack_after_buffer"
if fsync:
f.flush()
# simulate durable fsync
else:
return "ack_no_fsync"
return "ack_after_fsync"

def crash_before_fsync() -> None:
if WAL.exists():
raw = WAL.read_text(encoding="utf-8")
WAL.write_text(raw, encoding="utf-8") # partial ok

def main() -> None:
p = argparse.ArgumentParser(description="Write path durability")
p.add_argument("--break", dest="break_mode", action="store_true", help="ACK before fsync then crash")
args = p.parse_args()
if WAL.exists():
WAL.unlink()
fsync = not args.break_mode
ack_early = args.break_mode
state = write_record("k", "v1", fsync=fsync, ack_early=ack_early)
if args.break_mode:
crash_before_fsync()
recovered = WAL.read_text(encoding="utf-8") if WAL.exists() else ""
print(f"ack_point={state} fsync={fsync}")
print(f" wal_contents={recovered!r}")
if args.break_mode:
print("\n--break: ACK before fsync -> client thinks durable, crash may lose write")
else:
print(" durability: ack after fsync - safe after crash")

if __name__ == "__main__":
main()
