#!/usr/bin/env python3
"""Day 084: batch log analysis pipeline."""
from __future__ import annotations
import hashlib
from collections import Counter

LOGS = [
"GET /api/users 200 12",
"GET /api/users 500 45",
"POST /api/orders 201 30",
"GET /api/users 200 10",
"GET /api/health 200 1",
"CORRUPT LINE",
"GET /api/orders 404 8",
]

def parse(line: str) -> tuple[str, int] | None:
parts = line.split()
if len(parts) != 4 or not parts[2].isdigit():
return None
return f"{parts[0]} {parts[1]}", int(parts[2])

def run(lines: list[str], strict: bool) -> dict:
endpoints: Counter = Counter()
errors = total = 0
for line in lines:
rec = parse(line)
if rec is None:
if strict:
raise ValueError(f"bad line: {line!r}")
continue
ep, status = rec
total += 1
endpoints[ep] += 1
if status >= 400:
errors += 1
return {"total": total, "errors": errors, "top": endpoints.most_common(3)}

def digest(report: dict) -> str:
return hashlib.sha256(repr(report).encode()).hexdigest()[:12]

def main() -> None:
clean = [l for l in LOGS if l != "CORRUPT LINE"]
r1 = run(clean, strict=True)
r2 = run(clean, strict=True)
print("=== Batch log report (clean input) ===")
print(r1)
print(f"checksum run1={digest(r1)} run2={digest(r2)} match={digest(r1)==digest(r2)}")
try:
run(LOGS, strict=True)
except ValueError as e:
print(f"\nstrict mode on corrupt input: {e}")

if __name__ == "__main__":
main()
