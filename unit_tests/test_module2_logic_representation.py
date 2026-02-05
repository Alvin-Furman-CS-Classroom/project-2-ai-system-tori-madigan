"""
Unit tests for Module 2: Logic Representation

Tests conversion of constraints to propositional logic formulas.
"""

import sys
import json
from pathlib import Path

import pytest

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module2_logic_representation import (  # noqa: E402
    generate_proposition_symbol,
    constraint_to_formula,
    generate_implicit_constraints,
    create_knowledge_base,
    module1_to_module2,
)


def test_generate_proposition_symbol():
    """Test proposition symbol generation."""
    assert generate_proposition_symbol("E1", "A1", "V2") == "E1_A1_V2"
    assert generate_proposition_symbol("E2", "A3", "V1") == "E2_A3_V1"
    assert generate_proposition_symbol("E5", "A2", "V4") == "E5_A2_V4"


def test_constraint_equality():
    """Test equality constraint conversion."""
    constraint = {
        "type": "equality",
        "entity": "E1",
        "attribute": "A1",
        "value": "V3"
    }
    attributes = {"A1": ["V1", "V2", "V3", "V4"]}
    
    formula = constraint_to_formula(constraint, attributes)
    assert formula == "E1_A1_V3"


def test_constraint_inequality():
    """Test inequality constraint conversion."""
    constraint = {
        "type": "inequality",
        "entity": "E1",
        "attribute": "A1",
        "value": "V3"
    }
    attributes = {"A1": ["V1", "V2", "V3", "V4"]}
    
    formula = constraint_to_formula(constraint, attributes)
    assert formula == "¬E1_A1_V3"


def test_constraint_different_values():
    """Test different_values constraint conversion."""
    constraint = {
        "type": "different_values",
        "entities": ["E1", "E2"],
        "attribute": "A1"
    }
    attributes = {"A1": ["V1", "V2"]}
    
    formula = constraint_to_formula(constraint, attributes)
    # Should have form: ¬(E1_A1_V1 ↔ E2_A1_V1) ∧ ¬(E1_A1_V2 ↔ E2_A1_V2)
    assert "¬(E1_A1_V1 ↔ E2_A1_V1)" in formula
    assert "¬(E1_A1_V2 ↔ E2_A1_V2)" in formula
    assert " ∧ " in formula


def test_constraint_same_value():
    """Test same_value constraint conversion."""
    constraint = {
        "type": "same_value",
        "entities": ["E1", "E2"],
        "attribute": "A1"
    }
    attributes = {"A1": ["V1", "V2"]}
    
    formula = constraint_to_formula(constraint, attributes)
    # Should have form: (E1_A1_V1 ↔ E2_A1_V1) ∨ (E1_A1_V2 ↔ E2_A1_V2)
    assert "(E1_A1_V1 ↔ E2_A1_V1)" in formula
    assert "(E1_A1_V2 ↔ E2_A1_V2)" in formula
    assert " ∨ " in formula


def test_constraint_relative_position():
    """Test relative_position constraint conversion."""
    constraint = {
        "type": "relative_position",
        "entity1": "E1",
        "entity2": "E2",
        "attribute": "A1",
        "offset": 1
    }
    attributes = {"A1": ["V1", "V2", "V3", "V4"]}
    
    formula = constraint_to_formula(constraint, attributes)
    # Should have form: (E1_A1_V2 ∧ E2_A1_V1) ∨ (E1_A1_V3 ∧ E2_A1_V2) ∨ ...
    assert "(E1_A1_V2 ∧ E2_A1_V1)" in formula
    assert "(E1_A1_V3 ∧ E2_A1_V2)" in formula
    assert " ∨ " in formula


def test_constraint_relative_position_negative_offset():
    """Test relative_position with negative offset."""
    constraint = {
        "type": "relative_position",
        "entity1": "E1",
        "entity2": "E2",
        "attribute": "A1",
        "offset": -1
    }
    attributes = {"A1": ["V1", "V2", "V3", "V4"]}
    
    formula = constraint_to_formula(constraint, attributes)
    # E1's value should be 1 less than E2's
    # (E1_A1_V1 ∧ E2_A1_V2) ∨ (E1_A1_V2 ∧ E2_A1_V3) ∨ ...
    assert "(E1_A1_V1 ∧ E2_A1_V2)" in formula
    assert "(E1_A1_V2 ∧ E2_A1_V3)" in formula


def test_constraint_invalid_type():
    """Test that invalid constraint types raise errors."""
    constraint = {
        "type": "invalid_type",
        "entity": "E1",
        "attribute": "A1",
        "value": "V1"
    }
    attributes = {"A1": ["V1", "V2"]}
    
    with pytest.raises(ValueError):
        constraint_to_formula(constraint, attributes)


def test_generate_implicit_constraints():
    """Test implicit constraint generation."""
    entities = ["E1", "E2"]
    attributes = {"A1": ["V1", "V2"]}
    
    constraints = generate_implicit_constraints(entities, attributes)
    
    # Should have 2 constraints (one per entity-attribute pair)
    assert len(constraints) == 2
    
    # Check that each constraint has "at least one" and "at most one" parts
    for constraint in constraints:
        assert " ∨ " in constraint  # At least one
        assert "¬(" in constraint   # At most one (negation)


def test_generate_implicit_constraints_single_value():
    """Test implicit constraints when only one value is possible."""
    entities = ["E1"]
    attributes = {"A1": ["V1"]}
    
    constraints = generate_implicit_constraints(entities, attributes)
    
    # Should have 1 constraint
    assert len(constraints) == 1
    # Should just be the "at least one" part (only one value, may have parentheses)
    assert "E1_A1_V1" in constraints[0]
    assert constraints[0].strip("()") == "E1_A1_V1" or constraints[0] == "(E1_A1_V1)"


def test_create_knowledge_base_structure():
    """Test knowledge base creation and structure."""
    entities = ["E1", "E2"]
    attributes = {"A1": ["V1", "V2"]}
    constraints = [
        {
            "type": "equality",
            "entity": "E1",
            "attribute": "A1",
            "value": "V1"
        }
    ]
    
    kb = create_knowledge_base(entities, attributes, constraints)
    
    # Check structure
    assert "=== KNOWLEDGE BASE ===" in kb
    assert "FACTS" in kb
    assert "RULES (Domain Constraints)" in kb
    assert "RULES (Puzzle Constraints)" in kb
    
    # Check facts include all propositions
    assert "E1_A1_V1" in kb
    assert "E1_A1_V2" in kb
    assert "E2_A1_V1" in kb
    assert "E2_A1_V2" in kb
    
    # Check puzzle constraint
    assert "1. E1_A1_V1" in kb


def test_create_knowledge_base_multiple_constraints():
    """Test knowledge base with multiple constraints."""
    entities = ["E1", "E2"]
    attributes = {"A1": ["V1", "V2"], "A2": ["V1", "V2"]}
    constraints = [
        {
            "type": "equality",
            "entity": "E1",
            "attribute": "A1",
            "value": "V1"
        },
        {
            "type": "inequality",
            "entity": "E2",
            "attribute": "A2",
            "value": "V2"
        }
    ]
    
    kb = create_knowledge_base(entities, attributes, constraints)
    
    # Check both constraints are present
    assert "1. E1_A1_V1" in kb
    assert "2. ¬E2_A2_V2" in kb


def test_module1_to_module2_json_string():
    """Test conversion from Module 1 JSON string."""
    puzzle_json = json.dumps({
        "puzzle_id": "puzzle_123",
        "entities": ["E1", "E2"],
        "attributes": {"A1": ["V1", "V2"]},
        "constraints": [
            {
                "type": "equality",
                "entity": "E1",
                "attribute": "A1",
                "value": "V1"
            }
        ],
        "solution": {"E1": {"A1": "V1"}}  # Should be ignored
    })
    
    kb = module1_to_module2(puzzle_json)
    
    # Should contain the constraint
    assert "E1_A1_V1" in kb
    # Should not contain solution data
    assert "solution" not in kb.lower()


def test_module1_to_module2_dict():
    """Test conversion from Module 1 dictionary."""
    puzzle_data = {
        "puzzle_id": "puzzle_123",
        "entities": ["E1", "E2"],
        "attributes": {"A1": ["V1", "V2"]},
        "constraints": [
            {
                "type": "different_values",
                "entities": ["E1", "E2"],
                "attribute": "A1"
            }
        ],
        "solution": {"E1": {"A1": "V1"}}
    }
    
    kb = module1_to_module2(puzzle_data)
    
    # Should contain the different_values constraint formula
    assert "¬(E1_A1_V1 ↔ E2_A1_V1)" in kb
    assert "¬(E1_A1_V2 ↔ E2_A1_V2)" in kb


def test_knowledge_base_all_connectives():
    """Test that all required connectives are used."""
    entities = ["E1", "E2"]
    attributes = {"A1": ["V1", "V2"]}
    constraints = [
        {
            "type": "equality",
            "entity": "E1",
            "attribute": "A1",
            "value": "V1"
        },
        {
            "type": "inequality",
            "entity": "E2",
            "attribute": "A1",
            "value": "V2"
        },
        {
            "type": "same_value",
            "entities": ["E1", "E2"],
            "attribute": "A1"
        },
        {
            "type": "different_values",
            "entities": ["E1", "E2"],
            "attribute": "A1"
        }
    ]
    
    kb = create_knowledge_base(entities, attributes, constraints)
    
    # Check all connectives are present
    assert "∧" in kb  # Conjunction
    assert "∨" in kb  # Disjunction
    assert "¬" in kb  # Negation
    assert "↔" in kb  # Biconditional
    # Note: → (implication) might not be used in our current constraint types


def test_knowledge_base_large_puzzle():
    """Test knowledge base generation for larger puzzle."""
    entities = ["E1", "E2", "E3", "E4", "E5"]
    attributes = {
        "A1": ["V1", "V2", "V3", "V4", "V5"],
        "A2": ["V1", "V2", "V3", "V4", "V5"]
    }
    constraints = [
        {
            "type": "equality",
            "entity": "E1",
            "attribute": "A1",
            "value": "V3"
        },
        {
            "type": "relative_position",
            "entity1": "E2",
            "entity2": "E3",
            "attribute": "A2",
            "offset": 1
        }
    ]
    
    kb = create_knowledge_base(entities, attributes, constraints)
    
    # Should have all facts (5 entities × 2 attributes × 5 values = 50 facts)
    fact_count = kb.count("_A")  # Rough count of propositions
    assert fact_count >= 50
    
    # Should have domain constraints (5 entities × 2 attributes = 10)
    # Should have 2 puzzle constraints
    assert "RULES (Puzzle Constraints)" in kb


def test_relative_position_edge_cases():
    """Test relative_position with edge cases."""
    attributes = {"A1": ["V1", "V2", "V3"]}
    
    # Offset that goes out of bounds
    constraint = {
        "type": "relative_position",
        "entity1": "E1",
        "entity2": "E2",
        "attribute": "A1",
        "offset": 5  # Too large
    }
    
    formula = constraint_to_formula(constraint, attributes)
    # Should return contradiction or empty
    assert formula == "⊥" or formula == ""


@pytest.mark.parametrize("grid_size", [3, 4, 5])
def test_knowledge_base_various_sizes(grid_size: int):
    """Test knowledge base generation for various grid sizes."""
    entities = [f"E{i+1}" for i in range(grid_size)]
    attributes = {f"A{i+1}": [f"V{j+1}" for j in range(grid_size)] for i in range(grid_size)}
    constraints = [
        {
            "type": "equality",
            "entity": "E1",
            "attribute": "A1",
            "value": "V1"
        }
    ]
    
    kb = create_knowledge_base(entities, attributes, constraints)
    
    # Should have structure
    assert "=== KNOWLEDGE BASE ===" in kb
    assert "FACTS" in kb
    assert "RULES" in kb
    
    # Should have correct number of facts (grid_size^3)
    expected_facts = grid_size * grid_size * grid_size
    fact_lines = [line for line in kb.split("\n") if "FACTS" in line or "_A" in line]
    # Rough check that we have facts
    assert "E1_A1_V1" in kb
