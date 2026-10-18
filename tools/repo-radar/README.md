# Repo Radar (bundled tool)

A ready-made example of a finished OSINT-adjacent tool — the worked reference
for [Module 12](../../modules/12-ship-a-tool/).

Repo Radar discovers viral GitHub repositories by ranking brand-new repos by
stars-per-day velocity. It's real, working code with tests, so you can read it,
break it, extend it, or use it as the skeleton for your own capstone tool.

The canonical standalone repo lives at
[repo-radar](https://github.com/mehulpatel23b-pixel/repo-radar) — this is a
bundled copy for learning.

## Run it
```bash
cd tools/repo-radar
pip install -r requirements.txt
PYTHONPATH=src python3 -m repo_radar.cli trending --days 7 --limit 10
```

## Extension ideas for the capstone
- Add a `--output json` option for machine-readable results
- Add a filter for repos with no website (ties into your SiteSeller lead hunting)
- Chart the top repos' star velocity with matplotlib

## Legal scope note
Repo Radar only reads GitHub's public search API. Public data, public API, no scraping around limits.
