#!/usr/bin/env python3
"""Day 019: Normalized vs denormalized benchmark."""
from __future__ import annotations
import argparse, sqlite3, time

def bench(con: sqlite3.Connection, sql: str, n: int = 100) -> float:
t0 = time.perf_counter()
for _ in range(n):
con.execute(sql).fetchone()
return (time.perf_counter() - t0) * 1000

def main() -> None:
p = argparse.ArgumentParser(description="Norm vs denorm benchmark")
p.add_argument("--break", dest="break_mode", action="store_true", help="Skip denorm update -> drift")
args = p.parse_args()
con = sqlite3.connect(":memory:")
con.executescript('''
CREATE TABLE orders (id INT PRIMARY KEY, customer_id INT, total REAL);
CREATE TABLE denorm_summary (order_id INT PRIMARY KEY, summary TEXT);
INSERT INTO orders VALUES (1,1,10.0);
INSERT INTO denorm_summary VALUES (1, 'cust=1 total=10');
''')
read_norm = bench(con, "SELECT o.id, o.total FROM orders o WHERE o.id=1")
read_denorm = bench(con, "SELECT summary FROM denorm_summary WHERE order_id=1")
con.execute("UPDATE orders SET total=20 WHERE id=1")
if not args.break_mode:
con.execute("UPDATE denorm_summary SET summary='cust=1 total=20' WHERE order_id=1")
den = con.execute("SELECT summary FROM denorm_summary").fetchone()[0]
print(f"read_ms norm={read_norm:.2f} denorm={read_denorm:.2f}")
print(f" denorm_summary after write: {den!r}")
if args.break_mode:
print("\n--break: forgot denorm update -> stale summary visible")

if __name__ == "__main__":
main()
