from __future__ import annotations

from importlib.resources import files
from pathlib import Path

from .config import PipelineSettings
from .pipeline import ManimRunManager
from .tools import (
    estimate_render_complexity_report,
    validate_latex_report,
    validate_manim_code_report,
)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # pragma: no cover
    FastMCP = None

if FastMCP is None:  # pragma: no cover
    raise RuntimeError("mcp is required. Install with `pip install mcp`.")

mcp = FastMCP("HermesLearnsManim")
manager = ManimRunManager(PipelineSettings.from_env())


@mcp.tool()
def initialize_run_workspace(request: str, output_root: str = "runs") -> dict:
    return manager.initialize_run_workspace(request, output_root=Path(output_root)).to_dict()


@mcp.tool()
def save_text_artifact(run_dir: str, relative_path: str, content: str) -> dict:
    return manager.save_text_artifact(Path(run_dir), relative_path, content)


@mcp.tool()
def save_json_artifact(run_dir: str, relative_path: str, content: str) -> dict:
    return manager.save_json_artifact(Path(run_dir), relative_path, content)


@mcp.tool()
def read_artifact(run_dir: str, relative_path: str) -> str:
    return manager.read_artifact(Path(run_dir), relative_path)


@mcp.tool()
def summarize_workspace(run_dir: str) -> dict:
    return manager.summarize_workspace(Path(run_dir))


@mcp.tool()
def validate_latex_block(latex_code: str) -> dict:
    return validate_latex_report(latex_code)


@mcp.tool()
def validate_manim_scene(manim_code: str) -> dict:
    return validate_manim_code_report(manim_code)


@mcp.tool()
def estimate_scene_complexity(manim_code: str) -> dict:
    return estimate_render_complexity_report(manim_code)


@mcp.tool()
def render_scene(run_dir: str, scene_name: str, quality: str = "l") -> dict:
    return manager.render(Path(run_dir), scene_name, quality)


@mcp.tool()
def source_pipeline_review() -> str:
    review_path = files("hermes_learns_manim").joinpath(
        "resources",
        "source-pipeline-review.md",
    )
    return review_path.read_text(encoding="utf-8")
