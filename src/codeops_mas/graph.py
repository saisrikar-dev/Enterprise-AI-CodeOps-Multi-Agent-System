from __future__ import annotations

from pathlib import Path

from .agents import CoderAgent, PlannerAgent, ReviewerAgent, SecurityAgent, TesterAgent
from .memory import RunMemory
from .models import PipelineResult, TaskSpec


def run_pipeline(task: TaskSpec, output_dir: Path) -> PipelineResult:
    output_dir.mkdir(parents=True, exist_ok=True)

    planner = PlannerAgent()
    coder = CoderAgent()
    tester = TesterAgent()
    security = SecurityAgent()
    reviewer = ReviewerAgent()

    plan = planner.run(task)
    solution = coder.run(task, plan)
    tests = tester.run(solution)
    sec_report = security.run(solution, tests)
    review = reviewer.run(task, plan, solution, tests, sec_report)

    artifacts = [plan, solution, tests, sec_report, review]
    for artifact in artifacts:
        (output_dir / artifact.name).write_text(artifact.content, encoding="utf-8")

    result = PipelineResult(
        task=task,
        plan=plan,
        code=solution,
        tests=tests,
        security=sec_report,
        review=review,
    )

    memory_file = output_dir.parent / "memory" / "history.jsonl"
    RunMemory(memory_file).append(result)
    return result

