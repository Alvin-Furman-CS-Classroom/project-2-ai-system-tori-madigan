"""
Module 2: Logic Representation

Converts puzzle constraints from Module 1 into propositional logic knowledge bases.
Creates logical formulas using standard connectives (∧, ∨, ¬, →, ↔).
"""

import json
from typing import Dict, List, Any


def generate_proposition_symbol(entity: str, attribute: str, value: str) -> str:
    """
    Generate a proposition symbol for an entity-attribute-value assignment.
    
    Format: E{entity}_A{attribute}_V{value}
    Example: E1_A1_V2 means "Entity E1 has value V2 for attribute A1"
    """
    return f"{entity}_{attribute}_{value}"


def constraint_to_formula(constraint: Dict[str, Any], attributes: Dict[str, List[str]]) -> str:
    """
    Convert a constraint object to a propositional logic formula.
    
    Args:
        constraint: Constraint dictionary from Module 1
        attributes: Dictionary mapping attribute names to their possible values
    
    Returns:
        Logical formula string using connectives (∧, ∨, ¬, →, ↔)
    """
    constraint_type = constraint["type"]
    attribute = constraint["attribute"]
    values = attributes[attribute]
    
    if constraint_type == "equality":
        entity = constraint["entity"]
        value = constraint["value"]
        return generate_proposition_symbol(entity, attribute, value)
    
    elif constraint_type == "inequality":
        entity = constraint["entity"]
        value = constraint["value"]
        prop = generate_proposition_symbol(entity, attribute, value)
        return f"¬{prop}"
    
    elif constraint_type == "different_values":
        entities = constraint["entities"]
        e1, e2 = entities[0], entities[1]
        # For each value, ensure they don't both have it (not biconditional)
        formulas = []
        for value in values:
            prop1 = generate_proposition_symbol(e1, attribute, value)
            prop2 = generate_proposition_symbol(e2, attribute, value)
            formulas.append(f"¬({prop1} ↔ {prop2})")
        return " ∧ ".join(formulas)
    
    elif constraint_type == "same_value":
        entities = constraint["entities"]
        e1, e2 = entities[0], entities[1]
        # At least one value where both have it (biconditional)
        formulas = []
        for value in values:
            prop1 = generate_proposition_symbol(e1, attribute, value)
            prop2 = generate_proposition_symbol(e2, attribute, value)
            formulas.append(f"({prop1} ↔ {prop2})")
        return " ∨ ".join(formulas)
    
    elif constraint_type == "relative_position":
        entity1 = constraint.get("entity1") or constraint.get("entity")
        entity2 = constraint["entity2"]
        offset = constraint["offset"]
        
        # Generate pairs where entity1's value is offset more than entity2's
        formulas = []
        for i, value2 in enumerate(values):
            value1_index = i + offset
            if 0 <= value1_index < len(values):
                value1 = values[value1_index]
                prop1 = generate_proposition_symbol(entity1, attribute, value1)
                prop2 = generate_proposition_symbol(entity2, attribute, value2)
                formulas.append(f"({prop1} ∧ {prop2})")
        
        if not formulas:
            # Invalid offset, return contradiction
            return "⊥"
        
        return " ∨ ".join(formulas)
    
    else:
        raise ValueError(f"Unknown constraint type: {constraint_type}")


def generate_implicit_constraints(entities: List[str], attributes: Dict[str, List[str]]) -> List[str]:
    """
    Generate implicit domain constraints.
    
    For each entity-attribute pair:
    - At least one value must be true: (E_A_V1 ∨ E_A_V2 ∨ ... ∨ E_A_Vn)
    - At most one value is true: ¬(E_A_Vi ∧ E_A_Vj) for all i != j
    
    Returns list of constraint formulas.
    """
    constraints = []
    
    for entity in entities:
        for attribute, values in attributes.items():
            # At least one value
            props = [generate_proposition_symbol(entity, attribute, v) for v in values]
            at_least_one = "(" + " ∨ ".join(props) + ")"
            
            # At most one value (no two values can both be true)
            at_most_one_parts = []
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    prop_i = props[i]
                    prop_j = props[j]
                    at_most_one_parts.append(f"¬({prop_i} ∧ {prop_j})")
            
            if at_most_one_parts:
                at_most_one = " ∧ ".join(at_most_one_parts)
                # Combine: at least one AND at most one
                combined = f"{at_least_one} ∧ ({at_most_one})"
                constraints.append(combined)
            else:
                # Only one value possible, just use at_least_one
                constraints.append(at_least_one)
    
    return constraints


def create_knowledge_base(
    entities: List[str],
    attributes: Dict[str, List[str]],
    constraints: List[Dict[str, Any]]
) -> str:
    """
    Create a knowledge base in text format from puzzle data.
    
    Args:
        entities: List of entity identifiers
        attributes: Dictionary mapping attribute names to possible values
        constraints: List of constraint dictionaries from Module 1
    
    Returns:
        Formatted text knowledge base with facts and rules
    """
    # Generate all possible proposition symbols (facts)
    facts = []
    for entity in entities:
        for attribute, values in attributes.items():
            for value in values:
                facts.append(generate_proposition_symbol(entity, attribute, value))
    
    # Generate implicit domain constraints
    implicit_constraints = generate_implicit_constraints(entities, attributes)
    
    # Convert puzzle constraints to formulas
    puzzle_constraint_formulas = []
    for i, constraint in enumerate(constraints, 1):
        formula = constraint_to_formula(constraint, attributes)
        puzzle_constraint_formulas.append(f"{i}. {formula}")
    
    # Assemble knowledge base
    kb_lines = [
        "=== KNOWLEDGE BASE ===",
        "",
        "FACTS (All possible propositions):",
        ", ".join(facts),
        "",
        "RULES (Domain Constraints):"
    ]
    
    # Add implicit constraints
    for i, constraint in enumerate(implicit_constraints, 1):
        kb_lines.append(f"{i}. {constraint}")
    
    # Add puzzle constraints
    if puzzle_constraint_formulas:
        kb_lines.append("")
        kb_lines.append("RULES (Puzzle Constraints):")
        kb_lines.extend(puzzle_constraint_formulas)
    
    return "\n".join(kb_lines)


def module1_to_module2(puzzle_json: str) -> str:
    """
    Main entry point: Convert Module 1 JSON output to Module 2 knowledge base.
    
    Args:
        puzzle_json: JSON string from Module 1 (or dict)
    
    Returns:
        Knowledge base as text string
    """
    if isinstance(puzzle_json, str):
        puzzle_data = json.loads(puzzle_json)
    else:
        puzzle_data = puzzle_json
    
    # Extract required fields (exclude solution)
    entities = puzzle_data["entities"]
    attributes = puzzle_data["attributes"]
    constraints = puzzle_data["constraints"]
    
    return create_knowledge_base(entities, attributes, constraints)


def main() -> None:
    """
    Command-line entry point for Module 2.
    Reads Module 1 JSON from stdin or file, outputs knowledge base to stdout.
    """
    import sys
    
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], 'r') as f:
            puzzle_json = f.read()
    else:
        # Read from stdin
        puzzle_json = sys.stdin.read()
    
    knowledge_base = module1_to_module2(puzzle_json)
    print(knowledge_base)


if __name__ == "__main__":
    main()
