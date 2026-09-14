#!/usr/bin/env python3
"""Day 071: Sync vs async failure detection."""
import argparse

def detect(last_heartbeat_ms: float, now_ms: float, timeout_ms: float, model: str) -> str:
silent = now_ms - last_heartbeat_ms
if silent <= timeout_ms:
return "alive"
if model == "sync":
return "dead_certain"
return "maybe_delayed_not_dead_certain"

def main():
p = argparse.ArgumentParser()
p.add_argument("--model", choices=["sync", "async"], default="async")
p.add_argument("--pause-ms", type=float, default=5000)
p.add_argument("--timeout-ms", type=float, default=1000)
args = p.parse_args()
now = args.pause_ms
verdict = detect(0, now, args.timeout_ms, args.model)
print(f"model={args.model} silent_for={now}ms timeout={args.timeout_ms}ms")
print(f"detector verdict: {verdict}")
if args.model == "sync" and now > args.timeout_ms:
print("sync model claims dead - wrong if process was merely paused (GC/stop-world)")

if __name__ == "__main__":
main()
