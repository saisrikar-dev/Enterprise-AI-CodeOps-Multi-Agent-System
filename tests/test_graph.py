from __future__ import annotations

from pathlib import Path

from codeops_mas.graph import run_pipeline
from codeops_mas.models import TaskSpec


def test_run_pipeline_generates_expected_files(tmp_path: Path) -> None:
    task = TaskSpec(
        title="Build ride fare estimation endpoint",
        stack=["FastAPI", "Pydantic"],
        constraints=["p95<120ms", "unit tests required"],
    )
    output_dir = tmp_path / "artifacts" / "run1"

    result = run_pipeline(task, output_dir)

    assert result.plan.name == "00_plan.md"
    assert (output_dir / "00_plan.md").exists()
    assert (output_dir / "01_solution.py").exists()
    assert (output_dir / "02_tests.py").exists()
    assert (output_dir / "03_security_report.md").exists()
    assert (output_dir / "04_review.md").exists()
    assert (output_dir.parent / "memory" / "history.jsonl").exists()


def test_security_report_contains_scope(tmp_path: Path) -> None:
    task = TaskSpec(title="Create simple parser")
    output_dir = tmp_path / "artifacts" / "run2"

    result = run_pipeline(task, output_dir)
    assert "## Scope" in result.security.content
    assert "01_solution.py" in result.security.content
