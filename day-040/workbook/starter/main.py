#!/usr/bin/env python3
"""Day 040: API/event version compatibility checker."""
from __future__ import annotations

import argparse
import json


EVENTS = {
"order.created.v1": {"required": ["order_id", "amount"]},
"order.created.v2": {"required": ["order_id", "amount", "currency"]},
}


def compatible(event_type: str, payload: dict) -> bool:
spec = EVENTS[event_type]
return all(k in payload for k in spec["required"])


def main() -> None:
p = argparse.ArgumentParser(description="API/event evolution lab")
p.add_argument("--producer", default="order.created.v2")
p.add_argument("--consumer", default="order.created.v1")
p.add_argument("--break", dest="break_mode", action="store_true", help="consumer expects v2, producer emits v1")
args = p.parse_args()

if args.break_mode:
prod, cons = "order.created.v1", "order.created.v2"
else:
prod, cons = args.producer, args.consumer

payload = {"order_id": "o1", "amount": 10, "currency": "USD"}
if prod.endswith("v1"):
payload = {"order_id": "o1", "amount": 10}

ok = compatible(cons, payload)
print(f"producer={prod} consumer={cons} payload={json.dumps(payload)} compatible={ok}")


if __name__ == "__main__":
main()
