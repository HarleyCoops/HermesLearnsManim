---
name: hermes-learns-manim
description: Use Hermes subagents to build reverse-knowledge-tree Manim animations while the MCP server manages artifacts, validation, and rendering. Optimized for cinematic 3D scenes and current-events topics.
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

Use this skill when the user wants a mathematical, scientific, or newsworthy concept turned into a Manim animation.

Hermes is the only agent harness for this workflow.
Do not introduce another agent SDK.

## Required routine

1. Call `initialize_run_workspace` with the user's request.
2. If the topic is a current event, run the `news-researcher` subagent first to ground the narrative in verified facts and canonical citations.
3. Use Hermes subagents to rebuild the reasoning tree and downstream artifacts.
4. Save every artifact back through MCP tools (`save_text_artifact`, `save_json_artifact`) so the workspace stays canonical.
5. Validate (`validate_manim_scene`, `estimate_scene_complexity`, `validate_latex_block`) before rendering.
6. Render only if the user explicitly wants video output, and start at quality `l` for iteration.

## Recommended subagent split

Delegate only when it helps materially. Default split:

- `news-researcher` (optional): gather verified facts and citations for newsworthy topics; write `research.md`
- `concept-analyst`: fill `analysis.json`
- `prerequisite-explorer`: build `knowledge_tree.json`
- `math-enricher`: tighten equations, definitions, and numerical values inside the tree or notes
- `narrative-composer`: write `narrative.md` as a scene-by-scene cinematic plan
- `code-generator`: produce `scene.py` and call validators before handing back

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

Additional artifacts the coordinator may write:

- `research.md` — for current-events topics (facts, dates, numbers, sources)
- `validation.json` — merged output of the validators

Keep all of these in sync as the workflow progresses.

## Cinematic 3D defaults

When the user asks for a "3D", "cinematic", "best-in-class", or current-events animation, the code-generator should default to:

- `ThreeDScene` with `set_camera_orientation(phi=65-75°, theta=-45° to -55°)`
- Dark space background (e.g. `#050510`) with a `Dot` starfield for depth cues
- Ambient camera rotation at `0.08-0.15 rad/s` during wide shots
- A coherent color language declared at the top of the file (title / accent / data / warning)
- `add_fixed_in_frame_mobjects` for all titles, equations, captions
- Labeled, color-coded key terms (`MathTex` parts) so the viewer can follow symbolically
- A 3-to-6 act structure: hook → concept → math → key insight → counterfactual → payoff
- Raw strings (`r"..."`) for every `MathTex` and `Tex` literal
- Self-contained: no `ImageMobject` or external asset loads

## Validation gate

Before rendering:

1. `validate_manim_scene` on the full `scene.py` source
2. `estimate_scene_complexity` — if `complexity == "high"`, confirm the user still wants to render
3. `validate_latex_block` on any equation the narrative marks as load-bearing

Fix issues in `scene.py` and re-save through MCP before rendering.

## Current-events protocol

For news-driven topics the coordinator MUST:

- Anchor the animation in verifiable facts (dates, distances, speeds, crew names)
- Record sources in `research.md` with URLs and a last-checked timestamp
- Use honest numbers on screen (e.g. `252{,}756\ \text{mi}`) and preserve units
- Never invent quotes, statements, or unconfirmed mission outcomes

## Provider note

Hermes handles login and provider selection with `hermes setup` and `hermes model`.
This skill is provider-agnostic.

## References

- `references/mcp-config.yaml`
- `references/subagents.md`
