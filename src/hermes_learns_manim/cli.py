from __future__ import annotations

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from .config import PipelineSettings
from .mcp_server import mcp
from .pipeline import ManimRunManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hermes-learns-manim")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init-run", help="Seed a new Hermes run workspace.")
    init_parser.add_argument("prompt")
    init_parser.add_argument("--output-root", default="runs")

    summarize_parser = subparsers.add_parser("summarize", help="Summarize a run workspace.")
    summarize_parser.add_argument("run_dir")

    render_parser = subparsers.add_parser("render", help="Render a run workspace scene.py file.")
    render_parser.add_argument("run_dir")
    render_parser.add_argument("scene_name")
    render_parser.add_argument("--quality", default="l")

    subparsers.add_parser("serve-mcp", help="Run the Hermes MCP server.")
    return parser


def main() -> None:
    load_dotenv()
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "serve-mcp":
        mcp.run()
        return

    manager = ManimRunManager(PipelineSettings.from_env())

    if args.command == "init-run":
        workspace = manager.initialize_run_workspace(
            args.prompt,
            output_root=Path(args.output_root),
        )
        print(json.dumps(workspace.to_dict(), indent=2))
        return

    if args.command == "summarize":
        print(json.dumps(manager.summarize_workspace(Path(args.run_dir)), indent=2))
        return

    if args.command == "render":
        result = manager.render(Path(args.run_dir), args.scene_name, args.quality)
        print(json.dumps(result, indent=2))
        return


if __name__ == "__main__":
    main()
