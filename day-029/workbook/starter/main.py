#!/usr/bin/env python3
"""Day 029: in-memory B-tree page simulator."""
from __future__ import annotations

import argparse
import random
import time


class Node:
__slots__ = ("keys", "children", "leaf", "next", "order")

def __init__(self, leaf: bool, order: int):
self.keys: list[int] = []
self.children: list[Node] = []
self.leaf = leaf
self.next: Node | None = None
self.order = order

def is_full(self) -> bool:
return len(self.keys) >= self.order


class BTree:
def __init__(self, order: int = 4):
self.root = Node(True, order)
self.order = order
self.splits = 0
self.page_reads = 0

def insert(self, key: int) -> None:
root = self.root
if root.is_full():
new_root = Node(False, self.order)
new_root.children.append(root)
self._split_child(new_root, 0)
self.root = new_root
self._insert_nonfull(root, key)

def _split_child(self, parent: Node, idx: int) -> None:
full = parent.children[idx]
mid = self.order // 2
sibling = Node(full.leaf, self.order)
promote = full.keys[mid]
sibling.keys = full.keys[mid + 1 :]
full.keys = full.keys[:mid]
if not full.leaf:
sibling.children = full.children[mid + 1 :]
full.children = full.children[: mid + 1]
else:
sibling.next = full.next
full.next = sibling
parent.keys.insert(idx, promote)
parent.children.insert(idx + 1, sibling)
self.splits += 1

def _insert_nonfull(self, node: Node, key: int) -> None:
i = len(node.keys) - 1
if node.leaf:
node.keys.append(0)
while i >= 0 and key < node.keys[i]:
node.keys[i + 1] = node.keys[i]
i -= 1
node.keys[i + 1] = key
else:
while i >= 0 and key < node.keys[i]:
i -= 1
i += 1
if node.children[i].is_full():
self._split_child(node, i)
if key > node.keys[i]:
i += 1
self._insert_nonfull(node.children[i], key)

def get(self, key: int) -> bool:
node = self.root
self.page_reads = 0
while node:
self.page_reads += 1
i = 0
while i < len(node.keys) and key > node.keys[i]:
i += 1
if i < len(node.keys) and key == node.keys[i]:
return True
if node.leaf:
return False
node = node.children[i]
return False


def main() -> None:
p = argparse.ArgumentParser(description="B-tree insert lab")
p.add_argument("--n", type=int, default=5000)
p.add_argument("--random", action="store_true")
args = p.parse_args()

keys = list(range(args.n))
if args.random:
random.shuffle(keys)

tree = BTree(order=32)
t0 = time.perf_counter()
for k in keys:
tree.insert(k)
ms = (time.perf_counter() - t0) * 1000

tree.get(args.n // 2)
print(f"inserted={args.n} splits={tree.splits} insert_ms={ms:.2f}")
print(f"lookup_pages={tree.page_reads} mode={'random' if args.random else 'sequential'}")


if __name__ == "__main__":
main()
