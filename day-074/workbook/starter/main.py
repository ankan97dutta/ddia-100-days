#!/usr/bin/env python3
"""Day 074: Process pause and false leader death."""
import argparse
import time

def main():
p = argparse.ArgumentParser()
p.add_argument("--pause-sec", type=float, default=3.0)
p.add_argument("--timeout-sec", type=float, default=1.0)
p.add_argument("--resume-writes", action="store_true")
args = p.parse_args()
last_hb = time.monotonic()
leader = "node-A"
print(f"{leader} is leader, heartbeat every 0.2s, timeout={args.timeout_sec}s")
t0 = time.monotonic()
while time.monotonic() - t0 < 0.5:
last_hb = time.monotonic()
time.sleep(0.2)
print(f"PAUSE {args.pause_sec}s (GC / stop-world)...")
time.sleep(args.pause_sec)
silent = time.monotonic() - last_hb
if silent > args.timeout_sec:
new = "node-B"
print(f"followers: {leader} silent {silent:.1f}s - elect {new} as leader")
if args.resume_writes:
print(f"SPLIT BRAIN: {leader} resumes AND {new} is leader - both may write")

if __name__ == "__main__":
main()
