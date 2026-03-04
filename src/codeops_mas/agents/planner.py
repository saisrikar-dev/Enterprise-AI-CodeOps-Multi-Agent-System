from __future__ import annotations

from ..models import Artifact, TaskSpec


class PlannerAgent:
    name = "planner"

    def run(self, task: TaskSpec) -> Artifact:
        stack_text = ", ".join(task.stack) if task.stack else "Python"
        constraints_text = (
            "\n".join(f"- {item}" for item in task.constraints)
            if task.constraints
            else "- No explicit constraints"
        )

        plan = f"""# Implementation Plan

## Task
{task.title}

## Preferred Stack
- {stack_text}

## Constraints
{constraints_text}

## Steps
1. Define interfaces, request/response contracts, and validation rules.
2. Implement core business logic with clear boundaries.
3. Add error handling and logging hooks.
4. Write unit tests for happy path + edge cases.
5. Run lightweight security checks and document residual risk.
"""

        return Artifact(name="00_plan.md", content=plan, metadata={"agent": self.name})

