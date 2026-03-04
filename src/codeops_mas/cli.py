from __future__ import annotations

import argparse
from pathlib import Path

from .graph import run_pipeline
from .models import TaskSpec


def _csv_to_list(value: str) -> list[str]:
    if not value.strip():
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the Enterprise AI CodeOps multi-agent pipeline."
    )
    parser.add_argument("--task", required=True, help="Feature request or coding task description.")
    parser.add_argument(
        "--stack",
        default="",
        help="Comma-separated preferred stack, e.g. FastAPI,Pydantic,Redis",
    )
    parser.add_argument(
        "--constraints",
        default="",
        help="Comma-separated constraints, e.g. p95<120ms,include unit tests",
    )
    parser.add_argument(
        "--output",
        default="artifacts/latest_run",
        help="Output directory for generated artifacts.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    task = TaskSpec(
        title=args.task,
        stack=_csv_to_list(args.stack),
        constraints=_csv_to_list(args.constraints),
    )

    output_dir = Path(args.output)
    result = run_pipeline(task, output_dir)

    print("Pipeline finished successfully.")
    print(f"Output directory: {output_dir.resolve()}")
    print(f"Generated: {result.plan.name}, {result.code.name}, {result.tests.name}, {result.security.name}, {result.review.name}")


if __name__ == "__main__":
    main()
