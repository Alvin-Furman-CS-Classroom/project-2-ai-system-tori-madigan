"""
Module 6: Knowledge Representation

Generates a human-readable explanation from formal solver outputs.
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any, Dict, List


def explain_to_dict(
    solution_proof_text: str,
    knowledge_base_text: str,
    constraints_json_or_dict: str | Dict[str, Any],
    difficulty_metrics_text: str,
) -> Dict[str, Any]:
    """
    Canonical structured API for Module 6.

    Inputs:
    - solution_proof_text: Module 3 output
    - knowledge_base_text: Module 2 output
    - constraints_json_or_dict: Module 1 puzzle JSON/dict (at least constraints)
    - difficulty_metrics_text: Module 5 text report
    """
    puzzle_data = _parse_constraints_input(constraints_json_or_dict)
    constraints = puzzle_data.get("constraints", [])

    solution_lines = _extract_solution_lines(solution_proof_text)
    proof_steps = _extract_proof_steps(solution_proof_text)
    puzzle_formula_count = _count_puzzle_formulas(knowledge_base_text)
    metrics = _extract_metrics_from_module5_text(difficulty_metrics_text)

    strategy = _build_overall_strategy(metrics, proof_steps, len(constraints), puzzle_formula_count)
    reasoning_steps = _build_reasoning_steps(proof_steps, solution_lines)
    reasoning_phases = _group_reasoning_phases(reasoning_steps)
    final_solution_summary = "; ".join(solution_lines)

    return {
        "overall_strategy": strategy,
        "step_by_step_reasoning": reasoning_steps,
        "reasoning_phases": reasoning_phases,
        "final_solution_summary": final_solution_summary,
        "explanation_metadata": {
            "proof_step_count": len(proof_steps),
            "solution_line_count": len(solution_lines),
            "constraint_count": len(constraints),
            "puzzle_formula_count": puzzle_formula_count,
            "difficulty_label": metrics.get("overall_difficulty_label"),
            "difficulty_score": metrics.get("overall_difficulty_score"),
        },
    }


def explanation_dict_to_text(report: Dict[str, Any]) -> str:
    """Render a human-readable explanation report from `explain_to_dict`."""
    strategy = report.get("overall_strategy", "")
    steps: List[Dict[str, Any]] = report.get("step_by_step_reasoning", [])
    meta = report.get("explanation_metadata", {})
    phases: Dict[str, List[Dict[str, Any]]] = report.get("reasoning_phases", {})
    final_solution = report.get("final_solution_summary", "")

    lines = [
        "=== SOLUTION EXPLANATION ===",
        "",
        "OVERALL STRATEGY",
        "----------------",
        strategy,
        "",
        "REASONING PHASES",
        "----------------",
    ]

    phase_order = ["deductions", "decisions", "other"]
    for phase_name in phase_order:
        bucket = phases.get(phase_name, [])
        if not bucket:
            continue
        lines.append(f"{phase_name.capitalize()}:")
        for item in bucket:
            lines.append(f"  {item.get('index')}. {item.get('explanation')}")
        lines.append("")

    if not any(phases.get(name, []) for name in phase_order):
        lines.append("No explicit proof steps were available.")
        lines.append("")

    lines.extend(["FULL STEP-BY-STEP TRACE", "-----------------------"])
    if not steps:
        lines.append("No explicit proof steps were available.")
    else:
        for item in steps:
            lines.append(f"{item.get('index')}. {item.get('explanation')}")

    lines.extend(
        [
            "",
            "FINAL SOLUTION",
            "--------------",
            final_solution if final_solution else "No final assignment summary available.",
            "",
            "EXPLANATION METADATA",
            "--------------------",
            f"- proof_step_count: {meta.get('proof_step_count')}",
            f"- solution_line_count: {meta.get('solution_line_count')}",
            f"- constraint_count: {meta.get('constraint_count')}",
            f"- puzzle_formula_count: {meta.get('puzzle_formula_count')}",
            f"- difficulty_label: {meta.get('difficulty_label')}",
            f"- difficulty_score: {meta.get('difficulty_score')}",
        ]
    )

    return "\n".join(lines)


def module1_2_3_5_to_module6(
    module3_solution_proof: str,
    module2_knowledge_base: str,
    module1_constraints_json_or_dict: str | Dict[str, Any],
    module5_difficulty_report_text: str,
) -> str:
    """Main text entrypoint for Module 6."""
    report = explain_to_dict(
        solution_proof_text=module3_solution_proof,
        knowledge_base_text=module2_knowledge_base,
        constraints_json_or_dict=module1_constraints_json_or_dict,
        difficulty_metrics_text=module5_difficulty_report_text,
    )
    return explanation_dict_to_text(report)


def _parse_constraints_input(constraints_json_or_dict: str | Dict[str, Any]) -> Dict[str, Any]:
    if isinstance(constraints_json_or_dict, str):
        try:
            data = json.loads(constraints_json_or_dict)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid constraints json: {exc.msg}") from exc
    else:
        data = constraints_json_or_dict
    if not isinstance(data, dict):
        raise ValueError("constraints input must be a dictionary-like puzzle payload")
    if "constraints" not in data or not isinstance(data["constraints"], list):
        raise ValueError("constraints input must include key 'constraints' as a list")
    return data


def _extract_solution_lines(solution_proof_text: str) -> List[str]:
    lines: List[str] = []
    in_solution = False
    for raw in solution_proof_text.splitlines():
        line = raw.strip()
        if line == "=== SOLUTION ===":
            in_solution = True
            continue
        if line.startswith("INFERENCE STEP COUNT:") or line == "=== PROOF ===":
            break
        if in_solution and line.startswith("E") and ":" in line:
            lines.append(line)
    return lines


def _extract_proof_steps(solution_proof_text: str) -> List[str]:
    # Capture numbered proof lines like "1. [deduction] ..."
    return [m.group(1).strip() for m in re.finditer(r"^\s*\d+\.\s*(.+)$", solution_proof_text, flags=re.MULTILINE)]


def _count_puzzle_formulas(knowledge_base_text: str) -> int:
    if "RULES (Puzzle Constraints):" not in knowledge_base_text:
        return 0
    section = knowledge_base_text.split("RULES (Puzzle Constraints):", 1)[1]
    return len(re.findall(r"^\s*\d+\.\s+.+$", section, flags=re.MULTILINE))


def _extract_metrics_from_module5_text(difficulty_metrics_text: str) -> Dict[str, Any]:
    label_match = re.search(r"OVERALL DIFFICULTY LABEL:\s*(\w+)", difficulty_metrics_text)
    score_match = re.search(r"OVERALL DIFFICULTY SCORE \(0-100\):\s*([0-9]+(?:\.[0-9]+)?)", difficulty_metrics_text)
    return {
        "overall_difficulty_label": label_match.group(1) if label_match else "unknown",
        "overall_difficulty_score": float(score_match.group(1)) if score_match else None,
    }


def _build_overall_strategy(
    metrics: Dict[str, Any],
    proof_steps: List[str],
    constraint_count: int,
    puzzle_formula_count: int,
) -> str:
    label = metrics.get("overall_difficulty_label", "unknown")
    score = metrics.get("overall_difficulty_score")
    decision_steps = [s for s in proof_steps if "[decision]" in s]
    deduction_steps = [s for s in proof_steps if "[deduction]" in s]

    base = (
        f"This puzzle was solved using constraint propagation and logical inference "
        f"over {constraint_count} constraints and {puzzle_formula_count} puzzle formulas."
    )
    difficulty_sentence = f" Module 5 rates it as {label}"
    if isinstance(score, float):
        difficulty_sentence += f" (score={score:.2f}/100)."
    else:
        difficulty_sentence += "."

    step_sentence = (
        f" The proof contains {len(deduction_steps)} deduction steps and "
        f"{len(decision_steps)} decision steps."
    )

    if len(decision_steps) == 0:
        search_note = " The solution is primarily deduction-driven with little or no backtracking."
    else:
        search_note = " The solver used targeted search decisions when pure deduction was insufficient."

    return base + difficulty_sentence + step_sentence + search_note


def _build_reasoning_steps(proof_steps: List[str], solution_lines: List[str]) -> List[Dict[str, Any]]:
    reasoning: List[Dict[str, Any]] = []
    for idx, step in enumerate(proof_steps, start=1):
        reasoning.append({"index": idx, "source_step": step, "explanation": _translate_proof_step(step)})

    if solution_lines:
        reasoning.append(
            {
                "index": len(reasoning) + 1,
                "source_step": "solution_summary",
                "explanation": "Final assignment summary: " + "; ".join(solution_lines),
            }
        )
    return reasoning


def _translate_proof_step(step: str) -> str:
    if "[deduction]" in step:
        detail = step.replace("[deduction]", "").strip()
        return f"Deduction: using known constraints, we infer that {detail}."
    if "[decision]" in step:
        detail = step.replace("[decision]", "").strip()
        return f"Decision: to continue progress, the solver chooses to {detail}."
    return f"Inference: {step}"


def _group_reasoning_phases(steps: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    buckets: Dict[str, List[Dict[str, Any]]] = {"deductions": [], "decisions": [], "other": []}
    for step in steps:
        source = str(step.get("source_step", ""))
        if "[deduction]" in source:
            buckets["deductions"].append(step)
        elif "[decision]" in source:
            buckets["decisions"].append(step)
        else:
            buckets["other"].append(step)
    return buckets


def main() -> None:
    """
    CLI entrypoint.
    Usage:
      python -m src.module6_knowledge_representation <module3_output.txt> <module2_kb.txt> <module1_puzzle.json> <module5_report.txt>
    """
    parser = argparse.ArgumentParser(description="Module 6: Knowledge Representation")
    parser.add_argument("module3_output_path", help="Path to Module 3 output text file")
    parser.add_argument("module2_kb_path", help="Path to Module 2 knowledge base text file")
    parser.add_argument("module1_puzzle_path", help="Path to Module 1 puzzle JSON file")
    parser.add_argument("module5_report_path", help="Path to Module 5 report text file")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    args = parser.parse_args()

    with open(args.module3_output_path, "r", encoding="utf-8") as f:
        module3_output = f.read()
    with open(args.module2_kb_path, "r", encoding="utf-8") as f:
        module2_kb = f.read()
    with open(args.module1_puzzle_path, "r", encoding="utf-8") as f:
        module1_puzzle_json = f.read()
    with open(args.module5_report_path, "r", encoding="utf-8") as f:
        module5_report = f.read()

    report = explain_to_dict(
        solution_proof_text=module3_output,
        knowledge_base_text=module2_kb,
        constraints_json_or_dict=module1_puzzle_json,
        difficulty_metrics_text=module5_report,
    )

    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print(explanation_dict_to_text(report))


if __name__ == "__main__":
    main()
