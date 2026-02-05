## Project Context

- System title: Logic Puzzle Generation and Analysis System
- Theme: Logic puzzles as a vehicle for exploring AI concepts (CSP, Propositional Logic, Inference, Complexity Analysis, Knowledge Representation)
- Proposal link or summary: This system implements a 6-module pipeline for generating, solving, and analyzing logic puzzles using AI techniques. The proposal defines clear input/output specifications for each module and their integration points.

**Module plan:**

| Module | Topic(s) | Inputs | Outputs | Depends On | Checkpoint |
| ------ | -------- | ------ | ------- | ---------- | ---------- |
| 1 | Constraint Satisfaction Problems (CSP) | JSON: `grid_size` (int), `difficulty` (string: "easy"/"medium"/"hard") | JSON: `puzzle_id`, `entities`, `attributes`, `constraints`, `solution` (hidden) | None | Wednesday, Feb 11 (Checkpoint 1) |
| 2 | Propositional Logic (knowledge bases, logical formulas) | JSON from Module 1: `entities`, `attributes`, `constraints` | Text: Knowledge base with facts (propositions) and rules (logical formulas with ∧, ∨, ¬, →, ↔) | Module 1 | Thursday, Feb 26 (Checkpoint 2) |
| 3 | Propositional Logic (forward chaining, backward chaining, inference) | Text: Knowledge base from Module 2 | Text: Solution (full assignment) and Proof (inference steps) | Module 2 | Thursday, March 19 (Checkpoint 3) |
| 4 | Propositional Logic (logical entailment, satisfiability checking) | Solution (text), constraints (JSON), knowledge base (text), hidden solution (JSON) | Structured text: Validation result, per-constraint results, entailment check, violation summary | Modules 1, 2, 3 | Thursday, April 2 (Checkpoint 4) |
| 5 | Complexity Analysis | Puzzle structure (JSON), knowledge base (text), solution/proof (text), validation report (text) | Structured text: Explicit difficulty metrics (constraint count, search space size, inference step count, constraint density, logical formula complexity, branching factor, solution uniqueness) with interpretations | Modules 1, 2, 3, 4 | Thursday, April 16 (Checkpoint 5) |
| 6 | Knowledge Representation | Solution/proof (text), knowledge base (text), constraints (JSON), difficulty metrics (text) | Structured text: Overall strategy, step-by-step reasoning explanation | Modules 1, 2, 3, 5 | Thursday, April 23 (Final Demo) |

## Constraints

- 5-6 modules total, each tied to course topics.
- Each module must have clear inputs/outputs and tests.
- Align module timing with the course schedule.
- Module 1 must generate valid, solvable puzzles with appropriate constraint counts based on difficulty.
- Module 2 must convert constraints to propositional logic using standard connectives (∧, ∨, ¬, →, ↔).
- Module 3 must use forward chaining or backward chaining inference.
- Module 4 must verify solutions through both constraint satisfaction and logical entailment.
- Module 5 must compute all of the following explicit difficulty metrics with interpretations: constraint count, search space size, inference step count, constraint density, logical formula complexity, branching factor, and solution uniqueness.
- Module 6 must generate human-readable explanations from formal proofs.

## How the Agent Should Help

- Draft plans for each module before coding.
- Suggest clean architecture and module boundaries.
- Identify missing tests and edge cases.
- Review work against the rubric using the code-review skill.
- Ensure proper data format conversions between modules (JSON ↔ text).
- Help design test cases that validate module integration.

## Agent Workflow

1. Ask for the current module spec from `README.md`.
2. Produce a plan (use "Plan" mode if available).
3. Wait for approval before writing or editing code.
4. After implementation, run the code-review skill and list gaps.

## Key References

- Project Instructions: https://csc-343.path.app/projects/project-2-ai-system/ai-system.project.md
- Code elegance rubric: https://csc-343.path.app/rubrics/code-elegance.rubric.md
- Course schedule: https://csc-343.path.app/resources/course.schedule.md
- Rubric: https://csc-343.path.app/projects/project-2-ai-system/ai-system.rubric.md
