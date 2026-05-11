"""Build a seed list of Android repos to crawl for bug-prevalence study.

Sources:
  1. CARBON's own 100-bug benchmark (47 unique repos, all Android open-source)
  2. ReBL's 96-bug benchmark (owner+repo entries from rebl_bug_index.json)
  3. A curated short-list of popular F-Droid apps known to have high issue volume

Deduplicates (owner, repo) pairs, filters out UNRESOLVED entries, and writes
one {"owner":..., "repo":...} per line to seed_repos.jsonl.

Usage:
    python3 helpful_scripts/gesture_prevalence/build_seed_repos.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CARBON_DATASET = ROOT / "Dataset"
REBL_INDEX = ROOT / "helpful_scripts" / "rebl_dataset" / "rebl_bug_index.json"
OUT = Path(__file__).parent / "seed_repos.jsonl"

# Popular Android open-source apps with healthy issue volume. These aren't in
# the CARBON/ReBL benchmarks but are representative of real-world Android apps.
# Kept small and well-known so reviewers can verify the selection is unbiased.
FDROID_POPULAR = [
    ("signalapp", "Signal-Android"),
    ("element-hq", "element-android"),
    ("osmandapp", "OsmAnd"),
    ("nextcloud", "android"),
    ("termux", "termux-app"),
    ("mozilla-mobile", "focus-android"),
    ("mozilla-mobile", "fenix"),
    ("Mayura-Andrew", "Standard-Notes"),
    ("streetcomplete", "StreetComplete"),
    ("syncthing", "syncthing-android"),
    ("TeamAmaze", "AmazeFileManager"),
    ("MoneyManagerEx", "android-money-manager-ex"),
    ("zaidka", "genymobile-scrcpy"),
    ("wireguard", "wireguard-android"),
    ("organicmaps", "organicmaps"),
    ("KeePassDX", "KeePassDX"),
    ("bitfireAT", "davx5-ose"),
    ("thundernest", "k-9"),
    ("videolan", "vlc-android"),
    ("Tasks", "tasks"),
]


def collect_carbon_repos() -> set[tuple[str, str]]:
    repos = set()
    for cat in CARBON_DATASET.iterdir():
        if not cat.is_dir():
            continue
        for bug in cat.iterdir():
            if not bug.is_dir():
                continue
            br = bug / "bug_report.txt"
            if not br.exists():
                continue
            m = re.search(r"^App:\s+([^/]+)/(\S+)\s*$", br.read_text(errors="replace"), re.M)
            if m:
                repos.add((m.group(1).strip(), m.group(2).strip()))
    return repos


def collect_rebl_repos() -> set[tuple[str, str]]:
    data = json.loads(REBL_INDEX.read_text())
    repos = set()
    for section in ("crash_bugs", "non_crash_bugs"):
        for entry in data.get(section, {}).values():
            owner = entry.get("owner", "")
            repo = entry.get("repo", "")
            if owner and repo and owner != "UNRESOLVED" and repo != "UNRESOLVED":
                repos.add((owner, repo))
    return repos


def main() -> None:
    carbon = collect_carbon_repos()
    rebl = collect_rebl_repos()
    popular = set(FDROID_POPULAR)

    all_repos = carbon | rebl | popular
    print(f"CARBON benchmark repos:     {len(carbon):3d}")
    print(f"ReBL benchmark repos:       {len(rebl):3d}")
    print(f"F-Droid popular short-list: {len(popular):3d}")
    print(f"De-duplicated total:        {len(all_repos):3d}")

    # Write sorted for stable output
    sorted_repos = sorted(all_repos)
    with OUT.open("w") as f:
        for owner, repo in sorted_repos:
            tags = []
            if (owner, repo) in carbon:
                tags.append("carbon")
            if (owner, repo) in rebl:
                tags.append("rebl")
            if (owner, repo) in popular:
                tags.append("fdroid_popular")
            f.write(json.dumps({"owner": owner, "repo": repo, "source": tags}) + "\n")
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
