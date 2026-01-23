"""
Unit tests for Module 1 data structures (Constraint, Solution, Puzzle)

Tests the core data structures before implementing puzzle generation.
"""

import json
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import Constraint, Solution, Puzzle, generate_puzzle_id


def test_constraint_equality():
    """Test equality constraint creation and serialization."""
    constraint = Constraint(
        type="equality",
        entity="E1",
        attribute="A1",
        value="V3"
    )
    
    assert constraint.type == "equality"
    assert constraint.entity == "E1"
    assert constraint.attribute == "A1"
    assert constraint.value == "V3"
    
    # Test serialization
    constraint_dict = constraint.to_dict()
    assert constraint_dict["type"] == "equality"
    assert constraint_dict["entity"] == "E1"
    assert constraint_dict["attribute"] == "A1"
    assert constraint_dict["value"] == "V3"
    
    # Test deserialization
    constraint2 = Constraint.from_dict(constraint_dict)
    assert constraint2.type == constraint.type
    assert constraint2.entity == constraint.entity
    assert constraint2.attribute == constraint.attribute
    assert constraint2.value == constraint.value


def test_constraint_different_values():
    """Test different_values constraint."""
    constraint = Constraint(
        type="different_values",
        entities=["E1", "E2"],
        attribute="A1"
    )
    
    constraint_dict = constraint.to_dict()
    assert constraint_dict["type"] == "different_values"
    assert constraint_dict["entities"] == ["E1", "E2"]
    assert constraint_dict["attribute"] == "A1"


def test_solution():
    """Test Solution class."""
    solution = Solution()
    
    # Set some values
    solution.set_value("E1", "A1", "V3")
    solution.set_value("E1", "A2", "V1")
    solution.set_value("E2", "A1", "V1")
    
    # Get values
    assert solution.get_value("E1", "A1") == "V3"
    assert solution.get_value("E1", "A2") == "V1"
    assert solution.get_value("E2", "A1") == "V1"
    assert solution.get_value("E2", "A2") is None
    
    # Test serialization
    solution_dict = solution.to_dict()
    assert solution_dict["E1"]["A1"] == "V3"
    assert solution_dict["E1"]["A2"] == "V1"
    assert solution_dict["E2"]["A1"] == "V1"
    
    # Test deserialization
    solution2 = Solution.from_dict(solution_dict)
    assert solution2.get_value("E1", "A1") == "V3"


def test_puzzle():
    """Test Puzzle class creation and serialization."""
    puzzle_id = generate_puzzle_id()
    entities = ["E1", "E2", "E3"]
    attributes = {
        "A1": ["V1", "V2", "V3"],
        "A2": ["V1", "V2", "V3"]
    }
    
    constraints = [
        Constraint(type="equality", entity="E1", attribute="A1", value="V3"),
        Constraint(type="different_values", entities=["E1", "E2"], attribute="A2")
    ]
    
    solution = Solution()
    solution.set_value("E1", "A1", "V3")
    solution.set_value("E1", "A2", "V1")
    solution.set_value("E2", "A1", "V1")
    solution.set_value("E2", "A2", "V2")
    solution.set_value("E3", "A1", "V2")
    solution.set_value("E3", "A2", "V3")
    
    puzzle = Puzzle(
        puzzle_id=puzzle_id,
        entities=entities,
        attributes=attributes,
        constraints=constraints,
        solution=solution
    )
    
    # Test serialization
    puzzle_dict = puzzle.to_dict()
    assert puzzle_dict["puzzle_id"] == puzzle_id
    assert puzzle_dict["entities"] == entities
    assert puzzle_dict["attributes"] == attributes
    assert len(puzzle_dict["constraints"]) == 2
    assert "solution" in puzzle_dict
    
    # Test JSON serialization
    json_str = puzzle.to_json()
    assert isinstance(json_str, str)
    
    # Test deserialization
    puzzle2 = Puzzle.from_json(json_str)
    assert puzzle2.puzzle_id == puzzle_id
    assert puzzle2.entities == entities
    assert len(puzzle2.constraints) == 2


def test_puzzle_id_generation():
    """Test puzzle ID generation."""
    id1 = generate_puzzle_id()
    id2 = generate_puzzle_id()
    
    assert id1.startswith("puzzle_")
    assert id2.startswith("puzzle_")
    assert id1 != id2  # Should be unique


if __name__ == "__main__":
    print("Running data structure tests...")
    test_constraint_equality()
    print("✓ Constraint equality test passed")
    
    test_constraint_different_values()
    print("✓ Constraint different_values test passed")
    
    test_solution()
    print("✓ Solution test passed")
    
    test_puzzle()
    print("✓ Puzzle test passed")
    
    test_puzzle_id_generation()
    print("✓ Puzzle ID generation test passed")
    
    print("\nAll data structure tests passed! ✓")
