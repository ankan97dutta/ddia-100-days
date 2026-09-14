#!/usr/bin/env python3
"""Day 067: Two-phase commit with coordinator crash."""
import argparse
from enum import Enum

class State(str, Enum):
INIT = "init"
PREPARED = "prepared"
COMMITTED = "committed"
ABORTED = "aborted"

class Participant:
def __init__(self, name: str):
self.name = name
self.state = State.INIT

def prepare(self) -> bool:
self.state = State.PREPARED
return True

def commit(self):
self.state = State.COMMITTED

def abort(self):
self.state = State.ABORTED

def run(crash: bool):
parts = [Participant("db1"), Participant("db2")]
votes = [p.prepare() for p in parts]
if all(votes):
if crash:
print("COORDINATOR CRASH after prepare - participants blocked:")
for p in parts:
print(f" {p.name}: {p.state.value}")
return
for p in parts:
p.commit()
else:
for p in parts:
p.abort()
print("final:", {p.name: p.state.value for p in parts})

def main():
p = argparse.ArgumentParser()
p.add_argument("--crash", action="store_true")
args = p.parse_args()
run(args.crash)

if __name__ == "__main__":
main()
