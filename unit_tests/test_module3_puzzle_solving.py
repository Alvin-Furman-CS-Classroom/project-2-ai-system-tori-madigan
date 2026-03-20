"""
Unit tests for Module 3: Puzzle Solving

Focus:
- Module 3 output format (solution + proof)
- Solution completeness (all entities/attributes assigned)
- Solution correctness (satisfies puzzle constraints encoded in Module 2)
"""

import random
import sys
import re
from pathlib import Path

import pytest

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module3_puzzle_solving import (  # noqa: E402
    module2_to_module3,
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


def _parse_inference_step_count(output: str) -> int:
    m = re.search(r"INFERENCE STEP COUNT:\s*(\d+)", output)
    assert m is not None, "Expected inference step count line"
    return int(m.group(1))


def _count_proof_steps(output: str) -> int:
    if "=== PROOF ===" not in output:
        return 0
    proof_text = output.split("=== PROOF ===", 1)[1].strip()
    lines = [ln.strip() for ln in proof_text.splitlines() if ln.strip()]
    # Expected format: "1. ...", "2. ...", ...
    return sum(1 for ln in lines if re.match(r"^\d+\.\s*", ln))


@pytest.mark.parametrize(
    "grid_size,difficulty,seed",
    [
        (3, "easy", 10),
        (4, "easy", 20),
        (4, "medium", 30),
        (4, "hard", 40),
        (5, "medium", 50),
    ],
)
def test_module3_output_format_and_solution_completeness(grid_size: int, difficulty: str, seed: int):
    random.seed(seed)
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty)
    kb = module1_to_module2(puzzle.to_dict())
    out = module2_to_module3(kb)

    assert "=== SOLUTION ===" in out
    assert "=== PROOF ===" in out
    assert "INFERENCE STEP COUNT:" in out

    step_count = _parse_inference_step_count(out)
    proof_steps = _count_proof_steps(out)
    assert proof_steps == step_count

    sol = _parse_solution_from_output(out)
    entities, attributes = _extract_entities_attributes_values(kb)

    # Ensure all entities and all attributes are present.
    for ent in entities:
        assert ent in sol, f"Missing entity assignment for {ent}"
        for attr in attributes.keys():
            assert attr in sol[ent], f"Missing attribute assignment for {ent}:{attr}"
            val = sol[ent][attr]
            assert val in attributes[attr], f"Value {val} not allowed for {ent}:{attr}"


@pytest.mark.parametrize(
    "grid_size,difficulty,seed",
    [
        (3, "easy", 101),
        (4, "medium", 202),
        (4, "hard", 303),
        (5, "hard", 404),
    ],
)
def test_module3_solution_satisfies_puzzle_constraints(grid_size: int, difficulty: str, seed: int):
    random.seed(seed)
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty)
    kb = module1_to_module2(puzzle.to_dict())
    out = module2_to_module3(kb)

    sol = _parse_solution_from_output(out)
    entities, attributes = _extract_entities_attributes_values(kb)

    formulas = _extract_puzzle_rule_formulas(kb)
    constraints = [_parse_puzzle_constraint(f) for f in formulas]

    def _idx(val_symbol: str) -> int:
        assert val_symbol.startswith("V")
        return int(val_symbol[1:])

    # Check each puzzle constraint is satisfied by the produced solution.
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
            pytest.fail(f"Unknown/unsupported parsed constraint type: {c.type}")


def test_module3_missing_knowledge_base_markers_raises_value_error():
    kb = "this is not a valid knowledge base"
    with pytest.raises(ValueError):
        module2_to_module3(kb)


def test_module3_unrecognized_puzzle_constraint_formula_raises_value_error():
    # Minimal KB text that still lets Module 3 extract E*/A*/V* symbols from FACTS.
    kb = "\n".join(
        [
            "=== KNOWLEDGE BASE ===",
            "",
            "FACTS (All possible propositions):",
            "E1_A1_V1, E1_A1_V2, E2_A1_V1, E2_A1_V2",
            "",
            "RULES (Domain Constraints):",
            "1. (E1_A1_V1 ∨ E1_A1_V2) ∧ (¬(E1_A1_V1 ∧ E1_A1_V2))",
            "",
            "RULES (Puzzle Constraints):",
            "1. nonsense_formula",
        ]
    )

    with pytest.raises(ValueError):
        module2_to_module3(kb)

