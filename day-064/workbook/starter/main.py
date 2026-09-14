#!/usr/bin/env python3
"""Day 064: Phantom read simulation."""
import argparse

def main():
p = argparse.ArgumentParser()
p.add_argument("--lock", action="store_true", help="Predicate lock blocks insert")
args = p.parse_args()
seats = [{"id": 1, "free": 1}, {"id": 2, "free": 1}]
locked = args.lock
c1 = sum(1 for s in seats if s["free"])
print(f"TX A: COUNT free seats = {c1} (predicate locked={locked})")
if not locked:
seats.append({"id": 3, "free": 1})
print("TX B: INSERT new free seat id=3 and commits")
else:
print("TX B: INSERT blocked by predicate lock")
c2 = sum(1 for s in seats if s["free"])
print(f"TX A: COUNT again = {c2} phantom_rows={c2 - c1}")

if __name__ == "__main__":
main()
