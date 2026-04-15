# Module 6 — I/O contract (locked to current pipeline)

This document fixes **inputs and output shape** for Module 6 (Solution Explanation) using the **actual** formats produced by `src/module1`–`module5`. Use it as the single source of truth before writing `src/module6_*.py`.

**Course requirement:** human-readable explanations derived from the **formal proof** (Module 3), informed by the KB (Module 2), puzzle constraints (Module 1), and difficulty context (Module 5).

---

## Inputs (four artifacts)

| # | Source | Type | Role for Module 6 |
|---|--------|------|-------------------|
| 1 | Module 1 | `dict` **or** JSON `str` | `entities`, `attributes`, `constraints` — name constraint types and relate explanation to clues |
| 2 | Module 2 | `str` | Full knowledge base text (facts + domain rules + puzzle rules) |
| 3 | Module 3 | `str` | Solution block + inference count + numbered proof lines |
| 4 | Module 5 | `str` | Complexity report text (overall difficulty + metric interpretations) |

**Parsing note:** Module 1 may be passed as a Python dict (same as `puzzle.to_dict()`) or a JSON string; Module 6 should accept `str | dict` and normalize with `json.loads` when needed.

---

## Module 1 — puzzle JSON (constraints)

- **Required keys:** `entities` (list), `attributes` (dict of attr → list of values), `constraints` (list of dicts).
- **Constraint objects** match `Constraint.to_dict()` in `module1_puzzle_generator.py`:
  - `type`: `"equality"` | `"inequality"` | `"different_values"` | `"same_value"` | `"relative_position"`
  - Always: `"attribute"`
  - Type-specific: `entity`, `value`, `entities`, `entity1`, `entity2`, `offset`, etc.

Module 6 uses this to say *which kind of clue* each step supports (natural language), not to re-solve the puzzle.

---

## Module 2 — knowledge base text

Canonical structure from `module2_logic_representation.create_knowledge_base`:

```text
=== KNOWLEDGE BASE ===

FACTS (All possible propositions):
<comma-separated E#_A#_V# symbols>

RULES (Domain Constraints):
1. <formula>
2. <formula>
...

RULES (Puzzle Constraints):
1. <formula>
2. <formula>
...
```

Section markers are stable; Module 3 already depends on `FACTS (All possible propositions):`, `RULES (Domain Constraints):`, and `RULES (Puzzle Constraints):`.

---

## Module 3 — solution + proof text

Canonical structure from `module3_puzzle_solving.module2_to_module3` (see module docstring and implementation):

```text
=== SOLUTION ===
E1: A1=V2, A2=V3, ...
E2: ...

INFERENCE STEP COUNT: <n>
=== PROOF ===
1. [deduction] ...
2. [decision] set E1 A1 = V2
...
```

**Proof line patterns (stable strings today):**

- Deduction steps start with `[deduction]` (human-readable tail varies by constraint type).
- Search branching steps start with `[decision] set <entity> <attribute> = <value>`.

Module 6 should **iterate numbered lines under `=== PROOF ===`** (after the header) and treat `INFERENCE STEP COUNT` as the authoritative count of proof lines (same as Module 5).

---

## Module 5 — complexity report text

Canonical human-readable report from `module5_complexity_analysis.complexity_dict_to_text` begins with:

```text
=== COMPLEXITY ANALYSIS REPORT ===
OVERALL COMPLEXITY STATUS: ...
UPSTREAM VALIDATION PASS: ...
OVERALL DIFFICULTY SCORE (0-100): ...
OVERALL DIFFICULTY LABEL: ...

METRICS:
- constraint_count: ...
  interpretation: ...
...
```

Module 6 should **read this as opaque text** for the “Overall Solution Strategy” section (difficulty label, key metrics, interpretations), without re-implementing metrics.

---

## Output — Module 6 structured text

**Deliverable:** one string with **at least** these top-level sections (headings literal for easy tests):

1. **`## Overall Solution Strategy`** (or `=== OVERALL SOLUTION STRATEGY ===` — pick one convention and keep it)

   - Short narrative: how the solver approached the puzzle, informed by Module 5 (difficulty / search space / inference effort) and by whether the proof contains `[decision]` steps (search) vs mostly `[deduction]`.

2. **`## Step-by-Step Reasoning`** (or `=== STEP-BY-STEP REASONING ===`)

   - For each proof line `i.` under `=== PROOF ===`, one explanation block that paraphrases the step and ties it to **constraint types** from Module 1 where possible.

Optional third section for debugging/education: invalid upstream state — **not required** if Module 4 validation is assumed valid for the demo path.

---

## Suggested Python signature (next step)

```python
def module1_2_3_5_to_module6(
    puzzle_structure: dict | str,
    knowledge_base: str,
    solution_proof_text: str,
    complexity_report_text: str,
) -> str: ...
```

Internal helpers (private): parse M3 into `(solution_lines, proof_lines, inference_count)`, optionally index M1 constraints by type.

---

## Verification

- **Unit tests:** small fixed strings for KB + proof + complexity; assert output contains both main sections and N step paragraphs matching N proof lines.
- **Integration test:** `generate_puzzle` → `module1_to_module2` → `module2_to_module3` → `module1_2_3_4_to_module4` (if needed for valid M5) → `module1_2_3_4_to_module5` or `analyze_to_dict` + `complexity_dict_to_text` → Module 6.

This file completes **step 1: lock the contract**. Implementation starts with parsers that match the formats above.
