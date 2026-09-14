#!/usr/bin/env python3
"""Day 068: Partial failure / dual write ambiguity."""
import argparse
import random

def dual_write(fail_b: bool, assume_success_on_timeout: bool):
random.seed(0)
a_ok = True
b_ok = not fail_b
if fail_b:
print("service B failed after service A succeeded")
client_known = a_ok and b_ok
if not client_known and assume_success_on_timeout:
print("BUG: client marks both OK after timeout - inconsistent state")
else:
print(f"client sees: success={client_known} (needs reconciliation)")
return a_ok, b_ok

def main():
p = argparse.ArgumentParser()
p.add_argument("--fail-b", action="store_true")
p.add_argument("--assume-success", action="store_true")
args = p.parse_args()
dual_write(args.fail_b, args.assume_success)

if __name__ == "__main__":
main()
