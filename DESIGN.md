# Module 1 Design Decisions

## Overview
This document outlines the design decisions for Module 1: Puzzle Generator.

## Design Questions & Decisions

### 1. Puzzle Structure

**Question:** How should entities, attributes, and values be structured?

**Decision:**
- **Entities**: Named as "E1", "E2", ..., "En" where n = grid_size
- **Attributes**: Number of attributes = grid_size (creates square grid)
  - Named as "A1", "A2", ..., "An"
- **Values per Attribute**: Equal to grid_size
  - For attribute Ai, values are "V1", "V2", ..., "Vn"
- **Rationale**: Square grid ensures each entity has exactly one value for each attribute, creating a classic logic puzzle structure

**Example for grid_size=5:**
- Entities: ["E1", "E2", "E3", "E4", "E5"]
- Attributes: {"A1": ["V1", "V2", "V3", "V4", "V5"], "A2": [...], ...}
- Solution: Each entity gets exactly one value per attribute

---

### 2. Constraint Types

**Question:** What types of constraints should the system support?

**Decision:**
Support the following constraint types:

1. **Equality Constraint**: "Entity E1 has value V3 for attribute A1"
   - Format: `{"type": "equality", "entity": "E1", "attribute": "A1", "value": "V3"}`

2. **Inequality Constraint**: "Entity E1 does NOT have value V3 for attribute A1"
   - Format: `{"type": "inequality", "entity": "E1", "attribute": "A1", "value": "V3"}`

3. **Different Values Constraint**: "Entities E1 and E2 have different values for attribute A1"
   - Format: `{"type": "different_values", "entities": ["E1", "E2"], "attribute": "A1"}`

4. **Same Value Constraint**: "Entities E1 and E2 have the same value for attribute A1"
   - Format: `{"type": "same_value", "entities": ["E1", "E2"], "attribute": "A1"}`

5. **Relative Position Constraint**: "Entity E1's value for A1 is one more than E2's value for A1"
   - Format: `{"type": "relative_position", "entity1": "E1", "entity2": "E2", "attribute": "A1", "offset": 1}`

**Rationale**: These constraint types cover common logic puzzle patterns while remaining simple enough to convert to propositional logic in Module 2.

---

### 3. Difficulty Scaling

**Question:** How should constraint counts and complexity scale with difficulty?

**Decision:**

| Difficulty | Constraint Count | Constraint Types | Notes |
|------------|----------------|------------------|-------|
| **Easy** | grid_size × 1.5 (rounded) | Primarily equality, inequality | Simple, direct constraints |
| **Medium** | grid_size × 2.5 (rounded) | Mix of all types | Balanced complexity |
| **Hard** | grid_size × 3.5 (rounded) | All types, including relative position | Complex relationships |

**Examples:**
- grid_size=5, Easy: ~8 constraints
- grid_size=5, Medium: ~13 constraints
- grid_size=5, Hard: ~18 constraints

**Rationale**: 
- Easy puzzles have fewer constraints, making them more straightforward
- Medium puzzles have moderate constraint density
- Hard puzzles have high constraint density and complex relationships

---

### 4. Puzzle Generation Algorithm

**Question:** How should puzzles be generated?

**Decision:** Use a **"Solution-First" approach**:

1. **Generate a valid solution first**:
   - Randomly assign each entity one value per attribute
   - Ensure no two entities have the same value for the same attribute (uniqueness constraint)

2. **Generate constraints based on solution**:
   - For each constraint to generate:
     - Randomly select constraint type based on difficulty
     - Randomly select entities/attributes involved
     - Ensure constraint is consistent with the solution
     - Add constraint to list

3. **Validate solvability** (optional but recommended):
   - Use a simple CSP solver to verify puzzle has unique solution
   - If not unique, add more constraints or regenerate

**Alternative considered:** Template-based generation - rejected because it's less flexible and harder to ensure solvability.

**Rationale**: Solution-first ensures we always have a valid solution, and constraints are guaranteed to be satisfiable.

---

### 5. Solvability Guarantee

**Question:** How do we ensure puzzles are solvable?

**Decision:** 
- **Primary method**: Generate constraints from a known solution (solution-first approach)
- **Validation**: After generation, verify the puzzle has exactly one solution
  - If multiple solutions: Add more constraints
  - If no solution: Regenerate (shouldn't happen with solution-first)
- **Fallback**: If validation fails after 3 attempts, use a simpler constraint set

**Rationale**: Solution-first generation guarantees at least one solution exists. Validation ensures uniqueness and appropriate difficulty.

---

### 6. Puzzle ID Generation

**Question:** How should unique puzzle IDs be generated?

**Decision:**
- Use UUID4 for uniqueness
- Format: `"puzzle_<uuid>"` (e.g., "puzzle_550e8400-e29b-41d4-a716-446655440000")
- Alternative: Timestamp-based if UUID not available

---

### 7. Output Format Details

**Question:** Exact JSON structure for output?

**Decision:**
```json
{
  "puzzle_id": "puzzle_<uuid>",
  "entities": ["E1", "E2", ..., "En"],
  "attributes": {
    "A1": ["V1", "V2", ..., "Vn"],
    "A2": ["V1", "V2", ..., "Vn"],
    ...
  },
  "constraints": [
    {
      "type": "equality",
      "entity": "E1",
      "attribute": "A1",
      "value": "V3"
    },
    ...
  ],
  "solution": {
    "E1": {"A1": "V3", "A2": "V1", ...},
    "E2": {"A1": "V1", "A2": "V4", ...},
    ...
  }
}
```

---

## Implementation Plan

### Step 1: Core Data Structures
- Create Puzzle class/dataclass
- Create Constraint class/dataclass
- Create Solution representation

### Step 2: Solution Generation
- Generate random valid solution
- Ensure uniqueness (no two entities share same value for same attribute)

### Step 3: Constraint Generation
- Implement each constraint type
- Generate constraints based on difficulty
- Ensure constraints are consistent with solution

### Step 4: Validation
- Implement simple CSP solver for validation
- Verify solution uniqueness

### Step 5: Output Formatting
- Serialize to JSON
- Generate puzzle_id

---

## Open Questions / To Discuss

1. Should we support custom constraint types beyond the 5 listed?
2. Should difficulty affect which constraint types are used, or just the count?
3. Do we need a minimum constraint count to ensure solvability?
4. Should we allow puzzles with multiple solutions, or always enforce uniqueness?

---

## Next Steps

1. Review and approve these design decisions
2. Implement core data structures
3. Implement solution generation
4. Implement constraint generation
5. Add validation
6. Test with various grid sizes and difficulties
