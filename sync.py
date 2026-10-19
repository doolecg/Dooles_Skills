"""Refresh this marketplace from where the skills are actually edited.

    python sync.py              copy my own skills in from their home folders (SOURCES + themes.json)
    python sync.py --upstream   also pin the third-party plugins to their repos' latest commit
    python sync.py --dry-run    show what would change

My own skills live next to the projects they belong to (and are often git-ignored there), so
this repo is also their backup. Third-party skills aren't copied: marketplace.json points at
their original repos, pinned to a commit.
"""
import argparse
import filecmp
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPOS = Path("F:/PROGRAMMING/REPOS")
HOME = Path.home()

# plugin -> [(source folder, skill name in the plugin)]
SOURCES = {
    # voxel-icons, minecraft-test-setup and the core and ui-design skills now live in this repo and are edited here: ~/.claude/skills links to them.
    "games": [
        (HOME / ".claude/skills/Minecraft Mod Dev", "minecraft-mod-dev"),
    ],
}
JUNK = shutil.ignore_patterns(
    "__pycache__", "*.pyc", ".DS_Store", "Thumbs.db", "node_modules", ".git", ".venv",
    ".env", ".env.*", "credentials.json", "token.json", "client_secret*.json",
)
# skills that come from the pinned third-party plugins in marketplace.json
EXTERNAL = {"fabric-modding", "neoforge-modding", "minecraft-26-1-migration", "minecraft-multiloader"}
# skills edited in this repo itself; ~/.claude/skills holds links to them, so they are never copied in
REPO_OWNED = {"team-work", "ui-change", "minecraft-test-setup", "desktop-app-baseline", "repo-release", "plain-writing",
              "ui-critique", "ui-foundations", "voxel-icons",
              "aspnet-efcore-postgres", "docker-compose-dev", "pixijs-v8-isometric", "isometric-pixel-art"}
SKILL_ROOTS = [HOME / ".claude/skills", HOME / ".agents/skills"]  # first one wins on a duplicate name


def differs(a: Path, b: Path) -> bool:
    if not b.exists():
        return True
    c = filecmp.dircmp(a, b, ignore=["__pycache__"])
    stack = [c]
    while stack:
        d = stack.pop()
        if d.left_only or d.right_only or d.diff_files or d.funny_files:
            return True
        stack.extend(d.subdirs.values())
    return False


def sync_own(dry: bool) -> int:
    changed = 0
    for plugin, skills in SOURCES.items():
        for src, name in skills:
            dest = ROOT / "plugins" / plugin / "skills" / name
            if not (src / "SKILL.md").exists():
                print(f"  skip  {plugin}/{name}: no SKILL.md at {src}")
                continue
            if not differs(src, dest):
                continue
            changed += 1
            print(f"  {'would update' if dry else 'update'}  {plugin}/{name}  <-  {src}")
            if not dry:
                shutil.rmtree(dest, ignore_errors=True)
                shutil.copytree(src, dest, ignore=JUNK)
    return changed


def find_skills() -> dict[str, Path]:
    """Every skill folder in the source roots, one level of category folders included."""
    found: dict[str, Path] = {}
    for root in SKILL_ROOTS:
        if not root.is_dir():
            continue
        for p in sorted(root.iterdir()):
            if not p.is_dir():
                continue
            if (p / "SKILL.md").exists():
                found.setdefault(p.name, p)
                continue
            for q in sorted(p.iterdir()):
                if q.is_dir() and (q / "SKILL.md").exists():
                    found.setdefault(q.name, q)
    return found


def sync_themes(dry: bool) -> int:
    themes = json.loads((ROOT / "themes.json").read_text(encoding="utf8"))
    found = find_skills()
    provided = {name for skills in SOURCES.values() for _, name in skills}
    assigned: set[str] = set()
    changed = 0
    for plugin, info in themes.items():
        for name in info["skills"]:
            assigned.add(name)
            src = found.get(name)
            if src is None:
                print(f"  skip  {plugin}/{name}: not found in {', '.join(str(r) for r in SKILL_ROOTS)}")
                continue
            dest = ROOT / "plugins" / plugin / "skills" / name
            if not differs(src, dest):
                continue
            changed += 1
            print(f"  {'would update' if dry else 'update'}  {plugin}/{name}  <-  {src}")
            if not dry:
                shutil.rmtree(dest, ignore_errors=True)
                shutil.copytree(src, dest, ignore=JUNK)
    new = sorted(set(found) - assigned - provided - EXTERNAL - REPO_OWNED)
    if new:
        print(f"  {len(new)} skill(s) in the sources but in no plugin (add to themes.json): {', '.join(new)}")
    return changed


def sync_upstream(dry: bool) -> int:
    path = ROOT / ".claude-plugin/marketplace.json"
    market = json.loads(path.read_text(encoding="utf8"))
    changed = 0
    for p in market["plugins"]:
        src = p.get("source")
        if not isinstance(src, dict) or "url" not in src:
            continue
        out = subprocess.run(["git", "ls-remote", src["url"], src.get("ref", "HEAD")],
                             capture_output=True, text=True, check=True).stdout.split()
        if out and out[0] != src.get("sha"):
            changed += 1
            print(f"  {'would pin' if dry else 'pin'}  {p['name']}  {src.get('sha', '')[:8]} -> {out[0][:8]}")
            src["sha"] = out[0]
    if changed and not dry:
        path.write_text(json.dumps(market, indent=2, ensure_ascii=False) + "\n", encoding="utf8")
    return changed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    n = sync_own(a.dry_run)
    n += sync_themes(a.dry_run)
    if a.upstream:
        n += sync_upstream(a.dry_run)
    print(f"{n} change(s)" + (" (dry run)" if a.dry_run else ""))
    if n and not a.dry_run:
        print("Now: claude plugin validate . && git add -A && git commit && git push")


if __name__ == "__main__":
    sys.exit(main())
