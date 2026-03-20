"""
Module 3: Puzzle Solving

Takes the Module 2 knowledge base (text) and solves the puzzle using
constraint propagation (forward-chaining style) plus backtracking when needed.

Output format:
=== SOLUTION ===
E1: A1=V3, A2=V1, ...

=== PROOF ===
1. [deduction] ...
2. [decision] ...
...
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Set, Tuple


PropKey = Tuple[str, str]  # (entity, attribute)

FACTS_MARKER = "FACTS (All possible propositions):"
DOMAIN_RULES_MARKER = "RULES (Domain Constraints):"
PUZZLE_RULES_MARKER = "RULES (Puzzle Constraints):"

PROPOSITION_RE = re.compile(r"^E(?P<entity_num>\d+)_A(?P<attr_num>\d+)_V(?P<value_num>\d+)$")
PUNCTUATED_PROP_RE = re.compile(r"\bE\d+_A\d+_V\d+\b")


@dataclass(frozen=True)
class ParsedConstraint:
    type: str
    # equality / inequality
    entity: Optional[str] = None
    attribute: Optional[str] = None
    value: Optional[str] = None
    # same_value / different_values
    entity1: Optional[str] = None
    entity2: Optional[str] = None
    # relative_position
    offset: Optional[int] = None


def _value_index(value_symbol: str) -> int:
    # value_symbol like "V3"
    if not value_symbol.startswith("V"):
        raise ValueError(f"Unexpected value symbol: {value_symbol}")
    return int(value_symbol[1:])


def _extract_entities_attributes_values(knowledge_base: str) -> Tuple[List[str], Dict[str, List[str]]]:
    """
    Extract entity identifiers (E1..En) and attribute -> ordered values (A1 -> [V1..Vn])
    from Module 2's "FACTS" section.
    """
    try:
        facts_start = knowledge_base.index(FACTS_MARKER) + len(FACTS_MARKER)
        facts_end = knowledge_base.index(DOMAIN_RULES_MARKER)
    except ValueError as e:
        raise ValueError("Knowledge base missing required section markers.") from e

    facts_blob = knowledge_base[facts_start:facts_end]
    facts_symbols = [m.group(0) for m in PUNCTUATED_PROP_RE.finditer(facts_blob)]
    if not facts_symbols:
        raise ValueError("No proposition symbols found in FACTS section.")

    entities_nums: Dict[int, str] = {}
    attrs_nums: Dict[int, str] = {}
    values_by_attr_num: Dict[int, Set[int]] = {}

    for sym in set(facts_symbols):
        match = PROPOSITION_RE.match(sym.strip())
        if not match:
            continue
        entity_num = int(match.group("entity_num"))
        attr_num = int(match.group("attr_num"))
        value_num = int(match.group("value_num"))
        entities_nums[entity_num] = f"E{entity_num}"
        attrs_nums[attr_num] = f"A{attr_num}"
        values_by_attr_num.setdefault(attr_num, set()).add(value_num)

    entities = [entities_nums[i] for i in sorted(entities_nums)]
    attributes: Dict[str, List[str]] = {}
    for attr_num in sorted(attrs_nums):
        vals = sorted(values_by_attr_num.get(attr_num, set()))
        if not vals:
            raise ValueError(f"No values found for attribute {attrs_nums[attr_num]}")
        # Module 2 always uses contiguous V1..Vn; keep numeric ordering.
        attributes[attrs_nums[attr_num]] = [f"V{v}" for v in vals]

    return entities, attributes


def _extract_puzzle_rule_formulas(knowledge_base: str) -> List[str]:
    try:
        start = knowledge_base.index(PUZZLE_RULES_MARKER) + len(PUZZLE_RULES_MARKER)
    except ValueError as e:
        raise ValueError("Knowledge base missing RULES (Puzzle Constraints) marker.") from e

    rules_blob = knowledge_base[start:]
    formulas: List[str] = []
    for raw_line in rules_blob.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        m = re.match(r"^\d+\.\s*(.+)$", line)
        if not m:
            continue
        formulas.append(m.group(1).strip())
    if not formulas:
        raise ValueError("No puzzle constraint formulas found.")
    return formulas


def _parse_puzzle_constraint(formula: str) -> ParsedConstraint:
    """
    Parse Module 2 constraint_to_formula output back into a higher-level constraint.

    This relies on the fact that Module 2 generates constraints in a small set
    of patterns (equality, inequality, same_value, different_values, relative_position).
    """
    formula = formula.strip()
    if formula == "⊥":
        return ParsedConstraint(type="contradiction")

    # equality: "E1_A1_V3"
    if PROPOSITION_RE.match(formula):
        match = PROPOSITION_RE.match(formula)
        if match is None:
            raise ValueError(f"Could not parse equality constraint: {formula}")
        return ParsedConstraint(
            type="equality",
            entity=f"E{match.group('entity_num')}",
            attribute=f"A{match.group('attr_num')}",
            value=f"V{match.group('value_num')}",
        )

    # inequality: "¬E1_A1_V3"
    if formula.startswith("¬") and PROPOSITION_RE.match(formula[1:]):
        match = PROPOSITION_RE.match(formula[1:])
        if match is None:
            raise ValueError(f"Could not parse inequality constraint: {formula}")
        return ParsedConstraint(
            type="inequality",
            entity=f"E{match.group('entity_num')}",
            attribute=f"A{match.group('attr_num')}",
            value=f"V{match.group('value_num')}",
        )

    # different_values:
    #  ¬(E1_A1_V1 ↔ E2_A1_V1) ∧ ¬(E1_A1_V2 ↔ E2_A1_V2) ∧ ...
    if "↔" in formula and "¬(" in formula:
        dv_re = re.compile(
            r"¬\(\s*(E\d+)_(A\d+)_(V\d+)\s*↔\s*(E\d+)_\2_(V\d+)\s*\)"
        )
        m = dv_re.search(formula)
        if not m:
            raise ValueError(f"Could not parse different_values constraint: {formula}")
        entity1, attribute, _v1, entity2, _v2 = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        return ParsedConstraint(
            type="different_values",
            entity1=entity1,
            entity2=entity2,
            attribute=attribute,
        )

    # same_value:
    # (E1_A1_V1 ↔ E2_A1_V1) ∨ (E1_A1_V2 ↔ E2_A1_V2) ∨ ...
    # Note: for some edge offsets/dimensions, there may be only one disjunct
    # (no " ∨ " substring). So we just search for the first ↔-conjunction pattern.
    if "↔" in formula and "¬(" not in formula:
        sv_re = re.compile(
            r"\(\s*(E\d+)_(A\d+)_(V\d+)\s*↔\s*(E\d+)_\2_(V\d+)\s*\)"
        )
        m = sv_re.search(formula)
        if m:
            entity1, attribute, _v1, entity2, _v2 = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
            return ParsedConstraint(
                type="same_value",
                entity1=entity1,
                entity2=entity2,
                attribute=attribute,
            )

    # relative_position:
    # (E1_A1_V{k+offset} ∧ E2_A1_Vk) ∨ (E1_A1_V{k+1+offset} ∧ E2_A1_V{k+1}) ∨ ...
    # Note: can also be a single conjunction (no " ∨ " substring).
    if "↔" not in formula and "∧" in formula:
        rp_re = re.compile(
            r"\(\s*(E\d+)_(A\d+)_(V\d+)\s*∧\s*(E\d+)_\2_(V\d+)\s*\)"
        )
        m = rp_re.search(formula)
        if m:
            entity1, attribute, v1, entity2, v2 = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
            offset = _value_index(v1) - _value_index(v2)
            return ParsedConstraint(
                type="relative_position",
                entity1=entity1,
                entity2=entity2,
                attribute=attribute,
                offset=offset,
            )

    raise ValueError(f"Unrecognized constraint formula pattern: {formula}")


def _build_domains(entities: List[str], attributes: Dict[str, List[str]]) -> Dict[PropKey, Set[str]]:
    domains: Dict[PropKey, Set[str]] = {}
    for e in entities:
        for a, values in attributes.items():
            domains[(e, a)] = set(values)
    return domains


def _domains_to_assignment(domains: Dict[PropKey, Set[str]]) -> Dict[str, Dict[str, str]]:
    assignment: Dict[str, Dict[str, str]] = {}
    for (entity, attribute), dom in domains.items():
        if len(dom) != 1:
            raise ValueError(f"Cannot convert to assignment; {entity} {attribute} has domain {dom}")
        value = next(iter(dom))
        assignment.setdefault(entity, {})[attribute] = value
    # Ensure stable entity ordering in representation.
    return assignment


def _filter_same_value(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
) -> Tuple[bool, Optional[str]]:
    if c.type != "same_value":
        raise ValueError(f"Expected same_value, got {c.type}")
    if c.entity1 is None or c.entity2 is None or c.attribute is None:
        raise ValueError(f"Missing same_value fields in constraint: {c}")
    key1 = (c.entity1, c.attribute)
    key2 = (c.entity2, c.attribute)
    inter = domains[key1].intersection(domains[key2])
    changed = False
    reason = None
    if inter != domains[key1]:
        domains[key1] = inter
        changed = True
        reason = f"{key1} == {key2} => {c.attribute} in {sorted(inter)}"
    if inter != domains[key2]:
        domains[key2] = inter
        changed = True
        reason = reason or f"{key1} == {key2} => {c.attribute} in {sorted(inter)}"
    return changed, reason


def _filter_different_values(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
) -> Tuple[bool, Optional[str]]:
    if c.type != "different_values":
        raise ValueError(f"Expected different_values, got {c.type}")
    if c.entity1 is None or c.entity2 is None or c.attribute is None:
        raise ValueError(f"Missing different_values fields in constraint: {c}")
    key1 = (c.entity1, c.attribute)
    key2 = (c.entity2, c.attribute)
    domain1, domain2 = domains[key1], domains[key2]
    changed = False
    reason = None

    # Inequality propagation (domain filtering):
    # If one side is a singleton {v}, the other side cannot contain v.
    if len(domain1) == 1:
        v = next(iter(domain1))
        if v in domain2:
            new_domain2 = set(domain2)
            new_domain2.discard(v)
            if new_domain2 != domain2:
                domains[key2] = new_domain2
                changed = True
                reason = f"{key1} != {key2} => remove {v} from {key2}"
    if len(domain2) == 1:
        v = next(iter(domain2))
        if v in domain1:
            new_domain1 = set(domain1)
            new_domain1.discard(v)
            if new_domain1 != domain1:
                domains[key1] = new_domain1
                changed = True
                reason = reason or f"{key1} != {key2} => remove {v} from {key1}"

    return changed, reason


def _filter_relative_position(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
) -> Tuple[bool, Optional[str]]:
    if c.type != "relative_position":
        raise ValueError(f"Expected relative_position, got {c.type}")
    if c.entity1 is None or c.entity2 is None or c.attribute is None or c.offset is None:
        raise ValueError(f"Missing relative_position fields in constraint: {c}")
    key1 = (c.entity1, c.attribute)
    key2 = (c.entity2, c.attribute)
    domain1, domain2 = domains[key1], domains[key2]
    offset_value = c.offset

    # Generalized arc consistency:
    # Keep value1 only if there exists value2 in the other domain such that
    # idx(value1) == idx(value2) + offset.
    filtered_domain1: Set[str] = set()
    for v1 in domain1:
        need_idx2 = _value_index(v1) - offset_value
        v2_symbol = f"V{need_idx2}"
        if v2_symbol in domain2:
            filtered_domain1.add(v1)

    # Symmetrically filter value2 candidates.
    filtered_domain2: Set[str] = set()
    for v2 in domain2:
        need_idx1 = _value_index(v2) + offset_value
        v1_symbol = f"V{need_idx1}"
        if v1_symbol in domain1:
            filtered_domain2.add(v2)

    changed = (filtered_domain1 != domain1) or (filtered_domain2 != domain2)
    reason = None
    if changed:
        domains[key1] = filtered_domain1
        domains[key2] = filtered_domain2
        reason = f"{key1} is {offset_value:+d} from {key2}"
    return changed, reason


class _PropagationContradiction(Exception):
    """Raised when a constraint application makes at least one domain empty."""


def _apply_equality_constraint(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
    proof_steps: List[str],
):
    """Apply equality constraint: Entity/Attribute must be Value (singleton)."""
    if c.entity is None or c.attribute is None or c.value is None:
        raise ValueError(f"Missing equality fields in constraint: {c}")
    key = (c.entity, c.attribute)
    if c.value not in domains[key]:
        raise _PropagationContradiction()
    if domains[key] != {c.value}:
        domains[key] = {c.value}
        proof_steps.append(f"[deduction] {c.entity} {c.attribute} must be {c.value}")
        return True
    return False


def _apply_inequality_constraint(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
    proof_steps: List[str],
) -> bool:
    """Apply inequality constraint: Entity/Attribute cannot be a specific Value."""
    if c.entity is None or c.attribute is None or c.value is None:
        raise ValueError(f"Missing inequality fields in constraint: {c}")
    key = (c.entity, c.attribute)
    if c.value not in domains[key]:
        return False
    new_dom = set(domains[key])
    new_dom.discard(c.value)
    if not new_dom:
        raise _PropagationContradiction()
    if new_dom != domains[key]:
        domains[key] = new_dom
        if len(new_dom) == 1:
            proof_steps.append(f"[deduction] {c.entity} {c.attribute} becomes {next(iter(new_dom))}")
        return True
    return False


def _apply_same_value_constraint(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
    proof_steps: List[str],
) -> bool:
    """Apply same_value constraint: both Entity/Attribute pairs share a value."""
    if c.entity1 is None or c.entity2 is None or c.attribute is None:
        raise ValueError(f"Missing same_value fields in constraint: {c}")
    key1 = (c.entity1, c.attribute)
    key2 = (c.entity2, c.attribute)
    before1 = set(domains[key1])
    before2 = set(domains[key2])

    changed, _ = _filter_same_value(domains, c)
    if not changed:
        return False

    if not domains[key1] or not domains[key2]:
        raise _PropagationContradiction()

    after1 = domains[key1]
    after2 = domains[key2]
    if len(after1) == 1 and before1 != after1:
        proof_steps.append(
            f"[deduction] {c.entity1} {c.attribute} == {c.entity2} {c.attribute} => {next(iter(after1))}"
        )
    elif len(after2) == 1 and before2 != after2:
        proof_steps.append(
            f"[deduction] {c.entity2} {c.attribute} == {c.entity1} {c.attribute} => {next(iter(after2))}"
        )
    return True


def _apply_different_values_constraint(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
    proof_steps: List[str],
) -> bool:
    """Apply different_values constraint: the two Entity/Attribute domains differ."""
    if c.entity1 is None or c.entity2 is None or c.attribute is None:
        raise ValueError(f"Missing different_values fields in constraint: {c}")
    key1 = (c.entity1, c.attribute)
    key2 = (c.entity2, c.attribute)

    domain1 = domains[key1]
    domain2 = domains[key2]
    changed = False

    # Forward propagation: if one side is singleton, remove that value from the other.
    if len(domain1) == 1:
        v = next(iter(domain1))
        if v in domain2:
            new_dom2 = set(domain2)
            new_dom2.discard(v)
            if not new_dom2:
                raise _PropagationContradiction()
            domains[key2] = new_dom2
            changed = True
            if len(new_dom2) == 1:
                proof_steps.append(f"[deduction] {c.entity2} {c.attribute} becomes {next(iter(new_dom2))}")

    domain1 = domains[key1]
    domain2 = domains[key2]
    if len(domain2) == 1:
        v = next(iter(domain2))
        if v in domain1:
            new_dom1 = set(domain1)
            new_dom1.discard(v)
            if not new_dom1:
                raise _PropagationContradiction()
            domains[key1] = new_dom1
            changed = True
            if len(new_dom1) == 1:
                proof_steps.append(f"[deduction] {c.entity1} {c.attribute} becomes {next(iter(new_dom1))}")

    return changed


def _apply_relative_position_constraint(
    domains: Dict[PropKey, Set[str]],
    c: ParsedConstraint,
    proof_steps: List[str],
) -> bool:
    """Apply relative_position constraint: idx(e1) == idx(e2) + offset."""
    if c.entity1 is None or c.entity2 is None or c.attribute is None or c.offset is None:
        raise ValueError(f"Missing relative_position fields in constraint: {c}")
    key1 = (c.entity1, c.attribute)
    key2 = (c.entity2, c.attribute)
    before1 = set(domains[key1])
    before2 = set(domains[key2])

    changed, _ = _filter_relative_position(domains, c)
    if not changed:
        return False
    if not domains[key1] or not domains[key2]:
        raise _PropagationContradiction()

    after1 = domains[key1]
    after2 = domains[key2]
    if len(after1) == 1 and before1 != after1:
        proof_steps.append(f"[deduction] offset relation => {c.entity1} {c.attribute} is {next(iter(after1))}")
    if len(after2) == 1 and before2 != after2:
        proof_steps.append(f"[deduction] offset relation => {c.entity2} {c.attribute} is {next(iter(after2))}")

    return True


_ConstraintHandler = Callable[
    [Dict[PropKey, Set[str]], ParsedConstraint, List[str]],
    bool,
]

_APPLY_CONSTRAINT_BY_TYPE: Dict[str, _ConstraintHandler] = {
    "equality": _apply_equality_constraint,
    "inequality": _apply_inequality_constraint,
    "same_value": _apply_same_value_constraint,
    "different_values": _apply_different_values_constraint,
    "relative_position": _apply_relative_position_constraint,
}


def _propagate_constraints(
    domains: Dict[PropKey, Set[str]],
    constraints: List[ParsedConstraint],
    proof_steps: List[str],
) -> bool:
    """
    Forward-chaining-style propagation: iteratively reduce domains using constraints.
    Returns True if consistent, False if contradiction found.
    """
    while True:
        changed_any = False
        for c in constraints:
            if c.type == "contradiction":
                return False
            handler = _APPLY_CONSTRAINT_BY_TYPE.get(c.type)
            if handler is None:
                raise ValueError(f"Unknown constraint type: {c.type}")
            try:
                changed = handler(domains, c, proof_steps)
            except _PropagationContradiction:
                return False
            changed_any = changed_any or changed

        if not changed_any:
            break

    return all(dom for dom in domains.values())


def _solve_with_backtracking(
    domains: Dict[PropKey, Set[str]],
    constraints: List[ParsedConstraint],
    proof_steps: List[str],
    depth: int = 0,
) -> Optional[Dict[str, Dict[str, str]]]:
    # Unit propagation / forward chaining first.
    if not _propagate_constraints(domains, constraints, proof_steps):
        return None

    # Check if solved.
    all_singletons = all(len(dom) == 1 for dom in domains.values())
    if all_singletons:
        return _domains_to_assignment(domains)

    # Choose next variable to branch on (MRV heuristic).
    unassigned = [(k, dom) for k, dom in domains.items() if len(dom) > 1]
    if not unassigned:
        return None
    key_min, domain_min = min(unassigned, key=lambda item: len(item[1]))

    # Branch in a deterministic order to keep proofs stable.
    branch_values = sorted(domain_min, key=lambda v: _value_index(v))
    for v in branch_values:
        # Copy domains (small sizes, so deep copy is fine).
        new_domains = {k: set(d) for k, d in domains.items()}
        new_proof_steps = list(proof_steps)
        new_domains[key_min] = {v}
        new_proof_steps.append(f"[decision] set {key_min[0]} {key_min[1]} = {v}")

        result = _solve_with_backtracking(
            new_domains,
            constraints,
            new_proof_steps,
            depth=depth + 1,
        )
        if result is not None:
            # If solved, carry the proof chosen on that branch.
            proof_steps[:] = new_proof_steps
            return result

    return None


def module2_to_module3(knowledge_base: str) -> str:
    """
    Main entry point.
    Input: Module 2 knowledge base (text)
    Output: text with solution + proof steps
    """
    entities, attributes = _extract_entities_attributes_values(knowledge_base)
    formulas = _extract_puzzle_rule_formulas(knowledge_base)
    constraints = [_parse_puzzle_constraint(f) for f in formulas]

    domains = _build_domains(entities, attributes)
    proof_steps: List[str] = []

    assignment = _solve_with_backtracking(
        domains=domains,
        constraints=constraints,
        proof_steps=proof_steps,
    )
    if assignment is None:
        raise ValueError("No satisfying assignment found for this knowledge base.")

    # Build a stable, readable solution block.
    lines_solution: List[str] = []
    attrs_sorted = sorted(attributes.keys(), key=lambda a: int(a[1:]))
    entities_sorted = sorted(entities, key=lambda e: int(e[1:]))
    for e in entities_sorted:
        parts = []
        for a in attrs_sorted:
            parts.append(f"{a}={assignment[e][a]}")
        lines_solution.append(f"{e}: " + ", ".join(parts))

    lines_proof: List[str] = []
    lines_proof.append("=== PROOF ===")
    for i, step in enumerate(proof_steps, start=1):
        lines_proof.append(f"{i}. {step}")

    inference_step_count = len(proof_steps)
    proof_meta = f"INFERENCE STEP COUNT: {inference_step_count}"

    out = "\n".join(
        [
            "=== SOLUTION ===",
            *lines_solution,
            "",
            *[proof_meta],
            *lines_proof,
        ]
    )
    return out


def main() -> None:
    """
    CLI entry point:
    Reads Module 2 knowledge base from stdin or from a file path passed as argv[1].
    Prints Module 3 output to stdout.
    """
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            kb_text = f.read()
    else:
        kb_text = sys.stdin.read()

    print(module2_to_module3(kb_text))


if __name__ == "__main__":
    main()

