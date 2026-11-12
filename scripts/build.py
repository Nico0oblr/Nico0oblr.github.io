#!/usr/bin/env python3
"""Render Quarto, then stage generated files for the existing root-based Pages site."""
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "_site"
MANIFEST = ROOT / "scripts" / "generated-files.json"
PROTECTED = {"site", "scripts", ".github", ".git", "README.md", "AGENTS.md", "LICENSE", ".gitignore"}


def safe_target(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] in PROTECTED:
        raise ValueError(f"Unsafe generated path: {relative}")
    return ROOT / path


subprocess.run(["quarto", "render", "site"], cwd=ROOT, check=True)
current = sorted(str(p.relative_to(OUTPUT)) for p in OUTPUT.rglob("*") if p.is_file())
previous = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else []
for name in current:
    source, target = OUTPUT / name, safe_target(name)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
for name in sorted(set(previous) - set(current)):
    safe_target(name).unlink(missing_ok=True)
(ROOT / ".nojekyll").touch()
MANIFEST.write_text(json.dumps(current, indent=2) + "\n")
print(f"Staged {len(current)} generated files for GitHub Pages.")
