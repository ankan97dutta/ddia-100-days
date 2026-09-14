#!/usr/bin/env python3
"""Day 075: Lease TTL and fencing tokens."""
import argparse
import time

class LockService:
def __init__(self, ttl: float):
self.ttl = ttl
self.token = 0
self.holder = None
self.expires = 0.0

def acquire(self, client: str, now: float) -> int | None:
if self.holder and now < self.expires:
return None
self.token += 1
self.holder = client
self.expires = now + self.ttl
return self.token

class Storage:
def __init__(self):
self.max_token = 0
self.value = None

def write(self, token: int, value: str) -> bool:
if token < self.max_token:
print(f" REJECT stale token={token} (max={self.max_token})")
return False
self.max_token = token
self.value = value
print(f" ACCEPT token={token} value={value}")
return True

def main():
p = argparse.ArgumentParser()
p.add_argument("--pause-sec", type=float, default=2.0)
p.add_argument("--ttl-sec", type=float, default=1.0)
p.add_argument("--fence", action="store_true")
args = p.parse_args()
lock = LockService(args.ttl_sec)
store = Storage()
t0 = time.monotonic()
tok1 = lock.acquire("A", t0)
print(f"A acquired token={tok1}")
time.sleep(args.pause_sec)
now = time.monotonic()
tok2 = lock.acquire("B", now)
print(f"B acquired token={tok2} after A paused past TTL")
if args.fence:
store.write(tok1, "stale-from-A")
store.write(tok2, "from-B")
print(f"final value={store.value}")

if __name__ == "__main__":
main()
