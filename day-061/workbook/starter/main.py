#!/usr/bin/env python3
"""Day 061: Snapshot isolation simulated with row versions."""
import argparse
from dataclasses import dataclass

@dataclass
class Version:
value: int
created_by: int
deleted_by: int | None = None

class SnapshotDB:
def __init__(self):
self.rows: dict[int, list[Version]] = {1: [Version(10, 0)]}
self.tx_counter = 0
self.active: dict[int, int] = {}

def begin(self) -> int:
self.tx_counter += 1
self.active[self.tx_counter] = self.tx_counter
return self.tx_counter

def read(self, tx: int, key: int) -> int | None:
for v in reversed(self.rows[key]):
if v.deleted_by and v.deleted_by <= tx:
continue
if v.created_by <= tx:
return v.value
return None

def write(self, tx: int, key: int, value: int):
for v in self.rows[key]:
if v.deleted_by is None and v.created_by not in (0, tx):
raise RuntimeError(f"write-write conflict: tx{tx} vs tx{v.created_by}")
cur = self.read(tx, key)
if cur is not None:
self.rows[key][-1].deleted_by = tx
self.rows[key].append(Version(value, tx))

def main():
p = argparse.ArgumentParser()
p.add_argument("--conflict", action="store_true")
args = p.parse_args()
db = SnapshotDB()
t1 = db.begin()
t2 = db.begin()
print(f"t1 sees: {db.read(t1, 1)}")
db.write(t2, 1, 99)
print(f"t1 still sees: {db.read(t1, 1)}")
if args.conflict:
try:
db.write(t1, 1, 50)
except RuntimeError as e:
print("conflict:", e)

if __name__ == "__main__":
main()
