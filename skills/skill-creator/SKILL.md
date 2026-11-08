---
name: skill-creator
description: Create or improve reusable Agent Skills when a user needs a repeatable agent workflow, with clear scope, validation, and test scenarios.
---

# Skill creator

Use this skill when creating or revising a reusable Agent Skill. Do not use it for a one-off prompt or a task already covered by an existing skill.

1. Identify the user's objective, intended users, environment, inputs, outputs, and constraints.
2. Search the repository and available installed skills for an equivalent workflow. Extend an existing skill when its scope fits.
3. Define the skill's responsibility, trigger conditions, and explicit boundaries before writing files.
4. Create `skills/<name>/SKILL.md` using the [Agent Skills specification](https://agentskills.io/specification). Use a lowercase kebab-case directory and matching `name`; write a specific `description` that explains when to select it.
5. Write concise, executable steps. Keep platform-specific instructions conditional and avoid provider or model assumptions.
6. Put optional detailed material in `references/`, and read it only when needed. Add `scripts/` only for automation that improves reliability or repeatability. Never create empty directories.
7. Run `python3 validate_skills.py` and fix reported errors. Review the instructions manually for clarity, scope, and broken references.
8. Propose or run representative positive, negative, and boundary scenarios. Check whether the agent selects the skill at the right time and follows its steps correctly.
9. Revise the skill from the scenario results, rerun validation, and summarize changes and remaining limitations.
