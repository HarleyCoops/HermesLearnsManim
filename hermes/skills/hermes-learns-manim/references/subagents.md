# Suggested Hermes Subagents

This workflow works best when Hermes keeps one main coordinator and only delegates bounded slices.

## Suggested roles

### concept-analyst

Responsibility:

- write `analysis.json`
- clarify core concept, domain, audience, difficulty, and learning goal

### prerequisite-explorer

Responsibility:

- build `knowledge_tree.json`
- recurse only as deep as needed
- deduplicate overlapping prerequisites

### math-enricher

Responsibility:

- strengthen equations, definitions, examples, and interpretation
- avoid changing the tree shape unless the coordinator asks for it

### narrative-composer

Responsibility:

- write `narrative.md`
- convert the tree into a scene progression from foundations to target concept

### code-generator

Responsibility:

- write `scene.py`
- keep the code self-contained and Manim-native
- run validation before claiming completion

## Coordination rule

The main Hermes agent should own the final review and render decision.
Only the coordinator should decide whether to re-open earlier stages or start rendering.
