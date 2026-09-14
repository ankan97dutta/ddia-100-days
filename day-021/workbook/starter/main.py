#!/usr/bin/env python3
"""Day 021: Star schema ETL (sqlite)."""
from __future__ import annotations
import argparse, sqlite3, time

def main() -> None:
p = argparse.ArgumentParser(description="Star schema ETL")
p.add_argument("--break", dest="break_mode", action="store_true", help="SCD: rename product without history")
args = p.parse_args()
con = sqlite3.connect(":memory:")
con.executescript('''
CREATE TABLE oltp_orders (id INT, product TEXT, amount REAL, day TEXT);
CREATE TABLE dim_product (id INT PRIMARY KEY, name TEXT);
CREATE TABLE fact (id INT, product_id INT, amount REAL, day TEXT);
INSERT INTO oltp_orders VALUES (1,'Widget',10,'2024-01-01'),(2,'Widget',5,'2024-01-02');
''')
con.execute("INSERT INTO dim_product SELECT row_number() OVER (), product FROM oltp_orders GROUP BY product")
con.executescript("INSERT INTO fact SELECT o.id, d.id, o.amount, o.day FROM oltp_orders o JOIN dim_product d ON o.product=d.name")
if args.break_mode:
con.execute("UPDATE dim_product SET name='Gadget' WHERE name='Widget'")
t0 = time.perf_counter()
rows = con.execute("SELECT d.name, SUM(f.amount) FROM fact f JOIN dim_product d ON f.product_id=d.id GROUP BY d.name").fetchall()
ms = (time.perf_counter() - t0) * 1000
print(f"analytical query rows={rows} scanned={len(rows)} ms={ms:.3f}")
if args.break_mode:
print("\n--break: SCD Type-1 rename -> historical reports lose old name")

if __name__ == "__main__":
main()
