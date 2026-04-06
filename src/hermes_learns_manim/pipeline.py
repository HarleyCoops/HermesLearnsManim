from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .config import PipelineSettings
from .io import ensure_run_dir, write_json, write_text
from .prompts import (
    analysis_template,
    build_workflow_brief,
    knowledge_tree_template,
    manifest_template,
    narrative_template,
    scene_stub,
)
from .renderer import render_scene_file
from .tools import normalize_scene_name


@dataclass(slots=True)
class RunWorkspace:
    request: str
    created_at: str
    run_dir: Path
    request_path: Path
    workflow_path: Path
    analysis_path: Path
    tree_path: Path
    narrative_path: Path
    scene_path: Path
    manifest_path: Path

    def to_dict(self) -> dict[str, str]:
        return {
            "request": self.request,
            "created_at": self.created_at,
            "run_dir": str(self.run_dir),
            "request_path": str(self.request_path),
            "workflow_path": str(self.workflow_path),
            "analysis_path": str(self.analysis_path),
            "tree_path": str(self.tree_path),
            "narrative_path": str(self.narrative_path),
            "scene_path": str(self.scene_path),
            "manifest_path": str(self.manifest_path),
        }


class ManimRunManager:
    def __init__(self, settings: PipelineSettings | None = None) -> None:
        self.settings = settings or PipelineSettings.from_env()

    def initialize_run_workspace(
        self,
        request: str,
        *,
        output_root: Path | None = None,
    ) -> RunWorkspace:
        output_root = output_root or self.settings.default_output_root
        created_at = datetime.now(UTC).isoformat(timespec="seconds")
        run_dir = ensure_run_dir(output_root, request, created_at)
        scene_name = normalize_scene_name(request)

        workspace = RunWorkspace(
            request=request,
            created_at=created_at,
            run_dir=run_dir,
            request_path=run_dir / "request.md",
            workflow_path=run_dir / "workflow.md",
            analysis_path=run_dir / "analysis.json",
            tree_path=run_dir / "knowledge_tree.json",
            narrative_path=run_dir / "narrative.md",
            scene_path=run_dir / "scene.py",
            manifest_path=run_dir / "run_manifest.json",
        )

        write_text(workspace.request_path, f"# Request\n\n{request}\n")
        write_text(workspace.workflow_path, build_workflow_brief(request, scene_name))
        write_json(workspace.analysis_path, analysis_template())

        tree = knowledge_tree_template()
        tree["concept"] = request
        write_json(workspace.tree_path, tree)

        write_text(workspace.narrative_path, narrative_template())
        write_text(workspace.scene_path, scene_stub(scene_name))

        manifest = manifest_template(request, scene_name)
        manifest["created_at"] = created_at
        manifest["artifacts"] = {
            "request": str(workspace.request_path),
            "workflow": str(workspace.workflow_path),
            "analysis": str(workspace.analysis_path),
            "knowledge_tree": str(workspace.tree_path),
            "narrative": str(workspace.narrative_path),
            "scene": str(workspace.scene_path),
        }
        write_json(workspace.manifest_path, manifest)
        return workspace

    def save_text_artifact(
        self,
        run_dir: Path,
        relative_path: str,
        content: str,
    ) -> dict[str, Any]:
        path = self._resolve_artifact_path(run_dir, relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        write_text(path, content)
        self._update_status(run_dir, relative_path)
        return {"path": str(path), "bytes": len(content.encode("utf-8"))}

    def save_json_artifact(
        self,
        run_dir: Path,
        relative_path: str,
        content: str | dict[str, Any],
    ) -> dict[str, Any]:
        payload = json.loads(content) if isinstance(content, str) else content
        path = self._resolve_artifact_path(run_dir, relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        write_json(path, payload)
        self._update_status(run_dir, relative_path)
        return {"path": str(path), "keys": sorted(payload.keys())}

    def read_artifact(self, run_dir: Path, relative_path: str) -> str:
        path = self._resolve_artifact_path(run_dir, relative_path)
        return path.read_text(encoding="utf-8")

    def summarize_workspace(self, run_dir: Path) -> dict[str, Any]:
        manifest_path = self._resolve_artifact_path(run_dir, "run_manifest.json")
        manifest = {}
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        files = [
            str(path.relative_to(run_dir))
            for path in sorted(run_dir.rglob("*"))
            if path.is_file()
        ]
        return {
            "run_dir": str(run_dir),
            "manifest": manifest,
            "files": files,
        }

    def render(self, run_dir: Path, scene_name: str, quality: str | None = None) -> dict[str, Any]:
        quality = quality or self.settings.default_render_quality
        scene_path = self._resolve_artifact_path(run_dir, "scene.py")
        result = render_scene_file(scene_path, scene_name, quality)
        self._set_render_status(run_dir, "complete" if result.exit_code == 0 else "failed")
        return result.model_dump(mode="json")

    def _resolve_artifact_path(self, run_dir: Path, relative_path: str) -> Path:
        root = run_dir.resolve()
        candidate = (root / relative_path).resolve()
        if root not in candidate.parents and candidate != root:
            raise ValueError("Artifact path escapes the run directory.")
        return candidate

    def _update_status(self, run_dir: Path, relative_path: str) -> None:
        manifest_path = self._resolve_artifact_path(run_dir, "run_manifest.json")
        if not manifest_path.exists():
            return
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        status = manifest.setdefault("status", {})
        name = Path(relative_path).name
        mapping = {
            "analysis.json": "analysis",
            "knowledge_tree.json": "knowledge_tree",
            "narrative.md": "narrative",
            "scene.py": "scene_code",
        }
        if name in mapping:
            status[mapping[name]] = "complete"
        write_json(manifest_path, manifest)

    def _set_render_status(self, run_dir: Path, value: str) -> None:
        manifest_path = self._resolve_artifact_path(run_dir, "run_manifest.json")
        if not manifest_path.exists():
            return
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest.setdefault("status", {})["render"] = value
        write_json(manifest_path, manifest)
