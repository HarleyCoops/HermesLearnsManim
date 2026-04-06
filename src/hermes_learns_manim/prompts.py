from __future__ import annotations

import json


def analysis_template() -> dict:
    return {
        "core_concept": "",
        "domain": "",
        "audience": "",
        "difficulty": "beginner|intermediate|advanced",
        "learning_goal": "",
        "visual_priority": "",
    }


def knowledge_tree_template() -> dict:
    return {
        "concept": "",
        "depth": 0,
        "is_foundation": False,
        "prerequisites": [],
        "mathematical_content": None,
        "visual_plan": None,
    }


def narrative_template() -> str:
    return '''# Narrative Outline

## Opening Hook

## Global Style

## Scene Sequence

### Scene 1
- concept:
- goal:
- equations:
- beats:
- visual directions:
- transition in:
- transition out:
- duration:

## Ending Summary
'''


def scene_stub(scene_name: str) -> str:
    return (
        "from manim import *\n\n\n"
        f"class {scene_name}(Scene):\n"
        "    def construct(self) -> None:\n"
        "        title = Text(\"Replace with generated animation\")\n"
        "        self.play(Write(title))\n"
        "        self.wait(1)\n"
    )


def build_workflow_brief(request: str, scene_name: str) -> str:
    return f'''# HermesLearnsManim Workflow

User request:
{request}

Scene name target:
{scene_name}

Hermes is the only agent harness for this workflow.
The model provider is selected inside Hermes with `hermes setup` or `hermes model`.

## Required steps

1. Fill `analysis.json` with a precise teaching brief.
2. Build `knowledge_tree.json` by recursively asking what must be understood before the target concept.
3. Write `narrative.md` as a scene-by-scene teaching plan.
4. Generate `scene.py` using only Manim primitives and self-contained assets.
5. Validate code before render.
6. Render only if the user asked for video output.

## Rules

- Keep the workflow provider-agnostic.
- Do not introduce another agent SDK.
- Use Hermes subagents only when they materially help and keep artifact ownership clear.
- Save each artifact back through MCP tools so the run directory stays complete.
'''


def manifest_template(request: str, scene_name: str) -> dict:
    return {
        "request": request,
        "scene_name": scene_name,
        "status": {
            "analysis": "pending",
            "knowledge_tree": "pending",
            "narrative": "pending",
            "scene_code": "pending",
            "validation": "pending",
            "render": "not_requested",
        },
    }


def pretty_json(payload: dict) -> str:
    return json.dumps(payload, indent=2)
