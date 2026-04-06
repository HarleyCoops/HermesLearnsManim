from __future__ import annotations

import json
import re
from typing import Any

try:
    from agents import function_tool
except ImportError:  # pragma: no cover
    def function_tool(func=None, **_kwargs):  # type: ignore[override]
        if func is None:
            return lambda inner: inner
        return func


PREREQUISITE_CACHE: dict[str, list[str]] = {}


def _cache_key(concept: str) -> str:
    return concept.strip().casefold()


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        normalized = item.strip()
        if not normalized:
            continue
        key = normalized.casefold()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(normalized)
    return ordered


def validate_latex_report(latex_code: str) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if latex_code.count("$") % 2 != 0:
        errors.append("Unmatched dollar delimiters.")
    if latex_code.count("{") != latex_code.count("}"):
        errors.append("Unbalanced braces.")
    if "\\frac{}" in latex_code:
        errors.append("Empty \\frac command.")
    if "\\begin" in latex_code and "\\end" not in latex_code:
        warnings.append("Environment start without obvious end.")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
    }


def validate_manim_code_report(manim_code: str) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    suggestions: list[str] = []

    if "from manim import" not in manim_code and "import manim" not in manim_code:
        errors.append("Missing Manim import.")
    if "class " not in manim_code or "Scene)" not in manim_code:
        errors.append("No Scene subclass found.")
    if "def construct(self)" not in manim_code:
        errors.append("Missing construct(self) method.")
    if "ImageMobject(" in manim_code:
        warnings.append("External assets detected through ImageMobject.")
    if "MathTex(" in manim_code and 'MathTex("' in manim_code:
        suggestions.append("Prefer raw strings for MathTex content.")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "suggestions": suggestions,
    }


def estimate_render_complexity_report(manim_code: str) -> dict[str, Any]:
    play_calls = manim_code.count("self.play(")
    transforms = manim_code.count("Transform(") + manim_code.count("ReplacementTransform(")
    math_objects = manim_code.count("MathTex(") + manim_code.count("Tex(")
    three_d_objects = manim_code.count("ThreeDScene") + manim_code.count("Surface(")

    score = play_calls + transforms + math_objects + (three_d_objects * 4)
    estimated_seconds = 5 + (play_calls * 2) + math_objects + (three_d_objects * 8)

    if score < 15:
        complexity = "low"
    elif score < 35:
        complexity = "medium"
    else:
        complexity = "high"

    return {
        "complexity": complexity,
        "estimated_render_seconds": estimated_seconds,
        "score": score,
    }


@function_tool
def get_cached_prerequisites(concept: str) -> str:
    cached = PREREQUISITE_CACHE.get(_cache_key(concept))
    return json.dumps(
        {
            "found": cached is not None,
            "prerequisites": cached or [],
        }
    )


@function_tool
def cache_prerequisites(concept: str, prerequisites: list[str]) -> str:
    deduped = _dedupe(prerequisites)
    PREREQUISITE_CACHE[_cache_key(concept)] = deduped
    return json.dumps(
        {
            "concept": concept,
            "cached_count": len(deduped),
        }
    )


@function_tool
def validate_latex(latex_code: str) -> str:
    return json.dumps(validate_latex_report(latex_code))


@function_tool
def validate_manim_code(manim_code: str) -> str:
    return json.dumps(validate_manim_code_report(manim_code))


@function_tool
def estimate_render_complexity(manim_code: str) -> str:
    return json.dumps(estimate_render_complexity_report(manim_code))


def normalize_scene_name(concept: str) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z]+", " ", concept).title().replace(" ", "")
    if not cleaned:
        return "GeneratedScene"
    if cleaned[0].isdigit():
        return f"Scene{cleaned}"
    return cleaned
