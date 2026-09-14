#!/usr/bin/env python3
"""Day 056: Stale routing cache after partition move."""
import argparse

class Router:
def __init__(self):
self.version = 1
self.routes = {"p0": "node-a", "p1": "node-b"}

def move(self, part: str, dest: str):
self.routes[part] = dest
self.version += 1

class Client:
def __init__(self, router: Router):
self.router = router
self.cache = {}
self.cache_version = 0
self.stale_errors = 0
self.ok = 0

def resolve(self, part: str, force_refresh: bool = False):
if not force_refresh and part in self.cache and self.cache_version == self.router.version:
return self.cache[part]
node = self.router.routes[part]
self.cache[part] = node
self.cache_version = self.router.version
return node

def request(self, part: str, force_refresh: bool = False):
node = self.resolve(part, force_refresh)
actual = self.router.routes[part]
if node != actual:
self.stale_errors += 1
return False
self.ok += 1
return True

def main():
p = argparse.ArgumentParser()
p.add_argument("--refresh-after-stale", action="store_true")
args = p.parse_args()
r = Router()
c = Client(r)
for _ in range(3):
c.request("p0")
r.move("p0", "node-c")
ok = c.request("p0")
if not ok and args.refresh_after_stale:
c.request("p0", force_refresh=True)
print(f"router v{r.version} routes={r.routes}")
print(f"ok={c.ok} stale_errors={c.stale_errors}")

if __name__ == "__main__":
main()
