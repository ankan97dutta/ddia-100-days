#!/usr/bin/env python3
"""Day 031: primary + secondary index simulator."""
from __future__ import annotations

import argparse
import random
import time


class Table:
def __init__(self, secondary: bool):
self.rows: dict[int, dict] = {}
self.pk = {}
self.email_idx: dict[str, list[int]] = {}
self.secondary = secondary
self.write_touches = 0

def insert(self, rid: int, email: str, status: str) -> None:
self.write_touches += 1
self.rows[rid] = {"email": email, "status": status}
self.pk[rid] = rid
if self.secondary:
self.write_touches += 1
self.email_idx.setdefault(email, []).append(rid)

def update_email(self, rid: int, new_email: str) -> None:
old = self.rows[rid]["email"]
self.write_touches += 1
self.rows[rid]["email"] = new_email
if self.secondary:
self.write_touches += 2
self.email_idx[old].remove(rid)
self.email_idx.setdefault(new_email, []).append(rid)

def get_by_id(self, rid: int) -> dict | None:
return self.rows.get(rid)

def get_by_email(self, email: str) -> list[dict]:
if not self.secondary:
return [r for r in self.rows.values() if r["email"] == email]
return [self.rows[i] for i in self.email_idx.get(email, [])]


def main() -> None:
p = argparse.ArgumentParser(description="Secondary index lab")
p.add_argument("--rows", type=int, default=1000)
p.add_argument("--updates", type=int, default=200)
p.add_argument("--no-index", action="store_true")
args = p.parse_args()

t = Table(secondary=not args.no_index)
rng = random.Random(1)
emails = [f"u{i}@example.com" for i in range(args.rows)]

t0 = time.perf_counter()
for i, e in enumerate(emails):
t.insert(i, e, "active")
for _ in range(args.updates):
rid = rng.randrange(args.rows)
t.update_email(rid, f"changed{rid}@example.com")
ms = (time.perf_counter() - t0) * 1000

sample = t.get_by_email("changed0@example.com")
print(f"secondary_index={not args.no_index} write_touches={t.write_touches} elapsed_ms={ms:.2f}")
print(f"lookup_by_email_hits={len(sample)}")


if __name__ == "__main__":
main()
