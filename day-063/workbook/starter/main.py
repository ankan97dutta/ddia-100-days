#!/usr/bin/env python3
"""Day 063: Write skew: on-call doctors (in-process SI-style race)."""
from __future__ import annotations

import argparse
import threading


def run(fix: bool) -> None:
# Shared "database" state with a crude snapshot-isolation feel:
# each txn reads a snapshot, then commits if its predicate still looks OK.
state = {"Ann": 1, "Bob": 1}
lock = threading.Lock()
barrier = threading.Barrier(2)
errors: list[str] = []

def leave(name: str) -> None:
# Take a snapshot (no row locks by default - enables write skew).
snap = dict(state)
barrier.wait() # both see the same pre-commit world
oncall = sum(snap.values())
if oncall < 2:
errors.append(f"{name}: would leave system with <1 on-call")
return
if fix:
with lock:
# Serialize the critical section (predicate lock / SELECT FOR UPDATE feel).
live = sum(state.values())
if live >= 2:
state[name] = 0
else:
errors.append(f"{name}: aborted to protect invariant")
else:
# Both can pass the check against the snapshot, then both commit.
state[name] = 0

t1 = threading.Thread(target=leave, args=("Ann",))
t2 = threading.Thread(target=leave, args=("Bob",))
t1.start(); t2.start(); t1.join(); t2.join()
left = sum(state.values())
print(f"fix={fix} doctors still on call: {left} (invariant: at least 1)")
if errors:
print("notes:", "; ".join(errors))
print("skew_violated" if left < 1 else "invariant_holds")


def main() -> None:
p = argparse.ArgumentParser(description="Write-skew demo for on-call invariant")
p.add_argument("--fix-lock", action="store_true", help="serialize the leave check")
p.add_argument("--break", dest="break_mode", action="store_true",
help="alias: run without fix (default)")
args = p.parse_args()
run(fix=args.fix_lock)


if __name__ == "__main__":
main()
