from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PipelineSettings:
    model: str = "gpt-5"
    max_depth: int = 3
    max_prerequisites_per_node: int = 4
    default_output_root: Path = Path("runs")
    default_render_quality: str = "l"
    session_prefix: str = "hermes-learns-manim"

    @classmethod
    def from_env(cls) -> "PipelineSettings":
        model = os.getenv("HERMES_LEARNS_MANIM_MODEL", "gpt-5")
        max_depth = int(os.getenv("HERMES_LEARNS_MANIM_MAX_DEPTH", "3"))
        output_root = Path(os.getenv("HERMES_LEARNS_MANIM_OUTPUT_ROOT", "runs"))
        render_quality = os.getenv("HERMES_LEARNS_MANIM_RENDER_QUALITY", "l")
        session_prefix = os.getenv(
            "HERMES_LEARNS_MANIM_SESSION_PREFIX",
            "hermes-learns-manim",
        )
        return cls(
            model=model,
            max_depth=max_depth,
            default_output_root=output_root,
            default_render_quality=render_quality,
            session_prefix=session_prefix,
        )
