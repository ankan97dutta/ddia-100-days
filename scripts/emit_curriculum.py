#!/usr/bin/env python3
"""Emit day READMEs, workbooks, and runnable starters from scripts/content/*.json."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = Path(__file__).resolve().parent / "content"


def load_days() -> list[dict]:
    days: list[dict] = []
    for path in sorted(CONTENT.glob("days_*.json")):
        days.extend(json.loads(path.read_text(encoding="utf-8")))
    days.sort(key=lambda d: d["day"])
    assert [d["day"] for d in days] == list(range(1, 101)), "expected days 1..100"
    return days


def fence_mermaid(src: str) -> str:
    return src.replace("\\n", "\n").strip()


def day_readme(d: dict) -> str:
    n = d["day"]
    bullets = "\n".join(f"- {p}" for p in d["key_points"])
    mermaid = fence_mermaid(d["diagram_mermaid"])
    return f"""# Day {n:03d}: {d['title']}

Chapter {d['chapter']} | {d['deliverable']}

{d['objective']}

## Summary

{d['summary']}

> These notes and diagrams are original study aids for this repo, not copies of DDIA figures or prose. Read the matching section in your own copy of the book.

## Key points

{bullets}

## Diagram

{d['diagram_caption']}

```mermaid
{mermaid}
```

## Today

1. Read the matching DDIA section in your own copy of the book.
2. Skim [WORKFLOW.md](../WORKFLOW.md) if you need the shared checklist.
3. Run the starter, then do Try this / Break it / Measure.

### Run the starter

```bash
cd workbook/starter
python3 main.py --help
python3 main.py
```

See [workbook/starter/README.md](./workbook/starter/README.md).

### Try this

{d['try_this']}

### Break it

{d['break_it']}

### Measure

{d['measure']}

## Done when

- [ ] You can explain the idea simply
- [ ] You ran the starter and captured output
- [ ] You changed one variable or failure mode and noted what happened
- [ ] You wrote one trade-off you would defend in a design review

Workbook: [workbook/exercise.md](./workbook/exercise.md)
"""


def exercise(d: dict) -> str:
    n = d["day"]
    return f"""# Day {n:03d} workbook: {d['title']}

{d['objective']}

## Run

```bash
cd starter
python3 main.py
```

Paste interesting output below.

## Notes

**What I actually did**

> 

**Try this**

{d['try_this']}

**What I changed**

- Variable / failure:
- Before -> after:

**Break it**

{d['break_it']}

- Expected:
- Observed:
- Why they differ:

**Numbers**

{d['measure']}

| Metric | Baseline | After change | What it means |
| --- | ---: | ---: | --- |
| | | | |

**Explanation**

> 

**Design call**

- Option A:
- Option B:
- I would ship: ___ because ___
- Evidence that would change my mind:

## Artifacts

```text
results/
├── measurements.txt
├── notes.md
└── ...
```

## Quick check

- [ ] Explained it without the book open
- [ ] Reproduced the important behavior
- [ ] Broke it on purpose
- [ ] Have at least one number or clear qualitative result
- [ ] Made a choice between alternatives
"""


def workbook_readme(d: dict) -> str:
    n = d["day"]
    return f"""# Workbook: Day {n:03d} ({d['title']})

1. Read [../README.md](../README.md) (summary, key points, diagram).
2. Run [starter/main.py](./starter/main.py).
3. Fill in [exercise.md](./exercise.md) with measurements and decisions.

Prefer honest measurements over polished code.
"""


def _unescape_newlines(text: str) -> str:
    """Turn literal \\n sequences into real newlines when content was double-escaped."""
    if "\\n" in text and text.count("\n") <= text.count("\\n"):
        text = text.replace("\\n", "\n")
    if "\\t" in text:
        text = text.replace("\\t", "\t")
    return text.replace("\u2014", " - ").replace("\u2013", "-").replace("\u2026", "...")


def _extract_commands(text: str) -> list[str]:
    cmds: list[str] = []
    for block in re.findall(r"```(?:bash|sh|shell)?\n(.*?)```", text, flags=re.S | re.I):
        for line in block.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                cmds.append(line)
    for m in re.findall(r"`(python3 main\.py[^`]*)`", text):
        cmd = m.strip()
        if cmd and cmd not in cmds:
            cmds.append(cmd)
    for m in re.findall(r"(?<![`\w])(python3 main\.py[^\n`]*)", text):
        cmd = m.strip().rstrip(".")
        if cmd and cmd not in cmds:
            cmds.append(cmd)
    # Flags mentioned in prose but not yet in a command
    mentioned = re.findall(r"`(---?[a-z0-9-]+)`|--([a-z0-9-]+)", text)
    flags = []
    for a, b in mentioned:
        flag = a or f"--{b}"
        if flag in ("--help", "-h"):
            continue
        if flag not in flags:
            flags.append(flag)

    ordered: list[str] = []
    for preferred in ("python3 main.py --help", "python3 main.py"):
        ordered.append(preferred)
    for cmd in cmds:
        if cmd not in ordered:
            ordered.append(cmd)
    for flag in flags:
        candidate = f"python3 main.py {flag}"
        if candidate not in ordered and not any(flag in c for c in ordered):
            ordered.append(candidate)
    return ordered


def _extract_blurb(text: str, title: str, fallback: str = "") -> str:
    """Pull a short description from the original starter readme."""
    t = text.strip()
    lines = []
    for line in t.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        if s.startswith("```"):
            continue
        if s.lower().startswith("requires python"):
            continue
        if s.lower().startswith("run from the starter"):
            continue
        if re.match(r"^run:?$", s, flags=re.I):
            continue
        if s.lower().startswith("run without"):
            continue
        # Drop pure command lines
        if re.match(r"^python3 main\.py\b", s):
            continue
        # `python3 main.py --flag` does something...
        s = re.sub(r"^`python3 main\.py[^`]*`\s*", "", s).strip()
        # Run `python3 main.py` to do X / Run `python3 main.py` or pass...
        s = re.sub(
            r"^[Rr]un\s+`python3 main\.py[^`]*`(?:\s+or\s+[^.]+\.)?\s*(?:to\s+)?",
            "",
            s,
        ).strip()
        s = re.sub(r"^[Rr]un:\s*", "", s).strip()
        if not s:
            continue
        if s[0].islower():
            s = s[0].upper() + s[1:]
        lines.append(s)

    blurb = " ".join(lines).strip()
    blurb = re.sub(r"\s+", " ", blurb)
    fallback = fallback.strip()
    if not blurb:
        blurb = fallback or f"Runnable lab for {title}."
    elif fallback and len(blurb) < 90 and fallback.lower() not in blurb.lower():
        # Keep a useful flag note, but lead with the day's objective.
        blurb = f"{fallback.rstrip('.')}." + f" {blurb}"
    parts = re.split(r"(?<=[.!?])\s+", blurb)
    return " ".join(parts[:3]).strip()


def starter_readme(d: dict) -> str:
    raw = _unescape_newlines(d.get("starter_readme", "") or "")
    n = d["day"]
    blurb = _extract_blurb(raw, d["title"], fallback=d.get("objective", ""))
    cmds = _extract_commands(raw)
    bash = "\n".join(cmds)
    return f"""# Starter: Day {n:03d}

{blurb}

## Run

```bash
{bash}
```

Requires Python 3.10+ (stdlib only). Creates a `data/` folder next to `main.py` when needed.
"""


def emit(d: dict) -> None:
    n = d["day"]
    day_dir = ROOT / f"day-{n:03d}"
    wb = day_dir / "workbook"
    starter = wb / "starter"
    starter.mkdir(parents=True, exist_ok=True)

    (day_dir / "README.md").write_text(day_readme(d), encoding="utf-8")
    (wb / "exercise.md").write_text(exercise(d), encoding="utf-8")
    (wb / "README.md").write_text(workbook_readme(d), encoding="utf-8")
    (starter / "README.md").write_text(starter_readme(d), encoding="utf-8")

    main_py = d["starter_main_py"]
    if "\\n" in main_py and "\n" not in main_py.strip()[:80]:
        main_py = main_py.encode("utf-8").decode("unicode_escape")
    main_py = (
        main_py.replace("\u2014", " - ")
        .replace("\u2013", "-")
        .replace("\u2026", "...")
    )
    if not main_py.endswith("\n"):
        main_py += "\n"
    (starter / "main.py").write_text(main_py, encoding="utf-8")


def main() -> None:
    days = load_days()
    for d in days:
        emit(d)
    print(f"Emitted {len(days)} days with READMEs + runnable starters")


if __name__ == "__main__":
    main()
