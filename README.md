<p align="center">
  <img src="assets/Hermeshero.jpg" alt="Hermes Learns Manim" width="100%">
</p>

# HermesLearnsManim

`HermesLearnsManim` is a Hermes-first workspace for building Manim animations through reverse-knowledge-tree reasoning.

Hermes owns the agent loop and subagent routine. This repo gives Hermes the MCP tools, workspace artifacts, validation helpers, and render hooks needed to turn a concept into a runnable animation.

## What lives here

- a local MCP server for run initialization, artifact saving, validation, and rendering
- a Hermes skill pack for the reverse-knowledge-tree workflow
- stable file formats for analysis, knowledge trees, narrative plans, and generated Manim code
- deterministic validators for LaTeX and Manim

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

Then configure Hermes and pick a model provider inside Hermes itself:

```bash
hermes setup
hermes model
```

## Starter prompts

The root prompt catalog lives in [`PROMPTS.md`](PROMPTS.md). Each entry includes the full text so you can paste it directly into Hermes.

Quickstart links:

- [Cinematic Cosmology](PROMPTS.md#cinematic-cosmology)
- [Epic QED Journey](PROMPTS.md#epic-qed-journey)
- [Brownian Motion to Black-Scholes](PROMPTS.md#brownian-motion-to-black-scholes)
- [Geodesic Equation](PROMPTS.md#geodesic-equation)
- [Whiskering Exchange Law](PROMPTS.md#whiskering-exchange-law)
- [Klein Bottle and Mobius Strip](PROMPTS.md#klein-bottle-and-mobius-strip)
- [Taylor Series Topology of Convergence](PROMPTS.md#taylor-series-topology-of-convergence)
- [Pythagorean Theorem Verbose Teaching Prompt](PROMPTS.md#pythagorean-theorem-verbose-teaching-prompt)

## Hermes integration

This repo ships both pieces Hermes needs:

- `src/hermes_learns_manim/mcp_server.py`
- `hermes/skills/hermes-learns-manim/SKILL.md`

The skill defines the workflow.
The MCP server provides deterministic operations.

## Repo review

The legacy repo review that drove this refactor lives in:

- `docs/source-pipeline-review.md`
