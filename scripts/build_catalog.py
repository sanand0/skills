"""Build the skills catalog from SKILL.md frontmatter."""

from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
skills = []
for path in root.glob("*/SKILL.md"):
    content = path.read_text()
    if not content.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {path}")
    frontmatter = yaml.safe_load(content.split("---\n", 2)[1])
    name = frontmatter["name"]
    description = frontmatter["description"]
    if not isinstance(name, str) or not isinstance(description, str):
        raise ValueError(f"Invalid skill metadata: {path}")
    skills.append((name, description.strip().replace("\n", " "), path.parent.name))

names = [name for name, _, _ in skills]
if len(names) != len(set(names)):
    raise ValueError("Duplicate skill names")

header = """# Anand's Skills

Choose skills by their descriptions; read `./{name}/SKILL.md` when relevant.

"""
rows = [f"- {name}: {description}" for name, description, directory in sorted(skills)]
output = header + "\n".join(rows) + "\n"
path = root / "README.md"
if not path.exists() or path.read_text() != output:
    path.write_text(output)
print(f"Updated README.md catalog ({len(skills)} skills)")
