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

This is the most complete implementation. It coordinates:

1. concept analysis
2. prerequisite exploration
3. mathematical enrichment
4. visual design
5. narrative composition
6. Manim code generation

Strengths:

- Clear stage boundaries
- Reusable `KnowledgeNode`
- Good prompt decomposition
- Local artifact saving

Weaknesses:

- Anthropic-specific wiring
- Mostly plain-text parsing
- Validation and rendering are loosely coupled
- No stable remote integration boundary

### 2. Partial Claude SDK rewrite

Primary file: `src/agents/agent_orchestrator.py`

This attempted to move into a tool-enabled Claude agent runtime. It stopped halfway. Stages 3 through 6 are explicitly `TODO`.

Strengths:

- The direction was correct: stateful orchestration, MCP-style tools, video review

Weaknesses:

- Incomplete
- Competes with the linear orchestrator
- Adds another runtime abstraction without replacing the older one

### 3. Gemini and Kimi variants

Primary files:

- `Gemini3/src/pipeline.py`
- `KimiK2.5Swarm/swarm/orchestrator.py`
- `KimiK2.5Swarm/agents/enrichment_chain.py`

Gemini is a simple chained pipeline. Kimi is the most ambitious in terms of structured tool-calling and parallel enrichment.

Strengths:

- Kimi uses structured tool payloads instead of plain text parsing
- Kimi swarm shows the right instinct around parallel enrichment
- Gemini pipeline preserves the same pedagogical stages

Weaknesses:

- Each stack duplicates prompts and data flow
- Each stack has its own client model assumptions
- The repo drifted into model demos instead of one product boundary

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

This repo replaces the harness with:

1. OpenAI Agents SDK specialist agents using structured outputs.
2. Python manager orchestration for recursive tree traversal.
3. Local function tools for validation and caching.
4. Stage-specific sessions for memory where it helps and isolation where it matters.
5. An MCP server as the Hermes integration boundary.

## Why manager orchestration instead of free handoffs

The recursive prerequisite tree is a graph-building problem with cycle control, depth limits, deduplication, and deterministic artifact output. That is better handled by Python code than by letting an LLM own the entire control plane.

The LLM should reason inside each stage.
The application should own recursion, persistence, validation, and render execution.

## Result

The new repo keeps the pedagogical value of `Math-To-Manim` and removes the SDK sprawl that made the old codebase hard to evolve.
