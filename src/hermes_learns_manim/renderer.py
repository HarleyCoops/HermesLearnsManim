from __future__ import annotations

import subprocess
from pathlib import Path

from .models import RenderResult


def render_scene_file(
    code_path: Path,
    scene_name: str,
    quality: str = "l",
) -> RenderResult:
    command = ["manim", f"-q{quality}", str(code_path), scene_name]
    completed = subprocess.run(
        command,
        cwd=code_path.parent,
        capture_output=True,
        text=True,
        check=False,
    )

    video_path: str | None = None
    for line in reversed(completed.stdout.splitlines()):
        if ".mp4" in line:
            video_path = line.strip()
            break

    return RenderResult(
        command=command,
        exit_code=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        video_path=video_path,
    )
