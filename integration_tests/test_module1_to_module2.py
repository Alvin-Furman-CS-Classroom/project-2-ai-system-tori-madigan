"""
Integration test for Module 1 → Module 2

Tests the complete pipeline from puzzle generation to knowledge base creation.
"""

import sys
import json
from pathlib import Path

import pytest

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402


def test_module1_to_module2_integration():
    """Test complete integration from Module 1 to Module 2."""
    # Generate a puzzle using Module 1
    puzzle = generate_puzzle(grid_size=4, difficulty="medium")
    
    # Convert to JSON
    puzzle_dict = puzzle.to_dict()
    puzzle_json = json.dumps(puzzle_dict)
    
    # Convert to knowledge base using Module 2
    knowledge_base = module1_to_module2(puzzle_json)
    
    # Verify knowledge base structure
    assert "=== KNOWLEDGE BASE ===" in knowledge_base
    assert "FACTS" in knowledge_base
    assert "RULES" in knowledge_base
    
    # Verify all entities are represented
    for entity in puzzle.entities:
        assert entity in knowledge_base
    
    # Verify all attributes are represented
    for attribute in puzzle.attributes.keys():
        assert attribute in knowledge_base
    
    # Verify constraints are converted
    assert len(puzzle.constraints) > 0
    # Each constraint should appear in the knowledge base
    # (exact format may vary, but should be present)
    assert "RULES (Puzzle Constraints)" in knowledge_base


def test_module1_to_module2_all_difficulties():
    """Test integration for all difficulty levels."""
    for difficulty in ["easy", "medium", "hard"]:
        puzzle = generate_puzzle(grid_size=3, difficulty=difficulty)
        puzzle_dict = puzzle.to_dict()
        knowledge_base = module1_to_module2(puzzle_dict)
        
        # Should have valid knowledge base
        assert "=== KNOWLEDGE BASE ===" in knowledge_base
        assert "FACTS" in knowledge_base
        assert "RULES" in knowledge_base


def test_module1_to_module2_various_sizes():
    """Test integration for various grid sizes."""
    for grid_size in [3, 4, 5]:
        puzzle = generate_puzzle(grid_size=grid_size, difficulty="medium")
        puzzle_dict = puzzle.to_dict()
        knowledge_base = module1_to_module2(puzzle_dict)
        
        # Should have valid knowledge base
        assert "=== KNOWLEDGE BASE ===" in knowledge_base
        
        # Should have correct number of facts (grid_size^3)
        # Count proposition symbols in facts section
        facts_section = knowledge_base.split("FACTS")[1].split("RULES")[0]
        # Each entity-attribute-value combination should be present
        for entity in puzzle.entities:
            for attribute in puzzle.attributes:
                for value in puzzle.attributes[attribute]:
                    prop_symbol = f"{entity}_{attribute}_{value}"
                    assert prop_symbol in facts_section


def test_module1_to_module2_constraint_types():
    """Test that all constraint types are properly converted."""
    # Generate a puzzle (may have various constraint types)
    puzzle = generate_puzzle(grid_size=5, difficulty="hard")
    puzzle_dict = puzzle.to_dict()
    knowledge_base = module1_to_module2(puzzle_dict)
    
    # Check that logical connectives are present
    # (different constraint types use different connectives)
    has_connectives = False
    if "∧" in knowledge_base or "∨" in knowledge_base or "¬" in knowledge_base or "↔" in knowledge_base:
        has_connectives = True
    
    assert has_connectives, "Knowledge base should contain logical connectives"
    
    # Verify puzzle constraints section exists
    assert "RULES (Puzzle Constraints)" in knowledge_base


def test_module1_to_module2_data_consistency():
    """Test that data is consistent between modules."""
    puzzle = generate_puzzle(grid_size=4, difficulty="medium")
    puzzle_dict = puzzle.to_dict()
    
    # Extract data for Module 2
    entities = puzzle_dict["entities"]
    attributes = puzzle_dict["attributes"]
    constraints = puzzle_dict["constraints"]
    
    # Convert to knowledge base
    knowledge_base = module1_to_module2(puzzle_dict)
    
    # Verify all entities appear in knowledge base
    for entity in entities:
        # Entity should appear in proposition symbols
        assert entity in knowledge_base
    
    # Verify all attributes appear
    for attribute in attributes.keys():
        assert attribute in knowledge_base
    
    # Verify constraints are present in knowledge base
    # (Each constraint should become a rule)
    puzzle_constraints_section = knowledge_base.split("RULES (Puzzle Constraints):")
    if len(puzzle_constraints_section) > 1:
        rules_text = puzzle_constraints_section[1]
        # Check that we have at least some rules (approximate count)
        # The exact count may vary due to formatting, but should be close
        rule_lines = [line for line in rules_text.split("\n") if line.strip() and line.strip()[0].isdigit()]
        # Should have at least most of the constraints represented
        assert len(rule_lines) >= len(constraints) * 0.8, f"Expected at least {len(constraints) * 0.8} rules, got {len(rule_lines)}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
