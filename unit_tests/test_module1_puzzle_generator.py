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
    generate_entities,
    generate_attributes,
    generate_solution,
    generate_puzzle,
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


def test_generate_puzzle_invalid_grid_size():
    with pytest.raises(ValueError):
        generate_puzzle(0, "easy")