# Curriculum build

Source of truth for day content (summaries, key points, diagrams, starters):

- `content/days_001_025.json`
- `content/days_026_050.json`
- `content/days_051_075.json`
- `content/days_076_100.json`

Rebuild all day folders:

```bash
python3 scripts/emit_curriculum.py
```

Summaries and Mermaid diagrams are original study aids for this repo, not reproductions of DDIA book figures or prose.

## GitHub Pages site

```bash
pip install -r requirements-docs.txt
python3 scripts/build_docs_site.py
python3 scripts/render_mkdocs_config.py
mkdocs serve   # local
mkdocs build   # CI produces site/
```
