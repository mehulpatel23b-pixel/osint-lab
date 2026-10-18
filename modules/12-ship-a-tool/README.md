# Module 12 — Ship a Public OSINT Tool (Capstone)

Turn module 07's prototypes into a real published project — the same standard
as [repo-radar](https://github.com/mehulpatel23b-pixel/repo-radar).

## Your tool must have
- [ ] A focused purpose (one job, done well) — e.g., GSTIN verifier, metadata scrubber with a GUI, domain timeline builder
- [ ] Clean package layout (`src/`, tests, `requirements.txt`)
- [ ] A test suite (`pytest`) covering the core logic
- [ ] A README: badges, install, usage, example output
- [ ] CI: a GitHub Action that runs the tests on every push
- [ ] MIT LICENSE and a `.gitignore`
- [ ] Legal scope statement in the README (what the tool is for, what it won't do)

## CI starter
```yaml
# .github/workflows/tests.yml
name: tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.11"}
      - run: pip install -r requirements.txt pytest
      - run: pytest -q
```

## Level up
- Publish to PyPI so anyone can `pip install` it
- Add a CLI (`argparse`) and a `--help` that actually helps
- Write a demo GIF for the README (asciinema or vhs)

**Done when:** the repo passes its own CI on a fresh clone, and you'd show it to a recruiter without flinching.
