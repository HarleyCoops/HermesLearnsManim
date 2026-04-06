from __future__ import annotations

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from .config import PipelineSettings
from .io import save_run
from .models import (
    CodeValidation,
    ConceptAnalysis,
    FoundationDecision,
    KnowledgeNode,
    ManimCodeArtifact,
    MathematicalContent,
    NarrativeOutline,
    PipelineRun,
    PrerequisiteSet,
    VisualPlan,
)
from .prompts import (
    CODE_GENERATOR_INSTRUCTIONS,
    CONCEPT_ANALYZER_INSTRUCTIONS,
    FOUNDATION_CHECKER_INSTRUCTIONS,
    MATH_ENRICHER_INSTRUCTIONS,
    NARRATIVE_COMPOSER_INSTRUCTIONS,
    PREREQUISITE_EXPLORER_INSTRUCTIONS,
    VISUAL_DESIGNER_INSTRUCTIONS,
    build_narrative_brief,
)
from .renderer import render_scene_file
from .tools import (
    cache_prerequisites,
    estimate_render_complexity,
    estimate_render_complexity_report,
    get_cached_prerequisites,
    normalize_scene_name,
    validate_latex,
    validate_manim_code,
    validate_manim_code_report,
)

load_dotenv()

try:
    from agents import Agent, Runner, SQLiteSession
except ImportError as exc:  # pragma: no cover
    Agent = Runner = SQLiteSession = None
    _AGENTS_IMPORT_ERROR = exc
else:  # pragma: no cover
    _AGENTS_IMPORT_ERROR = None


class MathToManimPipeline:
    def __init__(self, settings: PipelineSettings | None = None) -> None:
        self.settings = settings or PipelineSettings.from_env()
        if Agent is None or Runner is None or SQLiteSession is None:
            raise RuntimeError(
                "openai-agents is required. Install with `pip install openai-agents`."
            ) from _AGENTS_IMPORT_ERROR
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set.")

        model = self.settings.model
        self.analysis_agent = Agent(
            name="ConceptAnalyzer",
            instructions=CONCEPT_ANALYZER_INSTRUCTIONS,
            model=model,
            output_type=ConceptAnalysis,
        )
        self.foundation_agent = Agent(
            name="FoundationChecker",
            instructions=FOUNDATION_CHECKER_INSTRUCTIONS,
            model=model,
            output_type=FoundationDecision,
        )
        self.prerequisite_agent = Agent(
            name="PrerequisiteExplorer",
            instructions=PREREQUISITE_EXPLORER_INSTRUCTIONS,
            model=model,
            tools=[get_cached_prerequisites, cache_prerequisites],
            output_type=PrerequisiteSet,
        )
        self.math_agent = Agent(
            name="MathEnricher",
            instructions=MATH_ENRICHER_INSTRUCTIONS,
            model=model,
            tools=[validate_latex],
            output_type=MathematicalContent,
        )
        self.visual_agent = Agent(
            name="VisualDesigner",
            instructions=VISUAL_DESIGNER_INSTRUCTIONS,
            model=model,
            output_type=VisualPlan,
        )
        self.narrative_agent = Agent(
            name="NarrativeComposer",
            instructions=NARRATIVE_COMPOSER_INSTRUCTIONS,
            model=model,
            output_type=NarrativeOutline,
        )
        self.code_agent = Agent(
            name="ManimCodeGenerator",
            instructions=CODE_GENERATOR_INSTRUCTIONS,
            model=model,
            tools=[validate_manim_code, estimate_render_complexity],
            output_type=ManimCodeArtifact,
        )

    async def run(
        self,
        request: str,
        *,
        output_root: Path | None = None,
        render: bool = False,
        quality: str | None = None,
        session_id: str | None = None,
    ) -> PipelineRun:
        output_root = output_root or self.settings.default_output_root
        quality = quality or self.settings.default_render_quality
        session_base = session_id or self._default_session_id(request)

        analysis = await self._run_analysis(request, session_base)
        tree = await self._build_tree(
            concept=analysis.core_concept,
            domain=analysis.domain,
            audience=analysis.audience,
            depth=0,
            lineage=set(),
            session_base=session_base,
        )
        await self._enrich_tree(tree, analysis, session_base)
        await self._design_tree(tree, analysis, session_base)
        narrative = await self._compose_narrative(tree, analysis, session_base)
        code = await self._generate_code(tree, analysis, narrative, session_base)
        validation = self._validate_code(code.python_code)

        if not validation.valid:
            code = await self._repair_code(
                tree,
                analysis,
                narrative,
                code,
                validation,
                session_base,
            )
            validation = self._validate_code(code.python_code)

        run = PipelineRun(
            request=request,
            analysis=analysis,
            knowledge_tree=tree,
            narrative=narrative,
            code=code,
            validation=validation,
        )
        run_dir = save_run(run, output_root)
        run.output_dir = str(run_dir)

        if render:
            render_result = render_scene_file(
                run_dir / "scene.py",
                run.code.scene_name,
                quality=quality,
            )
            run.render = render_result
            save_run(run, output_root)

        return run

    def run_sync(
        self,
        request: str,
        *,
        output_root: Path | None = None,
        render: bool = False,
        quality: str | None = None,
        session_id: str | None = None,
    ) -> PipelineRun:
        return asyncio.run(
            self.run(
                request,
                output_root=output_root,
                render=render,
                quality=quality,
                session_id=session_id,
            )
        )

    async def _run_analysis(self, request: str, session_base: str) -> ConceptAnalysis:
        session = SQLiteSession(f"{session_base}-analysis")
        result = await Runner.run(
            self.analysis_agent,
            f"User request: {request}",
            session=session,
        )
        return result.final_output

    async def _build_tree(
        self,
        *,
        concept: str,
        domain: str,
        audience: str,
        depth: int,
        lineage: set[str],
        session_base: str,
    ) -> KnowledgeNode:
        normalized = concept.casefold()
        if normalized in lineage:
            return KnowledgeNode(
                concept=concept,
                depth=depth,
                is_foundation=True,
                prerequisites=[],
            )

        foundation = await Runner.run(
            self.foundation_agent,
            (
                f"Concept: {concept}\n"
                f"Domain: {domain}\n"
                f"Audience: {audience}\n"
                f"Depth: {depth}\n"
                f"Max depth: {self.settings.max_depth}"
            ),
            session=SQLiteSession(f"{session_base}-explore"),
        )
        decision: FoundationDecision = foundation.final_output
        if depth >= self.settings.max_depth or decision.is_foundation:
            return KnowledgeNode(
                concept=concept,
                depth=depth,
                is_foundation=True,
                prerequisites=[],
            )

        prereq_result = await Runner.run(
            self.prerequisite_agent,
            (
                f"Concept: {concept}\n"
                f"Domain: {domain}\n"
                f"Audience: {audience}\n"
                "List only the essential prerequisites for understanding this concept in an educational animation."
            ),
            session=SQLiteSession(f"{session_base}-explore"),
        )
        prerequisite_set: PrerequisiteSet = prereq_result.final_output

        limited = prerequisite_set.prerequisites[: self.settings.max_prerequisites_per_node]
        children: list[KnowledgeNode] = []
        next_lineage = set(lineage)
        next_lineage.add(normalized)
        for prerequisite in limited:
            children.append(
                await self._build_tree(
                    concept=prerequisite,
                    domain=domain,
                    audience=audience,
                    depth=depth + 1,
                    lineage=next_lineage,
                    session_base=session_base,
                )
            )

        return KnowledgeNode(
            concept=concept,
            depth=depth,
            is_foundation=False,
            prerequisites=children,
        )

    async def _enrich_tree(
        self,
        tree: KnowledgeNode,
        analysis: ConceptAnalysis,
        session_base: str,
    ) -> None:
        for node in tree.walk_foundations_first():
            result = await Runner.run(
                self.math_agent,
                (
                    f"Concept: {node.concept}\n"
                    f"Domain: {analysis.domain}\n"
                    f"Audience: {analysis.audience}\n"
                    f"Difficulty: {analysis.difficulty}\n"
                    f"Depth: {node.depth}\n"
                    f"Foundation: {node.is_foundation}"
                ),
                session=SQLiteSession(f"{session_base}-math"),
            )
            node.mathematical_content = result.final_output

    async def _design_tree(
        self,
        tree: KnowledgeNode,
        analysis: ConceptAnalysis,
        session_base: str,
    ) -> None:
        ordered_nodes = tree.walk_foundations_first()
        previous_summary = "None"
        for node in ordered_nodes:
            math_content = (
                node.mathematical_content.model_dump_json(indent=2)
                if node.mathematical_content
                else "{}"
            )
            result = await Runner.run(
                self.visual_agent,
                (
                    f"Concept: {node.concept}\n"
                    f"Domain: {analysis.domain}\n"
                    f"Audience: {analysis.audience}\n"
                    f"Learning goal: {analysis.learning_goal}\n"
                    f"Previous visual context: {previous_summary}\n"
                    f"Math content JSON:\n{math_content}"
                ),
                session=SQLiteSession(f"{session_base}-visual"),
            )
            node.visual_plan = result.final_output
            previous_summary = (
                f"{node.concept}: "
                f"elements={node.visual_plan.elements}, "
                f"colors={node.visual_plan.colors}"
            )

    async def _compose_narrative(
        self,
        tree: KnowledgeNode,
        analysis: ConceptAnalysis,
        session_base: str,
    ) -> NarrativeOutline:
        ordered_nodes = tree.walk_foundations_first()
        payload = [
            {
                "concept": node.concept,
                "depth": node.depth,
                "foundation": node.is_foundation,
                "math": (
                    node.mathematical_content.model_dump(mode="json")
                    if node.mathematical_content
                    else {}
                ),
                "visual": (
                    node.visual_plan.model_dump(mode="json") if node.visual_plan else {}
                ),
            }
            for node in ordered_nodes
        ]
        result = await Runner.run(
            self.narrative_agent,
            (
                f"Core concept: {analysis.core_concept}\n"
                f"Domain: {analysis.domain}\n"
                f"Audience: {analysis.audience}\n"
                f"Difficulty: {analysis.difficulty}\n"
                f"Learning goal: {analysis.learning_goal}\n"
                f"Ordered node payload:\n{payload}"
            ),
            session=SQLiteSession(f"{session_base}-narrative"),
        )
        return result.final_output

    async def _generate_code(
        self,
        tree: KnowledgeNode,
        analysis: ConceptAnalysis,
        narrative: NarrativeOutline,
        session_base: str,
    ) -> ManimCodeArtifact:
        preferred_scene_name = normalize_scene_name(analysis.core_concept)
        result = await Runner.run(
            self.code_agent,
            (
                f"Preferred scene name: {preferred_scene_name}\n\n"
                f"{build_narrative_brief(analysis, tree, narrative)}"
            ),
            session=SQLiteSession(f"{session_base}-code"),
        )
        artifact: ManimCodeArtifact = result.final_output
        if not artifact.scene_name:
            artifact.scene_name = preferred_scene_name
        return artifact

    async def _repair_code(
        self,
        tree: KnowledgeNode,
        analysis: ConceptAnalysis,
        narrative: NarrativeOutline,
        code: ManimCodeArtifact,
        validation: CodeValidation,
        session_base: str,
    ) -> ManimCodeArtifact:
        result = await Runner.run(
            self.code_agent,
            (
                "Repair the generated Manim code.\n"
                f"Validation errors: {validation.errors}\n"
                f"Validation warnings: {validation.warnings}\n\n"
                f"Existing code:\n{code.python_code}\n\n"
                f"{build_narrative_brief(analysis, tree, narrative)}"
            ),
            session=SQLiteSession(f"{session_base}-code"),
        )
        artifact: ManimCodeArtifact = result.final_output
        if not artifact.scene_name:
            artifact.scene_name = code.scene_name
        return artifact

    def _validate_code(self, python_code: str) -> CodeValidation:
        report = validate_manim_code_report(python_code)
        complexity = estimate_render_complexity_report(python_code)
        return CodeValidation(
            valid=report["valid"],
            errors=report["errors"],
            warnings=report["warnings"],
            suggestions=report["suggestions"],
            complexity=complexity["complexity"],
            estimated_render_seconds=complexity["estimated_render_seconds"],
        )

    def _default_session_id(self, request: str) -> str:
        slug = normalize_scene_name(request).lower()
        return f"{self.settings.session_prefix}-{slug}"
