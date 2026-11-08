# Repository agent instructions

- Treat `skills/` as the single source of truth for skill content.
- Follow the open Agent Skills specification for every `SKILL.md`.
- Use lowercase kebab-case directory names; the frontmatter `name` must match the directory.
- Write agent-facing instructions, skill descriptions, references, and code documentation in English.
- Keep each skill focused, concise, executable, and independent of a particular model or provider where possible.
- Use `references/` for details loaded on demand and `scripts/` only for useful automation. Do not create empty directories or duplicate skill content.
- Inspect existing files before editing. Limit changes to the requested scope and preserve unrelated work.
- Run `python3 validate_skills.py` and relevant tests after changing skills or validation code.
- After completing requested changes, create a Conventional Commit and push it to the configured remote. Do not commit unrelated work.
