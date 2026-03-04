from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .models import PipelineResult


class RunMemory:
    """Append-only run memory for traceability."""

    def __init__(self, memory_file: Path) -> None:
        self.memory_file = memory_file
        self.memory_file.parent.mkdir(parents=True, exist_ok=True)

    def append(self, result: PipelineResult) -> None:
        entry = asdict(result)
        with self.memory_file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=True) + "\n")

