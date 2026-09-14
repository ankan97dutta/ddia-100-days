#!/usr/bin/env python3
"""Day 017: Relational schema with constraints (sqlite)."""
from __future__ import annotations
import argparse, sqlite3

DDL = '''
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL REFERENCES customers(id));
CREATE TABLE line_items (id INTEGER PRIMARY KEY, order_id INTEGER NOT NULL REFERENCES orders(id), qty INTEGER NOT NULL CHECK(qty > 0));
'''

def main() -> None:
p = argparse.ArgumentParser(description="Relational constraints lab")
p.add_argument("--break", dest="break_mode", action="store_true", help="Try orphan line item insert")
args = p.parse_args()
con = sqlite3.connect(":memory:")
con.executescript(DDL)
con.execute("INSERT INTO customers VALUES (1, 'Ada')")
con.execute("INSERT INTO orders VALUES (1, 1)")
con.execute("INSERT INTO line_items VALUES (1, 1, 2)")
print("valid inserts: OK")
tests = [("orphan line item", "INSERT INTO line_items VALUES (2, 99, 1)"), ("negative qty", "INSERT INTO line_items VALUES (3, 1, -1)")]
if not args.break_mode:
tests = tests[:1]
for label, sql in tests:
try:
con.execute(sql)
con.commit()
print(f" {label}: UNEXPECTED OK")
except sqlite3.IntegrityError as e:
print(f" {label}: blocked ({e})")

if __name__ == "__main__":
main()
