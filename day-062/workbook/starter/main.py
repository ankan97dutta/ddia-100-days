#!/usr/bin/env python3
"""Day 062: Lost update vs atomic fix."""
import argparse
import sqlite3
import threading

def race(db_path: str, atomic: bool, threads: int = 20, steps: int = 50):
conn = sqlite3.connect(db_path, check_same_thread=False)
conn.execute("CREATE TABLE c(v INT)")
conn.execute("INSERT INTO c VALUES(0)")
conn.commit()
lock = threading.Lock()

def worker():
c = sqlite3.connect(db_path, check_same_thread=False)
for _ in range(steps):
if atomic:
with lock:
c.execute("UPDATE c SET v=v+1")
c.commit()
else:
v = c.execute("SELECT v FROM c").fetchone()[0]
c.execute("UPDATE c SET v=?", (v + 1,))
c.commit()

ts = [threading.Thread(target=worker) for _ in range(threads)]
for t in ts:
t.start()
for t in ts:
t.join()
final = conn.execute("SELECT v FROM c").fetchone()[0]
expected = threads * steps
print(f"atomic={atomic} final={final} expected={expected} lost={expected-final}")

def main():
p = argparse.ArgumentParser()
p.add_argument("--atomic", action="store_true")
args = p.parse_args()
race("file:lu?mode=memory&cache=shared", args.atomic)

if __name__ == "__main__":
main()
