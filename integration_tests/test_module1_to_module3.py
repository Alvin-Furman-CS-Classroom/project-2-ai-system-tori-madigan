"""
Integration test for Module 1 → Module 2 → Module 3

Ensures the full pipeline produces a valid solution:
- Module 1 generates a puzzle (with hidden ground truth)
- Module 2 converts it into a propositional-logic knowledge base
- Module 3 solves the KB and returns a solution + proof

Correctness check:
We validate Module 3's produced assignment satisfies the "Puzzle Constraints"
rules encoded by Module 2 (rather than requiring an exact match to Module 1's
hidden solution, since multiple solutions can exist if the constraint encoding
doesn't fully enforce uniqueness).
"""

import random
import sys
from pathlib import Path

import pytest

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module3_puzzle_solving import (  # noqa: E402
    module2_to_module3,
    count_solutions_from_kb,
    _extract_entities_attributes_values,
    _extract_puzzle_rule_formulas,
    _parse_puzzle_constraint,
)


def _parse_solution_from_output(output: str):
    sol = {}
    for line in output.splitlines():
        line = line.strip()
        if not line.startswith("E") or ":" not in line:
            continue
        ent = line.split(":", 1)[0].strip()
        rhs = line.split(":", 1)[1].strip()
        parts = [p.strip() for p in rhs.split(",") if p.strip()]
        for part in parts:
            if "=" not in part:
                continue
            attr, val = part.split("=", 1)
            sol.setdefault(ent, {})[attr.strip()] = val.strip()
    return sol


@pytest.mark.parametrize(
    "grid_size,difficulty,seed",
    [
        (3, "easy", 777),
        (4, "medium", 888),
        (5, "hard", 999),
    ],
)
def test_module1_to_module2_to_module3_pipeline_satisfies_constraints(grid_size: int, difficulty: str, seed: int):
    random.seed(seed)
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty)
    kb = module1_to_module2(puzzle.to_dict())
    out = module2_to_module3(kb)
    # Module 1 uniqueness requirement: generated puzzle should have exactly one solution.
    assert count_solutions_from_kb(kb, max_solutions=2) == 1

    assert "=== SOLUTION ===" in out
    assert "=== PROOF ===" in out
    assert "INFERENCE STEP COUNT:" in out

    sol = _parse_solution_from_output(out)
    entities, attributes = _extract_entities_attributes_values(kb)
    formulas = _extract_puzzle_rule_formulas(kb)
    constraints = [_parse_puzzle_constraint(f) for f in formulas]

    def _idx(val_symbol: str) -> int:
        assert val_symbol.startswith("V")
        return int(val_symbol[1:])

    # Validate that the Module 3 solution satisfies every puzzle constraint.
    for c in constraints:
        if c.type == "equality":
            assert sol[c.entity][c.attribute] == c.value  # type: ignore[index]
        elif c.type == "inequality":
            assert sol[c.entity][c.attribute] != c.value  # type: ignore[index]
        elif c.type == "different_values":
            assert sol[c.entity1][c.attribute] != sol[c.entity2][c.attribute]  # type: ignore[index]
        elif c.type == "same_value":
            assert sol[c.entity1][c.attribute] == sol[c.entity2][c.attribute]  # type: ignore[index]
        elif c.type == "relative_position":
            v1 = _idx(sol[c.entity1][c.attribute])  # type: ignore[index]
            v2 = _idx(sol[c.entity2][c.attribute])  # type: ignore[index]
            assert v1 == v2 + c.offset  # type: ignore[operator]
        else:
            pytest.fail(f"Unsupported parsed constraint type: {c.type}")

