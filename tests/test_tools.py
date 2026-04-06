from hermes_learns_manim.tools import (
    estimate_render_complexity_report,
    normalize_scene_name,
    validate_latex_report,
    validate_manim_code_report,
)


def test_validate_latex_report_catches_unbalanced_delimiters() -> None:
    report = validate_latex_report(r"$\frac{a}{b}")
    assert not report["valid"]
    assert report["errors"]



def test_validate_manim_code_report_requires_scene_construct_and_import() -> None:
    report = validate_manim_code_report("class Demo:\n    pass\n")
    assert not report["valid"]
    assert "Missing Manim import." in report["errors"]



def test_estimate_render_complexity_report_returns_named_band() -> None:
    report = estimate_render_complexity_report(
        "from manim import *\nclass Demo(Scene):\n    def construct(self):\n        self.play(Create(Circle()))\n"
    )
    assert report["complexity"] in {"low", "medium", "high"}
    assert report["estimated_render_seconds"] > 0



def test_normalize_scene_name_strips_invalid_characters() -> None:
    assert normalize_scene_name("Fourier transform in 3D!") == "FourierTransformIn3D"
