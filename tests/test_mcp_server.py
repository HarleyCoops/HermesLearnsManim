from hermes_learns_manim.mcp_server import source_pipeline_review


def test_source_pipeline_review_loads_packaged_resource() -> None:
    review = source_pipeline_review()

    assert review.startswith("# Source Pipeline Review")
    assert "Chosen replacement architecture" in review
