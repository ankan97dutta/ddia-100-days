#!/usr/bin/env python3
"""Day 066: Deadlock with opposite lock order."""
import argparse
import sqlite3
import threading
import time

def transfer(db_path: str, ordered: bool, reverse: bool):
a = sqlite3.connect(db_path, check_same_thread=False)
b = sqlite3.connect(db_path, check_same_thread=False)
a.execute("CREATE TABLE IF NOT EXISTS bal(id TEXT PRIMARY KEY, v INT)")
b.execute("CREATE TABLE IF NOT EXISTS bal(id TEXT PRIMARY KEY, v INT)")
for c in (a, b):
c.execute("INSERT OR IGNORE INTO bal VALUES('x',100),('y',100)")
c.commit()

def move(conn, first: str, second: str):
conn.isolation_level = None
conn.execute("BEGIN IMMEDIATE")
conn.execute("UPDATE bal SET v=v-10 WHERE id=?", (first,))
time.sleep(0.05)
conn.execute("UPDATE bal SET v=v+10 WHERE id=?", (second,))
conn.execute("COMMIT")

t1 = threading.Thread(target=move, args=(a, "x", "y"))
t2 = threading.Thread(target=move, args=(b, "y" if not ordered else "x", "x" if not ordered else "y"))
t1.start(); t2.start()
t1.join(timeout=2); t2.join(timeout=2)
print(f"ordered={ordered} reverse={reverse} done (timeout => possible deadlock)")

def main():
p = argparse.ArgumentParser()
p.add_argument("--ordered", action="store_true")
args = p.parse_args()
path = "file:2pl?mode=memory&cache=shared"
transfer(path, args.ordered, not args.ordered)

if __name__ == "__main__":
main()
