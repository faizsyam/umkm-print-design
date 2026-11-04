#!/usr/bin/env python3
"""Package a skill folder (SKILL.md + references/) into a .skill file.

Usage:
    python build_skill.py [skill_folder] [output_file]

Defaults:
    skill_folder = ./jago-desain-apa-aja
    output_file  = ./<folder name>.skill
"""
import sys
import zipfile
from pathlib import Path


def build(folder: Path, output: Path) -> None:
    folder = folder.resolve()
    if not (folder / "SKILL.md").is_file():
        sys.exit(f"Error: {folder / 'SKILL.md'} not found")

    files = sorted(p for p in folder.rglob("*")
                   if p.is_file() and not p.name.startswith(".") and p.name != ".DS_Store")

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            # keep the top-level folder name inside the archive: jago-desain-apa-aja/SKILL.md
            z.write(p, Path(folder.name, p.relative_to(folder)).as_posix())

    print(f"Created {output} ({output.stat().st_size / 1024:.1f} KB, {len(files)} files)")


if __name__ == "__main__":
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("jago-desain-apa-aja")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(f"{src.resolve().name}.skill")
    build(src, out)
