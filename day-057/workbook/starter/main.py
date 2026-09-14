#!/usr/bin/env python3
"""Day 057: Local vs global secondary index fan-out."""
import argparse

def local_lookup(email: str, shards: list[dict]) -> list[str]:
hits = []
for s in shards:
if email in s.get("email_index", {}):
hits.append(s["email_index"][email])
return hits

def global_lookup(email: str, gindex: dict) -> str | None:
return gindex.get(email)

def main():
p = argparse.ArgumentParser()
p.add_argument("--change-email", action="store_true")
args = p.parse_args()
shards = [{"id": 0, "users": {"u1": "a@x.com"}, "email_index": {"a@x.com": "u1"}},
{"id": 1, "users": {}, "email_index": {}}]
gindex = {"a@x.com": ("shard0", "u1")}
email = "a@x.com"
print("LOCAL read fan-out:", len(shards), "shards queried")
print(" result:", local_lookup(email, shards))
print("GLOBAL read fan-out: 1 index shard")
print(" result:", global_lookup(email, gindex))
if args.change_email:
new = "b@x.com"
shards[0]["email_index"].pop(email)
shards[0]["email_index"][new] = "u1"
gindex.pop(email)
gindex[new] = ("shard0", "u1")
print(f"Email change write fan-out: local=1 shard, global=2 (primary+index)")
else:
print("Write fan-out: local=1, global=2 on indexed update")

if __name__ == "__main__":
main()
