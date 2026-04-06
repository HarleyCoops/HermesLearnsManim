import json

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
