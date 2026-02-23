# Logic Puzzle Generation and Analysis System

## Overview

This system provides an end-to-end pipeline for generating, solving, and analyzing logic puzzles using artificial intelligence techniques. The system begins by generating generic logic puzzle structures with entities, attributes, and constraints based on specified difficulty levels. These puzzles are then converted into propositional logic knowledge bases, where constraints become logical formulas using standard connectives. The system solves puzzles through forward and backward chaining inference, producing both complete solutions and formal proofs of the reasoning process. Solutions are verified through dual methods: checking constraint satisfaction and logical entailment validation. The system analyzes puzzle difficulty using multiple complexity metrics (constraint count, search space size, inference step count, etc.) to provide comprehensive difficulty assessments. Finally, the system generates human-readable explanations that translate formal logical proofs into step-by-step narratives, making the AI reasoning process transparent and understandable.

Logic puzzles are an ideal theme for exploring AI concepts because they naturally embody core AI principles. The puzzle constraints map directly to propositional logic, enabling exploration of knowledge representation, inference methods, and entailment checking. Puzzle generation requires constraint satisfaction techniques to ensure valid, solvable puzzles. The solving process demonstrates forward/backward chaining inference in action, while verification showcases logical entailment and satisfiability checking. Difficulty analysis provides opportunities to examine algorithmic complexity and problem space analysis. The explanation generation bridges formal logical reasoning with human understanding, illustrating knowledge representation concepts. This theme offers a coherent progression through multiple AI topics while remaining accessible and testable, with clear input/output specifications that enable rigorous module integration and validation.

## Team

- Tori
- Madigan

## Proposal

This system implements the Logic Puzzle Generation and Analysis System proposal. The proposal defines a 6-module pipeline that progresses from puzzle generation through solving, verification, analysis, and explanation.

## Module Plan

| Module | Topic(s) | Inputs | Outputs | Depends On | Checkpoint |
| ------ | -------- | ------ | ------- | ---------- | ---------- |
| 1 | Constraint Satisfaction Problems (CSP) | JSON: `grid_size` (int), `difficulty` (string: "easy"/"medium"/"hard") | JSON: `puzzle_id`, `entities`, `attributes`, `constraints`, `solution` (hidden) | None | Wednesday, Feb 11 (Checkpoint 1) |
| 2 | Propositional Logic (knowledge bases, logical formulas) | JSON from Module 1: `entities`, `attributes`, `constraints` | Text: Knowledge base with facts (propositions) and rules (logical formulas with ∧, ∨, ¬, →, ↔) | Module 1 | Thursday, Feb 26 (Checkpoint 2) |
| 3 | Propositional Logic (forward chaining, backward chaining, inference) | Text: Knowledge base from Module 2 | Text: Solution (full assignment) and Proof (inference steps) | Module 2 | Thursday, March 19 (Checkpoint 3) |
| 4 | Propositional Logic (logical entailment, satisfiability checking) | Solution (text), constraints (JSON), knowledge base (text), hidden solution (JSON) | Structured text: Validation result, per-constraint results, entailment check, violation summary | Modules 1, 2, 3 | Thursday, April 2 (Checkpoint 4) |
| 5 | Complexity Analysis | Puzzle structure (JSON), knowledge base (text), solution/proof (text), validation report (text) | Structured text: Explicit difficulty metrics (constraint count, search space size, inference step count, constraint density, logical formula complexity, branching factor, solution uniqueness) with interpretations | Modules 1, 2, 3, 4 | Thursday, April 16 (Checkpoint 5) |
| 6 | Knowledge Representation | Solution/proof (text), knowledge base (text), constraints (JSON), difficulty metrics (text) | Structured text: Overall strategy, step-by-step reasoning explanation | Modules 1, 2, 3, 5 | Thursday, April 23 (Final Demo) |

## Repository Layout

```
project-2-ai-system-tori-madigan/
├── src/                              # main system source code
├── unit_tests/                       # unit tests (parallel structure to src/)
├── integration_tests/                # integration tests (new folder for each module)
├── .claude/skills/code-review/SKILL.md  # rubric-based agent review
├── AGENTS.md                         # instructions for your LLM agent
└── README.md                         # system overview and checkpoints
```

## Setup

List dependencies, setup steps, and any environment variables required to run the system.

## Running

Provide commands or scripts for running modules and demos.

## Testing

**Unit Tests** (`unit_tests/`): Mirror the structure of `src/`. Each module should have corresponding unit tests.

**Integration Tests** (`integration_tests/`): Create a new subfolder for each module beyond the first, demonstrating how modules work together.

Provide commands to run tests and describe any test data needed.

## Checkpoint Log

| Checkpoint | Date | Modules Included | Status | Evidence |
| ---------- | ---- | ---------------- | ------ | -------- |
| 1 | Wednesday, Feb 11 | Module 1 (Puzzle Generator) |  |  |
| 2 | Thursday, Feb 26 | Modules 1-2 (Puzzle Generator, Logic Representation) |  |  |
| 3 | Thursday, March 19 | Modules 1-3 (Puzzle Generator, Logic Representation, Puzzle Solving) |  |  |
| 4 | Thursday, April 2 | Modules 1-4 (All modules through Solution Verification) |  |  |
| 5 | Thursday, April 16 | Modules 1-5 (All modules through Difficulty Analysis) |  |  |
| Final Demo | Thursday, April 23 | Modules 1-6 (Complete system) |  |  |

## Required Workflow (Agent-Guided)

Before each module:

1. Write a short module spec in this README (inputs, outputs, dependencies, tests).
2. Ask the agent to propose a plan in "Plan" mode.
3. Review and edit the plan. You must understand and approve the approach.
4. Implement the module in `src/`.
5. Unit test the module, placing tests in `unit_tests/` (parallel structure to `src/`).
6. For modules beyond the first, add integration tests in `integration_tests/` (new subfolder per module).
7. Run a rubric review using the code-review skill at `.claude/skills/code-review/SKILL.md`.

Keep `AGENTS.md` updated with your module plan, constraints, and links to APIs/data sources.

## Module Specifications

### Module 1: Puzzle Generator

**Topics:** Constraint Satisfaction Problems (CSP)

**Input:** JSON object specifying puzzle parameters:
- `grid_size` (integer): Number of entities in the puzzle (e.g., 5)
- `difficulty` (string): Difficulty level - "easy", "medium", or "hard"

The system automatically determines the number of attributes and values per attribute based on the grid size and difficulty level.

**Output:** JSON object containing:
- `puzzle_id`: Unique identifier for the puzzle
- `entities`: Array of entity identifiers (e.g., ["E1", "E2", ..., "E5"])
- `attributes`: Object mapping attribute names to arrays of possible values
- `constraints`: Array of constraint objects, each containing entity/attribute references and relation information (abstract representation)
- `solution`: Hidden solution object mapping entities to their attribute assignments

The number of constraints is determined automatically based on the difficulty level to ensure solvability and appropriate challenge.

**Integration:** The generated puzzle structure (entities, attributes, constraints) is passed to Module 2 (Logic Representation) where constraints are converted into propositional logic formulas. The hidden solution is used later by Module 4 (Solution Verification).

**Prerequisites:** Course content on Constraint Satisfaction Problems, including constraint representation and satisfaction algorithms. CSP topics are covered as part of Search topics by ~Feb 9, ensuring coverage before Checkpoint 1 (Feb 11).

---

### Module 2: Logic Representation

**Topics:** Propositional Logic (knowledge bases, logical formulas, entailment)

**Input:** JSON object from Module 1 containing:
- `entities`: Array of entity identifiers (e.g., ["E1", "E2", ..., "E5"])
- `attributes`: Object mapping attribute names to arrays of possible values
- `constraints`: Array of constraint objects with entity/attribute references and relation information

Note: The `solution` field from Module 1 is excluded from this input since it is not needed for logic representation.

**Output:** Text format knowledge base containing structured logical formulas:
- **Facts**: Base propositions representing potential assignments, encoded as proposition symbols (e.g., `Has(E1, A1, V2)` becomes proposition `E1_A1_V2`)
- **Rules**: Logical formulas expressing the puzzle constraints, using standard logical connectives (∧, ∨, ¬, →, ↔)

The knowledge base is represented as text using structured logical formulas (e.g., `P ∧ Q → R`, `¬(A ∨ B)`, etc.) where each proposition symbol represents a potential entity-attribute-value assignment.

**Integration:** The knowledge base output is passed to Module 3 (Puzzle Solving), which performs inference on the logical formulas to find the solution. The propositional representation allows Module 3 to use inference methods such as resolution, forward chaining, or model checking.

**Prerequisites:** Module 1 (Puzzle Generator) must provide the puzzle structure. Course content on Propositional Logic, including logical formulas, knowledge bases, and propositional symbols.

---

### Module 3: Puzzle Solving

**Topics:** Propositional Logic (forward chaining, backward chaining, inference)

**Input:** Knowledge base in text format from Module 2, containing structured logical formulas (facts and rules expressed using logical connectives).

**Output:** Text format containing:
- **Solution**: Full assignment mapping each entity to its attribute values, represented as text (e.g., "E1: A1=V2, A2=V4, A3=V1; E2: A1=V1, ..." or propositional format listing all true propositions)
- **Proof**: Logical derivation showing how the solution was inferred from the knowledge base, using forward chaining or backward chaining inference steps

The proof demonstrates the sequence of inference steps that lead from the initial knowledge base to the complete solution.

**Integration:** The solution output is passed to Module 4 (Solution Verification) for validation against the puzzle constraints. The proof is used by Module 6 (Solution Explanation) to generate step-by-step reasoning explanations. If Module 5 (Difficulty Analysis) measures solution complexity, it may also use information about the number of inference steps required.

**Prerequisites:** Module 2 (Logic Representation) must provide the knowledge base. Course content on Propositional Logic inference methods, specifically forward chaining and backward chaining algorithms.

---

### Module 4: Solution Verification

**Topics:** Propositional Logic (logical entailment, satisfiability checking)

**Input:**
- Solution in text format from Module 3 (full assignment mapping entities to attribute values)
- Puzzle constraints from Module 1 (original constraint objects with entity/attribute references)
- Knowledge base in text format from Module 2 (structured logical formulas)
- Hidden solution from Module 1 (for reference comparison during verification)

**Output:** Structured text report containing:
- Overall validation result (VALID or INVALID)
- Per-constraint validation results: For each constraint from Module 1, indicates whether it is satisfied or violated by the solution
- Logical entailment check: Verification that the solution logically entails (or is entailed by) the knowledge base
- Summary of any constraint violations (if invalid)

The report provides detailed information about which specific constraints are satisfied and which are not, enabling identification of solution errors.

**Integration:** The validation report confirms whether Module 3's solution is correct. If valid, the solution can be used by Module 5 (Difficulty Analysis) for measuring puzzle properties. If invalid, the report can inform Module 6 (Solution Explanation) about what went wrong in the solving process. The hidden solution from Module 1 serves as a reference for correctness checking.

**Prerequisites:** Module 1 (Puzzle Generator), Module 2 (Logic Representation), and Module 3 (Puzzle Solving) must be completed. Course content on Propositional Logic entailment and satisfiability checking.

---

### Module 5: Difficulty Analysis

**Topics:** Complexity Analysis (algorithmic complexity, problem space analysis)

**Input:**
- Puzzle structure from Module 1 (entities, attributes, constraints)
- Knowledge base in text format from Module 2 (logical formulas)
- Solution and proof in text format from Module 3 (full assignment and inference steps)
- Validation report in structured text format from Module 4

**Output:** Detailed breakdown in structured text format containing the following explicit difficulty metrics (all computed for every puzzle):
- **Constraint count**: Total number of constraints in the puzzle
- **Search space size**: Total number of possible assignments (product of attribute value counts)
- **Inference step count**: Number of inference steps required in the proof from Module 3
- **Constraint density**: Ratio of constraints to entities (constraints per entity)
- **Logical formula complexity**: Average number of connectives per constraint formula
- **Branching factor**: Average number of possible values per entity-attribute pair at each decision point (computed from proof backtracking if applicable)
- **Solution uniqueness**: Whether the puzzle has a unique solution (binary metric)

Each metric includes its computed value and an interpretation explaining how it contributes to overall puzzle difficulty. The metrics are always computed in this order and format, ensuring consistent analysis across all puzzles.

The output provides a comprehensive analysis of puzzle difficulty from multiple computational and logical perspectives, allowing for nuanced difficulty assessment.

**Integration:** The difficulty analysis informs Module 6 (Solution Explanation) about the puzzle characteristics, which helps explain the overall solution strategy. The analysis also validates that the puzzle generation in Module 1 produces puzzles with the intended difficulty level. The metrics may be used for categorizing puzzles or providing difficulty ratings to users.

**Prerequisites:** Modules 1-4 must be completed to provide all necessary inputs. Course content on Complexity Analysis, including time and space complexity, problem space size, and algorithmic complexity measurement. Complexity analysis concepts are covered throughout the course as a foundational CS/AI topic, with specific algorithmic complexity topics covered by Week 8-10 (by ~March 15), ensuring coverage before Checkpoint 5 (April 16).

---

### Module 6: Solution Explanation

**Topics:** Knowledge Representation (explaining logical reasoning, knowledge structures)

**Input:**
- Solution and proof in text format from Module 3 (full assignment and inference steps)
- Knowledge base in text format from Module 2 (structured logical formulas)
- Puzzle constraints from Module 1 (original constraint objects)
- Difficulty metrics breakdown from Module 5 (multiple complexity measures)

**Output:** Structured text explanation with sections containing:
- **Overall Solution Strategy**: High-level description of the approach used to solve the puzzle, informed by the proof structure and difficulty metrics
- **Step-by-Step Reasoning**: Detailed explanation of each inference step from the proof, showing how logical reasoning led from the initial knowledge base to the solution
- Sections organized by major reasoning phases or constraint applications, with clear explanations of how each step builds on previous knowledge

The explanation translates the formal logical proof into human-readable narrative, showing how the puzzle constraints were logically applied to reach the solution.

**Integration:** The explanation helps users understand how the solution was derived, making the system's reasoning process transparent. It bridges the gap between the formal logical representation (Module 2) and the solved result (Module 3), demonstrating the solving process. The explanation can also be used for educational purposes or debugging when solutions are incorrect.

**Prerequisites:** Modules 1-5 must be completed to provide all necessary inputs. Course content on Knowledge Representation, including how to represent and explain logical reasoning processes and knowledge structures. Knowledge Representation topics are covered as part of Propositional Logic and First-Order Logic by ~Feb 23, ensuring coverage well before the Final Demo (April 23).

---

## Feasibility Study

| Module | Required Topic(s) | Topic Covered By | Checkpoint Due |
| ------ | ----------------- | ---------------- | -------------- |
| 1      | Constraint Satisfaction Problems (CSP) | Covered as part of Search topics (by ~Feb 9) | Wednesday, Feb 11 (Checkpoint 1) |
| 2      | Propositional Logic (knowledge bases, logical formulas) | Week 1-2 (by ~Jan 26) | Thursday, Feb 26 (Checkpoint 2) |
| 3      | Propositional Logic (forward chaining, backward chaining, inference) | Week 1-2 (by ~Jan 26) | Thursday, March 19 (Checkpoint 3) |
| 4      | Propositional Logic (logical entailment, satisfiability checking) | Week 1-2 (by ~Jan 26) | Thursday, April 2 (Checkpoint 4) |
| 5      | Complexity Analysis (algorithmic complexity, problem space analysis) | Ongoing throughout course as foundational CS/AI concept; specific algorithmic complexity topics covered by Week 8-10 (by ~March 15) | Thursday, April 16 (Checkpoint 5) |
| 6      | Knowledge Representation (explaining logical reasoning, knowledge structures) | Covered as part of Propositional Logic and First-Order Logic (by ~Feb 23) | Thursday, April 23 (Final Demo) |

**Note on Module 1**: Module 1 uses Constraint Satisfaction Problems (CSP), not Knowledge Representation. Knowledge Representation is used in Module 6 for generating explanations. CSP topics are covered by ~Feb 9, ensuring coverage before Checkpoint 1.

**Note on Module 5**: Complexity analysis concepts are foundational and covered throughout the course. Specific algorithmic complexity measurement topics needed for Module 5 (time/space complexity, problem space size calculation) are covered by Week 8-10 (by ~March 15), well before Checkpoint 5 (April 16).

## References

List libraries, APIs, datasets, and other references used by the system.
