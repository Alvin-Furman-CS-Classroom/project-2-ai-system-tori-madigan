"""
Unit tests for Module 5: Complexity Analysis.
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
from module5_complexity_analysis import (  # noqa: E402
    _fallback_score_from_thresholds,
    analyze_to_dict,
    complexity_dict_to_text,
    module1_2_3_4_to_module5,
)


@pytest.mark.parametrize(
    "grid_size,difficulty,seed",
    [
        (3, "easy", 131),
        (4, "medium", 242),
    ],
)
def test_module5_metrics_present(grid_size: int, difficulty: str, seed: int):
    random.seed(seed)
    puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty)
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)

    report = analyze_to_dict(puzzle_data, kb, module3_output, module4_report)

    assert report["validation_pass"] is True
    metrics = report["metrics"]
    assert "constraint_count" in metrics
    assert "search_space_size" in metrics
    assert "inference_step_count" in metrics
    assert "constraint_density" in metrics
    assert "logical_formula_complexity" in metrics
    assert "branching_factor" in metrics
    assert "solution_uniqueness" in metrics
    assert metrics["solution_uniqueness"]["value"] == "unique"
    assert isinstance(report["overall_difficulty_score"], (int, float))
    assert report["overall_difficulty_label"] in {"easy", "medium", "hard"}


def test_module5_inference_step_count_uses_explicit_marker():
    puzzle_data = {
        "entities": ["E1", "E2", "E3"],
        "attributes": {"A1": ["V1", "V2", "V3"]},
        "constraints": [{"type": "equality", "entity": "E1", "attribute": "A1", "value": "V1"}],
    }
    kb = (
        "=== KNOWLEDGE BASE ===\n\n"
        "FACTS (All possible propositions):\nE1_A1_V1\n\n"
        "RULES (Domain Constraints):\n1. (E1_A1_V1)\n\n"
        "RULES (Puzzle Constraints):\n1. E1_A1_V1\n"
    )
    module3_output = (
        "=== SOLUTION ===\n"
        "E1: A1=V1\n"
        "E2: A1=V2\n"
        "E3: A1=V3\n\n"
        "INFERENCE STEP COUNT: 7\n"
        "=== PROOF ===\n"
        "1. [deduction] ...\n"
    )
    module4_report = "=== VALIDATION REPORT ===\nOVERALL VALIDATION RESULT: VALID\n"

    report = analyze_to_dict(puzzle_data, kb, module3_output, module4_report)
    assert report["metrics"]["inference_step_count"]["value"] == 7


def test_module5_text_report_contains_all_metric_labels():
    random.seed(808)
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)

    text_report = module1_2_3_4_to_module5(puzzle_data, kb, module3_output, module4_report)

    assert "=== COMPLEXITY ANALYSIS REPORT ===" in text_report
    assert "constraint_count" in text_report
    assert "search_space_size" in text_report
    assert "inference_step_count" in text_report
    assert "constraint_density" in text_report
    assert "logical_formula_complexity" in text_report
    assert "branching_factor" in text_report
    assert "solution_uniqueness" in text_report
    assert "OVERALL DIFFICULTY SCORE (0-100):" in text_report
    assert "OVERALL DIFFICULTY LABEL:" in text_report


def test_module5_uses_historical_dataset_for_percentile_scoring():
    random.seed(909)
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)

    historical_dataset = [
        {
            "constraint_count": 3,
            "search_space_size": 2_000,
            "inference_step_count": 1,
            "constraint_density": 0.2,
            "logical_formula_complexity": 5,
            "branching_factor": 1.2,
        },
        {
            "constraint_count": 7,
            "search_space_size": 5_000,
            "inference_step_count": 3,
            "constraint_density": 0.5,
            "logical_formula_complexity": 12,
            "branching_factor": 1.8,
        },
        {
            "constraint_count": 12,
            "search_space_size": 80_000,
            "inference_step_count": 8,
            "constraint_density": 0.9,
            "logical_formula_complexity": 40,
            "branching_factor": 3.0,
        },
    ]

    report = analyze_to_dict(
        puzzle_data,
        kb,
        module3_output,
        module4_report,
        historical_dataset=historical_dataset,
    )

    assert report["difficulty_scoring_details"]["method"] == "historical_percentile"
    assert report["difficulty_scoring_details"]["compared_against"] == "3 historical puzzles"
    assert 0 <= report["overall_difficulty_score"] <= 100
    rendered = complexity_dict_to_text(report)
    assert "per_metric_contribution" in rendered
    assert "constraint_count" in report["difficulty_scoring_details"]["metric_scores"]


def test_module5_invalid_historical_json_falls_back_gracefully():
    random.seed(919)
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)

    report = analyze_to_dict(
        puzzle_data,
        kb,
        module3_output,
        module4_report,
        historical_dataset="{not-json}",
    )

    assert report["difficulty_scoring_details"]["method"] == "fallback_thresholds"
    assert "invalid historical dataset json" in report["difficulty_scoring_details"]["compared_against"]


def test_module5_invalid_puzzle_json_raises_value_error():
    with pytest.raises(ValueError, match="invalid puzzle json"):
        analyze_to_dict(
            "{not-json}",
            knowledge_base="=== KNOWLEDGE BASE ===\nRULES (Puzzle Constraints):\n1. E1_A1_V1\n",
            solution_proof_text="",
            validation_report_text="",
        )


def test_module5_missing_required_puzzle_keys_raises_value_error():
    with pytest.raises(ValueError, match="missing required keys"):
        analyze_to_dict(
            {"entities": ["E1"], "attributes": {"A1": ["V1"]}},
            knowledge_base="=== KNOWLEDGE BASE ===\nRULES (Puzzle Constraints):\n1. E1_A1_V1\n",
            solution_proof_text="",
            validation_report_text="",
        )


def test_fallback_threshold_reflects_constraint_count_and_density():
    """Fewer clues / sparser density should increase fallback difficulty score (inverse signals)."""
    shared = {
        "search_space_size": {"value": 5000},
        "inference_step_count": {"value": 2},
        "branching_factor": {"value": 2.5},
        "logical_formula_complexity": {"value": 30},
        "solution_uniqueness": {"value": "unique"},
    }
    fewer_clues = {
        **shared,
        "constraint_count": {"value": 3},
        "constraint_density": {"value": 0.5},
    }
    more_clues = {
        **shared,
        "constraint_count": {"value": 20},
        "constraint_density": {"value": 0.5},
    }
    assert _fallback_score_from_thresholds(fewer_clues) > _fallback_score_from_thresholds(more_clues)

    sparse_density = {
        **shared,
        "constraint_count": {"value": 10},
        "constraint_density": {"value": 0.1},
    }
    dense_density = {
        **shared,
        "constraint_count": {"value": 10},
        "constraint_density": {"value": 1.2},
    }
    assert _fallback_score_from_thresholds(sparse_density) > _fallback_score_from_thresholds(dense_density)


def test_module5_non_list_historical_dataset_falls_back():
    random.seed(920)
    puzzle = generate_puzzle(grid_size=3, difficulty="easy")
    puzzle_data = puzzle.to_dict()
    kb = module1_to_module2(puzzle_data)
    module3_output = module2_to_module3(kb)
    module4_report = module1_2_3_to_module4(module3_output, puzzle_data, kb)

    report = analyze_to_dict(
        puzzle_data,
        kb,
        module3_output,
        module4_report,
        historical_dataset='{"bad":"shape"}',
    )
    assert report["difficulty_scoring_details"]["method"] == "fallback_thresholds"
    assert "must be a list" in report["difficulty_scoring_details"]["compared_against"]
