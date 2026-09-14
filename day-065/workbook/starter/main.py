#!/usr/bin/env python3
"""Day 065: Serial queue vs concurrent lost updates."""
import argparse
import sqlite3
import threading
import time

def work(serial: bool, threads: int = 8, n: int = 200):
db = sqlite3.connect("file:ser?mode=memory&cache=shared", uri=True, check_same_thread=False)
db.execute("CREATE TABLE c(v INT)")
db.execute("INSERT INTO c VALUES(0)")
db.commit()
ser_lock = threading.Lock()
aborts = 0

def tx():
nonlocal aborts
c = sqlite3.connect("file:ser?mode=memory&cache=shared", uri=True)
for _ in range(n // threads):
if serial:
with ser_lock:
v = c.execute("SELECT v FROM c").fetchone()[0]
c.execute("UPDATE c SET v=?", (v + 1,))
c.commit()
else:
v = c.execute("SELECT v FROM c").fetchone()[0]
time.sleep(0)
c.execute("UPDATE c SET v=?", (v + 1,))
c.commit()

t0 = time.perf_counter()
ts = [threading.Thread(target=tx) for _ in range(threads)]
for t in ts:
t.start()
for t in ts:
t.join()
final = db.execute("SELECT v FROM c").fetchone()[0]
dt = time.perf_counter() - t0
print(f"serial={serial} final={final} expected={n} time={dt:.3f}s aborts={aborts}")

def main():
p = argparse.ArgumentParser()
p.add_argument("--serial", action="store_true")
args = p.parse_args()
work(args.serial)

if __name__ == "__main__":
main()
