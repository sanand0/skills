"""Package the tracked skills and their supporting files for ChatGPT."""

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

import yaml

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--new-version", action="store_true", help="Increment only the minor version")
options = parser.parse_args()
version_path = root / "plugin.version"
version = version_path.read_text().strip()
parts = re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version)
if not parts:
    parser.error(f"{version_path.name} must contain a version such as 0.1.0")
if options.new_version:
    major, minor, patch = parts.groups()
    next_version = f"{major}.{int(minor) + 1}.{patch}"
    with NamedTemporaryFile(mode="w", dir=root, delete_on_close=False) as temporary:
        temporary.write(next_version + "\n")
        temporary.close()
        Path(temporary.name).replace(version_path)
    print(f"Bumped plugin version from {version} to {next_version}")
    raise SystemExit(0)

tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).split(b"\0")
paths = sorted({Path(os.fsdecode(path)) for path in tracked if path})
skills = {path.parent for path in paths if len(path.parts) == 2 and path.name == "SKILL.md"}
if not skills:
    raise ValueError("No tracked skills found")

manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
del manifest["skills"]
manifest.update(
    {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "version": version,
        "repository": "https://github.com/sanand0/skills",
        "license": "MIT",
        "extensions": {"com.openai": {"interface": {"displayName": "Anand Skills"}}},
    }
)

with NamedTemporaryFile(dir=root, suffix=".zip", delete_on_close=False) as temporary:
    with ZipFile(temporary, "w", compression=ZIP_DEFLATED) as archive:
        archive.writestr("plugin.json", json.dumps(manifest, indent=2) + "\n")
        archive.writestr("LICENSE", (root / "LICENSE").read_bytes())
        for path in paths:
            directory = Path(path.parts[0])
            if directory not in skills:
                continue
            source = root / path
            if source.resolve() != source or not source.is_file():
                raise ValueError(f"Expected a regular skill file: {path}")
            content = source.read_bytes()
            if path == directory / "SKILL.md":
                frontmatter = content.decode().split("---\n", 2)
                if len(frontmatter) != 3 or frontmatter[0] or not frontmatter[1].endswith("\n"):
                    raise ValueError(f"Missing skill frontmatter: {path}")
                metadata = yaml.safe_load(frontmatter[1])
                if not isinstance(metadata, dict) or metadata.get("name") != directory.name:
                    raise ValueError(f"Invalid skill frontmatter or name: {path}")
                description = metadata.get("description")
                if not isinstance(description, str) or not description.strip() or len(content) > 1024**2:
                    raise ValueError(f"Invalid skill description or file size: {path}")
            archive.writestr(f"skills/{path.as_posix()}", content)
    output = root / f"{manifest['name']}.zip"
    Path(temporary.name).replace(output)

print(f"Built {output.name} with {len(skills)} skills")
