#!/usr/bin/env python3
"""Day 023: SQL vs imperative query comparison."""
from __future__ import annotations
import argparse, sqlite3

ROWS = [(1, "east", 10), (2, "east", 20), (3, "west", 5)]

def imperative(region: str) -> int:
total = 0
for _id, reg, amt in ROWS:
if reg == region:
total += amt
return total

def main() -> None:
p = argparse.ArgumentParser(description="SQL vs imperative")
p.add_argument("--region", default="east")
p.add_argument("--break", dest="break_mode", action="store_true", help="Buggy imperative filter")
args = p.parse_args()
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE t(id INT, region TEXT, amt INT)")
con.executemany("INSERT INTO t VALUES (?,?,?)", ROWS)
sql = con.execute("SELECT SUM(amt) FROM t WHERE region=?", (args.region,)).fetchone()[0]
imp = imperative(args.region if not args.break_mode else "eas") # typo footgun
print(f"region={args.region!r} sql_sum={sql} imperative_sum={imp}")
print(f" sql_lines=1 imperative_lines=5")
if args.break_mode:
print("\n--break: typo in imperative filter -> silent wrong answer")

if __name__ == "__main__":
main()
