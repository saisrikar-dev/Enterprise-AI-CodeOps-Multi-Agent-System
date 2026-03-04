# Architecture

## Objective

Convert a natural language engineering task into implementation-ready artifacts using a deterministic multi-agent pipeline.

## Agents

1. **Planner Agent**
   - Produces a scoped implementation plan
   - Highlights assumptions and risks

2. **Coder Agent**
   - Drafts Python implementation skeleton
   - Aligns with stack preferences and constraints

3. **Tester Agent**
   - Produces `pytest` test skeletons
   - Covers success path, validation, and edge cases

4. **Security Agent**
   - Scans generated code for risky patterns
   - Produces actionable severity-tagged findings

5. **Reviewer Agent**
   - Summarizes quality, risk, and readiness
   - Provides next actions for developers

## Orchestration

The graph runs agents in strict order to keep behavior reproducible:

`Task -> Plan -> Code -> Tests -> Security -> Review -> Persist`

## Memory

Each run appends a summary record to:

`artifacts/memory/history.jsonl`

This enables:
- traceability across runs
- future ranking and benchmarking
- iterative improvements

## Extensibility

The current implementation is deterministic and local-first. You can extend it by:
- plugging real LLM providers in `llm.py`
- swapping security rules with AST analysis
- adding evaluator agents and scoring dashboards

