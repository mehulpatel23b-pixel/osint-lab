"""Thin wrapper around the GitHub Search API."""
import os
import requests

SEARCH_URL = "https://api.github.com/search/repositories"


def search_repos(language=None, days=7, min_stars=10, limit=25):
    """Return repos created in the last `days` days, sorted by stars."""
    from datetime import datetime, timedelta, timezone

    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    q = f"created:>{since} stars:>{min_stars}"
    if language:
        q += f" language:{language}"

    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repos, page = [], 1
    while len(repos) < limit:
        resp = requests.get(
            SEARCH_URL,
            params={"q": q, "sort": "stars", "order": "desc", "per_page": min(100, limit - len(repos)), "page": page},
            headers=headers,
            timeout=30,
        )
        resp.raise_for_status()
        batch = resp.json().get("items", [])
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos[:limit]


def as_dict(repo):
    """Project the API payload into the fields Repo Radar cares about."""
    return {
        "full_name": repo["full_name"],
        "url": repo["html_url"],
        "description": repo.get("description") or "",
        "stars": repo["stargazers_count"],
        "forks": repo.get("forks_count", 0),
        "language": repo.get("language") or "-",
        "created_at": repo.get("created_at", ""),
    }
