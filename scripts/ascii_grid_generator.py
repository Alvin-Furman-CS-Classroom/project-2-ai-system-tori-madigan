"""Generate GitHub-friendly ASCII logic grids from variable/value input."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Variable:
    """Represents one variable group in the logic grid."""

    name: str
    values: List[str]


def _validate_variables(variables: List[Variable]) -> None:
    if not 2 <= len(variables) <= 6:
        raise ValueError("Expected 2-6 variables.")

    for variable in variables:
        if not variable.name.strip():
            raise ValueError("Variable names must be non-empty.")
        if not 2 <= len(variable.values) <= 8:
            raise ValueError(
                f"Variable '{variable.name}' must contain 2-8 values."
            )
        if any(not str(value).strip() for value in variable.values):
            raise ValueError(
                f"Variable '{variable.name}' contains an empty value."
            )


def _resolve_columns(
    variable_map: Dict[str, Variable],
    variables: List[Variable],
    column_order: Optional[List[str]],
) -> List[Variable]:
    if column_order:
        missing = [name for name in column_order if name not in variable_map]
        if missing:
            raise ValueError(f"Unknown columns in column_order: {missing}")
        return [variable_map[name] for name in column_order]

    # Default pattern from spec: A, then backwards through remaining.
    # For names [A,B,C,D] -> [A,D,C,B]
    if len(variables) == 2:
        return [variables[0], variables[1]]
    return [variables[0]] + list(reversed(variables[1:]))


def _resolve_rows(
    variable_map: Dict[str, Variable],
    variables: List[Variable],
    row_order: Optional[List[str]],
) -> List[Variable]:
    if row_order:
        missing = [name for name in row_order if name not in variable_map]
        if missing:
            raise ValueError(f"Unknown rows in row_order: {missing}")
        return [variable_map[name] for name in row_order]

    # Default pattern from spec: last variable down to B (exclude A).
    # For [A,B,C,D] -> [D,C,B]
    return list(reversed(variables[1:]))


def _format_cell(text: str, width: int) -> str:
    return f"|{text:<{width}}"


def generate_ascii_grid(
    variables_input: List[Dict[str, List[str]]],
    column_order: Optional[List[str]] = None,
    row_order: Optional[List[str]] = None,
    unknown_symbol: str = ".",
) -> str:
    """Return a GitHub fenced code block containing the ASCII grid.

    Input format:
    [
      {"name": "A", "values": ["axe", "bow", "cup"]},
      {"name": "B", "values": ["red", "grn", "blu"]},
      ...
    ]
    """
    variables = [
        Variable(name=item["name"], values=[str(v) for v in item["values"]])
        for item in variables_input
    ]
    _validate_variables(variables)

    variable_map = {v.name: v for v in variables}
    columns = _resolve_columns(variable_map, variables, column_order)
    rows = _resolve_rows(variable_map, variables, row_order)

    # Width for each value cell (inner text area).
    value_width = max(3, max(len(value) for var in variables for value in var.values))

    # Width for row labels like "D east".
    label_candidates = [f"{row.name} {value}" for row in rows for value in row.values]
    label_width = max(10, max(len(text) for text in label_candidates))

    total_columns = sum(len(group.values) for group in columns)

    def separator() -> str:
        return "+" + "-" * label_width + "+" + "+".join(
            "-" * value_width for _ in range(total_columns)
        ) + "+"

    def row_prefix(text: str) -> str:
        return f"|{text:<{label_width}}"

    lines: List[str] = [separator()]

    # Header row 1: variable group labels.
    group_row = row_prefix("")
    for group in columns:
        for idx in range(len(group.values)):
            group_row += _format_cell(group.name if idx == 0 else "", value_width)
    group_row += "|"
    lines.append(group_row)
    lines.append(separator())

    # Header row 2: variable values.
    values_row = row_prefix("")
    for group in columns:
        for value in group.values:
            values_row += _format_cell(value, value_width)
    values_row += "|"
    lines.append(values_row)
    lines.append(separator())

    # Stair-step: each row block loses one column group from the right.
    for row_idx, row_var in enumerate(rows):
        active_groups = max(1, len(columns) - row_idx)

        for row_value in row_var.values:
            row_line = row_prefix(f"{row_var.name} {row_value}")

            for col_idx, col_var in enumerate(columns):
                is_active = col_idx < active_groups
                for _ in col_var.values:
                    if not is_active or col_var.name == row_var.name:
                        row_line += _format_cell("", value_width)
                    else:
                        row_line += _format_cell(unknown_symbol, value_width)

            row_line += "|"
            lines.append(row_line)

        lines.append(separator())

    return "```text\n" + "\n".join(lines) + "\n```"


def generate_module_style_markdown(
    variables_input: List[Dict[str, List[str]]],
    column_order: Optional[List[str]] = None,
    row_order: Optional[List[str]] = None,
    unknown_symbol: str = ".",
    title: str = "Grid Visualization",
) -> str:
    """Return markdown in the same style as module visualization docs."""
    grid_block = generate_ascii_grid(
        variables_input=variables_input,
        column_order=column_order,
        row_order=row_order,
        unknown_symbol=unknown_symbol,
    )

    variables_lines = []
    for item in variables_input:
        values = ", ".join(f"`{v}`" for v in item["values"])
        variables_lines.append(f"- **{item['name']}**: {values}")

    col_text = (
        ", ".join(f"`{name}`" for name in column_order)
        if column_order
        else "default rule (A, then reverse of the rest)"
    )
    row_text = (
        ", ".join(f"`{name}`" for name in row_order)
        if row_order
        else "default rule (last to B)"
    )

    return (
        f"## {title}\n\n"
        "### Inputs\n\n"
        + "\n".join(variables_lines)
        + "\n\n"
        f"- **Column order**: {col_text}\n"
        f"- **Row order**: {row_text}\n"
        f"- **Unknown symbol**: `{unknown_symbol}`\n\n"
        "### Output\n\n"
        + grid_block
        + "\n"
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an ASCII logic grid from JSON input."
    )
    parser.add_argument(
        "input_json",
        help="Path to JSON file containing variables, and optional row/column order.",
    )
    parser.add_argument(
        "--module-format",
        action="store_true",
        help="Emit markdown in module-visualization style.",
    )
    parser.add_argument(
        "--title",
        default="Grid Visualization",
        help="Section title used with --module-format.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    with open(args.input_json, "r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if args.module_format:
        output = generate_module_style_markdown(
            variables_input=payload["variables"],
            column_order=payload.get("column_order"),
            row_order=payload.get("row_order"),
            unknown_symbol=payload.get("unknown_symbol", "."),
            title=args.title,
        )
    else:
        output = generate_ascii_grid(
            variables_input=payload["variables"],
            column_order=payload.get("column_order"),
            row_order=payload.get("row_order"),
            unknown_symbol=payload.get("unknown_symbol", "."),
        )
    print(output)


if __name__ == "__main__":
    main()
