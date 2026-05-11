"""Phase 1 crawler: fetch bug-labeled issues from a seed list of Android repos.

Reads `seed_repos.jsonl` (one repo per line: {owner, repo, source}) and for
each repo pulls issues that match bug-ish labels, open OR closed. Writes one
JSONL record per issue to `raw_bugs.jsonl`.

Key design choices:
  - Use GitHub REST API `/search/issues` for server-side label + type filtering
    (search API has 30 req/min limit — we pace to 25 req/min to stay safe)
  - Alternately fall back to per-repo `/repos/{owner}/{repo}/issues` with
    `labels=bug,crash,defect` if search finds zero
  - Skip pull requests (only actual issues)
  - Skip locked/archived repos automatically (via GitHub's error codes)
  - Resume-friendly — re-runs skip repos whose issues have already been
    captured up to `per_repo_target`
  - Default target is 10 bugs per repo (116 repos * 10 = 1160, aiming for 1000)

Usage:
    # Default: ~1000 bugs from all 116 repos
    python3 helpful_scripts/gesture_prevalence/crawl_android_bugs.py

    # Adjust target per repo
    python3 helpful_scripts/gesture_prevalence/crawl_android_bugs.py --per-repo 15

    # Limit overall
    python3 helpful_scripts/gesture_prevalence/crawl_android_bugs.py --max-bugs 1000

Output record shape:
    {
      "owner": "...", "repo": "...", "issue_number": int,
      "url": "https://github.com/.../issues/N",
      "title": "...", "body": "...",
      "labels": ["bug", ...],
      "state": "open"|"closed",
      "created_at": "...", "closed_at": "..."|null,
      "comments_count": int,
      "source_tags": ["carbon", "rebl", "fdroid_popular"],
    }
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SEED_PATH = HERE / "seed_repos.jsonl"
OUT_PATH = HERE / "raw_bugs.jsonl"
PROGRESS_PATH = HERE / ".crawl_progress.json"

# Load token from BugCrawler/.env (existing convention in this repo)
load_dotenv(ROOT / "BugCrawler" / ".env")
load_dotenv(ROOT / ".env")  # also try root

GH_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
if not GH_TOKEN:
    print("ERROR: GITHUB_TOKEN not set. Check BugCrawler/.env or ~/.env", file=sys.stderr)
    sys.exit(2)

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "CARBON-gesture-prevalence-study",
}

BUG_LABEL_CANDIDATES = [
    "bug", "crash", "defect", "type: bug", "type:bug",
    "kind/bug", "bug-report", "Bug", "Crash", "Defect",
]


def _wait_for_rate_reset(resp: requests.Response) -> None:
    """Sleep until the GitHub rate-limit window resets if we got a 403/429."""
    reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
    remaining = int(resp.headers.get("X-RateLimit-Remaining", 0))
    now = int(time.time())
    wait = max(0, reset - now) + 5
    print(f"  [rate-limit] remaining={remaining}, sleeping {wait}s until {datetime.fromtimestamp(reset)}", file=sys.stderr)
    time.sleep(wait)


def gh_get(url: str, params: dict | None = None, max_retries: int = 3) -> dict | list | None:
    """GitHub GET with rate-limit awareness + backoff."""
    for attempt in range(max_retries):
        resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (403, 429):
            # Check secondary rate limit
            if "rate limit" in resp.text.lower():
                _wait_for_rate_reset(resp)
                continue
            # Secondary abuse-detection delay — honor Retry-After
            retry_after = int(resp.headers.get("Retry-After", 30))
            print(f"  [retry-after] sleeping {retry_after}s", file=sys.stderr)
            time.sleep(retry_after)
            continue
        if resp.status_code == 404:
            return None  # repo missing / renamed / private
        if resp.status_code == 410:
            return None  # issues disabled
        print(f"  HTTP {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
        time.sleep(2 ** attempt)
    return None


def fetch_bugs_for_repo(owner: str, repo: str, per_repo_target: int) -> list[dict]:
    """Pull up to `per_repo_target` bug-labeled issues from one repo.

    Strategy: try each bug-label candidate in order; stop once we've collected
    enough. Mixes open + closed (sorted by most recently updated first for
    relevance).
    """
    collected: dict[int, dict] = {}  # issue_number -> raw issue dict

    for label in BUG_LABEL_CANDIDATES:
        if len(collected) >= per_repo_target:
            break
        page = 1
        while len(collected) < per_repo_target and page <= 5:
            url = f"https://api.github.com/repos/{owner}/{repo}/issues"
            data = gh_get(url, {
                "state": "all",
                "labels": label,
                "per_page": min(100, per_repo_target - len(collected) + 5),
                "page": page,
                "sort": "updated",
                "direction": "desc",
            })
            if not data:  # None or empty list
                break
            if not isinstance(data, list):
                break
            new_in_page = 0
            for item in data:
                # Skip PRs
                if item.get("pull_request") is not None:
                    continue
                num = item.get("number")
                if num and num not in collected:
                    collected[num] = item
                    new_in_page += 1
            if new_in_page == 0:
                break
            page += 1
            time.sleep(0.2)  # gentle pacing — core API is 5000/hr

    return list(collected.values())[:per_repo_target]


def issue_to_record(owner: str, repo: str, issue: dict, source_tags: list[str]) -> dict:
    return {
        "owner": owner,
        "repo": repo,
        "issue_number": issue["number"],
        "url": issue["html_url"],
        "title": issue.get("title", "") or "",
        "body": (issue.get("body") or "")[:20000],  # cap at 20k chars
        "labels": [l["name"] for l in issue.get("labels", [])],
        "state": issue.get("state", "unknown"),
        "created_at": issue.get("created_at"),
        "closed_at": issue.get("closed_at"),
        "comments_count": issue.get("comments", 0),
        "source_tags": source_tags,
    }


def load_progress() -> dict:
    if PROGRESS_PATH.exists():
        try:
            return json.loads(PROGRESS_PATH.read_text())
        except json.JSONDecodeError:
            pass
    return {"done_repos": []}


def save_progress(state: dict) -> None:
    PROGRESS_PATH.write_text(json.dumps(state, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-repo", type=int, default=10, help="Issues per repo")
    ap.add_argument("--max-bugs", type=int, default=1000, help="Global cap")
    ap.add_argument("--fresh", action="store_true", help="Ignore progress, restart")
    args = ap.parse_args()

    if args.fresh and OUT_PATH.exists():
        OUT_PATH.unlink()
    if args.fresh and PROGRESS_PATH.exists():
        PROGRESS_PATH.unlink()

    progress = load_progress()
    done_set = set(map(tuple, progress.get("done_repos", [])))

    # Count existing bugs so we can resume precisely
    total_bugs = 0
    if OUT_PATH.exists():
        with OUT_PATH.open() as f:
            for _ in f:
                total_bugs += 1
        print(f"[resume] found {total_bugs} already-crawled bugs in raw_bugs.jsonl")

    repos = []
    with SEED_PATH.open() as f:
        for line in f:
            r = json.loads(line)
            repos.append(r)
    print(f"[start] {len(repos)} seed repos, target ~{args.max_bugs} bugs")

    with OUT_PATH.open("a") as out:
        for i, r in enumerate(repos, 1):
            key = (r["owner"], r["repo"])
            if key in done_set:
                continue
            if total_bugs >= args.max_bugs:
                print(f"[stop] reached max-bugs={args.max_bugs}")
                break

            print(f"[{i:3d}/{len(repos)}] {r['owner']}/{r['repo']:<30s} ", end="", flush=True)
            try:
                issues = fetch_bugs_for_repo(r["owner"], r["repo"], args.per_repo)
            except Exception as e:
                print(f"ERROR {e}")
                continue

            remaining = args.max_bugs - total_bugs
            if len(issues) > remaining:
                issues = issues[:remaining]

            wrote = 0
            for issue in issues:
                rec = issue_to_record(r["owner"], r["repo"], issue, r.get("source", []))
                out.write(json.dumps(rec) + "\n")
                wrote += 1
            out.flush()

            total_bugs += wrote
            print(f"+{wrote:3d}  (total {total_bugs})")

            done_set.add(key)
            progress["done_repos"] = [list(k) for k in done_set]
            save_progress(progress)

    print(f"\n[done] wrote {total_bugs} bugs to {OUT_PATH}")


if __name__ == "__main__":
    main()
