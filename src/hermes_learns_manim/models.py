from __future__ import annotations

from datetime import UTC, datetime
from typing import Literal

from pydantic import BaseModel, Field


Difficulty = Literal["beginner", "intermediate", "advanced"]


class ConceptAnalysis(BaseModel):
    core_concept: str
    domain: str
    audience: str
    difficulty: Difficulty
    learning_goal: str
    visual_priority: str


class FoundationDecision(BaseModel):
    concept: str
    is_foundation: bool
    rationale: str


class PrerequisiteSet(BaseModel):
    concept: str
    rationale: str
    prerequisites: list[str] = Field(default_factory=list)


class MathematicalContent(BaseModel):
    equations: list[str] = Field(default_factory=list)
    definitions: dict[str, str] = Field(default_factory=dict)
    interpretation: str = ""
    examples: list[str] = Field(default_factory=list)
    typical_values: dict[str, str] = Field(default_factory=dict)
    common_mistakes: list[str] = Field(default_factory=list)


class VisualPlan(BaseModel):
    elements: list[str] = Field(default_factory=list)
    colors: dict[str, str] = Field(default_factory=dict)
    animations: list[str] = Field(default_factory=list)
    transitions: list[str] = Field(default_factory=list)
    camera_movement: str = ""
    duration_seconds: int = 12
    layout: str = ""
    global_style: str = ""


class ScenePlan(BaseModel):
    concept: str
    title: str
    learning_goal: str
    equations: list[str] = Field(default_factory=list)
    beat_outline: list[str] = Field(default_factory=list)
    visual_directions: list[str] = Field(default_factory=list)
    transition_in: str = ""
    transition_out: str = ""
    duration_seconds: int = 12


class NarrativeOutline(BaseModel):
    title: str
    opening_hook: str
    global_style: str
    scene_sequence: list[ScenePlan] = Field(default_factory=list)
    ending_summary: str


class ManimCodeArtifact(BaseModel):
    scene_name: str
    python_code: str
    explanation: str = ""


class CodeValidation(BaseModel):
    valid: bool
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)
    complexity: str = "unknown"
    estimated_render_seconds: int = 0


class RenderResult(BaseModel):
    command: list[str] = Field(default_factory=list)
    exit_code: int
    stdout: str = ""
    stderr: str = ""
    video_path: str | None = None


class KnowledgeNode(BaseModel):
    concept: str
    depth: int
    is_foundation: bool
    prerequisites: list["KnowledgeNode"] = Field(default_factory=list)
    mathematical_content: MathematicalContent | None = None
    visual_plan: VisualPlan | None = None

    def walk_foundations_first(self) -> list["KnowledgeNode"]:
        ordered: list[KnowledgeNode] = []
        seen: set[str] = set()

        def visit(node: KnowledgeNode) -> None:
            key = node.concept.casefold()
            if key in seen:
                return
            for prerequisite in node.prerequisites:
                visit(prerequisite)
            seen.add(key)
            ordered.append(node)

        visit(self)
        return ordered


class PipelineRun(BaseModel):
    request: str
    created_at: str = Field(
        default_factory=lambda: datetime.now(UTC).isoformat(timespec="seconds")
    )
    analysis: ConceptAnalysis
    knowledge_tree: KnowledgeNode
    narrative: NarrativeOutline
    code: ManimCodeArtifact
    validation: CodeValidation
    render: RenderResult | None = None
    output_dir: str | None = None


KnowledgeNode.model_rebuild()
