from __future__ import annotations

from ..models import Artifact, TaskSpec


class ReviewerAgent:
    name = "reviewer"

    def run(self, task: TaskSpec, plan: Artifact, solution: Artifact, tests: Artifact, security: Artifact) -> Artifact:
        security_state = "security findings present"
        if "No high-confidence risky patterns detected" in security.content:
            security_state = "no high-confidence security findings"

        review = f"""# Final Review

## Task
{task.title}

## Summary
- Plan created and scoped
- Implementation draft generated
- Test skeleton generated
- Security status: {security_state}

## Merge Readiness
- Status: **Needs human review**
- Reason: Generated artifacts are scaffolds and require domain-specific validation.

## Next Actions
1. Replace placeholder business logic in `01_solution.py`.
2. Expand tests for real edge cases and integration behavior.
3. Run CI, SAST, dependency checks, and performance validation.
"""

        return Artifact(
            name="04_review.md",
            content=review,
            metadata={"agent": self.name, "based_on": [plan.name, solution.name, tests.name, security.name]},
        )

