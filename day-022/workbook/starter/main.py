#!/usr/bin/env python3
"""Day 022: Graph traversal (friends-of-friends)."""
from __future__ import annotations
import argparse, time
from collections import deque

EDGES = [(1,2),(2,3),(3,4),(4,5),(1,6),(6,7)]

def bfs(start: int, max_depth: int | None) -> tuple[set[int], int]:
seen = {start}
q = deque([(start, 0)])
edges_seen = 0
while q:
node, d = q.popleft()
if max_depth is not None and d >= max_depth:
continue
for a, b in EDGES:
nxt = b if a == node else (a if b == node else None)
if nxt is not None:
edges_seen += 1
if nxt not in seen:
seen.add(nxt)
q.append((nxt, d + 1))
return seen, edges_seen

def main() -> None:
p = argparse.ArgumentParser(description="Graph BFS lab")
p.add_argument("--depth", type=int, default=2)
p.add_argument("--break", dest="break_mode", action="store_true", help="Remove depth limit")
args = p.parse_args()
limit = None if args.break_mode else args.depth
t0 = time.perf_counter()
nodes, edges = bfs(1, limit)
ms = (time.perf_counter() - t0) * 1000
print(f"start=1 depth_limit={limit} nodes_visited={len(nodes)} edges_checked={edges} ms={ms:.3f}")
print(f" nodes: {sorted(nodes)}")
if args.break_mode:
print("\n--break: no depth limit on dense graph -> runtime/memory blow up")

if __name__ == "__main__":
main()
