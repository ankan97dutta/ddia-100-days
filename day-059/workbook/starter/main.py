#!/usr/bin/env python3
"""Day 059: ACID properties with sqlite3."""
import argparse
import os
import sqlite3
import tempfile

def demo_atomic(conn, fail: bool):
conn.execute("CREATE TABLE IF NOT EXISTS accounts(id INT PRIMARY KEY, bal INT)")
conn.execute("INSERT OR REPLACE INTO accounts VALUES(1,100),(2,0)")
try:
conn.execute("BEGIN")
conn.execute("UPDATE accounts SET bal=bal-30 WHERE id=1")
if fail:
raise RuntimeError("crash mid-transfer")
conn.execute("UPDATE accounts SET bal=bal+30 WHERE id=2")
conn.commit()
except Exception:
conn.rollback()
print("Atomicity:", conn.execute("SELECT * FROM accounts ORDER BY id").fetchall())

def demo_consistency(conn):
try:
conn.execute("CREATE TABLE t(x INT CHECK(x>0))")
conn.execute("INSERT INTO t VALUES(-1)")
except sqlite3.IntegrityError as e:
print("Consistency:", e)

def demo_durability(path: str):
conn = sqlite3.connect(path)
conn.execute("CREATE TABLE IF NOT EXISTS kv(k TEXT PRIMARY KEY, v TEXT)")
conn.execute("INSERT OR REPLACE INTO kv VALUES('done','yes')")
conn.commit()
conn.close()
conn2 = sqlite3.connect(path)
print("Durability after reopen:", conn2.execute("SELECT v FROM kv").fetchone())

def main():
p = argparse.ArgumentParser()
p.add_argument("--fail-mid", action="store_true")
args = p.parse_args()
conn = sqlite3.connect(":memory:")
demo_atomic(conn, args.fail_mid)
demo_consistency(conn)
fd, path = tempfile.mkstemp(suffix=".db")
os.close(fd)
demo_durability(path)
os.unlink(path)
print("Isolation: see days 060+ (levels vary by engine)")

if __name__ == "__main__":
main()
