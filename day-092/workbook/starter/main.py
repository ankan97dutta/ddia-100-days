#!/usr/bin/env python3
"""Day 092: stream join with watermark and late events."""
from __future__ import annotations

CLICKS = [(1, "c1", 5), (1, "c2", 12)]
IMPS = [(1, "i1", 6), (1, "i2", 15)]
WATERMARK = 10
WINDOW = 5

def join(clicks, imps, wm: int, drop_late: bool) -> tuple[list, int]:
joined, late = [], 0
for ck, cv, ct in clicks:
if ct > wm and drop_late:
late += 1
continue
for ik, iv, it in imps:
if ik != ck or abs(ct - it) > WINDOW:
continue
if it > wm and drop_late:
late += 1
continue
joined.append((ck, cv, iv))
return joined, late

def main() -> None:
for policy in (True, False):
j, late = join(CLICKS, IMPS, WATERMARK, drop_late=policy)
print(f"\n=== drop_late={policy} watermark={WATERMARK} ===")
print(f"joins={j} late_dropped={late}")

if __name__ == "__main__":
main()
