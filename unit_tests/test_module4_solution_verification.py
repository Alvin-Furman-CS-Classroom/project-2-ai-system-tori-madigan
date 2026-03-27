"""
Unit tests for Module 4: Solution Verification
"""

import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module3_puzzle_solving import module2_to_module3  # noqa: E402
from module4_solution_verification import (  # noqa: E402
    module1_2_3_to_module4,
    module3_to_module4,
    verify_to_dict,
)


@pytest.mark.parametrize(
    "grid_size,difficulty,seed",
    [
        (3, "easy", 11),
        (4, "medium", 22),
        (5, "hard", 33),
    ],
)
def test_module4_valid_pipeline_case(grid_size: int, difficulty: str, seed: int):
    random.seed(seed)
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty)
    kb = module1_to_module2(puzzle.to_dict())
    module3_output = module2_to_module3(kb)

    report = module1_2_3_to_module4(module3_output, puzzle.to_dict(), kb)

    assert "=== VALIDATION REPORT ===" in report
    assert "OVERALL VALIDATION RESULT: VALID" in report
    assert "LOGICAL ENTAILMENT CHECK: PASS" in report
    assert "VIOLATION SUMMARY:" in report
    assert "None" in report


def test_module4_detects_invalid_solution_text():
    random.seed(44)
    puzzle = generate_puzzle(grid_size=4, difficulty="medium")
    kb = module1_to_module2(puzzle.to_dict())
    module3_output = module2_to_module3(kb)

    # Corrupt one assignment value to force constraint violation.
    broken_output = module3_output.replace("A1=V1", "A1=V999", 1)

    report = module3_to_module4(
        solution_text=broken_output,
        constraints_data=puzzle.to_dict()["constraints"],
        knowledge_base=kb,
        hidden_solution=puzzle.to_dict()["solution"],
    )

    assert "OVERALL VALIDATION RESULT: INVALID" in report
    assert "VIOLATION SUMMARY:" in report
    assert "None" not in report


def test_module4_rejects_missing_solution_assignments():
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    kb = module1_to_module2(puzzle.to_dict())

    report = verify_to_dict(
        solution_text="=== SOLUTION ===\n(no assignments)\n=== PROOF ===",
        constraints_data=puzzle.to_dict()["constraints"],
        knowledge_base=kb,
        hidden_solution=puzzle.to_dict()["solution"],
    )
    assert report["overall_pass"] is False
    assert report["errors"]


def test_module4_json_report_structure_valid_case():
    random.seed(55)
    puzzle = generate_puzzle(grid_size=4, difficulty="medium")
    kb = module1_to_module2(puzzle.to_dict())
    module3_output = module2_to_module3(kb)

    report = verify_to_dict(
        solution_text=module3_output,
        constraints_data=puzzle.to_dict()["constraints"],
        knowledge_base=kb,
        hidden_solution=puzzle.to_dict()["solution"],
    )
    assert report["overall_pass"] is True
    assert report["errors"] == []
    assert isinstance(report["constraint_results"], list)
    assert report["entailment"]["pass"] is True

