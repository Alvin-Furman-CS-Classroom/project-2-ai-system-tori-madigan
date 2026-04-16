"""
Streamlit UI for the Logic Puzzle Generation and Analysis System.

Game-style interface for solving generated logic puzzles.

Start:
  PYTHONPATH=src streamlit run streamlit_app.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Dict, List

import streamlit as st

# Ensure `src/` is importable when running via Streamlit from repo root.
SRC_DIR = Path(__file__).parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from module1_puzzle_generator import generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module4_solution_verification import verify_to_dict  # noqa: E402

THEME_ENTITY_NAMES = ["Alice", "Bob", "Sally", "Molly", "Dan", "Charles"]
THEME_ATTRIBUTE_NAMES = ["Age", "Hair Color", "Favorite Color", "Pet", "Sport"]
THEME_VALUE_LABELS = {
    "Age": ["18", "20", "22", "24", "26", "28"],
    "Hair Color": ["Blonde", "Brunette", "Black", "Red", "Brown", "Gray"],
    "Favorite Color": ["Blue", "Green", "Purple", "Yellow", "Red", "Orange"],
    "Pet": ["Dog", "Cat", "Fish", "Bird", "Hamster", "Rabbit"],
    "Sport": ["Soccer", "Basketball", "Tennis", "Swimming", "Running", "Volleyball"],
}


def _human_name(symbol: Any, kind: str) -> str:
    raw = str(symbol)
    if kind == "entity" and raw.startswith("E") and raw[1:].isdigit():
        idx = int(raw[1:]) - 1
        if 0 <= idx < len(THEME_ENTITY_NAMES):
            return THEME_ENTITY_NAMES[idx]
        return f"Person {raw[1:]}"
    if kind == "attribute" and raw.startswith("A") and raw[1:].isdigit():
        idx = int(raw[1:]) - 1
        if 0 <= idx < len(THEME_ATTRIBUTE_NAMES):
            return THEME_ATTRIBUTE_NAMES[idx]
        return f"Category {raw[1:]}"
    if kind == "value" and raw.startswith("V") and raw[1:].isdigit():
        return f"Option {raw[1:]}"
    return raw


def _value_label(attribute_symbol: Any, value_symbol: Any) -> str:
    attr_label = _human_name(attribute_symbol, "attribute")
    raw_value = str(value_symbol)
    if raw_value.startswith("V") and raw_value[1:].isdigit():
        idx = int(raw_value[1:]) - 1
        label_values = THEME_VALUE_LABELS.get(attr_label, [])
        if 0 <= idx < len(label_values):
            return label_values[idx]
    return _human_name(raw_value, "value")


def _constraint_to_hint(constraint: Dict[str, Any]) -> str:
    ctype = constraint.get("type")
    attribute_symbol = constraint.get("attribute")
    attribute = _human_name(attribute_symbol, "attribute")
    if ctype == "equality":
        entity = _human_name(constraint.get("entity"), "entity")
        value = _value_label(attribute_symbol, constraint.get("value"))
        return f"{entity} has {attribute} = {value}."
    if ctype == "inequality":
        entity = _human_name(constraint.get("entity"), "entity")
        value = _value_label(attribute_symbol, constraint.get("value"))
        return f"{entity} does not have {attribute} = {value}."
    if ctype == "different_values":
        entities = constraint.get("entities", [])
        if len(entities) >= 2:
            e1 = _human_name(entities[0], "entity")
            e2 = _human_name(entities[1], "entity")
            return f"{e1} and {e2} have different values for {attribute}."
    if ctype == "same_value":
        entities = constraint.get("entities", [])
        if len(entities) >= 2:
            e1 = _human_name(entities[0], "entity")
            e2 = _human_name(entities[1], "entity")
            return f"{e1} and {e2} share the same value for {attribute}."
    if ctype == "relative_position":
        entity1 = _human_name(constraint.get("entity1") or constraint.get("entity"), "entity")
        entity2 = _human_name(constraint.get("entity2"), "entity")
        offset = constraint.get("offset")
        if isinstance(offset, int) and offset > 0:
            relation = f"{offset} step(s) ahead of"
        elif isinstance(offset, int) and offset < 0:
            relation = f"{abs(offset)} step(s) behind"
        else:
            relation = f"offset by {offset} from"
        return (
            f"For {attribute}, {entity1} is {relation} {entity2} "
            f"(using the attribute's natural ordering)."
        )
    return f"Constraint on {attribute}: {constraint}"


def _generate_natural_language_hints(puzzle_dict: Dict[str, Any], difficulty: str) -> List[str]:
    """
    Generate game-style hints from the hidden solution without exposing it directly.

    Primary style:
    - relational age hints (older/younger)
    - cross-category narrative hints
    """
    entities: List[str] = puzzle_dict.get("entities", [])
    attributes: Dict[str, List[str]] = puzzle_dict.get("attributes", {})
    solution: Dict[str, Dict[str, str]] = puzzle_dict.get("solution", {})

    hints: List[str] = []
    age_attr = _attribute_symbol_for_label(attributes, "Age")

    # 1) Build three age-based hints in the style requested by user.
    if age_attr and len(entities) >= 3:
        e1, e2, e3 = entities[0], entities[1], entities[2]
        age1 = _to_int_if_possible(_value_label(age_attr, solution.get(e1, {}).get(age_attr, "")))
        age2 = _to_int_if_possible(_value_label(age_attr, solution.get(e2, {}).get(age_attr, "")))
        age3 = _to_int_if_possible(_value_label(age_attr, solution.get(e3, {}).get(age_attr, "")))

        if age1 is not None and age2 is not None and age3 is not None:
            hints.append(
                "One hint: "
                + _age_relation_sentence(_human_name(e1, "entity"), age1, _human_name(e2, "entity"), age2)
            )
            hints.append(
                "Second hint: "
                + _age_relation_sentence(_human_name(e2, "entity"), age2, _human_name(e3, "entity"), age3)
            )
            hints.append(
                f"Third hint: {_human_name(e3, 'entity')} is {age3} years old."
            )

    # 2) Build additional hints from actual constraints (non-answer style when possible).
    constraint_hints = [_constraint_to_hint(c) for c in puzzle_dict.get("constraints", [])]

    # 3) Build anchor hints from hidden solution (ensures puzzle is solvable from hints list).
    anchor_hints = _build_anchor_hints_from_solution(entities, attributes, solution)

    normalized = difficulty.lower().strip()
    if normalized == "easy":
        # Easy: lots of direct information + all logical constraints.
        hints.extend(anchor_hints)
        hints.extend(constraint_hints)
    elif normalized == "medium":
        # Medium: keep age chain and use some anchors, plus all constraints.
        hints.extend(anchor_hints[: max(2, len(entities) // 2)])
        hints.extend(constraint_hints)
    else:
        # Hard: mostly relational constraints, minimal direct anchors.
        hints.extend(constraint_hints)
        hints.extend(anchor_hints[:2])

    # Deduplicate while preserving order.
    unique_hints: List[str] = []
    seen = set()
    for hint in hints:
        if hint not in seen:
            unique_hints.append(hint)
            seen.add(hint)

    # Guarantee enough clues to solve: at least number of constraints.
    min_hint_count = max(6, len(puzzle_dict.get("constraints", [])))
    if len(unique_hints) < min_hint_count:
        for extra in anchor_hints:
            if extra not in seen:
                unique_hints.append(extra)
                seen.add(extra)
            if len(unique_hints) >= min_hint_count:
                break

    return unique_hints


def _build_anchor_hints_from_solution(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
) -> List[str]:
    hints: List[str] = []
    for entity in entities:
        for attribute in attributes:
            value_symbol = solution.get(entity, {}).get(attribute)
            if value_symbol is None:
                continue
            entity_name = _human_name(entity, "entity")
            attribute_name = _human_name(attribute, "attribute")
            value_label = _value_label(attribute, value_symbol)
            if attribute_name == "Age":
                hints.append(f"{entity_name} is {value_label} years old.")
            else:
                hints.append(f"{entity_name}'s {attribute_name} is {value_label}.")
    return hints


def _attribute_symbol_for_label(attributes: Dict[str, List[str]], label: str) -> str | None:
    for attr_symbol in attributes:
        if _human_name(attr_symbol, "attribute") == label:
            return attr_symbol
    return None


def _to_int_if_possible(value: Any) -> int | None:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return None


def _age_relation_sentence(name1: str, age1: int, name2: str, age2: int) -> str:
    diff = age1 - age2
    if diff > 0:
        return f"{name1} is {diff} years older than {name2}."
    if diff < 0:
        return f"{name1} is {abs(diff)} years younger than {name2}."
    return f"{name1} and {name2} are the same age."


def _render_puzzle_grid(entities: List[str], attributes: Dict[str, List[str]]) -> None:
    rows: List[Dict[str, str]] = []
    for entity in entities:
        row = {"Entity": _human_name(entity, "entity")}
        for attribute in attributes:
            row[_human_name(attribute, "attribute")] = "?"
        rows.append(row)
    st.dataframe(rows, width="stretch")


def _attempt_to_solution_text(entities: List[str], attributes: Dict[str, List[str]]) -> str:
    lines = ["=== SOLUTION ==="]
    for entity in entities:
        parts = []
        for attribute in attributes:
            key = f"guess::{entity}::{attribute}"
            guess = st.session_state.get(key, "(blank)")
            if guess != "(blank)":
                parts.append(f"{attribute}={guess}")
        if parts:
            lines.append(f"{entity}: " + ", ".join(parts))
    lines.append("")
    lines.append("=== PROOF ===")
    lines.append("(user attempt)")
    return "\n".join(lines)


def _render_attempt_feedback(report: Dict[str, Any], total_constraints: int) -> None:
    satisfied = sum(1 for r in report.get("constraint_results", []) if r.get("pass"))
    violations = report.get("violation_summary", [])
    st.write(f"Constraints satisfied: **{satisfied} / {total_constraints}**")

    if violations:
        st.warning(f"Current violations: **{len(violations)}**")
        with st.expander("Show violation details"):
            for item in violations:
                st.markdown(f"- {_humanize_detail_text(item.get('details'))}")
    else:
        st.success("No current violations in your filled cells.")

    if report.get("overall_pass"):
        st.success("Puzzle solved! Your assignment satisfies all checks.")


st.set_page_config(page_title="Logic Puzzle Generator", layout="wide")
st.title("Logic Puzzle Game")
st.caption("Generate a puzzle, read hints, fill the grid, and check progress.")

with st.sidebar:
    st.header("New Puzzle")
    grid_size = st.slider("Grid size", min_value=3, max_value=6, value=4, step=1)
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"], index=1)
    # Keep symbolic internal names for solver compatibility.
    # The UI still renders natural-language labels via _human_name.
    use_real_names = False
    generate = st.button("Generate puzzle", type="primary")

if generate or "puzzle_dict" not in st.session_state:
    with st.spinner("Generating puzzle and hints…"):
        puzzle = generate_puzzle(grid_size=grid_size, difficulty=difficulty, use_real_names=use_real_names)
        puzzle_dict = puzzle.to_dict()
        kb_text = module1_to_module2(puzzle_dict)
        hints = _generate_natural_language_hints(puzzle_dict, difficulty=difficulty)
        st.session_state["puzzle_dict"] = puzzle_dict
        st.session_state["kb_text"] = kb_text
        st.session_state["hints"] = hints
        # Reset player guesses when a new puzzle is generated.
        for entity in puzzle_dict.get("entities", []):
            for attribute in puzzle_dict.get("attributes", {}):
                st.session_state[f"guess::{entity}::{attribute}"] = "(blank)"

puzzle_dict = st.session_state["puzzle_dict"]
kb_text = st.session_state["kb_text"]
hints = st.session_state["hints"]
entities = puzzle_dict["entities"]
attributes = puzzle_dict["attributes"]

st.subheader("Puzzle Grid")
_render_puzzle_grid(entities, attributes)

st.subheader("Hints")
for i, hint in enumerate(hints, start=1):
    st.markdown(f"{i}. {hint}")

st.subheader("Your Workspace")
st.caption("Fill guesses and click **Check attempt**. The app does not reveal the hidden solution.")
for entity in entities:
    with st.container():
        st.markdown(f"**{_human_name(entity, 'entity')}**")
        cols = st.columns(len(attributes))
        for idx, (attribute, values) in enumerate(attributes.items()):
            with cols[idx]:
                key = f"guess::{entity}::{attribute}"
                st.selectbox(
                    label=_human_name(attribute, "attribute"),
                    options=["(blank)"] + list(values),
                    format_func=lambda v, a=attribute: "(blank)" if v == "(blank)" else _value_label(a, v),
                    key=key,
                )

c1, c2 = st.columns([1, 1])
check = c1.button("Check attempt", type="primary")
reset = c2.button("Reset guesses")

if reset:
    for entity in entities:
        for attribute in attributes:
            st.session_state[f"guess::{entity}::{attribute}"] = "(blank)"
    st.rerun()

if check:
    attempt_solution_text = _attempt_to_solution_text(entities, attributes)
    attempt_report = verify_to_dict(
        solution_text=attempt_solution_text,
        constraints_data=puzzle_dict["constraints"],
        knowledge_base=kb_text,
        hidden_solution=puzzle_dict["solution"],
    )
    _render_attempt_feedback(attempt_report, total_constraints=len(puzzle_dict["constraints"]))

with st.expander("Downloads"):
    st.download_button(
        "Download hints text",
        data="\n".join(f"{i}. {h}" for i, h in enumerate(hints, start=1)),
        file_name="hints.txt",
        mime="text/plain",
    )


def _humanize_detail_text(detail: Any) -> str:
    text = str(detail)
    text = re.sub(r"\bE(\d+)\b", r"Person \1", text)
    text = re.sub(r"\bA(\d+)\b", r"Category \1", text)
    text = re.sub(r"\bV(\d+)\b", r"Option \1", text)
    return text

