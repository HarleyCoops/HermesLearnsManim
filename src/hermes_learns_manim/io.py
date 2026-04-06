from __future__ import annotations

import json
import re
from pathlib import Path

from .models import KnowledgeNode, NarrativeOutline, PipelineRun


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "run"


def ensure_run_dir(output_root: Path, concept: str, created_at: str) -> Path:
    stamp = created_at.replace(":", "").replace("+00:00", "z").replace("-", "")
    run_dir = output_root / f"{slugify(concept)}-{stamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def tree_to_markdown(tree: KnowledgeNode) -> str:
    lines: list[str] = []

    def visit(node: KnowledgeNode, indent: int) -> None:
        prefix = "  " * indent
        foundation = " [foundation]" if node.is_foundation else ""
        lines.append(f"{prefix}- {node.concept}{foundation}")
        for child in node.prerequisites:
            visit(child, indent + 1)

    visit(tree, 0)
    return "\n".join(lines)


def narrative_to_markdown(narrative: NarrativeOutline) -> str:
    lines = [
        f"# {narrative.title}",
        "",
        "## Opening Hook",
        narrative.opening_hook,
        "",
        "## Global Style",
        narrative.global_style,
        "",
        "## Scene Sequence",
    ]
    for index, scene in enumerate(narrative.scene_sequence, start=1):
        lines.extend(
            [
                "",
                f"### Scene {index}: {scene.title}",
                f"Concept: {scene.concept}",
                f"Goal: {scene.learning_goal}",
                f"Duration: {scene.duration_seconds}s",
                "",
                "Beats:",
            ]
        )
        lines.extend([f"- {beat}" for beat in scene.beat_outline] or ["- None"])
        lines.extend(["", "Visual Directions:"])
        lines.extend(
            [f"- {direction}" for direction in scene.visual_directions] or ["- None"]
        )
        if scene.equations:
            lines.extend(["", "Equations:"])
            lines.extend([f"- `{equation}`" for equation in scene.equations])
        if scene.transition_in:
            lines.extend(["", f"Transition In: {scene.transition_in}"])
        if scene.transition_out:
            lines.extend(["", f"Transition Out: {scene.transition_out}"])
    lines.extend(["", "## Ending Summary", narrative.ending_summary])
    return "\n".join(lines)


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def save_run(run: PipelineRun, output_root: Path) -> Path:
    run_dir = ensure_run_dir(output_root, run.analysis.core_concept, run.created_at)

    write_json(run_dir / "analysis.json", run.analysis.model_dump(mode="json"))
    write_json(run_dir / "knowledge_tree.json", run.knowledge_tree.model_dump(mode="json"))
    write_text(run_dir / "knowledge_tree.md", tree_to_markdown(run.knowledge_tree))
    write_json(run_dir / "narrative.json", run.narrative.model_dump(mode="json"))
    write_text(run_dir / "narrative.md", narrative_to_markdown(run.narrative))
    write_json(run_dir / "validation.json", run.validation.model_dump(mode="json"))
    write_text(run_dir / "scene.py", run.code.python_code)
    write_json(run_dir / "run.json", run.model_dump(mode="json"))

    if run.render is not None:
        write_json(run_dir / "render.json", run.render.model_dump(mode="json"))

    return run_dir
