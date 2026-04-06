# HermesLearnsManim

`HermesLearnsManim` is the clean-room successor to `Math-To-Manim`.

The old repository proved the pedagogical idea: take a user concept, recursively unpack the prerequisites, enrich the math, design the visuals, then synthesize Manim code. The problem was the harness. The codebase drifted into three parallel SDK stacks with duplicated prompts, incomplete orchestrators, and inconsistent tool boundaries.

This repo now takes a stricter approach:

- Hermes is the only agent harness.
- Hermes handles model login, provider selection, and subagent orchestration.
- This repo provides universal scaffolding, deterministic tools, artifact schemas, and render hooks.
- The integration boundary is MCP so Hermes can use the scaffold locally or remotely.

## What lives here

This repository is not another agent framework. It is a Hermes-first workspace package that ships:

- a local MCP server for run initialization, artifact saving, validation, and rendering
- a Hermes skill pack that teaches Hermes how to execute the reverse-knowledge-tree workflow with subagents
- stable file formats for analysis, knowledge trees, narrative plans, and generated Manim code
- deterministic validators for LaTeX and Manim

## Why Hermes-only

The current `Math-To-Manim` repo mixes:

- Anthropic-oriented orchestration in `src/agents/orchestrator.py`
- a second partial Claude SDK rewrite in `src/agents/agent_orchestrator.py`
- a Gemini chain in `Gemini3/src/pipeline.py`
- a Kimi swarm in `KimiK2.5Swarm/`

That fragmentation is the main technical problem.

This repo removes it by treating Hermes as the single control plane. The reasoning model can be OpenAI, Kimi, Nous, OpenRouter, or another provider, but Hermes owns the agent loop.

## Workflow

1. Hermes receives a math-animation request.
2. Hermes calls the MCP tool `initialize_run_workspace`.
3. Hermes uses its own subagent routine to recreate the reasoning tree and downstream artifacts.
4. Hermes saves intermediate artifacts back through MCP tools.
5. Hermes validates the generated Manim code.
6. Hermes optionally renders to MP4.

The scaffold stays universal because the reasoning model is configured in Hermes, not hardcoded here.

## Quickstart

```bash
git clone https://github.com/HarleyCoops/HermesLearnsManim.git
cd HermesLearnsManim
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
```

Start the MCP server:

```bash
python -m hermes_learns_manim.cli serve-mcp
```

Then point Hermes at it with the config snippet in:

- `hermes/skills/hermes-learns-manim/references/mcp-config.yaml`

Model login happens in Hermes, not in this repo:

```bash
hermes setup
hermes model
```

## Hermes integration

This repo ships both of the pieces Hermes needs:

- `src/hermes_learns_manim/mcp_server.py`
- `hermes/skills/hermes-learns-manim/SKILL.md`

The skill defines the multi-agent routine.
The MCP server gives Hermes the deterministic tools it needs.

## Repo review

The legacy repo review that drove this refactor lives in:

- `docs/source-pipeline-review.md`

It documents what was reusable, what was dead weight, and why Hermes plus MCP is the right replacement boundary.
