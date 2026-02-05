"""
Unit tests for Module 1: Puzzle Generator

Tests puzzle generation, constraint validation, and difficulty scaling.
"""

import sys
from pathlib import Path

import pytest

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import (  # noqa: E402
    Solution,
    Constraint,
    Puzzle,
    generate_entities,
    generate_attributes,
    generate_solution,
    generate_constraints,
    generate_puzzle,
    _difficulty_to_constraint_count,
    generate_puzzle_id,
)


def test_generate_entities_and_attributes():
    grid_size = 4
    entities = generate_entities(grid_size)
    attributes = generate_attributes(grid_size)

    assert entities == ["E1", "E2", "E3", "E4"]
    assert len(attributes) == grid_size
    assert set(attributes.keys()) == {"A1", "A2", "A3", "A4"}
    for values in attributes.values():
        assert values == ["V1", "V2", "V3", "V4"]


@pytest.mark.parametrize("grid_size", [3, 4, 5, 6, 10])
def test_generate_entities_various_sizes(grid_size: int):
    """Test entity generation for various grid sizes."""
    entities = generate_entities(grid_size)
    assert len(entities) == grid_size
    assert entities == [f"E{i+1}" for i in range(grid_size)]


@pytest.mark.parametrize("grid_size", [3, 4, 5, 6, 10])
def test_generate_attributes_various_sizes(grid_size: int):
    """Test attribute generation for various grid sizes."""
    attributes = generate_attributes(grid_size)
    assert len(attributes) == grid_size
    assert set(attributes.keys()) == {f"A{i+1}" for i in range(grid_size)}
    for attr_name, values in attributes.items():
        assert len(values) == grid_size
        assert values == [f"V{i+1}" for i in range(grid_size)]


def test_generate_solution_structure_and_uniqueness():
    grid_size = 5
    solution = generate_solution(grid_size)

    # Each entity should have exactly one value per attribute
    entities = [f"E{i+1}" for i in range(grid_size)]
    attributes = [f"A{i+1}" for i in range(grid_size)]

    for entity in entities:
        for attribute in attributes:
            value = solution.get_value(entity, attribute)
            assert value is not None

    # For each attribute, all entities should have unique values
    for attribute in attributes:
        values_seen = set()
        for entity in entities:
            value = solution.get_value(entity, attribute)
            assert value not in values_seen
            values_seen.add(value)
        assert len(values_seen) == grid_size


@pytest.mark.parametrize("grid_size", [3, 4, 5, 6])
def test_generate_solution_various_sizes(grid_size: int):
    """Test solution generation for various grid sizes."""
    solution = generate_solution(grid_size)
    entities = [f"E{i+1}" for i in range(grid_size)]
    attributes = [f"A{i+1}" for i in range(grid_size)]

    # Check all assignments exist
    for entity in entities:
        for attribute in attributes:
            value = solution.get_value(entity, attribute)
            assert value is not None
            assert value.startswith("V")

    # Check uniqueness per attribute
    for attribute in attributes:
        values = [solution.get_value(e, attribute) for e in entities]
        assert len(values) == len(set(values)) == grid_size


def test_difficulty_to_constraint_count():
    """Test constraint count calculation for different difficulties."""
    grid_size = 5
    
    easy_count = _difficulty_to_constraint_count(grid_size, "easy")
    medium_count = _difficulty_to_constraint_count(grid_size, "medium")
    hard_count = _difficulty_to_constraint_count(grid_size, "hard")
    
    # Check expected ranges (allowing for rounding)
    assert 5 <= easy_count <= 10  # 5 * 1.5 = 7.5 -> 8
    assert 10 <= medium_count <= 15  # 5 * 2.5 = 12.5 -> 13
    assert 15 <= hard_count <= 20  # 5 * 3.5 = 17.5 -> 18
    
    # Check ordering
    assert easy_count <= medium_count <= hard_count
    
    # Test invalid difficulty
    with pytest.raises(ValueError):
        _difficulty_to_constraint_count(5, "invalid")


def test_generate_constraints_consistency():
    """Test that generated constraints are consistent with the solution."""
    grid_size = 5
    entities = generate_entities(grid_size)
    attributes = generate_attributes(grid_size)
    solution = generate_solution(grid_size)
    
    constraints = generate_constraints(entities, attributes, solution, "medium")
    
    assert len(constraints) > 0
    
    # Check each constraint is valid and consistent with solution
    for constraint in constraints:
        assert constraint.type in ["equality", "inequality", "different_values", "relative_position"]
        assert constraint.attribute in attributes
        
        if constraint.type == "equality":
            # Equality constraint should match solution
            assert constraint.entity in entities
            assert constraint.value == solution.get_value(constraint.entity, constraint.attribute)
        
        elif constraint.type == "inequality":
            # Inequality constraint should NOT match solution
            assert constraint.entity in entities
            true_value = solution.get_value(constraint.entity, constraint.attribute)
            assert constraint.value != true_value
        
        elif constraint.type == "different_values":
            # Different values should be different in solution
            assert len(constraint.entities) == 2
            assert all(e in entities for e in constraint.entities)
            val1 = solution.get_value(constraint.entities[0], constraint.attribute)
            val2 = solution.get_value(constraint.entities[1], constraint.attribute)
            assert val1 != val2
        
        elif constraint.type == "relative_position":
            # Relative position should match solution
            assert constraint.entity1 in entities
            assert constraint.entity2 in entities
            val1 = solution.get_value(constraint.entity1, constraint.attribute)
            val2 = solution.get_value(constraint.entity2, constraint.attribute)
            # Extract numeric parts and check offset
            num1 = int(val1[1:])
            num2 = int(val2[1:])
            assert num1 == num2 + constraint.offset


@pytest.mark.parametrize("difficulty", ["easy", "medium", "hard"])
def test_generate_puzzle_basic_properties(difficulty: str):
    grid_size = 5
    puzzle = generate_puzzle(grid_size, difficulty)

    # Basic structure checks
    assert puzzle.puzzle_id.startswith("puzzle_")
    assert puzzle.entities == [f"E{i+1}" for i in range(grid_size)]
    assert set(puzzle.attributes.keys()) == {f"A{i+1}" for i in range(grid_size)}

    # Check solution shape matches entities/attributes
    for entity in puzzle.entities:
        for attribute in puzzle.attributes.keys():
            assert puzzle.solution.get_value(entity, attribute) in puzzle.attributes[attribute]

    # Constraint list should be non-empty and roughly scale with difficulty
    assert len(puzzle.constraints) > 0

    if difficulty == "easy":
        assert len(puzzle.constraints) <= len(puzzle.entities) * 2
    elif difficulty == "medium":
        assert len(puzzle.constraints) >= len(puzzle.entities)  # looser bound
    elif difficulty == "hard":
        assert len(puzzle.constraints) >= len(puzzle.entities) * 2


@pytest.mark.parametrize("difficulty", ["easy", "medium", "hard"])
@pytest.mark.parametrize("grid_size", [3, 4, 5, 6])
def test_generate_puzzle_various_configurations(difficulty: str, grid_size: int):
    """Test puzzle generation with various difficulty and grid size combinations."""
    puzzle = generate_puzzle(grid_size, difficulty)
    
    # Verify structure
    assert len(puzzle.entities) == grid_size
    assert len(puzzle.attributes) == grid_size
    assert len(puzzle.constraints) > 0
    
    # Verify solution completeness
    for entity in puzzle.entities:
        for attribute in puzzle.attributes:
            value = puzzle.solution.get_value(entity, attribute)
            assert value is not None
            assert value in puzzle.attributes[attribute]


def test_generate_puzzle_invalid_grid_size():
    """Test that invalid grid sizes raise errors."""
    with pytest.raises(ValueError):
        generate_puzzle(0, "easy")
    
    with pytest.raises(ValueError):
        generate_puzzle(-1, "easy")
    
    with pytest.raises(ValueError):
        generate_puzzle(1, "easy")  # Too small for meaningful puzzle


def test_generate_puzzle_invalid_difficulty():
    """Test that invalid difficulty levels raise errors."""
    with pytest.raises(ValueError):
        generate_puzzle(5, "invalid")
    
    # Note: The implementation is case-insensitive (converts to lowercase)
    # So "EASY" should work, not raise an error
    puzzle = generate_puzzle(5, "EASY")
    assert puzzle is not None


def test_puzzle_json_serialization():
    """Test that puzzles can be serialized to and from JSON."""
    puzzle = generate_puzzle(5, "medium")
    
    # Serialize to JSON
    json_str = puzzle.to_json()
    assert isinstance(json_str, str)
    
    # Deserialize from JSON
    puzzle_dict = puzzle.to_dict()
    puzzle2 = Puzzle.from_dict(puzzle_dict)
    
    # Verify all properties match
    assert puzzle2.puzzle_id == puzzle.puzzle_id
    assert puzzle2.entities == puzzle.entities
    assert puzzle2.attributes == puzzle.attributes
    assert len(puzzle2.constraints) == len(puzzle.constraints)
    assert puzzle2.solution.assignments == puzzle.solution.assignments


def test_puzzle_id_uniqueness():
    """Test that puzzle IDs are unique."""
    ids = [generate_puzzle_id() for _ in range(100)]
    assert len(ids) == len(set(ids))  # All unique


def test_constraint_types_distribution():
    """Test that different constraint types are generated."""
    grid_size = 5
    entities = generate_entities(grid_size)
    attributes = generate_attributes(grid_size)
    solution = generate_solution(grid_size)
    
    # Generate many constraints to ensure variety
    constraints = generate_constraints(entities, attributes, solution, "hard")
    
    constraint_types = [c.type for c in constraints]
    
    # Should have multiple types
    assert len(set(constraint_types)) > 1
    
    # Should include common types
    assert "equality" in constraint_types or "inequality" in constraint_types
    assert "different_values" in constraint_types


def test_puzzle_solution_satisfies_constraints():
    """Test that the puzzle solution satisfies all generated constraints."""
    puzzle = generate_puzzle(5, "medium")
    
    for constraint in puzzle.constraints:
        if constraint.type == "equality":
            value = puzzle.solution.get_value(constraint.entity, constraint.attribute)
            assert value == constraint.value
        
        elif constraint.type == "inequality":
            value = puzzle.solution.get_value(constraint.entity, constraint.attribute)
            assert value != constraint.value
        
        elif constraint.type == "different_values":
            val1 = puzzle.solution.get_value(constraint.entities[0], constraint.attribute)
            val2 = puzzle.solution.get_value(constraint.entities[1], constraint.attribute)
            assert val1 != val2
        
        elif constraint.type == "relative_position":
            val1 = puzzle.solution.get_value(constraint.entity1, constraint.attribute)
            val2 = puzzle.solution.get_value(constraint.entity2, constraint.attribute)
            num1 = int(val1[1:])
            num2 = int(val2[1:])
            assert num1 == num2 + constraint.offset


def test_multiple_puzzle_generation():
    """Test that generating multiple puzzles produces different results."""
    puzzles = [generate_puzzle(5, "medium") for _ in range(10)]
    
    # All should have unique IDs
    ids = [p.puzzle_id for p in puzzles]
    assert len(ids) == len(set(ids))
    
    # Solutions should be different (very likely with randomization)
    solutions = [p.solution.assignments for p in puzzles]
    # At least some should be different
    assert len(set(str(s) for s in solutions)) > 1


def test_constraint_serialization():
    """Test that constraints can be serialized and deserialized."""
    constraint = Constraint(
        type="equality",
        entity="E1",
        attribute="A1",
        value="V3"
    )
    
    constraint_dict = constraint.to_dict()
    constraint2 = Constraint.from_dict(constraint_dict)
    
    assert constraint2.type == constraint.type
    assert constraint2.entity == constraint.entity
    assert constraint2.attribute == constraint.attribute
    assert constraint2.value == constraint.value


def test_small_grid_size():
    """Test puzzle generation with minimum valid grid size."""
    puzzle = generate_puzzle(3, "easy")
    
    assert len(puzzle.entities) == 3
    assert len(puzzle.attributes) == 3
    assert len(puzzle.constraints) > 0


def test_large_grid_size():
    """Test puzzle generation with larger grid size."""
    puzzle = generate_puzzle(8, "hard")
    
    assert len(puzzle.entities) == 8
    assert len(puzzle.attributes) == 8
    # Should have many constraints for hard difficulty
    assert len(puzzle.constraints) >= 8 * 2