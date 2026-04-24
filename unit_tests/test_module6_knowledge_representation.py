"""
Unit tests for Module 6: Knowledge Representation.
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
from module5_complexity_analysis import module1_2_3_4_to_module5  # noqa: E402
from module6_knowledge_representation import (  # noqa: E402
    explain_to_dict,
    module1_2_3_5_to_module6,
)


def test_module6_generates_structured_explanation_dict():
    random.seed(1001)
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)
    module5_report = module1_2_3_4_to_module5(puzzle_data, kb, module3_output, module4_report)

    report = explain_to_dict(module3_output, kb, puzzle_data, module5_report)

    assert "overall_strategy" in report
    assert isinstance(report["overall_strategy"], str)
    assert "step_by_step_reasoning" in report
    assert isinstance(report["step_by_step_reasoning"], list)
    assert "explanation_metadata" in report
    assert report["explanation_metadata"]["constraint_count"] == len(puzzle_data["constraints"])


def test_module6_text_report_contains_expected_sections():
    random.seed(1002)
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)
    module5_report = module1_2_3_4_to_module5(puzzle_data, kb, module3_output, module4_report)

    text_report = module1_2_3_5_to_module6(module3_output, kb, puzzle_data, module5_report)

    assert "=== SOLUTION EXPLANATION ===" in text_report
    assert "OVERALL STRATEGY" in text_report
    assert "REASONING PHASES" in text_report
    assert "FULL STEP-BY-STEP TRACE" in text_report
    assert "EXPLANATION METADATA" in text_report
    assert "difficulty_label:" in text_report


def test_module6_rejects_invalid_constraints_json():
    with pytest.raises(ValueError, match="invalid constraints json"):
        explain_to_dict(
            solution_proof_text="=== SOLUTION ===\n=== PROOF ===\n",
            knowledge_base_text="",
            constraints_json_or_dict="{not-json}",
            difficulty_metrics_text="",
        )
