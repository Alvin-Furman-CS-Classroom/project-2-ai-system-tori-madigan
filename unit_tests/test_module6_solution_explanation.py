"""
Unit tests for Module 6: Solution Explanation.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from module6_solution_explanation import (  # noqa: E402
    _parse_module3_proof,
    module1_2_3_5_to_module6,
)


def test_module6_report_has_required_sections():
    puzzle = {
        "entities": ["E1", "E2"],
        "attributes": {"A1": ["V1", "V2"]},
        "constraints": [{"type": "equality", "entity": "E1", "attribute": "A1", "value": "V1"}],
    }
    kb = "=== KNOWLEDGE BASE ===\n\nFACTS (All possible propositions):\nE1_A1_V1\n"
    m3 = (
        "=== SOLUTION ===\nE1: A1=V1\n\n"
        "INFERENCE STEP COUNT: 2\n"
        "=== PROOF ===\n"
        "1. [deduction] E1 A1 must be V1\n"
        "2. [decision] set E2 A1 = V2\n"
    )
    m5 = (
        "=== COMPLEXITY ANALYSIS REPORT ===\n"
        "OVERALL DIFFICULTY SCORE (0-100): 42.5\n"
        "OVERALL DIFFICULTY LABEL: medium\n"
    )
    out = module1_2_3_5_to_module6(puzzle, kb, m3, m5)
    assert "=== SOLUTION EXPLANATION REPORT ===" in out
    assert "=== OVERALL SOLUTION STRATEGY ===" in out
    assert "=== STEP-BY-STEP REASONING ===" in out
    assert "### Step 1" in out
    assert "### Step 2" in out
    assert "medium" in out
    assert "Propagation" in out or "propagation" in out.lower()
    assert "Search decision" in out or "search decision" in out.lower()


def test_parse_module3_extracts_steps_and_count():
    text = (
        "=== SOLUTION ===\nx\n\nINFERENCE STEP COUNT: 3\n=== PROOF ===\n"
        "1. [deduction] first\n"
        "  2. [deduction] second\n"
        "3. [decision] third\n"
    )
    steps, n = _parse_module3_proof(text)
    assert n == 3
    assert len(steps) == 3
    assert "first" in steps[0]


def test_module6_invalid_puzzle_json_raises():
    with pytest.raises(ValueError):
        module1_2_3_5_to_module6("{not-json}", "kb", "m3", "m5")


def test_module6_missing_puzzle_keys_raises():
    with pytest.raises(ValueError, match="missing required key"):
        module1_2_3_5_to_module6({"entities": []}, "kb", "=== PROOF ===\n", "m5")
