#!/usr/bin/env python3
"""Day 047: multi-leader conflict simulator."""
from __future__ import annotations

import argparse
import itertools


def main() -> None:
p = argparse.ArgumentParser(description="Multi-leader replication lab")
p.add_argument("--keys", type=int, default=5)
p.add_argument("--break", dest="break_mode", action="store_true", help="force same-key concurrent writes")
args = p.parse_args()

us = {}
eu = {}
conflicts = 0

pairs = [(f"k{i}", f"v-us-{i}", f"v-eu-{i}") for i in range(args.keys)]
if args.break_mode:
pairs = [("cart", "us-item", "eu-item")] * 3

for k, v_us, v_eu in pairs:
us[k] = v_us
eu[k] = v_eu
us_to_eu = eu.get(k)
eu_to_us = us.get(k)
if v_us != v_eu:
conflicts += 1
print(f"conflict key={k} us={v_us} eu={v_eu}")

print(f"writes={len(pairs)} conflicts={conflicts}")


if __name__ == "__main__":
main()
