from __future__ import annotations

from textwrap import dedent

from ..models import Artifact


class TesterAgent:
    name = "tester"

    def run(self, solution: Artifact) -> Artifact:
        tests = dedent(
            """
            from solution import Request, execute


            def test_execute_happy_path():
                req = Request(payload={"distance_km": 12, "time_of_day": "peak"})
                res = execute(req)
                assert res.ok is True
                assert "item_count" in res.data


            def test_execute_rejects_invalid_payload():
                req = Request(payload="invalid")
                res = execute(req)
                assert res.ok is False
                assert "payload must be a dict" in res.message
            """
        ).strip() + "\n"

        return Artifact(
            name="02_tests.py",
            content=tests,
            metadata={"agent": self.name, "based_on": solution.name},
        )

