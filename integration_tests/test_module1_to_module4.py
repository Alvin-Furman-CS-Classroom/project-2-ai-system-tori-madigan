"""
Integration test for Module 1 -> Module 2 -> Module 3 -> Module 4
"""

import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module3_puzzle_solving import module2_to_module3  # noqa: E402
from module4_solution_verification import module1_2_3_to_module4  # noqa: E402


@pytest.mark.parametrize(
    "grid_size,difficulty,seed",
    [
        (3, "easy", 1010),
        (4, "medium", 2020),
    ],
)
def test_full_pipeline_to_module4(grid_size: int, difficulty: str, seed: int):
    random.seed(seed)
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty)

    puzzle_data = puzzle.to_dict()
    module2_kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(module2_kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, module2_kb)

    assert "=== VALIDATION REPORT ===" in module4_report
    assert "PER-CONSTRAINT RESULTS:" in module4_report
    assert "LOGICAL ENTAILMENT CHECK:" in module4_report
    assert "HIDDEN SOLUTION COMPARISON:" in module4_report
    assert "VIOLATION SUMMARY:" in module4_report

