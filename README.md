# 100 Days of DDIA

[![GitHub stars](https://img.shields.io/github/stars/ankan97dutta/ddia-100-days?style=social)](https://github.com/ankan97dutta/ddia-100-days)
[![GitHub forks](https://img.shields.io/github/forks/ankan97dutta/ddia-100-days?style=social)](https://github.com/ankan97dutta/ddia-100-days/fork)

A practical study track for [*Designing Data-Intensive Applications*](https://dataintensive.net/) (2nd edition).

If this helps your study, [star the repo on GitHub](https://github.com/ankan97dutta/ddia-100-days).

**Site (GitHub Pages):** [https://ankan97dutta.github.io/ddia-100-days/](https://ankan97dutta.github.io/ddia-100-days/)

Each day gives you:

1. An original **summary** and **key points** for the topic
2. An original **Mermaid study diagram** (not a book figure)
3. A **runnable Python starter** under `workbook/starter/`
4. Prompts to break something and measure a trade-off

You still need your own legal copy of the book. This repo does not ship DDIA text or figures.

## How a day works

```text
day-001/
├── README.md              # summary, key points, diagram, prompts
└── workbook/
    ├── exercise.md        # your notes and measurements
    └── starter/
        ├── README.md      # how to run
        └── main.py        # runnable lab (Python stdlib)
```

```bash
cd day-001/workbook/starter
python3 main.py --help
python3 main.py
```

Then fill in the workbook and check off [PROGRESS.md](./PROGRESS.md).

Shared habits: [WORKFLOW.md](./WORKFLOW.md) | Chapter map: [CHAPTERS.md](./CHAPTERS.md)

## Tools

Starters are **Python 3 stdlib** (plus `sqlite3` where useful). No pip install required for the default path. You can rewrite any lab in Go/Postgres/Docker if you prefer.

## GitHub Pages

The curriculum site is built with MkDocs Material on every push to `main`.

Preview locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
python3 scripts/build_docs_site.py
python3 scripts/render_mkdocs_config.py
mkdocs serve
```

Then open http://127.0.0.1:8000/

After the first deploy, enable Pages in the repo settings if needed:

**Settings → Pages → Build and deployment → Source: GitHub Actions**

## Regenerating day files

Content lives in `scripts/content/days_*.json`. To rebuild READMEs and starters:

```bash
python3 scripts/emit_curriculum.py
```

## What this is / isn't

| Is | Isn't |
| --- | --- |
| 100-day curriculum with study notes, diagrams, and runnable labs | A replacement for reading DDIA |
| Original summaries/diagrams for learning | Permission to copy book prose or figures |
| Stdlib Python starters you can extend | Production-ready reference implementations |
| A browsable GitHub Pages site | An in-browser Python runner |

## License

Curriculum text, diagrams, and starters: [MIT](./LICENSE.md). The book remains with its copyright holders.
