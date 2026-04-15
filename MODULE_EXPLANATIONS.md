# Modules 1–6: Easy Explanation

This document explains what each pipeline stage does in simple terms: **Module 1** (puzzle generation), **Module 2** (logic representation), **Module 3** (puzzle solving), **Module 4** (solution verification), **Module 5** (complexity analysis), and **Module 6** (solution explanation). Deeper data-flow diagrams live in [`VISUALIZATION_MODULE1.md`](VISUALIZATION_MODULE1.md) through [`VISUALIZATION_MODULE6.md`](VISUALIZATION_MODULE6.md).

---

## Module 1: Puzzle Generator

### What is it?
Module 1 creates logic puzzles. Think of puzzles like "Who owns the zebra?" or "Who lives in the blue house?" - these are logic puzzles where you have to figure out relationships between different things.

### What does it do?
Module 1 automatically creates these puzzles with:
- **Entities**: The things in the puzzle (like people: Person 1, Person 2, Person 3, etc.)
- **Attributes**: The categories we care about (like Color, Pet, Food, etc.)
- **Values**: The options for each category (like Red/Blue/Green for Color, or Dog/Cat/Bird for Pet)
- **Constraints**: The rules that make it a puzzle (like "Person 1 has a red house" or "Person 2 and Person 3 have different pets")

### How does it work?
1. **You tell it the size**: "Make a puzzle with 5 people" (grid_size = 5)
2. **You tell it the difficulty**: "easy", "medium", or "hard"
3. **It creates the puzzle**:
   - Makes 5 entities (E1, E2, E3, E4, E5)
   - Makes 5 attributes (A1, A2, A3, A4, A5)
   - Makes 5 values for each attribute (V1, V2, V3, V4, V5)
   - Creates a valid solution (who has what)
   - Generates constraints (rules) based on the difficulty

### Example Output
```json
{
  "puzzle_id": "puzzle_abc123",
  "entities": ["E1", "E2", "E3", "E4", "E5"],
  "attributes": {
    "A1": ["V1", "V2", "V3", "V4", "V5"],
    "A2": ["V1", "V2", "V3", "V4", "V5"]
  },
  "constraints": [
    {"type": "equality", "entity": "E1", "attribute": "A1", "value": "V3"},
    {"type": "inequality", "entity": "E2", "attribute": "A1", "value": "V1"}
  ],
  "solution": {
    "E1": {"A1": "V3", "A2": "V1"},
    "E2": {"A1": "V1", "A2": "V4"}
  }
}
```

### What are the constraint types?
1. **Equality**: "E1 has value V3 for attribute A1" 
   - Example: "Person 1 has a red house"
2. **Inequality**: "E1 does NOT have value V3 for attribute A1"
   - Example: "Person 1 does NOT have a red house"
3. **Different Values**: "E1 and E2 have different values for attribute A1"
   - Example: "Person 1 and Person 2 have different pets"
4. **Same Value**: "E1 and E2 have the same value for attribute A1"
   - Example: "Person 1 and Person 2 have the same favorite food"
5. **Relative Position**: "E1's value is offset from E2's value"
   - Example: "Person 1's house number is 2 more than Person 2's house number"

### Why is it useful?
- Automatically creates valid, solvable puzzles
- Ensures the puzzle has exactly one correct answer
- Can create puzzles of different difficulty levels
- Provides the hidden solution for later verification

---

## Module 2: Logic Representation

### What is it?
Module 2 takes the puzzle from Module 1 and converts it into formal logic (like math, but for reasoning). It translates the puzzle rules into logical formulas that a computer can use to solve the puzzle.

### What does it do?
Module 2 converts puzzle constraints into propositional logic:
- **Facts**: All possible statements that could be true or false
  - Example: "E1_A1_V2" means "Entity 1 has Value 2 for Attribute 1"
- **Rules**: Logical formulas using symbols like ∧ (AND), ∨ (OR), ¬ (NOT), ↔ (IFF)

### How does it work?
1. **Takes puzzle data from Module 1** (entities, attributes, constraints)
2. **Creates proposition symbols** for every possible combination
   - Format: `E{entity}_A{attribute}_V{value}`
   - Example: `E1_A1_V2` = "Entity 1 has Value 2 for Attribute 1"
3. **Converts each constraint to a logical formula**:
   - "E1 has V3 for A1" → `E1_A1_V3`
   - "E1 does NOT have V3 for A1" → `¬E1_A1_V3`
   - "E1 and E2 have different values" → `¬(E1_A1_V1 ↔ E2_A1_V1) ∧ ¬(E1_A1_V2 ↔ E2_A1_V2) ...`
4. **Creates domain constraints** (rules that are always true):
   - Each entity must have exactly one value per attribute
   - Example: "E1 must have V1 OR V2 OR V3 for A1, but not more than one"

### Example Output
```
=== KNOWLEDGE BASE ===

FACTS (All possible propositions):
E1_A1_V1, E1_A1_V2, E1_A1_V3, E2_A1_V1, E2_A1_V2, E2_A1_V3, ...

RULES (Domain Constraints):
1. (E1_A1_V1 ∨ E1_A1_V2 ∨ E1_A1_V3) ∧ (¬(E1_A1_V1 ∧ E1_A1_V2) ∧ ...)
   Translation: "E1 must have V1 OR V2 OR V3 for A1, but can't have two at once"

RULES (Puzzle Constraints):
1. E1_A1_V3
   Translation: "E1 has V3 for A1"
2. ¬E2_A1_V1
   Translation: "E2 does NOT have V1 for A1"
```

### What do the symbols mean?
- **∧ (AND)**: Both statements must be true
  - Example: `A ∧ B` means "A is true AND B is true"
- **∨ (OR)**: At least one statement must be true
  - Example: `A ∨ B` means "A is true OR B is true (or both)"
- **¬ (NOT)**: The statement is false
  - Example: `¬A` means "A is NOT true"
- **↔ (IFF - if and only if)**: Both statements have the same truth value
  - Example: `A ↔ B` means "A is true if and only if B is true"

### Why is it useful?
- Converts puzzle rules into a format that computers can reason about
- Enables automated puzzle solving (Module 3)
- Makes it possible to verify solutions mathematically (Module 4)
- Provides a formal representation for analysis

---

## Module 3: Puzzle Solving

### What is it?
Module 3 is the **solver**. It reads the **knowledge base** text that Module 2 produced and figures out a **complete assignment**: for every entity and every attribute, which value is chosen. It also writes a **proof**—a numbered list of steps showing how it got there (deductions from the rules, and sometimes explicit “decisions” when it has to try possibilities).

### What does it do?
- **Input**: The same kind of text Module 2 outputs (`=== KNOWLEDGE BASE ===`, FACTS, RULES including **Puzzle Constraints**).
- **Processing**:
  - Rebuilds which entities, attributes, and values exist from the **FACTS** section.
  - Reads each numbered puzzle rule (equality, inequality, different values, same value, relative position, etc.) and applies it to narrow down possibilities.
  - Uses **forward-chaining-style** reasoning: repeatedly shrink what’s possible for each cell until no more forced moves remain.
  - If the puzzle still isn’t fully decided, it uses **search with backtracking** (try a value, recurse, undo if it leads to a contradiction).
- **Output**: A text block with:
  - **`=== SOLUTION ===`** — lines like `E1: A1=V3, A2=V1, ...` for every entity.
  - **`INFERENCE STEP COUNT:`** — how many proof lines were recorded.
  - **`=== PROOF ===`** — numbered steps tagged `[deduction]` (forced by rules) or `[decision]` (search choice).

### How does it work? (step by step)
1. **Parse the knowledge base** — find the FACTS list and the **RULES (Puzzle Constraints)** section.
2. **Build a “domain” for each cell** — for pair (entity, attribute), start with all values that appear in FACTS (e.g. V1…Vn).
3. **Apply puzzle constraints** — e.g. “E1 must be V3 for A1” forces that cell to `{V3}`; “E1 and E2 differ on A1” removes shared values when one side is already fixed; relative-position rules link two cells’ numeric indices.
4. **Repeat** until nothing changes (fixpoint), then **branch** if some cells still have multiple options.
5. **Format** the final grid and the proof as readable text.

### Example Output (shape only; your puzzle will differ)
```
=== SOLUTION ===
E1: A1=V2, A2=V1
E2: A1=V1, A2=V2

INFERENCE STEP COUNT: 3

=== PROOF ===
1. [deduction] E1 A1 must be V2
2. [deduction] E2 A1 becomes V1
3. [decision] set E2 A2 = V2
```

### Why is it useful?
- **Automates solving** from the formal representation Module 2 built.
- **Shows your work** — the proof supports demos, grading, and later modules (e.g. explanations, difficulty metrics).
- **Feeds the next stage** — Module 4 can check this solution against constraints and logic.

### How do you run it in code?
```python
from module2_logic_representation import module1_to_module2
from module3_puzzle_solving import module2_to_module3

kb = module1_to_module2(puzzle_dict)   # JSON/dict from Module 1 (no need to pass solution to Module 2)
answer = module2_to_module3(kb)       # full text: solution + proof
```

**Hand-crafted puzzle examples** (stories + JSON + pipeline snippet) live in [`examples/LOGIC_PUZZLE_EXAMPLES.md`](examples/LOGIC_PUZZLE_EXAMPLES.md), with copy-paste JSON under [`examples/puzzles/`](examples/puzzles/).

---

## Module 4: Solution Verification

### What is it?
Module 4 is the **checker/validator**. It takes a proposed solution (usually from Module 3) and verifies whether that solution actually satisfies the puzzle constraints and is logically consistent with the knowledge base.

### What does it do?
- **Input**:
  - Solution text from Module 3
  - Original constraints from Module 1
  - Knowledge base text from Module 2
  - (Optional but useful) hidden solution from Module 1 for direct comparison
- **Processing**:
  - Parses the solved assignment into structured data
  - Checks each original constraint one by one (pass/fail)
  - Performs consistency checks against logical statements in the KB
  - Summarizes violations if any rule is broken
- **Output**:
  - A structured validation report with:
    - overall valid/invalid result
    - per-constraint results
    - entailment/consistency status
    - violation summary

### How does it work? (step by step)
1. **Read the candidate solution** and convert lines like `E1: A1=V2, A2=V1` into a dictionary.
2. **Re-check puzzle constraints** from Module 1:
   - equality/inequality
   - same-value / different-values
   - relative-position rules
3. **Cross-check with logic representation** from Module 2 to ensure no contradiction with required formulas.
4. **Report results clearly**:
   - If everything passes, mark solution as valid.
   - If not, list exactly which constraints failed and why.

### Example Output (shape only)
```
=== VALIDATION REPORT ===
Overall: VALID

Constraint checks:
1. equality(E1,A1,V2): PASS
2. inequality(E2,A3,V1): PASS
3. different_values(E1,E2,A2): PASS

Logical consistency:
Knowledge-base consistency: PASS
Entailment status: PASS

Violations: none
```

### Why is it useful?
- Confirms that Module 3’s answer is not just complete, but actually **correct**.
- Catches subtle errors (formatting mistakes, violated constraints, inconsistent assignments).
- Produces evidence for checkpoint demos and grading.
- Provides clean input for later analysis modules (difficulty metrics and explanations).

---

## Module 5: Complexity Analysis

### What is it?
Module 5 measures **how hard the puzzle was to solve** from several angles—not by guessing, but by computing explicit numbers (constraint count, size of the raw search space, how many inference lines were in the proof, how “dense” clues are, how complex the logical formulas are, an estimated branching factor, and whether the KB has a unique solution). It can also fold those into an **overall difficulty score** (optionally compared to a saved list of past puzzles).

### What does it do?
- **Input**:
  - Puzzle structure from Module 1 (JSON/dict)
  - Knowledge base text from Module 2
  - Solution + proof text from Module 3
  - Validation report text from Module 4 (so it knows if upstream said VALID)
- **Output**: A readable **complexity report** listing each metric, its value, and a short **interpretation** (e.g. “large search space; pruning matters”), plus an overall difficulty label when scoring is enabled.

### Why is it useful?
- Makes tradeoffs visible (many clues vs huge search space vs long proofs).
- Gives Module 6 a compact **difficulty story** to mention in the “overall strategy” part of the explanation.

### How do you run it in code?
```python
from module4_solution_verification import module1_2_3_to_module4
from module5_complexity_analysis import module1_2_3_4_to_module5

m4_report = module1_2_3_to_module4(module3_text, puzzle_dict, kb_text)
m5_report = module1_2_3_4_to_module5(puzzle_dict, kb_text, module3_text, m4_report)
```

**See also:** [`VISUALIZATION_MODULE5.md`](VISUALIZATION_MODULE5.md)

---

## Module 6: Solution Explanation

### What is it?
Module 6 is the **narrator**. It does not re-solve the puzzle; it reads the **formal proof** from Module 3, the **clue list** from Module 1, the fact that rules live in the **knowledge base** from Module 2, and the **complexity report** from Module 5, then writes a **human-readable explanation** with two parts: a high-level **overall strategy** and **step-by-step reasoning** that walks through each proof line.

### What does it do?
- **Input**: Module 1 puzzle (dict/JSON), Module 2 KB text, Module 3 output (solution + proof), Module 5 complexity report text.
- **Output**: Structured text with sections like `=== OVERALL SOLUTION STRATEGY ===` and `=== STEP-BY-STEP REASONING ===`, paraphrasing `[deduction]` and `[decision]` lines from the proof.

### Why is it useful?
- Connects **formal logic** (symbols and rules) to **plain language** for demos, teaching, and debugging.
- Satisfies the “knowledge representation / explanation” role: explaining *how* the system reasoned, not only *what* answer it picked.

### How do you run it in code?
```python
from module6_solution_explanation import module1_2_3_5_to_module6

explanation = module1_2_3_5_to_module6(
    puzzle_dict,
    kb_text,
    module3_text,
    m5_report_text,
)
```

**See also:** [`VISUALIZATION_MODULE6.md`](VISUALIZATION_MODULE6.md)

---

## How They Work Together

### The Pipeline:
1. **Module 1** creates a puzzle:
   ```
   Input: grid_size=5, difficulty="medium"
   Output: JSON with entities, attributes, constraints, and hidden solution
   ```

2. **Module 2** converts it to logic:
   ```
   Input: JSON from Module 1
   Output: Text knowledge base with facts and logical formulas
   ```

3. **Module 3** solves it using that knowledge base:
   ```
   Input: Text knowledge base from Module 2
   Output: Text solution (full assignment) + proof (inference steps)
   ```

4. **Module 4** verifies the solved result:
   ```
   Input: Solution/proof text + constraints + knowledge base (+ optional hidden solution)
   Output: Structured validation report (pass/fail + per-constraint checks)
   ```

5. **Module 5** analyzes difficulty:
   ```
   Input: Puzzle JSON + KB + Module 3 text + Module 4 report text
   Output: Complexity report (metrics + interpretations + overall difficulty scoring)
   ```

6. **Module 6** explains the reasoning:
   ```
   Input: Puzzle JSON + KB + Module 3 text + Module 5 report text
   Output: Narrative explanation (strategy + step-by-step)
   ```

### Real-World Analogy:
Think of it like building a house:
- **Module 1** = The architect who designs the house (creates the puzzle structure)
- **Module 2** = The blueprint translator who converts the design into technical drawings (converts puzzle to logic)
- **Module 3** = The builder who constructs the house (fills in the actual assignment and documents each major step)
- **Module 4** = The inspector who checks the finished house against code and plans (verifies every rule)
- **Module 5** = The energy auditor who measures square footage, materials, and workload (quantifies difficulty)
- **Module 6** = The walkthrough guide who explains to the owner how construction decisions followed from the plans (turns the formal record into a story)

---

## Key Concepts Explained Simply

### What is a Constraint Satisfaction Problem (CSP)?
A problem where you need to find values for variables that satisfy all the given rules (constraints). Like a Sudoku puzzle - you need to fill in numbers that follow all the rules.

### What is Propositional Logic?
A way of representing statements and their relationships using symbols. It's like algebra, but instead of numbers, you work with true/false statements.

### What is a Knowledge Base?
A collection of facts and rules that represent what we know about a problem. It's like a database of information that can be used for reasoning.

---

## Common Questions

**Q: Why do we need Module 2? Can't we just solve the puzzle directly?**
A: Module 2 converts the puzzle into a formal logical format that allows for automated reasoning. This makes it possible to use AI techniques like forward chaining or backward chaining to solve the puzzle systematically.

**Q: What happens if the puzzle is unsolvable?**
A: Module 1 ensures puzzles are solvable by generating constraints from a known solution. This guarantees at least one solution exists.

**Q: Why use symbols like ∧ and ∨ instead of words?**
A: These are standard mathematical/logical symbols that are universally understood in formal logic. They make the formulas more compact and precise.

**Q: Can I understand the output without knowing logic?**
A: Yes! The proposition symbols (like E1_A1_V2) are readable - they just say "Entity 1 has Value 2 for Attribute 1". The logical formulas are more complex, but you can think of them as rules written in a special language.

**Q: What does Module 3’s proof mean?**
A: Each line is either a **[deduction]** (something the rules forced) or a **[decision]** (the solver picked a value because propagation wasn’t enough). Together they explain *how* the final grid was reached.

**Q: Will Module 3’s answer always match Module 1’s hidden solution?**
A: Not necessarily. Module 3 finds *a* assignment that satisfies the puzzle constraints encoded in Module 2. If many grids satisfy those rules, it might pick a different one than Module 1’s internal solution. Module 4 checks whether the candidate answer is valid under the constraints and can also compare against the hidden solution when provided.

---

## Summary

- **Module 1**: Creates logic puzzles automatically
- **Module 2**: Converts puzzles into formal logic that computers can reason about
- **Module 3**: Solves the knowledge base and returns a full solution plus an inference-style proof
- **Module 4**: Verifies the proposed solution against constraints and logic, then reports pass/fail details
- **Module 5**: Computes difficulty metrics and interpretations (and optional overall scoring)
- **Module 6**: Produces a readable explanation of strategy and proof steps for people
- **Together**: They form a pipeline from puzzle generation → logic → solving → verification → analysis → explanation

These six modules transform a puzzle description into a formal logical system, a solved assignment with proof, a validation report, quantitative difficulty analysis, and a narrative explanation suitable for demos and teaching.
