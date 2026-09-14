#!/usr/bin/env python3
"""Day 033: row vs column storage micro-benchmark."""
from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path

DIR = Path("data/col")


def gen_rows(n: int) -> list[dict]:
return [{"id": i, "country": f"c{i%20}", "amount": i * 3 % 997, "note": f"n{i}"} for i in range(n)]


def write_row_csv(rows: list[dict]) -> Path:
DIR.mkdir(parents=True, exist_ok=True)
p = DIR / "rows.csv"
with p.open("w", newline="", encoding="utf-8") as f:
w = csv.DictWriter(f, fieldnames=rows[0].keys())
w.writeheader()
w.writerows(rows)
return p


def write_columns(rows: list[dict]) -> list[Path]:
DIR.mkdir(parents=True, exist_ok=True)
cols = {k: [] for k in rows[0]}
for r in rows:
for k, v in r.items():
cols[k].append(v)
paths = []
for k, vals in cols.items():
p = DIR / f"{k}.json"
p.write_text(json.dumps(vals), encoding="utf-8")
paths.append(p)
return paths


def bytes_read(paths: list[Path]) -> int:
return sum(p.stat().st_size for p in paths)


def main() -> None:
p = argparse.ArgumentParser(description="Columnar vs row lab")
p.add_argument("--rows", type=int, default=5000)
p.add_argument("--wide", action="store_true", help="read all columns")
args = p.parse_args()

rows = gen_rows(args.rows)
row_path = write_row_csv(rows)
col_paths = write_columns(rows)

t0 = time.perf_counter()
if args.wide:
data = list(csv.DictReader(row_path.open(encoding="utf-8")))
_ = sum(int(r["amount"]) for r in data)
rb = row_path.stat().st_size
else:
data = json.loads((DIR / "amount.json").read_text(encoding="utf-8"))
_ = sum(data)
rb = (DIR / "amount.json").stat().st_size
row_ms = (time.perf_counter() - t0) * 1000

t1 = time.perf_counter()
if args.wide:
cb = bytes_read(col_paths)
_ = {k: json.loads((DIR / f"{k}.json").read_text()) for k in rows[0]}
else:
cb = (DIR / "amount.json").stat().st_size
_ = sum(json.loads((DIR / "amount.json").read_text()))
col_ms = (time.perf_counter() - t1) * 1000

print(f"mode={'wide' if args.wide else 'aggregate'} rows={args.rows}")
print(f"row_bytes={rb} row_ms={row_ms:.2f}")
print(f"col_bytes={cb} col_ms={col_ms:.2f}")


if __name__ == "__main__":
main()
