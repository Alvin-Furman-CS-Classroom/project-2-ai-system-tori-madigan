"""
Module 5: Complexity Analysis

Computes explicit difficulty metrics from the outputs of Modules 1-4.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from typing import Any, Dict, List, Optional

from module3_puzzle_solving import count_solutions_from_kb

METRIC_RENDER_ORDER = [
    "constraint_count",
    "search_space_size",
    "inference_step_count",
    "constraint_density",
    "logical_formula_complexity",
    "branching_factor",
    "solution_uniqueness",
]

# Difficulty label boundaries.
EASY_MAX_EXCLUSIVE = 34.0
MEDIUM_MAX_EXCLUSIVE = 68.0

# Interpretation thresholds.
CONSTRAINT_COUNT_LOW_MAX_EXCLUSIVE = 8
CONSTRAINT_COUNT_MEDIUM_MAX_EXCLUSIVE = 16
SEARCH_SPACE_SMALL_MAX_EXCLUSIVE = 10_000
SEARCH_SPACE_MEDIUM_MAX_EXCLUSIVE = 1_000_000
DENSITY_SPARSE_MAX_EXCLUSIVE = 0.4
DENSITY_MODERATE_MAX_EXCLUSIVE = 1.0
FORMULA_SIMPLE_MAX_EXCLUSIVE = 20
FORMULA_MODERATE_MAX_EXCLUSIVE = 80
BRANCHING_LOW_MAX_EXCLUSIVE = 2.0
BRANCHING_MODERATE_MAX_EXCLUSIVE = 4.0

# Fallback score constants.
FALLBACK_SEARCH_SPACE_SMALL_SCORE = 15.0
FALLBACK_SEARCH_SPACE_MEDIUM_SCORE = 35.0
FALLBACK_SEARCH_SPACE_LARGE_SCORE = 55.0
FALLBACK_INFERENCE_STEP_CAP = 20.0
FALLBACK_BRANCHING_LOW_SCORE = 5.0
FALLBACK_BRANCHING_MEDIUM_SCORE = 12.0
FALLBACK_BRANCHING_HIGH_SCORE = 18.0
FALLBACK_FORMULA_SIMPLE_SCORE = 5.0
FALLBACK_FORMULA_MODERATE_SCORE = 10.0
FALLBACK_FORMULA_HIGH_SCORE = 15.0
FALLBACK_UNIQUENESS_MULTIPLE_SCORE = 10.0
FALLBACK_UNIQUENESS_UNIQUE_SCORE = 5.0

# Fallback: constraint count (inverse — fewer explicit clues tends to raise difficulty)
FALLBACK_CONSTRAINT_FEW_SCORE = 12.0
FALLBACK_CONSTRAINT_MODERATE_SCORE = 8.0
FALLBACK_CONSTRAINT_MANY_SCORE = 4.0

# Fallback: constraint density (inverse — sparser constraints per variable tends to raise difficulty)
FALLBACK_DENSITY_SPARSE_SCORE = 10.0
FALLBACK_DENSITY_MODERATE_SCORE = 6.0
FALLBACK_DENSITY_DENSE_SCORE = 3.0

# Historical scoring directions:
# - "direct": larger values imply harder puzzle
# - "inverse": larger values imply easier puzzle
DIFFICULTY_DIRECTION_BY_METRIC = {
    "constraint_count": "inverse",
    "search_space_size": "direct",
    "inference_step_count": "direct",
    "constraint_density": "direct",
    "logical_formula_complexity": "direct",
    "branching_factor": "direct",
}


def analyze_to_dict(
    puzzle_structure: Dict[str, Any] | str,
    knowledge_base: str,
    solution_proof_text: str,
    validation_report_text: str,
    historical_dataset: Optional[List[Dict[str, Any]] | str] = None,
) -> Dict[str, Any]:
    """
    Canonical structured API for Module 5.

    Inputs:
    - puzzle_structure: Module 1 puzzle dict/json
    - knowledge_base: Module 2 text output
    - solution_proof_text: Module 3 text output
    - validation_report_text: Module 4 text output
    - historical_dataset: optional JSON/list baseline for percentile scoring.

    Returns:
    - JSON-serializable dictionary containing metric values, interpretations,
      overall difficulty score/label, and scoring metadata.
    """
    puzzle_data = _parse_puzzle_structure(puzzle_structure)
    metrics = _build_metrics(
        puzzle_data=puzzle_data,
        knowledge_base=knowledge_base,
        solution_proof_text=solution_proof_text,
    )
    solution_count = count_solutions_from_kb(knowledge_base, max_solutions=2)
    validation_pass = "OVERALL VALIDATION RESULT: VALID" in validation_report_text
    metrics["solution_uniqueness"] = _build_solution_uniqueness_metric(solution_count)

    baseline_scoring = _compute_overall_difficulty(metrics, historical_dataset)

    return {
        "overall_pass": validation_pass and solution_count == 1,
        "validation_pass": validation_pass,
        "metrics": metrics,
        "overall_difficulty_score": baseline_scoring["score"],
        "overall_difficulty_label": baseline_scoring["label"],
        "difficulty_scoring_details": baseline_scoring,
    }


def complexity_dict_to_text(report: Dict[str, Any]) -> str:
    """
    Render a human-readable complexity report from `analyze_to_dict`.
    """
    metrics = report.get("metrics", {})
    lines = [
        "=== COMPLEXITY ANALYSIS REPORT ===",
        f"OVERALL COMPLEXITY STATUS: {'PASS' if report.get('overall_pass') else 'CHECK'}",
        f"UPSTREAM VALIDATION PASS: {report.get('validation_pass')}",
        f"OVERALL DIFFICULTY SCORE (0-100): {report.get('overall_difficulty_score')}",
        f"OVERALL DIFFICULTY LABEL: {report.get('overall_difficulty_label')}",
        "",
        "METRICS:",
    ]

    for metric_name in METRIC_RENDER_ORDER:
        metric = metrics.get(metric_name, {})
        value = metric.get("value")
        interpretation = metric.get("interpretation", "")
        lines.append(f"- {metric_name}: {value}")
        lines.append(f"  interpretation: {interpretation}")
        if metric_name == "solution_uniqueness":
            capped_count = metric.get("solution_count_capped_at_2")
            lines.append(f"  solution_count_capped_at_2: {capped_count}")

    scoring = report.get("difficulty_scoring_details", {})
    method = scoring.get("method")
    lines.extend(
        [
            "",
            "DIFFICULTY SCORING:",
            f"- method: {method}",
            f"- compared_against: {scoring.get('compared_against')}",
        ]
    )
    metric_scores = scoring.get("metric_scores") or {}
    if isinstance(metric_scores, dict) and metric_scores:
        lines.append("- per_metric_contribution (0-1, higher => harder):")
        for name in sorted(metric_scores.keys()):
            lines.append(f"  - {name}: {metric_scores[name]}")

    return "\n".join(lines)


def module1_2_3_4_to_module5(
    puzzle_structure: Dict[str, Any] | str,
    knowledge_base: str,
    solution_proof_text: str,
    validation_report_text: str,
    historical_dataset: Optional[List[Dict[str, Any]] | str] = None,
) -> str:
    """
    Main entry point for Module 5 complexity analysis.
    """
    report = analyze_to_dict(
        puzzle_structure=puzzle_structure,
        knowledge_base=knowledge_base,
        solution_proof_text=solution_proof_text,
        validation_report_text=validation_report_text,
        historical_dataset=historical_dataset,
    )
    return complexity_dict_to_text(report)


def _compute_overall_difficulty(
    metrics: Dict[str, Dict[str, Any]],
    historical_dataset: Optional[List[Dict[str, Any]] | str],
) -> Dict[str, Any]:
    """
    Compute overall difficulty score and label.

    Uses historical percentile scoring when valid baseline data is provided;
    otherwise falls back to deterministic threshold-based scoring.
    """
    if historical_dataset is None:
        return _fallback_scoring_result(metrics, "built-in threshold bands")

    try:
        historical_rows = _normalize_historical_dataset(historical_dataset)
    except ValueError as exc:
        return _fallback_scoring_result(metrics, str(exc))

    if not historical_rows:
        return _fallback_scoring_result(metrics, "empty historical dataset")

    metric_percentiles: Dict[str, float] = {}
    for metric_name, direction in DIFFICULTY_DIRECTION_BY_METRIC.items():
        current_value = metrics.get(metric_name, {}).get("value")
        if not isinstance(current_value, (int, float)):
            continue
        baseline_values = [
            float(row[metric_name])
            for row in historical_rows
            if isinstance(row, dict) and isinstance(row.get(metric_name), (int, float))
        ]
        if not baseline_values:
            continue
        percentile = _percentile_rank(float(current_value), baseline_values)
        score_component = percentile if direction == "direct" else (1.0 - percentile)
        metric_percentiles[metric_name] = max(0.0, min(1.0, score_component))

    if not metric_percentiles:
        return _fallback_scoring_result(metrics, "historical dataset missing required numeric fields")

    mean_component = sum(metric_percentiles.values()) / len(metric_percentiles)
    final_score = round(mean_component * 100.0, 2)
    return {
        "method": "historical_percentile",
        "compared_against": f"{len(historical_rows)} historical puzzles",
        "score": final_score,
        "label": _score_to_label(final_score),
        "metric_scores": metric_percentiles,
    }


def _normalize_historical_dataset(
    historical_dataset: List[Dict[str, Any]] | str,
) -> List[Dict[str, Any]]:
    """
    Parse and validate historical baseline data.

    Accepts either a JSON string or a Python list of dictionaries.
    Non-dict rows are ignored; malformed JSON and non-list top-level payloads
    raise ValueError so the caller can trigger safe fallback scoring.
    """
    if isinstance(historical_dataset, str):
        try:
            loaded = json.loads(historical_dataset)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid historical dataset json: {exc.msg}") from exc
    else:
        loaded = historical_dataset

    if not isinstance(loaded, list):
        raise ValueError("historical dataset must be a list of metric dictionaries")

    normalized_rows: List[Dict[str, Any]] = []
    for row in loaded:
        if isinstance(row, dict):
            normalized_rows.append(row)
    return normalized_rows


def _fallback_scoring_result(metrics: Dict[str, Dict[str, Any]], compared_against: str) -> Dict[str, Any]:
    """Build a standard fallback scoring payload."""
    fallback_score = _fallback_score_from_thresholds(metrics)
    return {
        "method": "fallback_thresholds",
        "compared_against": compared_against,
        "score": fallback_score,
        "label": _score_to_label(fallback_score),
        "metric_scores": {},
    }


def _percentile_rank(value: float, baseline_values: List[float]) -> float:
    """Return empirical percentile rank in [0, 1] using <= comparison."""
    sorted_vals = sorted(baseline_values)
    if not sorted_vals:
        return 0.5
    less_or_equal = sum(1 for v in sorted_vals if v <= value)
    return less_or_equal / len(sorted_vals)


def _fallback_score_from_thresholds(metrics: Dict[str, Dict[str, Any]]) -> float:
    """
    Compute deterministic fallback difficulty score.

    This path is used when no valid historical baseline is available.
    Incorporates all primary numeric signals (including constraint count and
    density) so the aggregate score reflects the same dimensions as the
    historical-percentile path.
    """
    score = 0.0

    # constraint_count (inverse vs difficulty: fewer clues => higher score)
    constraint_count = int(metrics.get("constraint_count", {}).get("value", 0))
    if constraint_count < CONSTRAINT_COUNT_LOW_MAX_EXCLUSIVE:
        score += FALLBACK_CONSTRAINT_FEW_SCORE
    elif constraint_count < CONSTRAINT_COUNT_MEDIUM_MAX_EXCLUSIVE:
        score += FALLBACK_CONSTRAINT_MODERATE_SCORE
    else:
        score += FALLBACK_CONSTRAINT_MANY_SCORE

    # constraint_density (inverse: sparser => higher score)
    density = float(metrics.get("constraint_density", {}).get("value", 0.0))
    if density < DENSITY_SPARSE_MAX_EXCLUSIVE:
        score += FALLBACK_DENSITY_SPARSE_SCORE
    elif density < DENSITY_MODERATE_MAX_EXCLUSIVE:
        score += FALLBACK_DENSITY_MODERATE_SCORE
    else:
        score += FALLBACK_DENSITY_DENSE_SCORE

    # search_space_size
    search_space = float(metrics.get("search_space_size", {}).get("value", 0.0))
    if search_space < SEARCH_SPACE_SMALL_MAX_EXCLUSIVE:
        score += FALLBACK_SEARCH_SPACE_SMALL_SCORE
    elif search_space < SEARCH_SPACE_MEDIUM_MAX_EXCLUSIVE:
        score += FALLBACK_SEARCH_SPACE_MEDIUM_SCORE
    else:
        score += FALLBACK_SEARCH_SPACE_LARGE_SCORE

    # inference_step_count
    steps = float(metrics.get("inference_step_count", {}).get("value", 0.0))
    score += min(FALLBACK_INFERENCE_STEP_CAP, steps)

    # branching_factor
    branching = float(metrics.get("branching_factor", {}).get("value", 0.0))
    if branching < BRANCHING_LOW_MAX_EXCLUSIVE:
        score += FALLBACK_BRANCHING_LOW_SCORE
    elif branching < BRANCHING_MODERATE_MAX_EXCLUSIVE:
        score += FALLBACK_BRANCHING_MEDIUM_SCORE
    else:
        score += FALLBACK_BRANCHING_HIGH_SCORE

    # formula complexity
    formula_complexity = float(metrics.get("logical_formula_complexity", {}).get("value", 0.0))
    if formula_complexity < FORMULA_SIMPLE_MAX_EXCLUSIVE:
        score += FALLBACK_FORMULA_SIMPLE_SCORE
    elif formula_complexity < FORMULA_MODERATE_MAX_EXCLUSIVE:
        score += FALLBACK_FORMULA_MODERATE_SCORE
    else:
        score += FALLBACK_FORMULA_HIGH_SCORE

    # uniqueness signal
    uniqueness = metrics.get("solution_uniqueness", {}).get("value")
    if uniqueness == "multiple":
        score += FALLBACK_UNIQUENESS_MULTIPLE_SCORE
    elif uniqueness == "unique":
        score += FALLBACK_UNIQUENESS_UNIQUE_SCORE

    return round(min(100.0, score), 2)


def _score_to_label(score: float) -> str:
    """Map numeric difficulty score to easy/medium/hard label."""
    if score < EASY_MAX_EXCLUSIVE:
        return "easy"
    if score < MEDIUM_MAX_EXCLUSIVE:
        return "medium"
    return "hard"


def _parse_puzzle_structure(puzzle_structure: Dict[str, Any] | str) -> Dict[str, Any]:
    """
    Parse and validate Module 1 puzzle structure input.

    Raises:
    - ValueError: if required keys are missing or have invalid types.
    """
    if isinstance(puzzle_structure, str):
        try:
            parsed = json.loads(puzzle_structure)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid puzzle json: {exc.msg}") from exc
    else:
        parsed = puzzle_structure
    _validate_puzzle_structure(parsed)
    return parsed


def _validate_puzzle_structure(puzzle_data: Dict[str, Any]) -> None:
    """Validate expected Module 1 puzzle dictionary shape for Module 5."""
    if not isinstance(puzzle_data, dict):
        raise ValueError("puzzle structure must be a dictionary")
    required = ("entities", "attributes", "constraints")
    missing = [k for k in required if k not in puzzle_data]
    if missing:
        raise ValueError(f"puzzle structure missing required keys: {missing}")
    if not isinstance(puzzle_data["entities"], list):
        raise ValueError("puzzle structure key 'entities' must be a list")
    if not isinstance(puzzle_data["attributes"], dict):
        raise ValueError("puzzle structure key 'attributes' must be a dict")
    if not isinstance(puzzle_data["constraints"], list):
        raise ValueError("puzzle structure key 'constraints' must be a list")


def _build_metrics(
    puzzle_data: Dict[str, Any],
    knowledge_base: str,
    solution_proof_text: str,
) -> Dict[str, Dict[str, Any]]:
    """
    Compute Module 5 metrics except solution uniqueness.

    Solution uniqueness is computed separately because it requires solver calls.
    """
    entities: List[str] = puzzle_data.get("entities", [])
    attributes: Dict[str, List[str]] = puzzle_data.get("attributes", {})
    constraints: List[Dict[str, Any]] = puzzle_data.get("constraints", [])

    variable_count = len(entities) * len(attributes)
    domain_sizes = [len(values) for values in attributes.values()]
    constraint_count = len(constraints)
    search_space_size = _compute_search_space_size(len(entities), attributes)
    inference_step_count = _extract_inference_step_count(solution_proof_text)
    decision_count = _extract_decision_count(solution_proof_text)
    formula_complexity = _compute_formula_complexity(knowledge_base)
    density = (constraint_count / variable_count) if variable_count > 0 else 0.0
    branching_factor = _estimate_branching_factor(search_space_size, variable_count, domain_sizes)

    return {
        "constraint_count": {
            "value": constraint_count,
            "interpretation": _interpret_constraint_count(constraint_count),
        },
        "search_space_size": {
            "value": search_space_size,
            "interpretation": _interpret_search_space(search_space_size),
        },
        "inference_step_count": {
            "value": inference_step_count,
            "interpretation": _interpret_inference_steps(inference_step_count, decision_count),
        },
        "constraint_density": {
            "value": round(density, 4),
            "interpretation": _interpret_density(density),
        },
        "logical_formula_complexity": {
            "value": formula_complexity,
            "interpretation": _interpret_formula_complexity(formula_complexity),
        },
        "branching_factor": {
            "value": round(branching_factor, 4),
            "interpretation": _interpret_branching_factor(branching_factor),
        },
    }


def _build_solution_uniqueness_metric(solution_count: int) -> Dict[str, Any]:
    """Build metric payload for uniqueness classification."""
    return {
        "value": (
            "unique"
            if solution_count == 1
            else ("unsatisfiable" if solution_count == 0 else "multiple")
        ),
        "solution_count_capped_at_2": solution_count,
        "interpretation": _interpret_solution_uniqueness(solution_count),
    }


def _compute_search_space_size(entities_count: int, attributes: Dict[str, List[str]]) -> int:
    """
    Compute raw assignment count across all entity-attribute variables.

    Formula: product_over_attributes( |domain(attr)| ^ |entities| ).
    """
    total = 1
    for values in attributes.values():
        total *= len(values) ** entities_count
    return total


def _extract_inference_step_count(solution_proof_text: str) -> int:
    """Extract inference step count from Module 3 output with regex fallback."""
    m = re.search(r"INFERENCE STEP COUNT:\s*(\d+)", solution_proof_text)
    if m:
        return int(m.group(1))
    # Fallback: count numbered proof lines.
    return len(re.findall(r"^\s*\d+\.\s+\[", solution_proof_text, flags=re.MULTILINE))


def _extract_decision_count(solution_proof_text: str) -> int:
    """Count explicit backtracking decision steps in proof text."""
    return len(re.findall(r"\[decision\]", solution_proof_text))


def _compute_formula_complexity(knowledge_base: str) -> int:
    """Count logical connective occurrences in puzzle-constraint formulas."""
    # Count logical connectives in puzzle formulas only.
    try:
        puzzle_section = knowledge_base.split("RULES (Puzzle Constraints):", 1)[1]
    except IndexError:
        return 0
    formulas = re.findall(r"^\s*\d+\.\s+(.+)$", puzzle_section, flags=re.MULTILINE)
    connective_count = 0
    for formula in formulas:
        connective_count += sum(formula.count(op) for op in ("∧", "∨", "¬", "→", "↔"))
    return connective_count


def _estimate_branching_factor(
    search_space_size: int,
    variable_count: int,
    domain_sizes: List[int],
) -> float:
    """
    Estimate branching factor via geometric-mean branching per variable.

    Uses search-space root as primary method and log-space fallback for
    overflow safety.
    """
    if variable_count <= 0:
        return 0.0
    if search_space_size <= 0:
        return 0.0
    # Geometric mean of branching choices per variable.
    try:
        return float(search_space_size ** (1.0 / variable_count))
    except OverflowError:
        if not domain_sizes:
            return 0.0
        return float(math.exp(sum(math.log(max(1, d)) for d in domain_sizes) / len(domain_sizes)))


def _interpret_constraint_count(constraint_count: int) -> str:
    """Return human-readable interpretation for constraint count."""
    if constraint_count < CONSTRAINT_COUNT_LOW_MAX_EXCLUSIVE:
        return "Low number of explicit clues; puzzle may be under-constrained."
    if constraint_count < CONSTRAINT_COUNT_MEDIUM_MAX_EXCLUSIVE:
        return "Moderate clue count; likely balanced difficulty."
    return "High clue count; stronger pruning and typically easier deduction."


def _interpret_search_space(search_space_size: int) -> str:
    """Return human-readable interpretation for search-space size."""
    if search_space_size < SEARCH_SPACE_SMALL_MAX_EXCLUSIVE:
        return "Small raw search space."
    if search_space_size < SEARCH_SPACE_MEDIUM_MAX_EXCLUSIVE:
        return "Medium raw search space."
    return "Large raw search space; pruning/inference is important."


def _interpret_inference_steps(inference_steps: int, decision_count: int) -> str:
    """Return human-readable interpretation for inference effort."""
    if inference_steps == 0:
        return "No proof steps recorded."
    if decision_count == 0:
        return "Solved through deduction only (no backtracking decisions)."
    return (
        f"Includes {decision_count} search decisions; "
        "higher counts indicate deeper search effort."
    )


def _interpret_density(density: float) -> str:
    """Return human-readable interpretation for constraint density."""
    if density < DENSITY_SPARSE_MAX_EXCLUSIVE:
        return "Sparse constraints per variable."
    if density < DENSITY_MODERATE_MAX_EXCLUSIVE:
        return "Moderate constraint density."
    return "Dense constraints per variable."


def _interpret_formula_complexity(formula_complexity: int) -> str:
    """Return human-readable interpretation for logical formula complexity."""
    if formula_complexity < FORMULA_SIMPLE_MAX_EXCLUSIVE:
        return "Simple logical formulas."
    if formula_complexity < FORMULA_MODERATE_MAX_EXCLUSIVE:
        return "Moderately complex logical formulas."
    return "High logical connective usage; formulas are relatively complex."


def _interpret_branching_factor(branching_factor: float) -> str:
    """Return human-readable interpretation for branching factor."""
    if branching_factor < BRANCHING_LOW_MAX_EXCLUSIVE:
        return "Low branching; fewer choices per variable."
    if branching_factor < BRANCHING_MODERATE_MAX_EXCLUSIVE:
        return "Moderate branching."
    return "High branching; search tree expands quickly."


def _interpret_solution_uniqueness(solution_count: int) -> str:
    """Return human-readable interpretation for uniqueness class."""
    if solution_count == 0:
        return "No satisfying assignment found."
    if solution_count == 1:
        return "Exactly one satisfying assignment found (unique solution)."
    return "At least two satisfying assignments found (not unique)."


def main() -> None:
    """
    CLI entrypoint.
    Usage:
      python -m src.module5_complexity_analysis <module1_puzzle.json> <module2_kb.txt> <module3_output.txt> <module4_report.txt>
    """
    parser = argparse.ArgumentParser(description="Module 5: Complexity Analysis")
    parser.add_argument("module1_puzzle_path", help="Path to Module 1 puzzle JSON file")
    parser.add_argument("module2_kb_path", help="Path to Module 2 knowledge base text file")
    parser.add_argument("module3_output_path", help="Path to Module 3 output text file")
    parser.add_argument("module4_report_path", help="Path to Module 4 report text file")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--historical_dataset_path",
        help="Optional path to JSON historical metrics dataset for percentile scoring",
    )
    args = parser.parse_args()

    with open(args.module1_puzzle_path, "r", encoding="utf-8") as f:
        puzzle_json = f.read()
    with open(args.module2_kb_path, "r", encoding="utf-8") as f:
        module2_kb = f.read()
    with open(args.module3_output_path, "r", encoding="utf-8") as f:
        module3_output = f.read()
    with open(args.module4_report_path, "r", encoding="utf-8") as f:
        module4_report = f.read()

    historical_dataset = None
    if args.historical_dataset_path:
        with open(args.historical_dataset_path, "r", encoding="utf-8") as f:
            historical_dataset = f.read()

    report = analyze_to_dict(
        puzzle_structure=puzzle_json,
        knowledge_base=module2_kb,
        solution_proof_text=module3_output,
        validation_report_text=module4_report,
        historical_dataset=historical_dataset,
    )

    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print(complexity_dict_to_text(report))


if __name__ == "__main__":
    main()
