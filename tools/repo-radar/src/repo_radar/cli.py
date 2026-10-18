"""Command line interface."""
import argparse
import sys

from .github_api import search_repos, as_dict
from .ranking import rank
from .report import markdown_report


def main(argv=None):
    parser = argparse.ArgumentParser(prog="repo-radar", description="Discover viral GitHub repositories.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_trend = sub.add_parser("trending", help="Print a ranked list of viral repos")
    p_trend.add_argument("--lang", default=None, help="Filter by language (e.g. python)")
    p_trend.add_argument("--days", type=int, default=7, help="Look back N days (default 7)")
    p_trend.add_argument("--min-stars", type=int, default=10, help="Minimum stars (default 10)")
    p_trend.add_argument("--limit", type=int, default=25, help="Max repos (default 25)")

    p_report = sub.add_parser("report", help="Generate a markdown report of viral repos")
    p_report.add_argument("--lang", default=None, help="Filter by language")
    p_report.add_argument("--days", type=int, default=7, help="Look back N days")
    p_report.add_argument("--limit", type=int, default=25, help="Max repos")
    p_report.add_argument("--min-stars", type=int, default=10, help="Minimum stars")
    p_report.add_argument("-o", "--output", default=None, help="Write to file instead of stdout")

    args = parser.parse_args(argv)

    try:
        repos = [as_dict(r) for r in search_repos(args.lang, args.days, args.min_stars, args.limit)]
    except Exception as e:  # noqa: BLE001
        print(f"error: {e}", file=sys.stderr)
        return 1

    ranked = rank(repos)
    if not ranked:
        print("no repositories matched", file=sys.stderr)
        return 1

    if args.command == "trending":
        for i, r in enumerate(ranked, 1):
            print(f"{i:>3}. {r['full_name']} — ⭐{r['stars']:,} ({r['language']})")
            if r["description"]:
                print(f"     {r['description'][:100]}")
    else:
        out = markdown_report(ranked, args.lang, args.days)
        if args.output:
            with open(args.output, "w") as f:
                f.write(out + "\n")
            print(f"wrote {args.output}")
        else:
            print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
