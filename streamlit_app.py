"""
Streamlit UI for the Logic Puzzle Generation and Analysis System.

Game-style interface for solving generated logic puzzles.

Start:
  PYTHONPATH=src streamlit run streamlit_app.py
"""

from __future__ import annotations

import re
import random
import sys
from pathlib import Path
from typing import Any, Dict, List

import streamlit as st

# Ensure `src/` is importable when running via Streamlit from repo root.
SRC_DIR = Path(__file__).parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from module1_puzzle_generator import build_logic_grid_layout, generate_puzzle  # noqa: E402
from module2_logic_representation import module1_to_module2  # noqa: E402
from module4_solution_verification import verify_to_dict  # noqa: E402

THEME_ENTITY_NAMES = [
    "Alice", "Bob", "Sally", "Molly", "Dan", "Charles", "Nina", "Owen", "Priya", "Leo",
    "Maya", "Ethan", "Zara", "Noah", "Ava", "Liam", "Iris", "Kai",
]
THEME_ATTRIBUTE_NAMES = [
    "Person", "Age", "Hair Color", "Favorite Color", "Pet", "Sport", "Movie Genre", "Dream Vacation", "Hobby"
]
THEME_VALUE_LABELS = {
    "Person": THEME_ENTITY_NAMES,
    "Age": ["18", "20", "22", "24", "26", "28", "30", "32"],
    "Hair Color": ["Blonde", "Brunette", "Black", "Red", "Brown", "Gray", "Auburn", "Silver"],
    "Favorite Color": ["Blue", "Green", "Purple", "Yellow", "Red", "Orange", "Teal", "Pink"],
    "Pet": ["Dog", "Cat", "Fish", "Bird", "Hamster", "Rabbit", "Turtle", "Parrot"],
    "Sport": ["Soccer", "Basketball", "Tennis", "Swimming", "Running", "Volleyball", "Golf", "Cycling"],
    "Movie Genre": ["Comedy", "Drama", "SciFi", "Horror", "Action", "Mystery", "Fantasy", "Romance"],
    "Dream Vacation": ["Beach", "City", "Mtn", "Cruise", "Desert", "Lake", "Forest", "Island"],
    "Hobby": ["Reading", "Gaming", "Cooking", "Gardening", "Photography", "Painting", "Yoga", "Hiking"],
}
RECENT_MAPPING_MEMORY = 3


def _build_display_mappings(puzzle_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Build rotating display labels so new puzzles use new variables/values."""
    entities = list(puzzle_dict.get("entities", []))
    attributes = list(puzzle_dict.get("attributes", {}).keys())
    attribute_values = puzzle_dict.get("attributes", {})

    recent_signatures = st.session_state.get("recent_mapping_signatures", [])
    signature = ""
    entity_map: Dict[str, str] = {}
    attribute_map: Dict[str, str] = {}
    value_map: Dict[str, Dict[str, str]] = {}

    for _ in range(25):
        entity_labels = random.sample(THEME_ENTITY_NAMES, k=len(entities))
        candidate_entity_map = {entity: entity_labels[idx] for idx, entity in enumerate(entities)}

        # Reserve one always-visible grid variable for names.
        first_attribute = attributes[0] if attributes else None
        remaining_attributes = attributes[1:] if len(attributes) > 1 else []
        remaining_label_pool = [label for label in THEME_ATTRIBUTE_NAMES if label != "Person"]
        sampled_remaining_labels = random.sample(remaining_label_pool, k=len(remaining_attributes))
        candidate_attribute_map = {}
        if first_attribute is not None:
            candidate_attribute_map[first_attribute] = "Person"
        for idx, attribute in enumerate(remaining_attributes):
            candidate_attribute_map[attribute] = sampled_remaining_labels[idx]

        candidate_value_map: Dict[str, Dict[str, str]] = {}
        for attribute in attributes:
            label = candidate_attribute_map[attribute]
            values = list(attribute_values.get(attribute, []))
            if label == "Person":
                value_pool = list(entity_labels)
            else:
                value_pool = THEME_VALUE_LABELS.get(label, [f"{label} {i+1}" for i in range(max(8, len(values)))])
            if len(value_pool) < len(values):
                value_pool = value_pool + [f"{label} {i+1}" for i in range(len(value_pool), len(values))]
            selected = random.sample(value_pool, k=len(values))
            candidate_value_map[attribute] = {value: selected[idx] for idx, value in enumerate(values)}

        attribute_labels_for_signature = [
            candidate_attribute_map[attr] for attr in attributes if attr in candidate_attribute_map
        ]
        signature = "|".join(entity_labels + attribute_labels_for_signature)
        if signature not in recent_signatures:
            entity_map = candidate_entity_map
            attribute_map = candidate_attribute_map
            value_map = candidate_value_map
            break
        entity_map = candidate_entity_map
        attribute_map = candidate_attribute_map
        value_map = candidate_value_map

    recent_signatures = (recent_signatures + [signature])[-RECENT_MAPPING_MEMORY:]
    st.session_state["recent_mapping_signatures"] = recent_signatures

    return {
        "entity_map": entity_map,
        "attribute_map": attribute_map,
        "value_map": value_map,
    }


def _human_name(symbol: Any, kind: str) -> str:
    raw = str(symbol)
    display_maps = st.session_state.get("display_maps", {})
    if kind == "entity":
        mapped = display_maps.get("entity_map", {}).get(raw)
        if mapped:
            return mapped
    if kind == "attribute":
        mapped = display_maps.get("attribute_map", {}).get(raw)
        if mapped:
            return mapped
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
    raw_attribute = str(attribute_symbol)
    raw_value = str(value_symbol)
    display_maps = st.session_state.get("display_maps", {})
    mapped_value = display_maps.get("value_map", {}).get(raw_attribute, {}).get(raw_value)
    if mapped_value:
        return mapped_value

    attr_label = _human_name(attribute_symbol, "attribute")
    raw_value = str(value_symbol)
    if raw_value.startswith("V") and raw_value[1:].isdigit():
        idx = int(raw_value[1:]) - 1
        label_values = THEME_VALUE_LABELS.get(attr_label, [])
        if 0 <= idx < len(label_values):
            return label_values[idx]
    return _human_name(raw_value, "value")


def _generate_solution_based_hints(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
    difficulty: str,
) -> List[str]:
    """Create indirect, natural-language clues from solution with difficulty-based counts."""
    hints: List[str] = []
    direct_hints: List[str] = []
    seen_hints = set()
    attribute_order = list(attributes.keys())
    first_attr = attribute_order[0] if attribute_order else None
    covered_attributes: set[str] = set()

    def _add_hint(text: str, is_direct: bool = False, attrs: List[str] | None = None) -> None:
        clean = text.strip()
        if clean and clean not in seen_hints:
            hints.append(clean)
            seen_hints.add(clean)
            if is_direct:
                direct_hints.append(clean)
            if attrs:
                covered_attributes.update(attrs)

    def _entity_reference(entity: str, mention_idx: int) -> str:
        """
        Build person references only from generated grid variables.
        This avoids name-only references that don't appear in the grid.
        """
        if first_attr is None:
            return "that person"
        value = solution.get(entity, {}).get(first_attr)
        if value is None:
            return "that person"
        first_attr_label = _human_name(first_attr, "attribute").lower()
        value_label = _value_label(first_attr, value)
        if first_attr_label in {"person", "name"}:
            return value_label
        if mention_idx % 2 == 0:
            return f"the person whose {first_attr_label} is {value_label}"
        return f"the one with {first_attr_label} {value_label}"

    negative_templates = [
        "{entity} is not associated with {value} for {attribute}.",
        "{entity} does not have {value} in the {attribute} category.",
        "You can rule out {value} for {entity}'s {attribute}.",
        "It is not the case that {entity}'s {attribute} is {value}.",
    ]
    relational_templates = [
        "The person whose {attr_a} is {value_a} is also the one with {attr_b} {value_b}.",
        "Whoever has {value_a} for {attr_a} also has {value_b} for {attr_b}.",
        "The {value_a} entry under {attr_a} belongs to the same person tied to {value_b} in {attr_b}.",
    ]
    direct_templates = [
        "{entity}'s {attribute} is {value}.",
        "For {entity}, the {attribute} is {value}.",
        "One direct link: {entity} is the person whose {attribute} is {value}.",
    ]

    # 1) Negative clues: rule out incorrect assignments.
    negative_idx = 0
    for entity_idx, entity in enumerate(entities):
        entity_ref = _entity_reference(entity, entity_idx)
        for attribute in attribute_order[:2]:
            values = attributes.get(attribute, [])
            true_value = solution.get(entity, {}).get(attribute)
            wrong_value = next((v for v in values if v != true_value), None)
            if wrong_value is None:
                continue
            attribute_name = _human_name(attribute, "attribute")
            wrong_label = _value_label(attribute, wrong_value)
            template = negative_templates[negative_idx % len(negative_templates)]
            negative_idx += 1
            _add_hint(
                template.format(
                    entity=entity_ref,
                    value=wrong_label,
                    attribute=attribute_name.lower(),
                ),
                attrs=[attribute],
            )

    # 2) Relational clues across two attributes (person linked across categories).
    if len(attribute_order) >= 2:
        attr_a = attribute_order[0]
        attr_b = attribute_order[1]
        attr_a_label = _human_name(attr_a, "attribute")
        attr_b_label = _human_name(attr_b, "attribute")
        for entity in entities:
            v_a = solution.get(entity, {}).get(attr_a)
            v_b = solution.get(entity, {}).get(attr_b)
            if v_a is None or v_b is None:
                continue
            a_name = _value_label(attr_a, v_a)
            b_name = _value_label(attr_b, v_b)
            template = relational_templates[len(hints) % len(relational_templates)]
            _add_hint(
                template.format(
                    attr_a=attr_a_label.lower(),
                    value_a=a_name,
                    attr_b=attr_b_label.lower(),
                    value_b=b_name,
                ),
                attrs=[attr_a, attr_b],
            )

    # 2b) A few direct "is" clues for clarity, scaled by difficulty.
    direct_count_by_difficulty = {"easy": 3, "medium": 2, "hard": 1}
    direct_target = direct_count_by_difficulty.get(difficulty.lower().strip(), 2)
    direct_added = 0
    for entity in entities:
        if direct_added >= direct_target:
            break
        for attribute in attribute_order[:2]:
            value_symbol = solution.get(entity, {}).get(attribute)
            if value_symbol is None:
                continue
            template = direct_templates[direct_added % len(direct_templates)]
            _add_hint(
                template.format(
                    entity=_entity_reference(entity, direct_added),
                    attribute=_human_name(attribute, "attribute").lower(),
                    value=_value_label(attribute, value_symbol),
                )
            , is_direct=True, attrs=[attribute])
            direct_added += 1
            if direct_added >= direct_target:
                break

    # 3) Comparative clues using first attribute ordering.
    if len(attribute_order) >= 1 and len(entities) >= 2:
        ordered_attr = attribute_order[0]
        ordered_label = _human_name(ordered_attr, "attribute")
        index_by_value = {value: idx for idx, value in enumerate(attributes.get(ordered_attr, []))}
        for i in range(len(entities) - 1):
            e1 = entities[i]
            e2 = entities[i + 1]
            v1 = solution.get(e1, {}).get(ordered_attr)
            v2 = solution.get(e2, {}).get(ordered_attr)
            if v1 not in index_by_value or v2 not in index_by_value:
                continue
            n1 = index_by_value[v1]
            n2 = index_by_value[v2]
            e1_name = _human_name(e1, "entity")
            e2_name = _human_name(e2, "entity")
            if n1 > n2:
                _add_hint(
                    f"In {ordered_label.lower()}, {e1_name} comes after {e2_name}.",
                    attrs=[ordered_attr],
                )
            elif n1 < n2:
                _add_hint(
                    f"In {ordered_label.lower()}, {e1_name} comes before {e2_name}.",
                    attrs=[ordered_attr],
                )
            else:
                _add_hint(
                    f"{e1_name} and {e2_name} share the same {ordered_label.lower()} value.",
                    attrs=[ordered_attr],
                )

    # 4) Either/or clues.
    if len(attribute_order) >= 2:
        either_attr = attribute_order[1]
        either_label = _human_name(either_attr, "attribute")
        values = attributes.get(either_attr, [])
        for entity in entities[: max(1, len(entities) // 2)]:
            true_value = solution.get(entity, {}).get(either_attr)
            if true_value is None:
                continue
            alt_value = next((v for v in values if v != true_value), None)
            if alt_value is None:
                continue
            entity_name = _human_name(entity, "entity")
            true_label = _value_label(either_attr, true_value)
            alt_label = _value_label(either_attr, alt_value)
            _add_hint(
                f"For {entity_name}, the {either_label.lower()} is either {true_label} or {alt_label}."
            , attrs=[either_attr]
            )

    # 5) Light anchoring clue in sentence form (kept to a minimum).
    if len(attribute_order) >= 3 and entities:
        anchor_entity = entities[-1]
        anchor_attr = attribute_order[2]
        anchor_value = solution.get(anchor_entity, {}).get(anchor_attr)
        if anchor_value is not None:
            _add_hint(
                f"Among all possibilities, {_human_name(anchor_entity, 'entity')} is linked with {_value_label(anchor_attr, anchor_value)} for {_human_name(anchor_attr, 'attribute').lower()}."
            , attrs=[anchor_attr]
            )

    # 6) Guarantee each variable/category appears in at least one hint.
    for attribute in attribute_order:
        if attribute in covered_attributes:
            continue
        attr_label = _human_name(attribute, "attribute").lower()
        entity = entities[0] if entities else None
        if entity is None:
            continue
        value_symbol = solution.get(entity, {}).get(attribute)
        if value_symbol is None:
            continue
        _add_hint(
            f"As an additional clue, {_entity_reference(entity, len(hints))} is tied to {_value_label(attribute, value_symbol)} in {attr_label}.",
            is_direct=True,
            attrs=[attribute],
        )

    max_hints_by_difficulty = {
        "easy": max(8, len(entities) + 4),
        "medium": max(6, len(entities) + 2),
        "hard": max(4, len(entities)),
    }
    normalized = difficulty.lower().strip()
    max_hints = max_hints_by_difficulty.get(normalized, max_hints_by_difficulty["medium"])
    required_direct_by_difficulty = {"easy": 3, "medium": 2, "hard": 1}
    required_direct = required_direct_by_difficulty.get(normalized, 2)
    direct_selected = direct_hints[:required_direct]

    # Guarantee at least one selected hint per variable/category.
    attr_hint_map: Dict[str, List[str]] = {attr: [] for attr in attribute_order}
    for hint in hints:
        hint_l = hint.lower()
        for attr in attribute_order:
            attr_label_l = _human_name(attr, "attribute").lower()
            if attr_label_l in hint_l:
                attr_hint_map[attr].append(hint)
    coverage_selected: List[str] = []
    for attr in attribute_order:
        candidates = attr_hint_map.get(attr, [])
        if candidates:
            chosen = candidates[0]
            if chosen not in coverage_selected:
                coverage_selected.append(chosen)

    base_selected: List[str] = []
    for hint in direct_selected + coverage_selected:
        if hint not in base_selected:
            base_selected.append(hint)

    remaining_slots = max(0, max_hints - len(base_selected))
    non_base = [hint for hint in hints if hint not in set(base_selected)]
    hints = base_selected + non_base[:remaining_slots]
    random.shuffle(hints)

    if len(entities) >= 2 and len(attribute_order) >= 1:
        first_attribute = attribute_order[0]
        attr_name = _human_name(first_attribute, "attribute")
        e1, e2 = entities[0], entities[1]
        v1 = solution.get(e1, {}).get(first_attribute)
        v2 = solution.get(e2, {}).get(first_attribute)
        if v1 is not None and v2 is not None:
            extra_hint = (
                f"The {attr_name.lower()} linked to {_human_name(e1, 'entity')} "
                f"is different from the one linked to {_human_name(e2, 'entity')}."
            )
            if extra_hint not in seen_hints and len(hints) < max_hints:
                hints.append(extra_hint)

    return hints


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

    # 2) Build relation-style hints (no direct "Name has Category = Value" reveals).
    relation_hints = _build_relation_hints_from_solution(entities, attributes, solution)
    negative_hints = _build_negative_hints_from_solution(entities, attributes, solution)

    normalized = difficulty.lower().strip()
    if normalized == "easy":
        # Easy: more relation hints + more negative hints.
        hints.extend(relation_hints)
        hints.extend(negative_hints[: max(6, len(entities) * 2)])
    elif normalized == "medium":
        hints.extend(relation_hints)
        hints.extend(negative_hints[: max(4, len(entities))])
    else:
        # Hard: mostly relational hints, fewer negatives.
        hints.extend(relation_hints)
        hints.extend(negative_hints[: max(2, len(entities) // 2)])

    # Deduplicate while preserving order (semantic-normalized).
    unique_hints, seen = _dedupe_hints(hints)

    # Guarantee enough clues to solve: at least number of constraints.
    min_hint_count = max(6, len(puzzle_dict.get("constraints", [])))
    if len(unique_hints) < min_hint_count:
        for extra in relation_hints + negative_hints:
            norm = _normalize_hint_key(extra)
            if norm not in seen:
                unique_hints.append(extra)
                seen.add(norm)
            if len(unique_hints) >= min_hint_count:
                break

    return unique_hints


def _build_relation_hints_from_solution(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
) -> List[str]:
    hints: List[str] = []
    attr_symbols = list(attributes.keys())
    age_attr = _attribute_symbol_for_label(attributes, "Age")

    # Cross-attribute relation hints:
    # "The person whose Hair Color is Brunette has Favorite Color = Purple."
    non_age_attrs = [a for a in attr_symbols if a != age_attr]
    if len(non_age_attrs) >= 2:
        a1 = non_age_attrs[0]
        a2 = non_age_attrs[1]
        for entity in entities:
            v1 = solution.get(entity, {}).get(a1)
            v2 = solution.get(entity, {}).get(a2)
            if v1 is None or v2 is None:
                continue
            hints.append(
                f"The person whose {_human_name(a1, 'attribute')} is {_value_label(a1, v1)} "
                f"has {_human_name(a2, 'attribute')} {_value_label(a2, v2)}."
            )

    # If we have at least 3 non-age attributes, add another relation layer.
    if len(non_age_attrs) >= 3:
        a2 = non_age_attrs[1]
        a3 = non_age_attrs[2]
        for entity in entities:
            v2 = solution.get(entity, {}).get(a2)
            v3 = solution.get(entity, {}).get(a3)
            if v2 is None or v3 is None:
                continue
            hints.append(
                f"Whoever has {_human_name(a2, 'attribute')} {_value_label(a2, v2)} "
                f"also has {_human_name(a3, 'attribute')} {_value_label(a3, v3)}."
            )

    # Add age-relative hints between consecutive entities.
    if age_attr and len(entities) >= 2:
        for i in range(len(entities) - 1):
            e1, e2 = entities[i], entities[i + 1]
            age1 = _to_int_if_possible(_value_label(age_attr, solution.get(e1, {}).get(age_attr, "")))
            age2 = _to_int_if_possible(_value_label(age_attr, solution.get(e2, {}).get(age_attr, "")))
            if age1 is not None and age2 is not None:
                hints.append(_age_relation_sentence(_human_name(e1, "entity"), age1, _human_name(e2, "entity"), age2))
    return hints


def _build_negative_hints_from_solution(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
) -> List[str]:
    hints: List[str] = []
    attr_symbols = list(attributes.keys())
    for entity in entities:
        entity_name = _human_name(entity, "entity")
        for attribute in attr_symbols:
            true_value = solution.get(entity, {}).get(attribute)
            values = attributes.get(attribute, [])
            false_value = next((v for v in values if v != true_value), None)
            if false_value is None:
                continue
            attr_name = _human_name(attribute, "attribute")
            false_label = _value_label(attribute, false_value)
            hints.append(f"{entity_name}'s {attr_name} is not {false_label}.")
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


def _cell_mark(
    entities: List[str],
    row_attribute: str,
    row_value: str,
    column_attribute: str,
    column_value: str,
) -> str:
    """
    Return grid cell mark based on current partial guesses.

    ✓ means a guessed match is present.
    × means ruled out by a conflicting guess on the same entity.
    blank means still unknown.
    """
    row_owner = None
    col_owner = None

    for entity in entities:
        row_guess = st.session_state.get(f"guess::{entity}::{row_attribute}", "(blank)")
        col_guess = st.session_state.get(f"guess::{entity}::{column_attribute}", "(blank)")

        if row_guess == row_value and col_guess == column_value:
            return "✓"
        if row_guess == row_value:
            row_owner = entity
        if col_guess == column_value:
            col_owner = entity

    if row_owner is not None:
        col_guess = st.session_state.get(f"guess::{row_owner}::{column_attribute}", "(blank)")
        if col_guess != "(blank)" and col_guess != column_value:
            return "×"

    if col_owner is not None:
        row_guess = st.session_state.get(f"guess::{col_owner}::{row_attribute}", "(blank)")
        if row_guess != "(blank)" and row_guess != row_value:
            return "×"

    return ""


def _render_single_logic_worksheet(
    entities: List[str],
    attributes: Dict[str, List[str]],
    layout: Dict[str, Any],
) -> None:
    """Render one worksheet grid using the docs example structure."""
    row_attributes = layout.get("row_attributes", [])
    column_attributes = layout.get("column_attributes", [])
    top_header_cells: List[str] = []
    second_header_cells: List[str] = []
    col_palette_classes = ["col-a", "col-b", "col-c"]
    for col_idx, col_attribute in enumerate(column_attributes):
        palette_class = col_palette_classes[col_idx % len(col_palette_classes)]
        col_label = _human_name(col_attribute, "attribute")
        col_values = attributes.get(col_attribute, [])
        top_header_cells.append(
            f"<th colspan='{len(col_values)}' class='group-hdr {palette_class}-hdr'>{col_label}</th>"
        )
        for col_value in col_values:
            second_header_cells.append(
                f"<th class='value-hdr {palette_class}'>{_value_label(col_attribute, col_value)}</th>"
            )

    body_rows: List[str] = []
    for block_idx, row_attribute in enumerate(row_attributes):
        row_class = ["d-block", "c-block", "b-block"][block_idx % 3]
        row_label = _human_name(row_attribute, "attribute")
        row_values_for_attr = attributes.get(row_attribute, [])
        for row_idx, row_value in enumerate(row_values_for_attr):
            row_cells: List[str] = []
            if row_idx == 0:
                row_cells.append(
                    (
                        f"<th class='row-group-head' rowspan='{len(row_values_for_attr)}'>"
                        f"<span class='row-attr'>{row_label}</span>"
                        "</th>"
                    )
                )
            row_cells.append(
                (
                    "<th class='row-head'>"
                    f"<span class='row-value'>{_value_label(row_attribute, row_value)}</span>"
                    "</th>"
                )
            )
            for col_attribute in column_attributes:
                for col_value in attributes.get(col_attribute, []):
                    if row_attribute == col_attribute:
                        row_cells.append("<td class='empty'></td>")
                        continue
                    mark = _cell_mark(
                        entities=entities,
                        row_attribute=row_attribute,
                        row_value=row_value,
                        column_attribute=col_attribute,
                        column_value=col_value,
                    )
                    if mark == "✓":
                        row_cells.append("<td class='mark-yes'>✓</td>")
                    elif mark == "×":
                        row_cells.append("<td class='mark-no'>×</td>")
                    else:
                        row_cells.append("<td></td>")
            body_rows.append(f"<tr class='{row_class}' data-row-category='{row_label}'>{''.join(row_cells)}</tr>")

    html = f"""
    <style>
      .worksheet-table {{
        width: 100%;
        border-collapse: collapse;
        table-layout: auto;
        font-size: 0.78rem;
        color: #111827;
        background: #ffffff;
      }}
      .worksheet-table th, .worksheet-table td {{
        border: 1px solid #2d333b;
        text-align: center;
        padding: 0.24rem 0.2rem;
        color: #111827;
        background: #ffffff;
        white-space: normal;
        word-break: break-word;
        overflow-wrap: anywhere;
        min-width: 2rem;
        line-height: 1.2;
      }}
      .worksheet-table .corner {{
        background: #f0f3f6;
        color: #111827;
        font-weight: 700;
        white-space: nowrap;
      }}
      .worksheet-table .group-hdr {{
        background: #e7eef9;
        color: #111827;
        font-weight: 700;
        white-space: normal;
      }}
      .worksheet-table .value-hdr {{
        background: #f5f8fc;
        color: #111827;
        font-weight: 600;
        white-space: normal;
      }}
      .worksheet-table .col-a-hdr {{ background: #dce2ff; }}
      .worksheet-table .col-b-hdr {{ background: #ffe8c4; }}
      .worksheet-table .col-c-hdr {{ background: #d5f0e8; }}
      .worksheet-table .col-a {{ background: #e8ecff; }}
      .worksheet-table .col-b {{ background: #fff4e0; }}
      .worksheet-table .col-c {{ background: #e4f7f1; }}
      .worksheet-table .row-group-head {{
        text-align: left;
        width: 7rem;
        background: #f0f3f6;
        color: #111827;
        font-weight: 700;
        white-space: normal;
        vertical-align: middle;
      }}
      .worksheet-table .row-head {{
        text-align: left;
        width: 9rem;
        background: #fafbfc;
        color: #111827;
        font-weight: 600;
        white-space: normal;
      }}
      .worksheet-table .row-attr {{
        font-weight: 700;
      }}
      .worksheet-table .row-value {{
        display: inline-block;
        padding: 0.1rem 0.3rem;
        border-radius: 4px;
      }}
      .worksheet-table tr.d-block .row-value {{ background: #ddf4ff; border-left: 3px solid #0969da; }}
      .worksheet-table tr.c-block .row-value {{ background: #fff8c5; border-left: 3px solid #bf8700; }}
      .worksheet-table tr.b-block .row-value {{ background: #dafbe1; border-left: 3px solid #1a7f37; }}
      .worksheet-table .empty {{ background: #f6f8fa; }}
      .worksheet-table .mark-yes {{ color: #1a7f37; font-weight: 800; }}
      .worksheet-table .mark-no {{ color: #cf222e; font-weight: 700; }}
    </style>
    <table class="worksheet-table">
      <thead>
        <tr>
          <th rowspan="2" colspan="2" class="corner">Rows</th>
          {''.join(top_header_cells)}
        </tr>
        <tr>
          {''.join(second_header_cells)}
        </tr>
      </thead>
      <tbody>{''.join(body_rows)}</tbody>
    </table>
    """
    st.caption("Worksheet layout matches the docs example structure.")
    st.markdown(html, unsafe_allow_html=True)
def _normalize_hint_sentence(hint: str) -> str:
    sentence = hint.strip()
    sentence = re.sub(r"^(One|First|Second|Third|Fourth|Fifth)\s+hint:\s*", "", sentence, flags=re.IGNORECASE)
    sentence = sentence.replace(" = ", " ")
    if sentence and sentence[-1] not in ".!?":
        sentence += "."
    return sentence


def _normalize_hint_key(hint: str) -> str:
    sentence = _normalize_hint_sentence(hint).lower()
    sentence = re.sub(r"\s+", " ", sentence).strip()
    return sentence


def _dedupe_hints(hints: List[str]) -> tuple[List[str], set[str]]:
    unique: List[str] = []
    seen: set[str] = set()
    for hint in hints:
        key = _normalize_hint_key(hint)
        if key in seen:
            continue
        unique.append(hint)
        seen.add(key)
    return unique, seen


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


def _update_revealed_cells_from_attempt(
    entities: List[str],
    attributes: Dict[str, List[str]],
    hidden_solution: Dict[str, Dict[str, str]],
) -> int:
    newly_revealed = 0
    for entity in entities:
        for attribute in attributes:
            guess_key = f"guess::{entity}::{attribute}"
            reveal_key = f"reveal::{entity}::{attribute}"
            guess = st.session_state.get(guess_key, "(blank)")
            if guess == "(blank)":
                continue
            correct_value = hidden_solution.get(entity, {}).get(attribute)
            if guess == correct_value and not st.session_state.get(reveal_key):
                st.session_state[reveal_key] = _value_label(attribute, correct_value)
                newly_revealed += 1
    return newly_revealed


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
        display_maps = _build_display_mappings(puzzle_dict)
        kb_text = module1_to_module2(puzzle_dict)
        hints = _generate_solution_based_hints(
            entities=puzzle_dict.get("entities", []),
            attributes=puzzle_dict.get("attributes", {}),
            solution=puzzle_dict.get("solution", {}),
            difficulty=difficulty,
        )
        layout = build_logic_grid_layout(puzzle_dict.get("attributes", {}))
        st.session_state["puzzle_dict"] = puzzle_dict
        st.session_state["display_maps"] = display_maps
        st.session_state["kb_text"] = kb_text
        st.session_state["hints"] = hints
        st.session_state["layout"] = layout
        # Reset player guesses when a new puzzle is generated.
        for entity in puzzle_dict.get("entities", []):
            for attribute in puzzle_dict.get("attributes", {}):
                st.session_state[f"guess::{entity}::{attribute}"] = "(blank)"
                st.session_state[f"reveal::{entity}::{attribute}"] = None
        st.session_state["puzzle_solved"] = False

puzzle_dict = st.session_state["puzzle_dict"]
kb_text = st.session_state["kb_text"]
hints = st.session_state["hints"]
layout = st.session_state["layout"]
entities = puzzle_dict["entities"]
attributes = puzzle_dict["attributes"]

st.subheader("Logic Worksheet")
_render_single_logic_worksheet(entities, attributes, layout)

st.subheader("Hints")
for i, hint in enumerate(hints, start=1):
    st.markdown(f"{i}. {_normalize_hint_sentence(hint)}")

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
            st.session_state[f"reveal::{entity}::{attribute}"] = None
    st.session_state["puzzle_solved"] = False
    st.rerun()

if check:
    attempt_solution_text = _attempt_to_solution_text(entities, attributes)
    attempt_report = verify_to_dict(
        solution_text=attempt_solution_text,
        constraints_data=puzzle_dict["constraints"],
        knowledge_base=kb_text,
        hidden_solution=puzzle_dict["solution"],
    )
    newly_revealed = _update_revealed_cells_from_attempt(
        entities=entities,
        attributes=attributes,
        hidden_solution=puzzle_dict["solution"],
    )
    if newly_revealed > 0:
        st.success(f"You revealed {newly_revealed} new correct cell(s).")
    if attempt_report.get("overall_pass"):
        if not st.session_state.get("puzzle_solved", False):
            st.session_state["puzzle_solved"] = True
            st.toast("Puzzle complete! Great job!", icon="🎉")
            st.balloons()
    st.rerun()
    _render_attempt_feedback(attempt_report, total_constraints=len(puzzle_dict["constraints"]))

if st.session_state.get("puzzle_solved", False):
    st.success("You solved the puzzle! All cells are correct.")

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

