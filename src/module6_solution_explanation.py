"""
Module 6: Solution Explanation (Knowledge Representation)

Turns formal solver output into a human-readable narrative: overall strategy
(informed by complexity metrics) and step-by-step reasoning aligned with the
Module 3 proof.

Inputs: Module 1 puzzle (JSON/dict), Module 2 knowledge base text, Module 3
solution+proof text, Module 5 complexity report text.
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any, Dict, List, Tuple

INFERENCE_COUNT_RE = re.compile(r"INFERENCE\s+STEP\s+COUNT:\s*(\d+)", re.IGNORECASE)
PROOF_LINE_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")
DIFFICULTY_LABEL_RE = re.compile(
    r"OVERALL\s+DIFFICULTY\s+LABEL:\s*(\S+)", re.IGNORECASE
)
DIFFICULTY_SCORE_RE = re.compile(
    r"OVERALL\s+DIFFICULTY\s+SCORE\s*\(0-100\):\s*(\S+)", re.IGNORECASE
)


def module1_2_3_5_to_module6(
    puzzle_structure: Dict[str, Any] | str,
    knowledge_base: str,
    solution_proof_text: str,
    complexity_report_text: str,
) -> str:
    """
    Build a structured explanation from upstream module artifacts.

    Parameters
    ----------
    puzzle_structure:
        Module 1 puzzle dict or JSON string (`entities`, `attributes`, `constraints`).
    knowledge_base:
        Module 2 knowledge base text.
    solution_proof_text:
        Module 3 output (solution block, inference count, proof lines).
    complexity_report_text:
        Module 5 text report (from `complexity_dict_to_text` or equivalent).

    Returns
    -------
    str
        Report with sections `=== OVERALL SOLUTION STRATEGY ===` and
        `=== STEP-BY-STEP REASONING ===`.
    """
    puzzle = _parse_puzzle_structure(puzzle_structure)
    proof_steps, inference_count = _parse_module3_proof(solution_proof_text)
    strategy = _build_overall_strategy(
        puzzle=puzzle,
        knowledge_base=knowledge_base,
        complexity_report_text=complexity_report_text,
        proof_steps=proof_steps,
        inference_count=inference_count,
    )
    steps = _build_step_by_step(proof_steps=proof_steps)
    return "\n".join(
        [
            "=== SOLUTION EXPLANATION REPORT ===",
            "",
            "=== OVERALL SOLUTION STRATEGY ===",
            strategy,
            "",
            "=== STEP-BY-STEP REASONING ===",
            steps,
            "",
        ]
    )


def _parse_puzzle_structure(puzzle_structure: Dict[str, Any] | str) -> Dict[str, Any]:
    if isinstance(puzzle_structure, str):
        parsed = json.loads(puzzle_structure)
    else:
        parsed = puzzle_structure
    if not isinstance(parsed, dict):
        raise ValueError("puzzle structure must be a dictionary or JSON object")
    for key in ("entities", "attributes", "constraints"):
        if key not in parsed:
            raise ValueError(f"puzzle structure missing required key: {key!r}")
    return parsed


def _parse_module3_proof(solution_proof_text: str) -> Tuple[List[str], int]:
    """Return proof step bodies (without leading 'n.') and inference count."""
    m = INFERENCE_COUNT_RE.search(solution_proof_text)
    inference_count = int(m.group(1)) if m else 0

    if "=== PROOF ===" not in solution_proof_text:
        return [], inference_count

    _, _, after = solution_proof_text.partition("=== PROOF ===")
    steps: List[str] = []
    for line in after.splitlines():
        m2 = PROOF_LINE_RE.match(line)
        if m2:
            steps.append(m2.group(2).strip())

    if inference_count == 0 and steps:
        inference_count = len(steps)
    return steps, inference_count


def _constraint_type_summary(constraints: List[Dict[str, Any]]) -> str:
    if not constraints:
        return "The puzzle has no explicit puzzle constraints listed."
    counts: Dict[str, int] = {}
    for c in constraints:
        t = c.get("type", "unknown")
        counts[t] = counts.get(t, 0) + 1
    parts = [f"{n} {t.replace('_', ' ')}" for t, n in sorted(counts.items())]
    return "Stated clues include: " + ", ".join(parts) + "."


def _extract_difficulty_context(complexity_report_text: str) -> str:
    lines: List[str] = []
    m = DIFFICULTY_SCORE_RE.search(complexity_report_text)
    if m:
        lines.append(f"Reported overall difficulty score: {m.group(1)} (0–100).")
    m = DIFFICULTY_LABEL_RE.search(complexity_report_text)
    if m:
        lines.append(f"Difficulty label: {m.group(1)}.")
    if not lines:
        return "Complexity metrics were supplied; see the Module 5 report for details."
    return " ".join(lines)


def _build_overall_strategy(
    puzzle: Dict[str, Any],
    knowledge_base: str,
    complexity_report_text: str,
    proof_steps: List[str],
    inference_count: int,
) -> str:
    n_entities = len(puzzle.get("entities", []))
    n_attrs = len(puzzle.get("attributes", {}))
    clue_summary = _constraint_type_summary(puzzle.get("constraints", []))
    difficulty = _extract_difficulty_context(complexity_report_text)

    decisions = sum(1 for s in proof_steps if "[decision]" in s)
    deductions = sum(1 for s in proof_steps if "[deduction]" in s)

    if decisions > 0:
        search_note = (
            f"The proof includes {decisions} search decision(s) and {deductions} "
            "propagation step(s), so the solver combined deduction with backtracking."
        )
    else:
        search_note = (
            "The proof consists of propagation-only steps (no explicit search decisions "
            "were recorded)."
        )

    kb_note = (
        "The knowledge base encodes domain uniqueness rules and each puzzle clue as "
        "propositional formulas over entity–attribute–value symbols."
    )
    if "=== KNOWLEDGE BASE ===" not in knowledge_base:
        kb_note = (
            "A structured knowledge base was provided; Module 6 expects the standard "
            "Module 2 section markers for full traceability."
        )

    return (
        f"This puzzle has {n_entities} entities and {n_attrs} attributes. {clue_summary}\n"
        f"{kb_note}\n"
        f"{difficulty}\n"
        f"{search_note}\n"
        f"The solver recorded {inference_count} inference line(s) in the formal proof."
    )


def _paraphrase_step(raw: str) -> str:
    """Turn a single proof line into plain language."""
    s = raw.strip()
    if s.startswith("[deduction]"):
        body = s[len("[deduction]") :].strip()
        return (
            f"**Propagation:** {body} "
            "(a domain reduction or forced assignment from the current clues)."
        )
    if s.startswith("[decision]"):
        body = s[len("[decision]") :].strip()
        return (
            f"**Search decision:** {body} "
            "(the solver guessed an assignment and continued propagating)."
        )
    return f"**Step:** {s}"


def _build_step_by_step(proof_steps: List[str]) -> str:
    if not proof_steps:
        return "No proof lines were found under `=== PROOF ===`."

    blocks: List[str] = []
    for i, raw in enumerate(proof_steps, start=1):
        para = _paraphrase_step(raw)
        blocks.append(f"### Step {i}")
        blocks.append(para)
        blocks.append("")
    return "\n".join(blocks).rstrip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Module 6: Solution Explanation")
    parser.add_argument("module1_puzzle_path", help="Path to Module 1 puzzle JSON")
    parser.add_argument("module2_kb_path", help="Path to Module 2 knowledge base text")
    parser.add_argument("module3_output_path", help="Path to Module 3 output text")
    parser.add_argument("module5_report_path", help="Path to Module 5 complexity report text")
    args = parser.parse_args()

    with open(args.module1_puzzle_path, "r", encoding="utf-8") as f:
        puzzle_raw = f.read()
    with open(args.module2_kb_path, "r", encoding="utf-8") as f:
        kb = f.read()
    with open(args.module3_output_path, "r", encoding="utf-8") as f:
        m3 = f.read()
    with open(args.module5_report_path, "r", encoding="utf-8") as f:
        m5 = f.read()

    print(module1_2_3_5_to_module6(puzzle_raw, kb, m3, m5))


if __name__ == "__main__":
    main()
