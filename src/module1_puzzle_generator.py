"""
Module 1: Puzzle Generator

This module generates logic puzzles (like "Who owns the zebra?" puzzles) using 
Constraint Satisfaction Problem (CSP) techniques.

WHAT IT DOES:
- Creates a puzzle with entities (people, houses, etc.), attributes (color, pet, etc.), 
  and values (red, blue, dog, cat, etc.)
- Generates constraints (rules) that define relationships between entities
- Creates a hidden solution that satisfies all constraints

EXAMPLE:
    puzzle = generate_puzzle(grid_size=5, difficulty="medium")
    # Creates a 5x5 puzzle with 5 entities, 5 attributes, and appropriate constraints
"""

import json
import uuid
import random
import argparse
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


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
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert puzzle to dictionary for JSON serialization."""
        return {
            "puzzle_id": self.puzzle_id,
            "entities": self.entities,
            "attributes": self.attributes,
            "constraints": [c.to_dict() for c in self.constraints],
            "solution": self.solution.to_dict()
        }
    
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
            solution=Solution.from_dict(data["solution"])
        )
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Puzzle':
        """Create puzzle from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)


def generate_puzzle_id() -> str:
    """Generate a unique puzzle ID using UUID."""
    return f"puzzle_{uuid.uuid4()}"


def generate_entities(grid_size: int) -> List[str]:
    """Generate entity identifiers: E1, E2, ..., En."""
    return [f"E{i+1}" for i in range(grid_size)]


def generate_attributes(grid_size: int) -> Dict[str, List[str]]:
    """
    Generate attribute names and values.
    
    Attributes: A1..An
    Values for each attribute: V1..Vn
    """
    values = [f"V{i+1}" for i in range(grid_size)]
    return {f"A{i+1}": list(values) for i in range(grid_size)}


def generate_solution(grid_size: int) -> Solution:
    """
    Generate a valid solution for a square grid puzzle.
    
    Ensures:
    - Each entity has exactly one value for each attribute.
    - No two entities share the same value for the same attribute
      (per DESIGN.md uniqueness requirement).
    """
    entities = generate_entities(grid_size)
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
    """
    difficulty = difficulty.lower()
    if difficulty == "easy":
        factor = 1.5
    elif difficulty == "medium":
        factor = 2.5
    elif difficulty == "hard":
        factor = 3.5
    else:
        raise ValueError(f"Unknown difficulty: {difficulty}")

    # Round to nearest integer
    return max(1, int(round(grid_size * factor)))


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

    # Helper to pick two distinct entities
    def pick_two_entities() -> tuple[str, str]:
        e1, e2 = random.sample(entities, 2)
        return e1, e2

    while len(constraints) < num_constraints:
        attribute = random.choice(attribute_names)
        values = attributes[attribute]
        constraint_type = random.choice(
            ["equality", "inequality", "different_values", "relative_position"]
        )

        if constraint_type == "equality":
            entity = random.choice(entities)
            value = solution.get_value(entity, attribute)
            if value is None:
                continue
            constraints.append(
                Constraint(
                    type="equality",
                    entity=entity,
                    attribute=attribute,
                    value=value,
                )
            )

        elif constraint_type == "inequality":
            entity = random.choice(entities)
            true_value = solution.get_value(entity, attribute)
            if true_value is None:
                continue
            # Pick a value different from the true one
            possible_values = [v for v in values if v != true_value]
            if not possible_values:
                continue
            value = random.choice(possible_values)
            constraints.append(
                Constraint(
                    type="inequality",
                    entity=entity,
                    attribute=attribute,
                    value=value,
                )
            )

        elif constraint_type == "different_values":
            # Our solution enforces different values per attribute, so any pair works
            entity1, entity2 = pick_two_entities()
            constraints.append(
                Constraint(
                    type="different_values",
                    entities=[entity1, entity2],
                    attribute=attribute,
                )
            )

        elif constraint_type == "relative_position":
            # Interpret values as ordered positions: V1..Vn -> 1..n
            entity1, entity2 = pick_two_entities()
            v1 = solution.get_value(entity1, attribute)
            v2 = solution.get_value(entity2, attribute)
            if v1 is None or v2 is None:
                continue
            idx1 = values.index(v1)
            idx2 = values.index(v2)
            offset = idx1 - idx2
            # Skip trivial zero-offset constraints
            if offset == 0:
                continue
            constraints.append(
                Constraint(
                    type="relative_position",
                    entity1=entity1,
                    entity2=entity2,
                    attribute=attribute,
                    offset=offset,
                )
            )

    return constraints


def generate_puzzle(grid_size: int, difficulty: str) -> Puzzle:
    """
    High-level puzzle generation function.
    
    - Builds entities and attributes for a square grid.
    - Generates a valid solution.
    - Generates constraints consistent with that solution.
    - Wraps everything into a Puzzle object.
    """
    if grid_size <= 0:
        raise ValueError("grid_size must be a positive integer")

    entities = generate_entities(grid_size)
    attributes = generate_attributes(grid_size)
    solution = generate_solution(grid_size)
    constraints = generate_constraints(entities, attributes, solution, difficulty)

    return Puzzle(
        puzzle_id=generate_puzzle_id(),
        entities=entities,
        attributes=attributes,
        constraints=constraints,
        solution=solution,
    )


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

    args = parser.parse_args()
    puzzle = generate_puzzle(args.grid_size, args.difficulty)
    print(puzzle.to_json())


if __name__ == "__main__":
    main()
