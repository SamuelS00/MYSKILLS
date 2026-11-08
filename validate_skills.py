"""Validate the portable subset of Agent Skills frontmatter without dependencies."""

from pathlib import Path
import re
import sys

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KEY = re.compile(r"^([a-z][a-z0-9-]*):(?:\s+(.*))?$")


def validate(root: Path) -> list[str]:
    errors = []
    if not root.is_dir():
        return [f"{root}: skills directory does not exist"]
    for directory in sorted(root.iterdir()):
        if not directory.is_dir():
            continue
        path = directory / "SKILL.md"
        if not path.is_file():
            errors.append(f"{path}: missing SKILL.md")
            continue
        if not NAME.fullmatch(directory.name) or len(directory.name) > 64:
            errors.append(f"{directory}: invalid skill directory name")
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---":
            errors.append(f"{path}: YAML frontmatter must start on the first line")
            continue
        try:
            end = lines.index("---", 1)
        except ValueError:
            errors.append(f"{path}: missing closing frontmatter delimiter")
            continue
        fields = {}
        for number, line in enumerate(lines[1:end], 2):
            match = KEY.fullmatch(line)
            if not match:
                errors.append(f"{path}:{number}: unsupported YAML syntax; use simple key: value fields")
                continue
            key, value = match.groups()
            if key in fields:
                errors.append(f"{path}:{number}: duplicate field '{key}'")
            fields[key] = (value or "").strip().strip("\"'")
        if fields.get("name") != directory.name:
            errors.append(f"{path}: name must match directory '{directory.name}'")
        description = fields.get("description", "")
        if not 1 <= len(description) <= 1024:
            errors.append(f"{path}: description must contain 1-1024 characters")
        if not any(line.strip() for line in lines[end + 1:]):
            errors.append(f"{path}: instructions are empty")
    return errors


if __name__ == "__main__":
    problems = validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "skills")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("Skills valid.")
