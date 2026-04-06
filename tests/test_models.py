from hermes_learns_manim.models import KnowledgeNode


def test_walk_foundations_first_orders_prerequisites_before_root() -> None:
    leaf = KnowledgeNode(concept="vectors", depth=2, is_foundation=True)
    mid = KnowledgeNode(
        concept="linear transformations",
        depth=1,
        is_foundation=False,
        prerequisites=[leaf],
    )
    root = KnowledgeNode(
        concept="eigenvalues",
        depth=0,
        is_foundation=False,
        prerequisites=[mid],
    )

    ordered = [node.concept for node in root.walk_foundations_first()]
    assert ordered == ["vectors", "linear transformations", "eigenvalues"]
