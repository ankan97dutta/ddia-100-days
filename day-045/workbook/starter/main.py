#!/usr/bin/env python3
"""Day 045: read-your-writes via session stickiness."""
from __future__ import annotations

import argparse
import random


class Cluster:
def __init__(self):
self.leader = {}
self.follower = {}
self.lag = 2

def write(self, session: str, k: str, v: int) -> None:
self.leader[k] = v

def replicate(self) -> None:
for k, v in self.leader.items():
if k not in self.follower or self.follower[k] < v - self.lag:
self.follower[k] = max(self.follower.get(k, 0), v - self.lag)

def read(self, session: str, k: str, sticky: bool) -> int | None:
if sticky and session in sticky_sessions:
return self.leader.get(k)
self.replicate()
return self.follower.get(k)


sticky_sessions: set[str] = set()


def main() -> None:
p = argparse.ArgumentParser(description="Read-your-writes lab")
p.add_argument("--sticky", action="store_true")
p.add_argument("--trials", type=int, default=100)
p.add_argument("--break", dest="no_sticky", action="store_true")
args = p.parse_args()

c = Cluster()
violations = 0
use_sticky = args.sticky and not args.no_sticky
rng = random.Random(1)

for i in range(args.trials):
sess = f"s{i%5}"
k = "profile"
val = i
c.write(sess, k, val)
if use_sticky:
sticky_sessions.add(sess)
got = c.read(sess, k, use_sticky)
if got != val:
violations += 1

print(f"sticky={use_sticky} trials={args.trials} ryw_violations={violations}")


if __name__ == "__main__":
main()
