"""
Module 1: Puzzle Generator

Generates logic puzzles using Constraint Satisfaction Problem (CSP) techniques.
Creates puzzles with entities, attributes, constraints, and hidden solutions.
"""

import json
import uuid
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


# TODO: Implement puzzle generation functions
# - generate_solution()
# - generate_constraints()
# - generate_puzzle()
