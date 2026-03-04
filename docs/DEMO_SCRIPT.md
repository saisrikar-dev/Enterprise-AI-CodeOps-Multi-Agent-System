# 90-Second Demo Script

## Goal

Showcase the repo like a production AI engineering project.

## Script

1. "This project is a deterministic multi-agent code generation system inspired by enterprise engineering workflows."
2. "I pass one product requirement and the graph orchestrates Planner, Coder, Tester, Security, and Reviewer agents."
3. Run:
   - `python -m codeops_mas.cli --task "Build ride fare estimator API" --stack "FastAPI,Redis" --constraints "p95<120ms" --output artifacts/demo`
4. Open generated files in order:
   - `00_plan.md`
   - `01_solution.py`
   - `02_tests.py`
   - `03_security_report.md`
   - `04_review.md`
5. "Every run is logged into memory for traceability and future benchmarking."
6. "This architecture is designed for CI integration and GitHub PR workflows."
