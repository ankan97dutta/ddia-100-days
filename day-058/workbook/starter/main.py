#!/usr/bin/env python3
"""Day 058: Checkout transaction boundaries."""
import argparse
import sqlite3

def checkout(db_path: str, unified: bool, fail_payment: bool):
conn = sqlite3.connect(db_path)
conn.execute("CREATE TABLE IF NOT EXISTS inventory(sku TEXT PRIMARY KEY, qty INT)")
conn.execute("CREATE TABLE IF NOT EXISTS orders(id INT PRIMARY KEY, sku TEXT)")
conn.execute("INSERT OR IGNORE INTO inventory VALUES('widget', 5)")
conn.commit()
before = conn.execute("SELECT qty FROM inventory WHERE sku='widget'").fetchone()[0]
orders_before = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
try:
conn.execute("BEGIN")
conn.execute("UPDATE inventory SET qty=qty-1 WHERE sku='widget'")
if unified:
if fail_payment:
raise RuntimeError("payment declined")
conn.execute("INSERT INTO orders VALUES(1, 'widget')")
conn.commit()
else:
conn.commit() # inventory committed alone
if fail_payment:
print("payment failed AFTER inventory committed - needs compensation")
return
conn.execute("INSERT INTO orders VALUES(1, 'widget')")
conn.commit()
except Exception as e:
conn.rollback()
print(f"rolled back: {e}")
after = conn.execute("SELECT qty FROM inventory WHERE sku='widget'").fetchone()[0]
orders = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
print(f"inventory {before}->{after} orders {orders_before}->{orders} unified={unified}")

def main():
p = argparse.ArgumentParser()
p.add_argument("--unified-tx", action="store_true")
p.add_argument("--fail-payment", action="store_true")
args = p.parse_args()
checkout(":memory:", args.unified_tx, args.fail_payment)

if __name__ == "__main__":
main()
