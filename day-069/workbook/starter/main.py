#!/usr/bin/env python3
"""Day 069: Unreliable network + idempotency keys."""
import argparse
import random

class Server:
def __init__(self):
self.seen: set[str] = set()
self.charges = 0

def charge(self, key: str, idempotent: bool) -> str:
if idempotent and key in self.seen:
return "deduped"
if idempotent:
self.seen.add(key)
self.charges += 1
return "ok"

def network_deliver(messages: list[str], drop: float, dupe: float, rng: random.Random):
out = []
for m in messages:
if rng.random() < drop:
continue
out.append(m)
if rng.random() < dupe:
out.append(m)
return out

def main():
p = argparse.ArgumentParser()
p.add_argument("--idempotent", action="store_true")
p.add_argument("--drop", type=float, default=0.2)
p.add_argument("--dupe", type=float, default=0.3)
args = p.parse_args()
rng = random.Random(7)
srv = Server()
msgs = ["pay:order42"] * 3
delivered = network_deliver(msgs, args.drop, args.dupe, rng)
for m in delivered:
key = m.split(":")[1]
print(m, "->", srv.charge(key, args.idempotent))
print(f"total charges={srv.charges} idempotent={args.idempotent}")

if __name__ == "__main__":
main()
