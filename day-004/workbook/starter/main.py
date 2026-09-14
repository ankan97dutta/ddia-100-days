#!/usr/bin/env python3
"""Day 004: Cloud vs self-hosted ADR scorer."""
from __future__ import annotations

import argparse

OPTIONS = {
"managed": {"monthly_usd": 1200, "rto_hr": 1, "rpo_min": 5, "ops_hr_week": 2, "owner": "vendor"},
"self_hosted": {"monthly_usd": 400, "rto_hr": 4, "rpo_min": 15, "ops_hr_week": 12, "owner": "your_team"},
}


def score(opt: dict, break_region: bool) -> dict:
s = dict(opt)
if break_region:
s["rto_hr"] *= 2 if opt["owner"] == "your_team" else 1.5
s["note"] = "region outage: recovery owner differs"
return s


def main() -> None:
p = argparse.ArgumentParser(description="Compare managed vs self-hosted Postgres ADR")
p.add_argument("--break", dest="break_mode", action="store_true", help="Simulate region outage")
args = p.parse_args()

print("=== Postgres hosting ADR (sample numbers) ===")
for name, opt in OPTIONS.items():
row = score(opt, args.break_mode)
print(f" {name:12} $/mo={row['monthly_usd']:4} RTO={row['rto_hr']}h RPO={row['rpo_min']}m ops={row['ops_hr_week']}h/wk paged={row['owner']}")
if args.break_mode:
print("\n--break: region outage - managed=vendor ticket, self=your on-call")


if __name__ == "__main__":
main()
