"""
Module 4: Solution Verification

Validates Module 3 solutions using:
- original constraints from Module 1
- knowledge base from Module 2 (entailment-style consistency check)
- hidden solution from Module 1 (reference comparison)

Output is structured text with:
- overall validation result (VALID / INVALID)
- per-constraint validation
- entailment check
- violation summary
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any, Dict, List, Tuple

from module3_puzzle_solving import _parse_puzzle_constraint, _extract_puzzle_rule_formulas


def verify_to_dict(
    solution_text: str,
    constraints_data: List[Dict[str, Any]],
    knowledge_base: str,
    hidden_solution: Dict[str, Dict[str, str]],
) -> Dict[str, Any]:
    """
    Canonical structured verification API for Module 4.

    Returns a JSON-serializable dict intended for UI rendering.
    This function does not raise for common user errors; instead it returns
    `overall_pass=False` and populates `errors`.
    """
    errors: List[str] = []
    try:
        assignment = _parse_solution_text(solution_text)
    except Exception as e:  # noqa: BLE001 - convert to user-facing error
        return {
            "overall_pass": False,
            "errors": [str(e)],
            "constraint_results": [],
            "entailment": {"pass": False, "details": "Skipped due to parse failure"},
            "hidden_solution_match": {"pass": False, "details": "Skipped due to parse failure"},
        }

    constraint_results: List[Dict[str, Any]] = []
    violations: List[Dict[str, Any]] = []
    for i, constraint in enumerate(constraints_data, start=1):
        ok, detail = _check_constraint(assignment, constraint)
        result = {
            "index": i,
            "type": constraint.get("type"),
            "attribute": constraint.get("attribute"),
            "pass": ok,
            "details": detail,
            "constraint": constraint,
        }
        constraint_results.append(result)
        if not ok:
            violations.append(result)

    entailment_ok = False
    entailment_detail = "Skipped"
    try:
        entailment_ok, entailment_detail = _entailment_check(assignment, knowledge_base)
    except Exception as e:  # noqa: BLE001
        errors.append(f"Entailment check error: {e}")

    hidden_match = assignment == hidden_solution
    overall_valid = (len(violations) == 0) and entailment_ok and (len(errors) == 0)

    return {
        "overall_pass": overall_valid,
        "errors": errors,
        "constraint_results": constraint_results,
        "violation_summary": violations,
        "entailment": {"pass": entailment_ok, "details": entailment_detail},
        "hidden_solution_match": {"pass": hidden_match, "details": "Exact match of assignment dicts"},
    }


def verification_dict_to_text(report: Dict[str, Any]) -> str:
    """
    Render a human-readable report from `verify_to_dict` output.
    """
    overall_valid = bool(report.get("overall_pass"))
    errors: List[str] = list(report.get("errors", []))
    per_constraint = report.get("constraint_results", [])
    entailment = report.get("entailment", {})
    hidden = report.get("hidden_solution_match", {})
    violations = report.get("violation_summary", [])

    lines: List[str] = [
        "=== VALIDATION REPORT ===",
        f"OVERALL VALIDATION RESULT: {'VALID' if overall_valid else 'INVALID'}",
        "",
    ]

    if errors:
        lines.extend(["ERRORS:"] + [f"- {e}" for e in errors] + [""])

    lines.append("PER-CONSTRAINT RESULTS:")
    for item in per_constraint:
        status = "SATISFIED" if item.get("pass") else "VIOLATED"
        lines.append(f"{item.get('index')}. [{status}] {item.get('type')} - {item.get('details')}")

    lines.extend(
        [
            "",
            f"LOGICAL ENTAILMENT CHECK: {'PASS' if entailment.get('pass') else 'FAIL'} ({entailment.get('details')})",
            f"HIDDEN SOLUTION COMPARISON: {'MATCH' if hidden.get('pass') else 'MISMATCH'}",
            "",
            "VIOLATION SUMMARY:",
        ]
    )

    if violations:
        for item in violations:
            lines.append(f"{item.get('index')}. {item.get('type')} - {item.get('details')}")
    else:
        lines.append("None")

    return "\n".join(lines)


def _parse_solution_text(solution_text: str) -> Dict[str, Dict[str, str]]:
    """
    Parse Module 3 solution block from text.

    Expected line shape:
        E1: A1=V3, A2=V1, ...
    """
    assignment: Dict[str, Dict[str, str]] = {}
    for raw_line in solution_text.splitlines():
        line = raw_line.strip()
        if not line or not line.startswith("E") or ":" not in line:
            continue
        entity, rhs = line.split(":", 1)
        entity = entity.strip()
        parts = [p.strip() for p in rhs.split(",") if p.strip()]
        for part in parts:
            if "=" not in part:
                continue
            attribute, value = part.split("=", 1)
            assignment.setdefault(entity, {})[attribute.strip()] = value.strip()
    if not assignment:
        raise ValueError("No entity assignments found in solution text.")
    return assignment


def _value_index(value_symbol: str) -> int:
    if not value_symbol.startswith("V"):
        raise ValueError(f"Unexpected value symbol: {value_symbol}")
    return int(value_symbol[1:])


def _check_constraint(
    assignment: Dict[str, Dict[str, str]],
    constraint: Dict[str, Any],
) -> Tuple[bool, str]:
    """
    Check one Module 1 constraint against the parsed solution assignment.

    Returns (is_satisfied, human_readable_message).
    """
    constraint_type = constraint["type"]
    attribute = constraint["attribute"]

    if constraint_type == "equality":
        entity = constraint["entity"]
        expected = constraint["value"]
        actual = assignment.get(entity, {}).get(attribute)
        ok = actual == expected
        return ok, f"{entity}.{attribute} == {expected} (actual: {actual})"

    if constraint_type == "inequality":
        entity = constraint["entity"]
        forbidden = constraint["value"]
        actual = assignment.get(entity, {}).get(attribute)
        ok = actual != forbidden
        return ok, f"{entity}.{attribute} != {forbidden} (actual: {actual})"

    if constraint_type == "different_values":
        entity1, entity2 = constraint["entities"][0], constraint["entities"][1]
        value1 = assignment.get(entity1, {}).get(attribute)
        value2 = assignment.get(entity2, {}).get(attribute)
        ok = value1 is not None and value2 is not None and value1 != value2
        return ok, f"{entity1}.{attribute} != {entity2}.{attribute} ({value1} vs {value2})"

    if constraint_type == "same_value":
        entity1, entity2 = constraint["entities"][0], constraint["entities"][1]
        value1 = assignment.get(entity1, {}).get(attribute)
        value2 = assignment.get(entity2, {}).get(attribute)
        ok = value1 is not None and value2 is not None and value1 == value2
        return ok, f"{entity1}.{attribute} == {entity2}.{attribute} ({value1} vs {value2})"

    if constraint_type == "relative_position":
        entity1 = constraint.get("entity1") or constraint.get("entity")
        entity2 = constraint["entity2"]
        offset = constraint["offset"]
        value1 = assignment.get(entity1, {}).get(attribute)
        value2 = assignment.get(entity2, {}).get(attribute)
        if value1 is None or value2 is None:
            return False, f"{entity1}.{attribute} and {entity2}.{attribute} must both be assigned"
        index1 = _value_index(value1)
        index2 = _value_index(value2)
        ok = index1 == index2 + offset
        return ok, f"{entity1}.{attribute} = {entity2}.{attribute} + {offset} ({value1} vs {value2})"

    raise ValueError(f"Unknown constraint type: {constraint_type}")


def _evaluate_parsed_constraint(
    assignment: Dict[str, Dict[str, str]],
    parsed_constraint: Any,
) -> bool:
    """
    Evaluate a parsed Module 2 formula (via Module 3 parser) on a concrete assignment.
    """
    if parsed_constraint.type == "contradiction":
        return False
    if parsed_constraint.type == "equality":
        return (
            assignment.get(parsed_constraint.entity, {}).get(parsed_constraint.attribute)
            == parsed_constraint.value
        )
    if parsed_constraint.type == "inequality":
        return (
            assignment.get(parsed_constraint.entity, {}).get(parsed_constraint.attribute)
            != parsed_constraint.value
        )
    if parsed_constraint.type == "different_values":
        return (
            assignment.get(parsed_constraint.entity1, {}).get(parsed_constraint.attribute)
            != assignment.get(parsed_constraint.entity2, {}).get(parsed_constraint.attribute)
        )
    if parsed_constraint.type == "same_value":
        return (
            assignment.get(parsed_constraint.entity1, {}).get(parsed_constraint.attribute)
            == assignment.get(parsed_constraint.entity2, {}).get(parsed_constraint.attribute)
        )
    if parsed_constraint.type == "relative_position":
        value1 = assignment.get(parsed_constraint.entity1, {}).get(parsed_constraint.attribute)
        value2 = assignment.get(parsed_constraint.entity2, {}).get(parsed_constraint.attribute)
        if value1 is None or value2 is None:
            return False
        return _value_index(value1) == _value_index(value2) + parsed_constraint.offset
    raise ValueError(f"Unsupported parsed constraint type: {parsed_constraint.type}")


def _entailment_check(solution_assignment: Dict[str, Dict[str, str]], knowledge_base: str) -> Tuple[bool, str]:
    """
    Practical entailment-style check:
    verify that the solution satisfies all puzzle-constraint formulas in the KB.
    """
    formulas = _extract_puzzle_rule_formulas(knowledge_base)
    parsed = [_parse_puzzle_constraint(f) for f in formulas]
    for i, parsed_constraint in enumerate(parsed, start=1):
        if not _evaluate_parsed_constraint(solution_assignment, parsed_constraint):
            return False, f"Formula {i} not satisfied"
    return True, f"All {len(parsed)} puzzle formulas satisfied"


def module3_to_module4(
    solution_text: str,
    constraints_data: List[Dict[str, Any]],
    knowledge_base: str,
    hidden_solution: Dict[str, Dict[str, str]],
) -> str:
    """
    Main entry point for Module 4 verification.
    """
    report = verify_to_dict(
        solution_text=solution_text,
        constraints_data=constraints_data,
        knowledge_base=knowledge_base,
        hidden_solution=hidden_solution,
    )
    return verification_dict_to_text(report)


def module1_2_3_to_module4(
    module3_output: str,
    module1_puzzle_json_or_dict: str | Dict[str, Any],
    module2_knowledge_base: str,
) -> str:
    """
    Convenience adapter that wires Module 1/2/3 outputs into Module 4.
    """
    if isinstance(module1_puzzle_json_or_dict, str):
        puzzle_data = json.loads(module1_puzzle_json_or_dict)
    else:
        puzzle_data = module1_puzzle_json_or_dict

    constraints = puzzle_data["constraints"]
    hidden_solution = puzzle_data["solution"]
    return module3_to_module4(
        solution_text=module3_output,
        constraints_data=constraints,
        knowledge_base=module2_knowledge_base,
        hidden_solution=hidden_solution,
    )


def main() -> None:
    """
    CLI entrypoint.
    Usage:
      python -m src.module4_solution_verification <module3_output.txt> <module1_puzzle.json> <module2_kb.txt>
    """
    parser = argparse.ArgumentParser(description="Module 4: Solution Verification")
    parser.add_argument("module3_output_path", help="Path to Module 3 output text file")
    parser.add_argument("module1_puzzle_path", help="Path to Module 1 puzzle JSON file")
    parser.add_argument("module2_kb_path", help="Path to Module 2 knowledge base text file")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    args = parser.parse_args()

    with open(args.module3_output_path, "r", encoding="utf-8") as f:
        module3_output = f.read()
    with open(args.module1_puzzle_path, "r", encoding="utf-8") as f:
        module1_json = f.read()
    with open(args.module2_kb_path, "r", encoding="utf-8") as f:
        module2_kb = f.read()

    if args.format == "text":
        print(module1_2_3_to_module4(module3_output, module1_json, module2_kb))
        return

    # JSON format
    puzzle_data = json.loads(module1_json)
    report = verify_to_dict(
        solution_text=module3_output,
        constraints_data=puzzle_data["constraints"],
        knowledge_base=module2_kb,
        hidden_solution=puzzle_data["solution"],
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

