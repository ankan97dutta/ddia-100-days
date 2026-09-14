#!/usr/bin/env python3
"""Day 020: SQL join vs app-side join."""
from __future__ import annotations
import argparse, sqlite3, time

def main() -> None:
p = argparse.ArgumentParser(description="Join benchmark")
p.add_argument("--break", dest="break_mode", action="store_true", help="Simulate torn read between fetches")
args = p.parse_args()
con = sqlite3.connect(":memory:")
con.executescript("CREATE TABLE u(id INT, name TEXT); CREATE TABLE o(id INT, uid INT, amt REAL);")
con.executemany("INSERT INTO u VALUES (?,?)", [(1, "Ada"), (2, "Bob")])
con.executemany("INSERT INTO o VALUES (?,?,?)", [(1, 1, 10.0), (2, 2, 5.0)])
t0 = time.perf_counter()
sql_rows = con.execute("SELECT u.name, o.amt FROM u JOIN o ON u.id=o.uid").fetchall()
sql_ms = (time.perf_counter() - t0) * 1000
t1 = time.perf_counter()
users = {r[0]: r[1] for r in con.execute("SELECT id, name FROM u")}
if args.break_mode:
con.execute("UPDATE o SET amt=999 WHERE id=1")
orders = list(con.execute("SELECT uid, amt FROM o"))
app_rows = [(users[uid], amt) for uid, amt in orders]
app_ms = (time.perf_counter() - t1) * 1000
print(f"sql_join rows={len(sql_rows)} ms={sql_ms:.3f} round_trips=1")
print(f"app_join rows={len(app_rows)} ms={app_ms:.3f} round_trips=2")
if args.break_mode:
print("\n--break: update between fetches -> app join saw inconsistent state")

if __name__ == "__main__":
main()
