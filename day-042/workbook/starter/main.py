#!/usr/bin/env python3
"""Day 042: sync vs async replication latency/durability."""
from __future__ import annotations

import argparse
import time


class Cluster:
def __init__(self, sync: bool, follower_delay_ms: float):
self.sync = sync
self.delay = follower_delay_ms / 1000
self.leader_log: list[str] = []
self.follower_log: list[str] = []

def write(self, val: str) -> tuple[float, bool]:
t0 = time.perf_counter()
self.leader_log.append(val)
if self.sync:
time.sleep(self.delay)
self.follower_log.append(val)
else:
pass
return (time.perf_counter() - t0) * 1000, len(self.follower_log) == len(self.leader_log)

def replicate_async(self) -> None:
while len(self.follower_log) < len(self.leader_log):
time.sleep(self.delay)
self.follower_log.append(self.leader_log[len(self.follower_log)])

def lose_leader(self) -> int:
return len(self.leader_log) - len(self.follower_log)


def main() -> None:
p = argparse.ArgumentParser(description="Sync vs async replication lab")
p.add_argument("--sync", action="store_true")
p.add_argument("--delay-ms", type=float, default=5.0)
p.add_argument("--break", dest="break_mode", action="store_true", help="crash leader before async replicate")
args = p.parse_args()

c = Cluster(args.sync, args.delay_ms)
lats = []
for i in range(20):
ms, _ = c.write(f"e{i}")
lats.append(ms)

if not args.sync and not args.break_mode:
c.replicate_async()
lost = c.lose_leader() if args.break_mode and not args.sync else 0

mode = "sync" if args.sync else "async"
print(f"mode={mode} avg_write_ms={sum(lats)/len(lats):.3f} max_ms={max(lats):.3f}")
print(f"leader={len(c.leader_log)} follower={len(c.follower_log)} possible_lost={lost}")


if __name__ == "__main__":
main()
