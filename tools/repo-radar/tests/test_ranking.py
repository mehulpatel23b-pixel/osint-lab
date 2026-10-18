from src.repo_radar.ranking import viral_score, rank


def test_score_new_repo_higher():
    new = {"stars": 100, "created_at": "2026-10-17T00:00:00Z"}
    old = {"stars": 100, "created_at": "2026-10-01T00:00:00Z"}
    assert viral_score(new) > viral_score(old)


def test_rank_orders_desc():
    repos = [
        {"full_name": "slow", "stars": 500, "created_at": "2026-04-01T00:00:00Z"},
        {"full_name": "fast", "stars": 500, "created_at": "2026-10-16T00:00:00Z"},
    ]
    assert [r["full_name"] for r in rank(repos)] == ["fast", "slow"]
