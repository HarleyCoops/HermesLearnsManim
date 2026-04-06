# Source Pipeline Review

Date: April 6, 2026

Source repository reviewed: `C:\Users\chris\Math-To-Manim`

## Files inspected

- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/AGENT_PIPELINE_GUIDE.md`
- `src/agents/orchestrator.py`
- `src/agents/agent_orchestrator.py`
- `src/agents/prerequisite_explorer_claude.py`
- `src/agents/mathematical_enricher.py`
- `src/agents/visual_designer.py`
- `src/agents/narrative_composer.py`
- `src/agents/claude_sdk_tools.py`
- `Gemini3/src/pipeline.py`
- `Gemini3/src/agents.py`
- `KimiK2.5Swarm/swarm/orchestrator.py`
- `KimiK2.5Swarm/agents/enrichment_chain.py`
- `tests/test_agent_pipeline.py`

## What is actually in the legacy repo

There are three real orchestration families, not one:

### 1. Claude linear pipeline

Primary file: `src/agents/orchestrator.py`

This is the most complete implementation. It coordinates concept analysis, prerequisite exploration, mathematical enrichment, visual design, narrative composition, and Manim code generation.

### 2. Partial Claude SDK rewrite

Primary file: `src/agents/agent_orchestrator.py`

This attempted to move into a tool-enabled Claude runtime. It stopped halfway. Stages 3 through 6 are explicitly `TODO`.

### 3. Gemini and Kimi variants

Primary files:

- `Gemini3/src/pipeline.py`
- `KimiK2.5Swarm/swarm/orchestrator.py`
- `KimiK2.5Swarm/agents/enrichment_chain.py`

Gemini is a simple chained pipeline. Kimi is the most ambitious in terms of structured tool-calling and parallel enrichment.

## Reusable assets worth keeping

- Reverse-knowledge-tree workflow
- `KnowledgeNode` as the core recursive data shape
- Stage prompts for analysis, enrichment, visuals, and narration
- Local validators from `src/agents/claude_sdk_tools.py`
- The idea of post-generation validation before rendering

## What should not be carried forward

- Multiple agent SDKs in the same product path
- UI-first entrypoints as the main integration layer
- Model-specific directories acting as parallel products
- Partial orchestrators with overlapping responsibilities
- Marketing docs that overstate implementation completeness

## Chosen replacement architecture

This repo now uses Hermes as the only agent harness.

The replacement boundary is:

1. Hermes skill instructions for orchestration.
2. A repo-local MCP server for deterministic operations.
3. Provider-agnostic model selection handled by Hermes itself.
4. Shared artifact formats for analysis, tree construction, narrative planning, code generation, validation, and rendering.

## Why this is the right split

The recursive prerequisite tree is a graph-building problem with cycle control, depth limits, deduplication, and deterministic artifact output. Hermes is a better place to own the agent loop than yet another embedded SDK inside this repo.

This repository should not pick the reasoning provider.
It should give Hermes the workspace, tools, templates, and render pipeline.

## Result

The new repo keeps the pedagogical value of `Math-To-Manim` and removes the SDK sprawl that made the old codebase hard to evolve.
