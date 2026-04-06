import json
import sys

from hermes_learns_manim.config import PipelineSettings
from hermes_learns_manim.pipeline import ManimRunManager


def test_initialize_run_workspace_seeds_expected_files(tmp_path) -> None:
    settings = PipelineSettings(default_output_root=tmp_path)
    manager = ManimRunManager(settings)

    workspace = manager.initialize_run_workspace("Explain eigenvectors", output_root=tmp_path)

    assert workspace.request_path.exists()
    assert workspace.workflow_path.exists()
    assert workspace.analysis_path.exists()
    assert workspace.tree_path.exists()
    assert workspace.narrative_path.exists()
    assert workspace.scene_path.exists()
    assert workspace.manifest_path.exists()

    manifest = json.loads(workspace.manifest_path.read_text(encoding="utf-8"))
    assert manifest["request"] == "Explain eigenvectors"
    assert manifest["scene_name"] == "ExplainEigenvectors"


def test_save_validation_artifact_marks_manifest_complete(tmp_path) -> None:
    settings = PipelineSettings(default_output_root=tmp_path)
    manager = ManimRunManager(settings)

    workspace = manager.initialize_run_workspace("Explain eigenvectors", output_root=tmp_path)
    manager.save_json_artifact(
        workspace.run_dir,
        "validation.json",
        {
            "valid": True,
            "errors": [],
            "warnings": [],
            "suggestions": [],
            "complexity": "low",
            "estimated_render_seconds": 1,
        },
    )

    manifest = json.loads(workspace.manifest_path.read_text(encoding="utf-8"))
    assert manifest["status"]["validation"] == "complete"


def test_render_returns_failure_result_and_marks_manifest_failed_on_launch_error(
    tmp_path,
    monkeypatch,
) -> None:
    settings = PipelineSettings(default_output_root=tmp_path)
    manager = ManimRunManager(settings)
    workspace = manager.initialize_run_workspace("Explain eigenvectors", output_root=tmp_path)

    def raise_launch_error(*_args, **_kwargs):
        raise FileNotFoundError("manim not found")

    monkeypatch.setattr("hermes_learns_manim.renderer.subprocess.run", raise_launch_error)

    result = manager.render(workspace.run_dir, "ExplainEigenvectors", "l")
    manifest = json.loads(workspace.manifest_path.read_text(encoding="utf-8"))

    assert result["exit_code"] == 1
    assert result["command"][:3] == [sys.executable, "-m", "manim"]
    assert "Failed to launch Manim" in result["stderr"]
    assert manifest["status"]["render"] == "failed"
