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

from module1_puzzle_generator import (  # noqa: E402
    build_logic_grid_layout,
    generate_puzzle_fixed_value_count,
)
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
    excluded_answer_pairs: set[str] | None = None,
) -> List[str]:
    """Create varied, non-redundant puzzle-book style clues from the solution."""
    attribute_order = list(attributes.keys())
    if len(attribute_order) < 2 or not entities:
        return []
    excluded_answer_pairs = excluded_answer_pairs or set()

    # Difficulty no longer changes hint count; it now controls pre-filled grid cells.
    # Keep hint profile consistent across easy/medium/hard.
    max_hints = 6
    direct_target = 1
    indirect_min = 3

    clues: List[Dict[str, Any]] = []
    used_relation_keys: set[str] = set()
    used_answer_pairs: set[str] = set()
    covered_attributes: set[str] = set()

    def _canonical_pair(attr_a: str, val_a: str, attr_b: str, val_b: str) -> str:
        left = f"{attr_a}={val_a}"
        right = f"{attr_b}={val_b}"
        return "|".join(sorted([left, right]))

    def _add_clue(
        text: str,
        clue_type: str,
        attrs: List[str],
        relation_key: str,
        answer_pair_key: str | None = None,
        anchor_key: str | None = None,
    ) -> None:
        clean = text.strip()
        if not clean or relation_key in used_relation_keys:
            return
        # Prevent multiple clues that encode the same true answer relation.
        if answer_pair_key is not None and answer_pair_key in used_answer_pairs:
            return
        # Suppress clues that directly correspond to prefilled visible answers.
        if answer_pair_key is not None and answer_pair_key in excluded_answer_pairs:
            return
        used_relation_keys.add(relation_key)
        if answer_pair_key is not None:
            used_answer_pairs.add(answer_pair_key)
        clues.append(
            {
                "text": clean,
                "type": clue_type,
                "attrs": attrs,
                "answer_pair_key": answer_pair_key,
                "anchor_key": anchor_key,
            }
        )
        covered_attributes.update(attrs)

    def _attr_label(attr: str) -> str:
        return _human_name(attr, "attribute").lower()

    # Build canonical pair facts from the solved assignment.
    pair_facts: List[Dict[str, str]] = []
    for i, attr_a in enumerate(attribute_order):
        for j in range(i + 1, len(attribute_order)):
            attr_b = attribute_order[j]
            for entity in entities:
                v_a = solution.get(entity, {}).get(attr_a)
                v_b = solution.get(entity, {}).get(attr_b)
                if v_a is None or v_b is None:
                    continue
                pair_facts.append(
                    {
                        "attr_a": attr_a,
                        "attr_b": attr_b,
                        "value_a": _value_label(attr_a, v_a),
                        "value_b": _value_label(attr_b, v_b),
                    }
                )

    random.shuffle(pair_facts)
    all_true_pair_keys: set[str] = {
        _canonical_pair(f["attr_a"], f["value_a"], f["attr_b"], f["value_b"]) for f in pair_facts
    }

    # Relational clues (indirect).
    relational_templates = [
        "Whoever has {value_a} in {attr_a} also has {value_b} in {attr_b}.",
        "The {attr_a} value {value_a} belongs to the same person as {attr_b} {value_b}.",
        "{value_a} under {attr_a} corresponds to {value_b} under {attr_b}.",
    ]
    for idx, fact in enumerate(pair_facts):
        pair_key = _canonical_pair(
            fact["attr_a"], fact["value_a"], fact["attr_b"], fact["value_b"]
        )
        key = "pair-rel|" + pair_key
        anchor_key = f"{fact['attr_a']}={fact['value_a']}|{fact['attr_b']}"
        template = relational_templates[idx % len(relational_templates)]
        _add_clue(
            template.format(
                attr_a=_attr_label(fact["attr_a"]),
                value_a=fact["value_a"],
                attr_b=_attr_label(fact["attr_b"]),
                value_b=fact["value_b"],
            ),
            clue_type="relational",
            attrs=[fact["attr_a"], fact["attr_b"]],
            relation_key=key,
            answer_pair_key=pair_key,
            anchor_key=anchor_key,
        )

    # Negative clues (indirect): uses true anchor with a wrong partner value.
    for fact in pair_facts:
        values_b = [v for v in attributes.get(fact["attr_b"], [])]
        wrong_b_raw = next(
            (raw for raw in values_b if _value_label(fact["attr_b"], raw) != fact["value_b"]),
            None,
        )
        if wrong_b_raw is None:
            continue
        wrong_b = _value_label(fact["attr_b"], wrong_b_raw)
        key = "pair-neg|" + "|".join(
            [fact["attr_a"], fact["value_a"], fact["attr_b"], wrong_b]
        )
        anchor_key = f"{fact['attr_a']}={fact['value_a']}|{fact['attr_b']}"
        _add_clue(
            f"The person with {fact['value_a']} in {_attr_label(fact['attr_a'])} does not go with {wrong_b} in {_attr_label(fact['attr_b'])}.",
            clue_type="negative",
            attrs=[fact["attr_a"], fact["attr_b"]],
            relation_key=key,
            anchor_key=anchor_key,
        )

    # Either/or clues (indirect): one true option plus one decoy.
    either_templates = [
        "If {attr_a} is {value_a}, then {attr_b} is either {value_b} or {alt_b}.",
        "The {attr_a} value {value_a} pairs with either {value_b} or {alt_b} in {attr_b}.",
    ]
    for idx, fact in enumerate(pair_facts):
        values_b = [v for v in attributes.get(fact["attr_b"], [])]
        alt_b_raw = next(
            (raw for raw in values_b if _value_label(fact["attr_b"], raw) != fact["value_b"]),
            None,
        )
        if alt_b_raw is None:
            continue
        alt_b = _value_label(fact["attr_b"], alt_b_raw)
        pair_key = _canonical_pair(fact["attr_a"], fact["value_a"], fact["attr_b"], fact["value_b"])
        key = "pair-either|" + pair_key
        anchor_key = f"{fact['attr_a']}={fact['value_a']}|{fact['attr_b']}"
        template = either_templates[idx % len(either_templates)]
        _add_clue(
            template.format(
                attr_a=_attr_label(fact["attr_a"]),
                value_a=fact["value_a"],
                attr_b=_attr_label(fact["attr_b"]),
                value_b=fact["value_b"],
                alt_b=alt_b,
            ),
            clue_type="either_or",
            attrs=[fact["attr_a"], fact["attr_b"]],
            relation_key=key,
            answer_pair_key=pair_key,
            anchor_key=anchor_key,
        )

    # Direct clues (sparingly).
    direct_templates = [
        "{attr_a} {value_a} is paired with {attr_b} {value_b}.",
        "A direct match is {attr_a} {value_a} with {attr_b} {value_b}.",
    ]
    direct_added = 0
    for idx, fact in enumerate(pair_facts):
        if direct_added >= direct_target:
            break
        pair_key = _canonical_pair(
            fact["attr_a"], fact["value_a"], fact["attr_b"], fact["value_b"]
        )
        key = "pair-direct|" + pair_key
        anchor_key = f"{fact['attr_a']}={fact['value_a']}|{fact['attr_b']}"
        if key in used_relation_keys:
            continue
        template = direct_templates[idx % len(direct_templates)]
        _add_clue(
            template.format(
                attr_a=_attr_label(fact["attr_a"]),
                value_a=fact["value_a"],
                attr_b=_attr_label(fact["attr_b"]),
                value_b=fact["value_b"],
            ),
            clue_type="direct",
            attrs=[fact["attr_a"], fact["attr_b"]],
            relation_key=key,
            answer_pair_key=pair_key,
            anchor_key=anchor_key,
        )
        direct_added += 1

    # Ensure every variable appears in at least one clue.
    for attr in attribute_order:
        if attr in covered_attributes:
            continue
        fallback = next((f for f in pair_facts if f["attr_a"] == attr or f["attr_b"] == attr), None)
        if fallback is None:
            continue
        key = "pair-cover|" + _canonical_pair(
            fallback["attr_a"], fallback["value_a"], fallback["attr_b"], fallback["value_b"]
        )
        _add_clue(
            f"For coverage, {_attr_label(fallback['attr_a'])} {fallback['value_a']} aligns with {_attr_label(fallback['attr_b'])} {fallback['value_b']}.",
            clue_type="direct",
            attrs=[fallback["attr_a"], fallback["attr_b"]],
            relation_key=key,
            anchor_key=f"{fallback['attr_a']}={fallback['value_a']}|{fallback['attr_b']}",
        )

    # Select final clue set with guaranteed indirect minimum.
    direct_pool = [c for c in clues if c["type"] == "direct"]
    indirect_pool = [c for c in clues if c["type"] != "direct"]
    random.shuffle(direct_pool)
    random.shuffle(indirect_pool)

    selected: List[Dict[str, Any]] = []
    selected.extend(indirect_pool[:indirect_min])
    remaining_slots = max(0, max_hints - len(selected))
    # Fill with a mix, keeping direct clues limited.
    direct_allow = max(0, min(direct_target, remaining_slots))
    selected.extend(direct_pool[:direct_allow])
    remaining_slots = max(0, max_hints - len(selected))

    remainder = [c for c in (indirect_pool[indirect_min:] + direct_pool[direct_allow:]) if c not in selected]
    selected.extend(remainder[:remaining_slots])

    # Final solvability guard:
    # Ensure hints cover every true pair relation from the hidden solution.
    selected_true_pairs = {
        c.get("answer_pair_key") for c in selected if c.get("answer_pair_key") is not None
    }
    required_pair_keys = all_true_pair_keys - excluded_answer_pairs
    missing_true_pairs = [k for k in required_pair_keys if k not in selected_true_pairs]
    if missing_true_pairs:
        pair_to_clue: Dict[str, Dict[str, Any]] = {}
        for c in clues:
            pair_key = c.get("answer_pair_key")
            if pair_key is None:
                continue
            existing = pair_to_clue.get(pair_key)
            # Prefer relational wording over very direct clues when available.
            if existing is None:
                pair_to_clue[pair_key] = c
            elif existing.get("type") == "direct" and c.get("type") != "direct":
                pair_to_clue[pair_key] = c
        for pair_key in missing_true_pairs:
            clue = pair_to_clue.get(pair_key)
            if clue is not None and clue not in selected:
                selected.append(clue)

    # Remove logically redundant clues:
    # if a direct/relational clue exists for an anchor, discard weaker
    # either_or/negative clues using that same anchor.
    rank = {"direct": 3, "relational": 2, "either_or": 1, "negative": 0}
    best_anchor_rank: Dict[str, int] = {}
    for clue in selected:
        anchor = clue.get("anchor_key")
        if anchor is None:
            continue
        clue_rank = rank.get(str(clue.get("type", "")), 0)
        if anchor not in best_anchor_rank or clue_rank > best_anchor_rank[anchor]:
            best_anchor_rank[anchor] = clue_rank

    deduped_selected: List[Dict[str, Any]] = []
    for clue in selected:
        anchor = clue.get("anchor_key")
        clue_type = str(clue.get("type", ""))
        clue_rank = rank.get(clue_type, 0)
        if anchor is not None and best_anchor_rank.get(anchor, clue_rank) > clue_rank and clue_type in {"either_or", "negative"}:
            continue
        deduped_selected.append(clue)
    selected = deduped_selected

    random.shuffle(selected)

    return [c["text"] for c in selected]


def _derive_prefilled_answer_pairs(
    prefilled: Dict[str, str],
    entities: List[str],
    attributes: Dict[str, List[str]],
) -> set[str]:
    """
    Build canonical answer-pair keys implied by prefilled visible cells.
    """
    entity_to_attrs: Dict[str, Dict[str, str]] = {entity: {} for entity in entities}
    for key, value in prefilled.items():
        parts = key.split("::")
        if len(parts) != 3:
            continue
        _, entity, attribute = parts
        if entity not in entity_to_attrs:
            continue
        entity_to_attrs[entity][attribute] = value

    pair_keys: set[str] = set()
    attr_order = list(attributes.keys())
    for entity in entities:
        filled = entity_to_attrs.get(entity, {})
        for i, attr_a in enumerate(attr_order):
            for j in range(i + 1, len(attr_order)):
                attr_b = attr_order[j]
                if attr_a not in filled or attr_b not in filled:
                    continue
                left = f"{attr_a}={_value_label(attr_a, filled[attr_a])}"
                right = f"{attr_b}={_value_label(attr_b, filled[attr_b])}"
                pair_keys.add("|".join(sorted([left, right])))
    return pair_keys


def _build_prefilled_assignments(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
    difficulty: str,
) -> Dict[str, str]:
    """
    Prefill some solved cells before puzzle starts.
    Difficulty controls how much is pre-filled.
    """
    normalized = difficulty.lower().strip()
    all_pairs: List[tuple[str, str]] = []
    for entity in entities:
        for attribute in attributes:
            all_pairs.append((entity, attribute))

    random.shuffle(all_pairs)
    variable_count = len(attributes)
    explicit_targets = {
        "easy": {3: 4, 4: 5, 5: 7},
        "medium": {3: 2, 4: 3, 5: 4},
        # Keep hard sparse, but ensure at least one visible match in the worksheet.
        "hard": {3: 2, 4: 2, 5: 2},
    }
    target = explicit_targets.get(normalized, {}).get(variable_count)
    if target is None:
        fill_ratio_by_difficulty = {"easy": 0.45, "medium": 0.25, "hard": 0.10}
        ratio = fill_ratio_by_difficulty.get(normalized, 0.25)
        target = int(len(all_pairs) * ratio + 0.5)
        target = max(1 if normalized != "hard" else 0, target)

    return _build_prefilled_assignments_with_visible_matches(
        entities=entities,
        attributes=attributes,
        solution=solution,
        target=target,
    )


def _build_prefilled_assignments_with_visible_matches(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
    target: int,
) -> Dict[str, str]:
    """
    Build prefilled guesses that create visible worksheet matches.

    Strategy:
    - Fill multiple attributes for one entity first (creates cross-variable ✓ marks).
    - Use remaining slots for random additional cells.
    """
    prefilled: Dict[str, str] = {}
    if target <= 0 or not entities or not attributes:
        return prefilled

    attr_keys = list(attributes.keys())
    anchor_entity = random.choice(entities)
    random.shuffle(attr_keys)
    anchor_fill_count = min(target, max(2, min(len(attr_keys), target)))

    for attribute in attr_keys[:anchor_fill_count]:
        value = solution.get(anchor_entity, {}).get(attribute)
        if value is None:
            continue
        prefilled[f"guess::{anchor_entity}::{attribute}"] = value

    if len(prefilled) >= target:
        return dict(list(prefilled.items())[:target])

    remaining_pairs: List[tuple[str, str]] = []
    for entity in entities:
        for attribute in attr_keys:
            key = f"guess::{entity}::{attribute}"
            if key in prefilled:
                continue
            remaining_pairs.append((entity, attribute))
    random.shuffle(remaining_pairs)

    for entity, attribute in remaining_pairs:
        if len(prefilled) >= target:
            break
        value = solution.get(entity, {}).get(attribute)
        if value is None:
            continue
        prefilled[f"guess::{entity}::{attribute}"] = value
    return prefilled


def _expected_prefill_count(variable_count: int, difficulty: str) -> int:
    """Single source of truth for target prefilled cells by size/difficulty."""
    explicit_targets = {
        "easy": {3: 4, 4: 5, 5: 7},
        "medium": {3: 2, 4: 3, 5: 4},
        "hard": {3: 1, 4: 1, 5: 2},
    }
    normalized = difficulty.lower().strip()
    target = explicit_targets.get(normalized, {}).get(variable_count)
    if target is not None:
        return target
    # Safe fallback for unexpected sizes.
    fallback_ratio = {"easy": 0.45, "medium": 0.25, "hard": 0.10}.get(normalized, 0.25)
    return max(0, int(variable_count * 3 * fallback_ratio + 0.5))


def _validate_or_rebuild_prefilled_assignments(
    entities: List[str],
    attributes: Dict[str, List[str]],
    solution: Dict[str, Dict[str, str]],
    difficulty: str,
    prefilled: Dict[str, str],
) -> Dict[str, str]:
    """
    Ensure prefilled count exactly matches policy before showing puzzle.
    Rebuilds deterministic-sized prefill set if mismatch occurs.
    """
    variable_count = len(attributes)
    expected = _expected_prefill_count(variable_count, difficulty)
    current = len(prefilled)
    if current == expected:
        return prefilled

    return _build_prefilled_assignments_with_visible_matches(
        entities=entities,
        attributes=attributes,
        solution=solution,
        target=expected,
    )


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
        white-space: nowrap;
        word-break: normal;
        overflow-wrap: normal;
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
        white-space: nowrap;
        word-break: normal;
        overflow-wrap: normal;
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
    variable_count = st.selectbox("Grid size (number of variables)", [3, 4, 5], index=0)
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"], index=0)
    # Keep symbolic internal names for solver compatibility.
    # The UI still renders natural-language labels via _human_name.
    use_real_names = False
    generate = st.button("Generate puzzle", type="primary")

current_config = {"variable_count": variable_count, "difficulty": difficulty}
last_config = st.session_state.get("last_generated_config")
config_changed = last_config != current_config

if generate or "puzzle_dict" not in st.session_state or config_changed:
    with st.spinner("Generating puzzle and hints…"):
        puzzle = generate_puzzle_fixed_value_count(
            variable_count=variable_count,
            value_count=3,
            difficulty=difficulty,
            use_real_names=use_real_names,
        )
        puzzle_dict = puzzle.to_dict()
        display_maps = _build_display_mappings(puzzle_dict)
        # Set mappings before hint generation so clue labels match current grid labels.
        st.session_state["display_maps"] = display_maps
        kb_text = module1_to_module2(puzzle_dict)
        prefilled = _build_prefilled_assignments(
            entities=puzzle_dict.get("entities", []),
            attributes=puzzle_dict.get("attributes", {}),
            solution=puzzle_dict.get("solution", {}),
            difficulty=difficulty,
        )
        prefilled = _validate_or_rebuild_prefilled_assignments(
            entities=puzzle_dict.get("entities", []),
            attributes=puzzle_dict.get("attributes", {}),
            solution=puzzle_dict.get("solution", {}),
            difficulty=difficulty,
            prefilled=prefilled,
        )
        excluded_answer_pairs = _derive_prefilled_answer_pairs(
            prefilled=prefilled,
            entities=puzzle_dict.get("entities", []),
            attributes=puzzle_dict.get("attributes", {}),
        )
        hints = _generate_solution_based_hints(
            entities=puzzle_dict.get("entities", []),
            attributes=puzzle_dict.get("attributes", {}),
            solution=puzzle_dict.get("solution", {}),
            difficulty=difficulty,
            excluded_answer_pairs=excluded_answer_pairs,
        )
        layout = build_logic_grid_layout(puzzle_dict.get("attributes", {}))
        st.session_state["puzzle_dict"] = puzzle_dict
        st.session_state["kb_text"] = kb_text
        st.session_state["hints"] = hints
        st.session_state["layout"] = layout
        st.session_state["last_generated_config"] = current_config
        # Reset player guesses when a new puzzle is generated.
        for entity in puzzle_dict.get("entities", []):
            for attribute in puzzle_dict.get("attributes", {}):
                key = f"guess::{entity}::{attribute}"
                st.session_state[key] = prefilled.get(key, "(blank)")
                st.session_state[f"reveal::{entity}::{attribute}"] = None
        st.session_state["puzzle_solved"] = False

puzzle_dict = st.session_state["puzzle_dict"]
kb_text = st.session_state["kb_text"]
hints = st.session_state["hints"]
layout = st.session_state["layout"]
entities = puzzle_dict["entities"]
attributes = puzzle_dict["attributes"]
prefilled_count = sum(
    1
    for entity in entities
    for attribute in attributes
    if st.session_state.get(f"guess::{entity}::{attribute}", "(blank)") != "(blank)"
)

st.subheader("Logic Worksheet")
st.caption(
    f"Variables: {len(attributes)} | Values per variable: 3 | Difficulty: {difficulty.capitalize()} | Prefilled cells: {prefilled_count}"
)
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

