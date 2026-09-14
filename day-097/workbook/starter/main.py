#!/usr/bin/env python3
"""Day 097: feedback loop risk scorer for a design JSON."""
from __future__ import annotations
import json
import sys

DEFAULT = {
"product": "ranking_feed",
"uses_model_output_as_label": True,
"has_randomized_exploration": False,
"tracks_holdout": False,
"monitors_counterfactual": False,
}

CHECKS = [
("uses_model_output_as_label", False, "Avoid training on self-generated labels without correction."),
("has_randomized_exploration", True, "Exploration breaks popularity feedback loops."),
("tracks_holdout", True, "Holdouts measure true lift vs loop-inflated metrics."),
("monitors_counterfactual", True, "Counterfactual metrics detect bias amplification."),
]

def score(design: dict) -> None:
print(f"=== Feedback loop review: {design.get('product', '?')} ===")
pts = 0
for key, want, hint in CHECKS:
val = design.get(key, False)
ok = val == want
pts += int(ok)
print(f"[{'PASS' if ok else 'FAIL'}] {key}={val} - {hint}")
print(f"\nScore: {pts}/{len(CHECKS)}")

def main() -> None:
raw = sys.argv[1] if len(sys.argv) > 1 else json.dumps(DEFAULT)
score(json.loads(raw))

if __name__ == "__main__":
main()
