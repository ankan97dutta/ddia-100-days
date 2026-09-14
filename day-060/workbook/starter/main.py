#!/usr/bin/env python3
"""Day 060: Read Committed visibility (simulated sessions)."""
import argparse

def main():
p = argparse.ArgumentParser()
p.add_argument("--break", dest="break_it", action="store_true", help="Leave B uncommitted")
args = p.parse_args()
committed = {1: 10}
b_pending = 99
a_reads = committed[1]
print(f"B pending v={b_pending}; A reads v={a_reads} (no dirty read)")
if not args.break_it:
committed[1] = b_pending
print(f"B committed; A now reads v={committed[1]}")
else:
print("B still uncommitted - A never sees 99")
a_first = committed[1]
committed[1] = 77
a_second = committed[1]
print(f"non-repeatable read: A first={a_first} after B commit={a_second}")

if __name__ == "__main__":
main()
