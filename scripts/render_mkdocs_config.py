#!/usr/bin/env python3
"""Merge mkdocs.base.yml with generated nav into mkdocs.yml."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    base = (ROOT / "mkdocs.base.yml").read_text(encoding="utf-8")
    nav = (ROOT / "scripts" / "nav.generated.yml").read_text(encoding="utf-8")
    # Drop trailing comment block about nav from base if present; append nav
    out = base.rstrip() + "\n\n" + nav
    (ROOT / "mkdocs.yml").write_text(out, encoding="utf-8")
    print("Wrote mkdocs.yml")


if __name__ == "__main__":
    main()
