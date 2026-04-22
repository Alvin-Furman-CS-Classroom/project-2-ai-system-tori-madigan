"""
Module 1: Puzzle Generator

This module generates logic puzzles (like "Who owns the zebra?" puzzles) using
Constraint Satisfaction Problem (CSP) techniques.

WHAT IT DOES:
- Creates a puzzle with entities (people, houses, etc.), attributes (color, pet, etc.),
  and values (red, blue, dog, cat, etc.)
- Generates constraints (rules) that define relationships between entities
- Creates a hidden solution that satisfies all constraints

BASIC USAGE (Python):
    from src.module1_puzzle_generator import generate_puzzle

    puzzle = generate_puzzle(grid_size=5, difficulty="medium")
    puzzle_json = puzzle.to_json()

    # To feed into Module 2 (logic representation):
    # from src.module2_logic_representation import module1_to_module2
    # kb_text = module1_to_module2(puzzle_json)

CLI USAGE:
    python -m src.module1_puzzle_generator --grid_size 5 --difficulty medium
"""

import argparse
import json
import random
import time
import uuid
from dataclasses import dataclass, field
from itertools import combinations
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class Constraint:
    """
    Represents a constraint in the logic puzzle.
    
    Supported types:
    - equality: entity has specific value for attribute
    - inequality: entity does NOT have specific value for attribute
    - different_values: two entities have different values for same attribute
    - same_value: two entities have same value for same attribute
    - relative_position: entity1's value is offset from entity2's value
    """
    type: str  # "equality", "inequality", "different_values", "same_value", "relative_position"
    entity: Optional[str] = None  # For equality, inequality, relative_position
    entity1: Optional[str] = None  # For relative_position (alternative to entity)
    entity2: Optional[str] = None  # For relative_position, different_values, same_value
    entities: Optional[List[str]] = None  # For different_values, same_value
    attribute: str = ""
    value: Optional[str] = None  # For equality, inequality
    offset: Optional[int] = None  # For relative_position
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert constraint to dictionary for JSON serialization."""
        result = {"type": self.type, "attribute": self.attribute}
        
        if self.type in ["equality", "inequality"]:
            result["entity"] = self.entity
            result["value"] = self.value
        elif self.type in ["different_values", "same_value"]:
            result["entities"] = self.entities
        elif self.type == "relative_position":
            # Use entity1/entity2 if available, otherwise entity/entity2
            if self.entity1 and self.entity2:
                result["entity1"] = self.entity1
                result["entity2"] = self.entity2
            elif self.entity and self.entity2:
                result["entity1"] = self.entity
                result["entity2"] = self.entity2
            result["offset"] = self.offset
        
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Constraint':
        """Create constraint from dictionary."""
        constraint_type = data["type"]
        
        if constraint_type in ["equality", "inequality"]:
            return cls(
                type=constraint_type,
                entity=data["entity"],
                attribute=data["attribute"],
                value=data["value"]
            )
        elif constraint_type in ["different_values", "same_value"]:
            return cls(
                type=constraint_type,
                entities=data["entities"],
                attribute=data["attribute"]
            )
        elif constraint_type == "relative_position":
            return cls(
                type=constraint_type,
                entity1=data.get("entity1"),
                entity2=data["entity2"],
                attribute=data["attribute"],
                offset=data["offset"]
            )
        else:
            raise ValueError(f"Unknown constraint type: {constraint_type}")


@dataclass
class Solution:
    """
    Represents the solution to a puzzle.
    Maps each entity to its attribute-value assignments.
    """
    assignments: Dict[str, Dict[str, str]] = field(default_factory=dict)
    # Format: {"E1": {"A1": "V3", "A2": "V1", ...}, ...}
    
    def get_value(self, entity: str, attribute: str) -> Optional[str]:
        """Get the value assigned to an entity for a given attribute."""
        return self.assignments.get(entity, {}).get(attribute)
    
    def set_value(self, entity: str, attribute: str, value: str) -> None:
        """Set the value for an entity-attribute pair."""
        if entity not in self.assignments:
            self.assignments[entity] = {}
        self.assignments[entity][attribute] = value
    
    def to_dict(self) -> Dict[str, Dict[str, str]]:
        """Convert solution to dictionary for JSON serialization."""
        return self.assignments
    
    @classmethod
    def from_dict(cls, data: Dict[str, Dict[str, str]]) -> 'Solution':
        """Create solution from dictionary."""
        solution = cls()
        solution.assignments = data
        return solution


@dataclass
class Puzzle:
    """
    Represents a complete logic puzzle with entities, attributes, constraints, and solution.
    """
    puzzle_id: str
    entities: List[str]
    attributes: Dict[str, List[str]]  # {"A1": ["V1", "V2", ...], ...}
    constraints: List[Constraint]
    solution: Solution
    generation_stats: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert puzzle to dictionary for JSON serialization."""
        result = {
            "puzzle_id": self.puzzle_id,
            "entities": self.entities,
            "attributes": self.attributes,
            "constraints": [c.to_dict() for c in self.constraints],
            "solution": self.solution.to_dict(),
        }
        if self.generation_stats is not None:
            result["generation_stats"] = self.generation_stats
        return result
    
    def to_json(self) -> str:
        """Convert puzzle to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Puzzle':
        """Create puzzle from dictionary."""
        return cls(
            puzzle_id=data["puzzle_id"],
            entities=data["entities"],
            attributes=data["attributes"],
            constraints=[Constraint.from_dict(c) for c in data["constraints"]],
            solution=Solution.from_dict(data["solution"]),
            generation_stats=data.get("generation_stats"),
        )
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Puzzle':
        """Create puzzle from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)


#: Minimum grid size for a meaningful puzzle (at least 3 entities/values).
MIN_GRID_SIZE: int = 3

#: Difficulty scaling factors taken directly from DESIGN.md.
DIFFICULTY_MULTIPLIERS: Dict[str, float] = {
    "easy": 1.5,
    "medium": 2.5,
    "hard": 3.5,
}

#: Default retry budget for regenerate-until-unique generation.
DEFAULT_UNIQUE_MAX_ATTEMPTS: int = 30


def generate_puzzle_id() -> str:
    """Generate a unique puzzle ID using UUID."""
    return f"puzzle_{uuid.uuid4()}"


# Real-world name mappings for examples
REAL_ENTITY_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
REAL_ATTRIBUTE_NAMES = [
    "Hair Color", "Age", "Favorite Food", "Pet", "Hobby",
    "Favorite Sport", "Favorite Color", "Occupation", "Favorite Music", "Transportation"
]
REAL_VALUE_SETS = {
    "Hair Color": ["Blonde", "Brunette", "Red", "Black", "Gray"],
    "Age": ["20", "25", "30", "35", "40"],
    "Favorite Food": ["Pizza", "Sushi", "Burgers", "Pasta", "Salad"],
    "Pet": ["Dog", "Cat", "Bird", "Fish", "Hamster"],
    "Hobby": ["Reading", "Gaming", "Cooking", "Gardening", "Photography"],
    "Favorite Sport": ["Soccer", "Basketball", "Tennis", "Swimming", "Running"],
    "Favorite Color": ["Red", "Blue", "Green", "Yellow", "Purple"],
    "Occupation": ["Teacher", "Engineer", "Doctor", "Artist", "Chef"],
    "Favorite Music": ["Rock", "Jazz", "Pop", "Classical", "Hip-Hop"],
    "Transportation": ["Car", "Bike", "Bus", "Train", "Walking"]
}


def generate_entities(grid_size: int, use_real_names: bool = False) -> List[str]:
    """
    Generate entity identifiers: E1, E2, ..., En.
    
    If use_real_names is True, returns real-world names like "Alice", "Bob", etc.
    """
    if use_real_names:
        return REAL_ENTITY_NAMES[:grid_size]
    return [f"E{i+1}" for i in range(grid_size)]


def generate_attributes(grid_size: int, use_real_names: bool = False) -> Dict[str, List[str]]:
    """
    Generate attribute names and values.
    
    Attributes: A1..An (or real names if use_real_names=True)
    Values for each attribute: V1..Vn (or real values if use_real_names=True)
    """
    if use_real_names:
        attributes = {}
        for i in range(grid_size):
            attr_name = REAL_ATTRIBUTE_NAMES[i] if i < len(REAL_ATTRIBUTE_NAMES) else f"Attribute {i+1}"
            values = REAL_VALUE_SETS.get(attr_name, [f"Value {j+1}" for j in range(grid_size)])
            # Ensure we have exactly grid_size values
            if len(values) >= grid_size:
                attributes[attr_name] = values[:grid_size]
            else:
                # Pad with generic values if needed
                attributes[attr_name] = values + [f"Value {j+1}" for j in range(len(values), grid_size)]
        return attributes
    
    values = [f"V{i+1}" for i in range(grid_size)]
    return {f"A{i+1}": list(values) for i in range(grid_size)}


def generate_solution(grid_size: int, entities: Optional[List[str]] = None, attributes: Optional[Dict[str, List[str]]] = None) -> Solution:
    """
    Generate a valid solution for a square grid puzzle.
    
    Ensures:
    - Each entity has exactly one value for each attribute.
    - No two entities share the same value for the same attribute
      (per DESIGN.md uniqueness requirement).
    """
    if entities is None:
        entities = generate_entities(grid_size)
    if attributes is None:
        attributes = generate_attributes(grid_size)
    solution = Solution()

    for attribute, values in attributes.items():
        # Use a random permutation of values so each entity gets a unique one
        permuted_values = list(values)
        random.shuffle(permuted_values)
        for entity, value in zip(entities, permuted_values):
            solution.set_value(entity, attribute, value)

    return solution


def _difficulty_to_constraint_count(grid_size: int, difficulty: str) -> int:
    """
    Map difficulty string to a constraint count based on DESIGN.md.
    
    Easy:  grid_size * 1.5
    Medium: grid_size * 2.5
    Hard:   grid_size * 3.5

    The exact multipliers and their intended effect on constraint density are
    documented in `DESIGN.md` under the difficulty scaling table.
    """
    normalized = difficulty.lower()
    if normalized not in DIFFICULTY_MULTIPLIERS:
        allowed = sorted(DIFFICULTY_MULTIPLIERS.keys())
        raise ValueError(
            f"Unknown difficulty '{difficulty}'. Expected one of: {', '.join(allowed)}."
        )

    factor = DIFFICULTY_MULTIPLIERS[normalized]

    # Round to nearest integer and require at least one constraint
    return max(1, int(round(grid_size * factor)))


def _pick_two_entities(entities: List[str]) -> Tuple[str, str]:
    """Pick two distinct entities uniformly at random."""
    return tuple(random.sample(entities, 2))  # type: ignore[return-value]


def _make_equality_constraint(
    entities: List[str],
    attribute: str,
    solution: Solution,
) -> Optional[Constraint]:
    """Create an equality constraint consistent with the solution."""
    entity = random.choice(entities)
    value = solution.get_value(entity, attribute)
    if value is None:
        return None
    return Constraint(
        type="equality",
        entity=entity,
        attribute=attribute,
        value=value,
    )


def _make_inequality_constraint(
    entities: List[str],
    attribute: str,
    values: List[str],
    solution: Solution,
) -> Optional[Constraint]:
    """Create an inequality constraint consistent with the solution."""
    entity = random.choice(entities)
    true_value = solution.get_value(entity, attribute)
    if true_value is None:
        return None
    # Pick a value different from the true one
    possible_values = [v for v in values if v != true_value]
    if not possible_values:
        return None
    value = random.choice(possible_values)
    return Constraint(
        type="inequality",
        entity=entity,
        attribute=attribute,
        value=value,
    )


def _make_different_values_constraint(
    entities: List[str],
    attribute: str,
) -> Constraint:
    """Create a different_values constraint between two entities."""
    entity1, entity2 = _pick_two_entities(entities)
    return Constraint(
        type="different_values",
        entities=[entity1, entity2],
        attribute=attribute,
    )


def _make_relative_position_constraint(
    entities: List[str],
    attribute: str,
    values: List[str],
    solution: Solution,
) -> Optional[Constraint]:
    """
    Create a relative_position constraint consistent with the solution.

    Interprets values as ordered positions: V1..Vn -> 1..n and uses the
    difference between two entities' positions as the offset.
    """
    entity1, entity2 = _pick_two_entities(entities)
    v1 = solution.get_value(entity1, attribute)
    v2 = solution.get_value(entity2, attribute)
    if v1 is None or v2 is None:
        return None

    idx1 = values.index(v1)
    idx2 = values.index(v2)
    offset = idx1 - idx2
    # Skip trivial zero-offset constraints
    if offset == 0:
        return None

    return Constraint(
        type="relative_position",
        entity1=entity1,
        entity2=entity2,
        attribute=attribute,
        offset=offset,
    )


def generate_constraints(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Solution,
    difficulty: str,
) -> List[Constraint]:
    """
    Generate constraints consistent with the provided solution.
    
    Uses a mix of:
    - equality
    - inequality
    - different_values
    - relative_position
    
    Note: We skip same_value because the solution enforces unique values
    per attribute across entities.
    """
    num_constraints = _difficulty_to_constraint_count(len(entities), difficulty)
    constraints: List[Constraint] = []

    attribute_names = list(attributes.keys())

    while len(constraints) < num_constraints:
        attribute = random.choice(attribute_names)
        values = attributes[attribute]
        constraint_type = random.choice(
            ["equality", "inequality", "different_values", "relative_position"]
        )

        new_constraint: Optional[Constraint]

        if constraint_type == "equality":
            new_constraint = _make_equality_constraint(entities, attribute, solution)
        elif constraint_type == "inequality":
            new_constraint = _make_inequality_constraint(
                entities,
                attribute,
                values,
                solution,
            )
        elif constraint_type == "different_values":
            # Our solution enforces different values per attribute, so any pair works
            new_constraint = _make_different_values_constraint(entities, attribute)
        else:  # "relative_position"
            new_constraint = _make_relative_position_constraint(
                entities,
                attribute,
                values,
                solution,
            )

        if new_constraint is not None:
            constraints.append(new_constraint)

    return constraints


def _generate_guaranteed_unique_base_constraints(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Solution,
) -> List[Constraint]:
    """
    Build a guaranteed-unique base constraint set.

    For every entity-attribute pair, add an equality constraint that pins the
    exact value from the hidden solution. This fully determines one assignment.
    """
    constraints: List[Constraint] = []
    for entity in entities:
        for attribute in attributes:
            value = solution.get_value(entity, attribute)
            if value is None:
                raise ValueError(
                    f"Missing solution value for entity '{entity}' and attribute '{attribute}'."
                )
            constraints.append(
                Constraint(
                    type="equality",
                    entity=entity,
                    attribute=attribute,
                    value=value,
                )
            )
    return constraints


def _shrink_constraints_while_unique(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Solution,
    constraints: List[Constraint],
    target_count: int,
) -> List[Constraint]:
    """
    Remove constraints greedily while preserving uniqueness.

    Starts from a guaranteed-unique set and attempts to drop clues one by one.
    A removal is kept only if the puzzle still has exactly one solution.
    """
    if target_count < 1:
        target_count = 1
    if len(constraints) <= target_count:
        return constraints

    working = list(constraints)
    candidate_indices = list(range(len(working)))
    random.shuffle(candidate_indices)

    for idx in candidate_indices:
        if len(working) <= target_count:
            break
        if idx >= len(working):
            continue

        removed = working.pop(idx)
        test_puzzle = Puzzle(
            puzzle_id="puzzle_shrink_check",
            entities=entities,
            attributes=attributes,
            constraints=working,
            solution=solution,
        )
        if _count_candidate_solutions(test_puzzle, max_solutions=2) != 1:
            # Reinsert at the same location if uniqueness is lost.
            working.insert(idx, removed)

    return working


def generate_puzzle(grid_size: int, difficulty: str, use_real_names: bool = False) -> Puzzle:
    """
    High-level puzzle generation function.
    
    - Builds entities and attributes for a square grid.
    - Generates a valid solution.
    - Generates constraints consistent with that solution.
    - Wraps everything into a Puzzle object.

    Args:
        grid_size: Number of entities and values per attribute. Must be >= MIN_GRID_SIZE
            for a meaningful logic puzzle.
        difficulty: String difficulty level ('easy', 'medium', or 'hard',
            case-insensitive).
    """
    if grid_size < MIN_GRID_SIZE:
        raise ValueError(
            f"grid_size must be an integer >= {MIN_GRID_SIZE} for a meaningful puzzle "
            f"(got {grid_size})."
        )

    normalized_difficulty = difficulty.lower()

    return generate_unique_puzzle(
        grid_size=grid_size,
        difficulty=normalized_difficulty,
        use_real_names=use_real_names,
        max_attempts=DEFAULT_UNIQUE_MAX_ATTEMPTS,
    )


def _build_candidate_puzzle(
    grid_size: int,
    difficulty: str,
    use_real_names: bool,
) -> Puzzle:
    """Generate a single guaranteed-unique puzzle candidate."""
    entities = generate_entities(grid_size, use_real_names=use_real_names)
    attributes = generate_attributes(grid_size, use_real_names=use_real_names)
    solution = generate_solution(grid_size, entities=entities, attributes=attributes)
    constraints = _generate_guaranteed_unique_base_constraints(
        entities,
        attributes,
        solution,
    )
    target_count = _difficulty_to_constraint_count(grid_size, difficulty)
    constraints = _shrink_constraints_while_unique(
        entities=entities,
        attributes=attributes,
        solution=solution,
        constraints=constraints,
        target_count=target_count,
    )
    return Puzzle(
        puzzle_id=generate_puzzle_id(),
        entities=entities,
        attributes=attributes,
        constraints=constraints,
        solution=solution,
    )


def _count_candidate_solutions(candidate: Puzzle, max_solutions: int = 2) -> int:
    """
    Count satisfying assignments for a generated candidate using Module 2+3.
    """
    # Local imports prevent module-level coupling across the pipeline.
    from module2_logic_representation import module1_to_module2
    from module3_puzzle_solving import count_solutions_from_kb

    kb = module1_to_module2(candidate.to_dict())
    return count_solutions_from_kb(kb, max_solutions=max_solutions)


def generate_unique_puzzle(
    grid_size: int,
    difficulty: str,
    use_real_names: bool = False,
    max_attempts: int = DEFAULT_UNIQUE_MAX_ATTEMPTS,
) -> Puzzle:
    """
    Generate a puzzle with exactly one satisfying assignment.

    Regenerates candidates until uniqueness is achieved or max_attempts is hit.
    """
    if max_attempts <= 0:
        raise ValueError(f"max_attempts must be positive (got {max_attempts}).")

    started_at = time.perf_counter()

    for attempt in range(1, max_attempts + 1):
        candidate = _build_candidate_puzzle(
            grid_size=grid_size,
            difficulty=difficulty,
            use_real_names=use_real_names,
        )
        solution_count = _count_candidate_solutions(candidate, max_solutions=2)
        if solution_count == 1:
            elapsed = time.perf_counter() - started_at
            candidate.generation_stats = {
                "attempts": attempt,
                "regenerations": attempt - 1,
                "generation_time_seconds": round(elapsed, 6),
            }
            return candidate

    elapsed = time.perf_counter() - started_at
    raise ValueError(
        "Failed to generate a uniquely solvable puzzle within "
        f"{max_attempts} attempts (grid_size={grid_size}, difficulty='{difficulty}'). "
        f"Elapsed time: {elapsed:.6f}s."
    )


def _generate_attributes_with_counts(
    variable_count: int,
    value_count: int,
    use_real_names: bool = False,
) -> Dict[str, List[str]]:
    """Generate attributes where variable and value counts can differ."""
    if use_real_names:
        attributes: Dict[str, List[str]] = {}
        for i in range(variable_count):
            attr_name = (
                REAL_ATTRIBUTE_NAMES[i]
                if i < len(REAL_ATTRIBUTE_NAMES)
                else f"Attribute {i+1}"
            )
            raw_values = REAL_VALUE_SETS.get(
                attr_name,
                [f"Value {j+1}" for j in range(value_count)],
            )
            if len(raw_values) >= value_count:
                attributes[attr_name] = list(raw_values[:value_count])
            else:
                attributes[attr_name] = list(raw_values) + [
                    f"Value {j+1}" for j in range(len(raw_values), value_count)
                ]
        return attributes

    values = [f"V{i+1}" for i in range(value_count)]
    return {f"A{i+1}": list(values) for i in range(variable_count)}


def generate_puzzle_fixed_value_count(
    variable_count: int,
    difficulty: str,
    value_count: int = 3,
    use_real_names: bool = False,
    max_attempts: int = DEFAULT_UNIQUE_MAX_ATTEMPTS,
) -> Puzzle:
    """
    Generate puzzle with variable_count categories and fixed value_count values each.

    Typical UI usage:
    - variable_count in {3,4,5}
    - value_count fixed at 3
    """
    if variable_count < 3:
        raise ValueError(f"variable_count must be >= 3 (got {variable_count}).")
    if value_count < 3:
        raise ValueError(f"value_count must be >= 3 (got {value_count}).")
    if max_attempts <= 0:
        raise ValueError(f"max_attempts must be positive (got {max_attempts}).")

    normalized_difficulty = difficulty.lower().strip()
    started_at = time.perf_counter()

    for attempt in range(1, max_attempts + 1):
        entities = generate_entities(value_count, use_real_names=use_real_names)
        attributes = _generate_attributes_with_counts(
            variable_count=variable_count,
            value_count=value_count,
            use_real_names=use_real_names,
        )
        solution = generate_solution(
            value_count,
            entities=entities,
            attributes=attributes,
        )
        constraints = _generate_guaranteed_unique_base_constraints(
            entities,
            attributes,
            solution,
        )
        target_count = _difficulty_to_constraint_count(variable_count, normalized_difficulty)
        constraints = _shrink_constraints_while_unique(
            entities=entities,
            attributes=attributes,
            solution=solution,
            constraints=constraints,
            target_count=target_count,
        )
        candidate = Puzzle(
            puzzle_id=generate_puzzle_id(),
            entities=entities,
            attributes=attributes,
            constraints=constraints,
            solution=solution,
        )

        if _count_candidate_solutions(candidate, max_solutions=2) == 1:
            elapsed = time.perf_counter() - started_at
            candidate.generation_stats = {
                "attempts": attempt,
                "regenerations": attempt - 1,
                "generation_time_seconds": round(elapsed, 6),
                "variable_count": variable_count,
                "value_count": value_count,
            }
            return candidate

    elapsed = time.perf_counter() - started_at
    raise ValueError(
        "Failed to generate fixed-value-count puzzle within "
        f"{max_attempts} attempts (variable_count={variable_count}, value_count={value_count}, "
        f"difficulty='{difficulty}'). Elapsed time: {elapsed:.6f}s."
    )


def build_logic_grid_layout(attributes: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Build a compact logic-grid layout that covers each attribute pair exactly once.

    Layout strategy mirrors the docs examples:
    - columns: all attributes except the last, in original order
    - rows: remaining attributes in reverse order
    """
    attribute_order = list(attributes.keys())
    if len(attribute_order) < 3:
        raise ValueError("Grid layout requires at least 3 attributes.")

    column_attributes = attribute_order[:-1]
    row_attributes = list(reversed(attribute_order[1:]))

    covered_pairs = set()
    blocks: List[Dict[str, str]] = []
    for row_attribute in row_attributes:
        for col_attribute in column_attributes:
            if row_attribute == col_attribute:
                continue
            pair = tuple(sorted((row_attribute, col_attribute)))
            if pair in covered_pairs:
                continue
            covered_pairs.add(pair)
            blocks.append(
                {
                    "row_attribute": row_attribute,
                    "column_attribute": col_attribute,
                }
            )

    all_pairs = {tuple(sorted(pair)) for pair in combinations(attribute_order, 2)}
    if covered_pairs != all_pairs:
        raise ValueError(
            "Generated grid layout does not cover every unordered attribute pair exactly once."
        )

    return {
        "attribute_order": attribute_order,
        "column_attributes": column_attributes,
        "row_attributes": row_attributes,
        "pair_blocks": blocks,
    }


def constraints_to_hint_sentences(constraints: List[Constraint]) -> List[str]:
    """Convert formal constraints into human-readable hint sentences."""
    hints: List[str] = []

    for constraint in constraints:
        if constraint.type == "equality":
            hints.append(
                f"{constraint.entity} has {constraint.attribute} = {constraint.value}."
            )
        elif constraint.type == "inequality":
            hints.append(
                f"{constraint.entity} does not have {constraint.attribute} = {constraint.value}."
            )
        elif constraint.type == "different_values" and constraint.entities and len(constraint.entities) >= 2:
            hints.append(
                f"{constraint.entities[0]} and {constraint.entities[1]} have different values for {constraint.attribute}."
            )
        elif constraint.type == "same_value" and constraint.entities and len(constraint.entities) >= 2:
            hints.append(
                f"{constraint.entities[0]} and {constraint.entities[1]} share the same value for {constraint.attribute}."
            )
        elif constraint.type == "relative_position":
            e1 = constraint.entity1 or constraint.entity
            e2 = constraint.entity2
            offset = constraint.offset
            if e1 is None or e2 is None or offset is None:
                continue
            if offset > 0:
                relation = f"{offset} step(s) ahead of"
            elif offset < 0:
                relation = f"{abs(offset)} step(s) behind"
            else:
                relation = "aligned with"
            hints.append(
                f"For {constraint.attribute}, {e1} is {relation} {e2}."
            )

    return hints


def build_puzzle_view_model(puzzle: Puzzle) -> Dict[str, Any]:
    """
    Build UI-ready puzzle data from a generated puzzle.

    Includes:
    - compact grid layout specification
    - human-readable hint sentences derived from constraints
    """
    return {
        "puzzle_id": puzzle.puzzle_id,
        "entities": list(puzzle.entities),
        "attributes": dict(puzzle.attributes),
        "layout": build_logic_grid_layout(puzzle.attributes),
        "hints": constraints_to_hint_sentences(puzzle.constraints),
        "constraints": [constraint.to_dict() for constraint in puzzle.constraints],
    }


def main() -> None:
    """
    Command-line entry point for generating a puzzle.
    
    Example:
        python -m src.module1_puzzle_generator --grid_size 5 --difficulty easy
    """
    parser = argparse.ArgumentParser(description="Module 1: Puzzle Generator")
    parser.add_argument(
        "--grid_size",
        type=int,
        default=5,
        help="Number of entities / attribute values (default: 5)",
    )
    parser.add_argument(
        "--difficulty",
        type=str,
        default="easy",
        choices=["easy", "medium", "hard"],
        help="Puzzle difficulty level (default: easy)",
    )
    parser.add_argument(
        "--use_real_names",
        action="store_true",
        help="Use real-world names instead of generic variables (E1, A1, V1, etc.)",
    )

    args = parser.parse_args()
    puzzle = generate_puzzle(args.grid_size, args.difficulty, use_real_names=args.use_real_names)
    print(puzzle.to_json())


if __name__ == "__main__":
    main()
