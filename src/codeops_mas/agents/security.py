from __future__ import annotations

import re

from ..models import Artifact


class SecurityAgent:
    name = "security"

    _rules: list[tuple[str, str, str]] = [
        (r"\beval\(", "high", "Avoid eval(); it enables code injection."),
        (r"\bexec\(", "high", "Avoid exec(); it enables arbitrary execution."),
        (
            r"subprocess\..*shell=True",
            "high",
            "Avoid shell=True in subprocess unless fully sanitized.",
        ),
        (r"pickle\.loads\(", "medium", "Avoid untrusted pickle deserialization."),
        (r"md5\(", "medium", "Avoid MD5 for security-sensitive hashing."),
    ]

    def run(self, solution: Artifact, tests: Artifact) -> Artifact:
        combined = f"{solution.content}\n{tests.content}"
        findings: list[str] = []
        for pattern, severity, message in self._rules:
            if re.search(pattern, combined):
                findings.append(f"- [{severity.upper()}] `{pattern}`: {message}")

        if not findings:
            findings.append("- [LOW] No high-confidence risky patterns detected in generated artifacts.")

        report = "\n".join(
            [
                "# Security Report",
                "",
                "## Scope",
                f"- Scanned: `{solution.name}`, `{tests.name}`",
                "",
                "## Findings",
                *findings,
                "",
                "## Recommendation",
                "- Run SAST and dependency scan before merging to production.",
            ]
        ) + "\n"

        return Artifact(
            name="03_security_report.md",
            content=report,
            metadata={"agent": self.name, "based_on": [solution.name, tests.name]},
        )

