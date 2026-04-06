# HermesLearnsManim

`HermesLearnsManim` is the clean-room successor to `Math-To-Manim`.

The old repository proved the pedagogical idea: take a user concept, recursively unpack the prerequisites, enrich the math, design the visuals, then synthesize Manim code. The problem was the harness. The codebase drifted into three parallel SDK stacks with duplicated prompts, incomplete orchestrators, and inconsistent tool boundaries.

This repo resets the foundation around one runtime:

- OpenAI Agents SDK for typed stage agents, tool-calling, sessions, and tracing
- Manager-style orchestration in Python for deterministic recursive traversal
- Hermes-ready MCP exposure so Hermes can call the pipeline remotely
- A single artifact layout for prompts, trees, code, and renders

## Why this protocol

The current `Math-To-Manim` repo mixes:

- Anthropic-oriented linear orchestration in `src/agents/orchestrator.py`
- A second partial Claude SDK rewrite in `src/agents/agent_orchestrator.py`
- A Gemini chain in `Gemini3/src/pipeline.py`
- A Kimi swarm with better structured tool-calling in `KimiK2.5Swarm/`

This repo keeps the stage semantics and drops the framework fragmentation.

The protocol choice here is:

1. Use OpenAI Agents SDK specialist agents with structured outputs.
2. Keep the recursive control flow in Python, not in freeform handoffs.
3. Give the code generation stage local validators as tools.
4. Expose the final pipeline to Hermes through MCP, because Hermes already speaks MCP cleanly.

That gives better tool discipline and easier reasoning about failure modes than another model-specific swarm.

## Pipeline

The pipeline remains the same conceptually:

1. Analyze the user request into a target concept, domain, audience, and goal.
2. Build a reverse knowledge tree by recursively asking what must be understood first.
3. Enrich each node with equations, definitions, examples, and interpretation.
4. Design visuals for each node with continuity-aware transitions.
5. Compose a scene outline for the full animation.
6. Generate Manim code.
7. Validate the code locally and optionally render to MP4.

## Quickstart

```bash
git clone https://github.com/HarleyCoops/HermesLearnsManim.git
cd HermesLearnsManim
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`, then run:

```bash
hermes-learns-manim run "Explain the Fourier transform as a story from waves to spectra"
```

To generate and render:

```bash
hermes-learns-manim run "Visualize special relativity from inertial frames to time dilation" --render
```

Artifacts are written under `runs/<concept>-<timestamp>/`.

## Hermes integration

Hermes has two natural integration points:

- As an MCP server: Hermes calls the generator as a tool.
- As a skill: Hermes learns when to route math-animation requests into the MCP tool or CLI.

This repo ships both:

- `src/hermes_learns_manim/mcp_server.py`
- `hermes/skills/hermes-learns-manim/SKILL.md`

Example MCP launch:

```bash
python -m hermes_learns_manim.cli serve-mcp
```

## Repo review

The legacy repo review that drove this refactor lives in:

- `docs/source-pipeline-review.md`

It documents what was reusable, what was dead weight, and why manager orchestration plus MCP is the right replacement boundary.
