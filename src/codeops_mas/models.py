from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass(slots=True)
class TaskSpec:
    title: str
    stack: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Artifact:
    name: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class PipelineResult:
    task: TaskSpec
    plan: Artifact
    code: Artifact
    tests: Artifact
    security: Artifact
    review: Artifact
    created_at_utc: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

