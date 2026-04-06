---
name: hermes-learns-manim
description: Use Hermes subagents to build reverse-knowledge-tree Manim animations while the MCP server manages artifacts, validation, and rendering.
license: MIT
metadata:
  owner: Harley Coops
  category: animation
  tags:
    - manim
    - mathematics
    - education
    - mcp
    - hermes
---

# Hermes Learns Manim

Use this skill when the user wants a mathematical or scientific concept turned into a Manim animation.

Hermes is the only agent harness for this workflow.
Do not introduce another agent SDK.

## Required routine

1. Call `initialize_run_workspace`.
2. Use Hermes subagents to rebuild the reasoning tree and downstream artifacts.
3. Save artifacts back through MCP tools.
4. Validate before rendering.
5. Render only if the user explicitly wants video output.

## Recommended subagent split

Use subagents only when they help materially. A good default split is:

- `concept-analyst`: fill `analysis.json`
- `prerequisite-explorer`: build `knowledge_tree.json`
- `math-enricher`: improve equations and definitions inside the tree or notes
- `narrative-composer`: write `narrative.md`
- `code-generator`: produce `scene.py`

Keep artifact ownership clear so subagents do not overwrite each other casually.

## Artifact contract

The MCP workspace seeds these files:

- `request.md`
- `workflow.md`
- `analysis.json`
- `knowledge_tree.json`
- `narrative.md`
- `scene.py`
- `run_manifest.json`

You should keep them in sync as the workflow progresses.

## Validation routine

Before rendering:

- call `validate_manim_scene`
- call `estimate_scene_complexity`
- fix obvious issues in `scene.py`

If equations are dense or suspect, also call `validate_latex_block` on the most important strings.

## Provider note

Hermes handles login and provider selection with `hermes setup` and `hermes model`.
This skill is provider-agnostic.

## References

- `references/mcp-config.yaml`
- `references/subagents.md`
