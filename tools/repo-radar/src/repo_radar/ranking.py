"""Viral score — how fast is a repo actually growing?"""
from datetime import datetime, timezone


def viral_score(repo):
    """stars per day since creation. Higher = more viral."""
    try:
        created = datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        age_days = max((datetime.now(timezone.utc) - created).total_seconds() / 86400.0, 1.0)
    except (KeyError, ValueError):
        age_days = 1.0
    return repo["stars"] / age_days


def rank(repos):
    """Sort a list of repo dicts by viral score, descending."""
    return sorted(repos, key=viral_score, reverse=True)
