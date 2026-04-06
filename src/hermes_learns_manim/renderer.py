from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from .models import RenderResult


def render_scene_file(
    code_path: Path,
    scene_name: str,
    quality: str = "l",
) -> RenderResult:
    command = [sys.executable, "-m", "manim", f"-q{quality}", code_path.name, scene_name]
    try:
        completed = subprocess.run(
            command,
            cwd=code_path.parent,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        return RenderResult(
            command=command,
            exit_code=1,
            stdout="",
            stderr=f"Failed to launch Manim: {exc}",
            video_path=None,
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
