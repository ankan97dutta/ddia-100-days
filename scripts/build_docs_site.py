#!/usr/bin/env python3
"""Build MkDocs docs/ from the curriculum for GitHub Pages."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CHAPTERS = [
    (1, "Trade-offs in data systems architecture", range(1, 7)),
    (2, "Defining nonfunctional requirements", range(7, 17)),
    (3, "Data models and query languages", range(17, 25)),
    (4, "Storage and retrieval", range(25, 35)),
    (5, "Encoding and evolution", range(35, 41)),
    (6, "Replication", range(41, 51)),
    (7, "Sharding", range(51, 58)),
    (8, "Transactions", range(58, 68)),
    (9, "The trouble with distributed systems", range(68, 77)),
    (10, "Consistency and consensus", range(77, 84)),
    (11, "Batch processing", range(84, 89)),
    (12, "Stream processing", range(89, 94)),
    (13, "A philosophy of streaming systems", range(94, 97)),
    (14, "Doing the right thing", range(97, 101)),
]


def day_title(n: int) -> str:
    readme = (ROOT / f"day-{n:03d}" / "README.md").read_text(encoding="utf-8")
    m = re.search(r"^# Day \d+:\s*(.+)$", readme, re.M)
    return m.group(1).strip() if m else f"Day {n:03d}"


def rewrite_day_markdown(n: int, text: str) -> str:
    text = text.replace("](../WORKFLOW.md)", "](../../workflow.md)")
    text = text.replace("](./workbook/exercise.md)", "](./exercise.md)")
    text = text.replace("](./workbook/starter/README.md)", "](./starter.md)")
    text = text.replace(
        "See [workbook/starter/README.md](./starter.md).",
        "Starter notes: [starter.md](./starter.md). Exercise sheet: [exercise.md](./exercise.md).",
    )
    gh = f"https://github.com/ankan97dutta/ddia-100-days/blob/main/day-{n:03d}/workbook/starter/main.py"
    footer = f"""

## Lab files on GitHub

- Starter script: [`main.py`]({gh})
- Clone the repo to run labs locally (`python3 main.py` needs a checkout)

"""
    if "## Lab files on GitHub" not in text:
        text = text.rstrip() + footer
    return text


def write_nav() -> str:
    lines = [
        "nav:",
        "  - Home: index.md",
        "  - How to use: workflow.md",
        "  - Chapters: chapters.md",
        "  - Progress: progress.md",
        "  - Days:",
    ]
    for ch, title, days in CHAPTERS:
        lines.append(f'    - "Chapter {ch}: {title}":')
        for n in days:
            t = day_title(n).replace('"', "'")
            lines.append(f'      - "Day {n:03d}: {t}": days/day-{n:03d}/index.md')
    return "\n".join(lines) + "\n"


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    # Top-level pages
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = (
        readme.replace("](./PROGRESS.md)", "](progress.md)")
        .replace("](./WORKFLOW.md)", "](workflow.md)")
        .replace("](./CHAPTERS.md)", "](chapters.md)")
        .replace(
            "](./LICENSE.md)",
            "](https://github.com/ankan97dutta/ddia-100-days/blob/main/LICENSE.md)",
        )
    )
    (DOCS / "index.md").write_text(
        readme
        + "\n\n## Browse by chapter\n\nSee [Chapters](chapters.md) or pick a day from the left nav.\n",
        encoding="utf-8",
    )

    (DOCS / "workflow.md").write_text(
        (ROOT / "WORKFLOW.md").read_text(encoding="utf-8").replace(
            "](./PROGRESS.md)", "](progress.md)"
        ),
        encoding="utf-8",
    )
    chapters = (ROOT / "CHAPTERS.md").read_text(encoding="utf-8")
    # Link day ranges in table to first day of each chapter
    extra = ["\n## Jump to days\n"]
    for ch, title, days in CHAPTERS:
        links = ", ".join(
            f"[Day {n:03d}](days/day-{n:03d}/index.md)" for n in list(days)[:3]
        )
        more = f" ... [Day {list(days)[-1]:03d}](days/day-{list(days)[-1]:03d}/index.md)"
        extra.append(f"- **Chapter {ch}: {title}** - {links}{more}")
    (DOCS / "chapters.md").write_text(chapters + "\n".join(extra) + "\n", encoding="utf-8")
    (DOCS / "progress.md").write_text(
        (ROOT / "PROGRESS.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    for n in range(1, 101):
        day_dir = DOCS / "days" / f"day-{n:03d}"
        day_dir.mkdir(parents=True)
        src = ROOT / f"day-{n:03d}"
        day_md = rewrite_day_markdown(n, (src / "README.md").read_text(encoding="utf-8"))
        (day_dir / "index.md").write_text(day_md, encoding="utf-8")
        (day_dir / "exercise.md").write_text(
            (src / "workbook" / "exercise.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        starter = (src / "workbook" / "starter" / "README.md").read_text(encoding="utf-8")
        starter += (
            f"\n## Source\n\n"
            f"[`main.py` on GitHub](https://github.com/ankan97dutta/ddia-100-days/blob/main/day-{n:03d}/workbook/starter/main.py)\n"
        )
        (day_dir / "starter.md").write_text(starter, encoding="utf-8")

    # Write nav fragment for mkdocs.yml merge helper
    (ROOT / "scripts" / "nav.generated.yml").write_text(write_nav(), encoding="utf-8")
    print(f"Built {DOCS} with 100 day pages")


if __name__ == "__main__":
    main()
