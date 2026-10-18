# Module 11 — Relationship & Network Mapping (Advanced)

Mapping connections in public data. Targets: open-source projects (great
practice — commit data is public by design) and companies.

## Concepts
- Graph thinking: nodes (accounts), edges (shared projects, co-authorship)
- GitHub's public API as a rich, fully legal dataset
- Visualizing networks with Python (networkx) or Gephi

## Exercise
1. Pick any open-source project you like (yours works too).
2. Pull its contributors and their co-commit patterns:
```python
import requests
r = requests.get("https://api.github.com/repos/{owner}/{repo}/contributors?per_page=100").json()
for c in r: print(c["login"], c["contributions"])
```
3. Build a graph: edge between two contributors who touched the same project. Which people are the hidden connectors?
4. Repeat for your own account — map your own network across your repos.
5. Bonus: apply the same analysis to a company's org on GitHub — who is actually doing the work?

**Done when:** you can produce a network diagram and name the key connectors in it.
