#!/usr/bin/env python3
"""Day 018: Document modeling with SQLite JSON."""
from __future__ import annotations
import argparse, json, sqlite3, time

def main() -> None:
p = argparse.ArgumentParser(description="Document modeling lab")
p.add_argument("--orders", type=int, default=1000)
p.add_argument("--break", dest="break_mode", action="store_true", help="Update one sku across all orders")
args = p.parse_args()
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, doc TEXT NOT NULL)")
sku = "WIDGET-A"
for i in range(args.orders):
doc = {"id": i, "items": [{"sku": sku, "qty": 1}]}
con.execute("INSERT INTO orders VALUES (?, ?)", (i, json.dumps(doc)))
t0 = time.perf_counter()
if args.break_mode:
rows = con.execute("SELECT id, doc FROM orders").fetchall()
for oid, raw in rows:
d = json.loads(raw)
for it in d["items"]:
if it["sku"] == sku:
it["sku"] = "WIDGET-B"
con.execute("UPDATE orders SET doc=? WHERE id=?", (json.dumps(d), oid))
con.commit()
else:
row = con.execute("SELECT doc FROM orders WHERE id=0").fetchone()
print(f"single read: {json.loads(row[0])}")
ms = (time.perf_counter() - t0) * 1000
print(f"orders={args.orders} ms={ms:.1f}")
if args.break_mode:
print("\n--break: partial update scanned all docs - boundary signal")

if __name__ == "__main__":
main()
