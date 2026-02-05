# Module 2 Design Decisions: Logic Representation

## Overview
Module 2 converts puzzle constraints from Module 1 into propositional logic knowledge bases.

## Requirements

**Input:** JSON from Module 1
- `entities`: ["E1", "E2", ..., "En"]
- `attributes`: {"A1": ["V1", "V2", ...], ...}
- `constraints`: Array of constraint objects

**Output:** Text format knowledge base
- **Facts**: Base propositions (e.g., `E1_A1_V2`)
- **Rules**: Logical formulas using connectives (∧, ∨, ¬, →, ↔)

## Design Decisions

### 1. Proposition Symbol Encoding

**Decision:** Use format `E{entity}_A{attribute}_V{value}`

**Examples:**
- `E1_A1_V2` means "Entity E1 has value V2 for attribute A1"
- `E2_A3_V1` means "Entity E2 has value V1 for attribute A3"

**Rationale:** 
- Clear and unambiguous
- Easy to parse
- Matches the pattern from the specification

### 2. Constraint Type Conversions

#### Equality Constraint
**Input:** `{"type": "equality", "entity": "E1", "attribute": "A1", "value": "V3"}`

**Output:** `E1_A1_V3`

**Rationale:** Direct proposition - if true, E1 has V3 for A1.

#### Inequality Constraint
**Input:** `{"type": "inequality", "entity": "E1", "attribute": "A1", "value": "V3"}`

**Output:** `¬E1_A1_V3`

**Rationale:** Negation of the proposition.

#### Different Values Constraint
**Input:** `{"type": "different_values", "entities": ["E1", "E2"], "attribute": "A1"}`

**Output:** For each possible value V:
- `(E1_A1_V1 ∧ ¬E2_A1_V1) ∨ (E1_A1_V2 ∧ ¬E2_A1_V2) ∨ ... ∨ (E1_A1_Vn ∧ ¬E2_A1_Vn)`

**Alternative (more concise):**
- `¬(E1_A1_V1 ↔ E2_A1_V1) ∧ ¬(E1_A1_V2 ↔ E2_A1_V2) ∧ ... ∧ ¬(E1_A1_Vn ↔ E2_A1_Vn)`

**Decision:** Use the alternative (biconditional negation) as it's more compact and expresses "not the same" directly.

**Rationale:** 
- More concise
- Uses biconditional (↔) as required
- Clear logical meaning: "E1 and E2 do not have the same value"

#### Same Value Constraint
**Input:** `{"type": "same_value", "entities": ["E1", "E2"], "attribute": "A1"}`

**Output:** `(E1_A1_V1 ↔ E2_A1_V1) ∨ (E1_A1_V2 ↔ E2_A1_V2) ∨ ... ∨ (E1_A1_Vn ↔ E2_A1_Vn)`

**Rationale:** 
- Uses biconditional (↔) to express "same value"
- Disjunction covers all possible values

#### Relative Position Constraint
**Input:** `{"type": "relative_position", "entity1": "E1", "entity2": "E2", "attribute": "A1", "offset": 1}`

**Output:** For offset = 1 (E1's value is 1 more than E2's):
- `(E1_A1_V2 ∧ E2_A1_V1) ∨ (E1_A1_V3 ∧ E2_A1_V2) ∨ ... ∨ (E1_A1_Vn ∧ E2_A1_V{n-1})`

**General formula:** For offset = k:
- `(E1_A1_V{k+1} ∧ E2_A1_V1) ∨ (E1_A1_V{k+2} ∧ E2_A1_V2) ∨ ... ∨ (E1_A1_Vn ∧ E2_A1_V{n-k})`

**Rationale:**
- Expresses the relationship using conjunction and disjunction
- Covers all valid value pairs

### 3. Knowledge Base Structure

**Format:**
```
FACTS:
E1_A1_V1
E1_A1_V2
...
E1_A1_Vn
E1_A2_V1
...
En_Am_Vn

RULES:
[Constraint 1 formula]
[Constraint 2 formula]
...
```

**Alternative (more structured):**
```
=== KNOWLEDGE BASE ===

FACTS (All possible propositions):
E1_A1_V1, E1_A1_V2, ..., E1_A1_Vn
E1_A2_V1, E1_A2_V2, ..., E1_A2_Vn
...
En_Am_V1, En_Am_V2, ..., En_Am_Vn

RULES (Constraints):
1. [formula for constraint 1]
2. [formula for constraint 2]
...
```

**Decision:** Use structured format with clear sections.

### 4. Additional Constraints (Implicit Facts)

**Question:** Should we include implicit constraints like "each entity has exactly one value per attribute"?

**Decision:** YES - Include these as rules:
- For each entity E and attribute A: `(E_A_V1 ∨ E_A_V2 ∨ ... ∨ E_A_Vn)` - at least one value
- For each entity E, attribute A, and distinct values Vi, Vj: `¬(E_A_Vi ∧ E_A_Vj)` - at most one value

**Combined:** `(E_A_V1 ∨ E_A_V2 ∨ ... ∨ E_A_Vn) ∧ ¬(E_A_V1 ∧ E_A_V2) ∧ ¬(E_A_V1 ∧ E_A_V3) ∧ ...`

**Rationale:**
- Ensures completeness of the knowledge base
- Makes the puzzle constraints explicit
- Helps Module 3 (solving) understand the domain

### 5. Output Format Details

**Text Format Structure:**
```
=== KNOWLEDGE BASE ===

FACTS (All possible propositions):
[List all E_A_V propositions, one per line or comma-separated]

RULES (Domain Constraints):
[Implicit constraints about one value per attribute]

RULES (Puzzle Constraints):
[Explicit constraints from Module 1]
```

## Implementation Plan

### Step 1: Proposition Symbol Generation
- Function: `generate_proposition_symbol(entity, attribute, value) -> str`
- Returns: `E{entity}_A{attribute}_V{value}`

### Step 2: Constraint to Formula Conversion
- Function: `constraint_to_formula(constraint, attributes) -> str`
- Handles each constraint type
- Returns logical formula string

### Step 3: Implicit Constraint Generation
- Function: `generate_implicit_constraints(entities, attributes) -> List[str]`
- Generates "exactly one value per attribute" constraints

### Step 4: Knowledge Base Assembly
- Function: `create_knowledge_base(puzzle_data) -> str`
- Takes Module 1 JSON output
- Assembles facts and rules
- Returns formatted text

### Step 5: Integration
- Function: `module1_to_module2(puzzle_json) -> str`
- Main entry point
- Reads Module 1 output, generates knowledge base

## Example Output

For a simple puzzle with 2 entities, 1 attribute, 2 values:

```
=== KNOWLEDGE BASE ===

FACTS (All possible propositions):
E1_A1_V1, E1_A1_V2, E2_A1_V1, E2_A1_V2

RULES (Domain Constraints):
(E1_A1_V1 ∨ E1_A1_V2) ∧ ¬(E1_A1_V1 ∧ E1_A1_V2)
(E2_A1_V1 ∨ E2_A1_V2) ∧ ¬(E2_A1_V1 ∧ E2_A1_V2)

RULES (Puzzle Constraints):
1. E1_A1_V1
2. ¬(E1_A1_V1 ↔ E2_A1_V1) ∧ ¬(E1_A1_V2 ↔ E2_A1_V2)
```

## Open Questions

1. Should we simplify formulas (e.g., distribute negations)?
2. Should we use parentheses for clarity or minimal parentheses?
3. How to handle very long formulas (line breaks, formatting)?
