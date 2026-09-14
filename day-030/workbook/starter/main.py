#!/usr/bin/env python3
"""Day 030: toy B-tree vs LSM benchmark."""
from __future__ import annotations

import argparse
import json
import random
import time
from pathlib import Path


class LSM:
def __init__(self):
self.segs: list[dict[str, int]] = []

def put(self, k: str, v: int) -> None:
self.segs.append({k: v})

def get(self, k: str) -> int | None:
val, fanout = None, 0
for seg in reversed(self.segs):
fanout += 1
if k in seg:
val = seg[k]
return val, fanout


class BTreeKV:
def __init__(self):
self.pages: dict[str, int] = {}

def put(self, k: str, v: int) -> None:
self.pages[k] = v

def get(self, k: str) -> tuple[int | None, int]:
return self.pages.get(k), 1


def bench(name: str, store, keys: list[str], updates: int) -> None:
t0 = time.perf_counter()
for i, k in enumerate(keys):
store.put(k, i)
write_ops = len(keys)
write_ms = (time.perf_counter() - t0) * 1000

t1 = time.perf_counter()
fanouts = []
for _ in range(updates):
k = random.choice(keys)
if name == "lsm":
cur, f = store.get(k)
fanouts.append(f)
store.put(k, (cur or 0) + 1)
else:
cur, f = store.get(k)
fanouts.append(f)
store.put(k, (cur or 0) + 1)
upd_ms = (time.perf_counter() - t1) * 1000

print(f"[{name}] write_ops={write_ops} write_ms={write_ms:.2f} update_ops={updates} update_ms={upd_ms:.2f}")
if fanouts:
print(f"[{name}] avg_read_fanout={sum(fanouts)/len(fanouts):.2f} max_fanout={max(fanouts)}")


def main() -> None:
p = argparse.ArgumentParser(description="B-tree vs LSM toy benchmark")
p.add_argument("--keys", type=int, default=800)
p.add_argument("--updates", type=int, default=400)
args = p.parse_args()

keys = [f"k{i}" for i in range(args.keys)]
bench("btree", BTreeKV(), keys, args.updates)
bench("lsm", LSM(), keys, args.updates)


if __name__ == "__main__":
main()
