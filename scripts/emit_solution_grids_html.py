"""Build filled solution grids (newspaper stair layout — same as blank grid)."""
from __future__ import annotations

from newspaper_logic_grid import build_newspaper_table_html, solution_cell

DAY_ABBR = {
    "Monday": "Mon",
    "Tuesday": "Tue",
    "Wednesday": "Wed",
    "Thursday": "Thu",
}

PUZZLES = {
    "easy": [
        ("Ava", "Cat", "Tea", "Monday"),
        ("Ben", "Dog", "Coffee", "Tuesday"),
        ("Cleo", "Fish", "Juice", "Wednesday"),
        ("Dana", "Bird", "Water", "Thursday"),
    ],
    "medium": [
        ("Ava", "Dog", "Juice", "Thursday"),
        ("Ben", "Fish", "Water", "Monday"),
        ("Cleo", "Bird", "Tea", "Tuesday"),
        ("Dana", "Cat", "Coffee", "Wednesday"),
    ],
    "hard": [
        ("Ava", "Fish", "Coffee", "Thursday"),
        ("Ben", "Bird", "Juice", "Monday"),
        ("Cleo", "Cat", "Water", "Tuesday"),
        ("Dana", "Dog", "Tea", "Wednesday"),
    ],
}


def _owners(rows: list[tuple[str, str, str, str]]) -> dict[str, int]:
    owners: dict[str, int] = {}
    for i, (n, p, d, dy) in enumerate(rows):
        dy_key = DAY_ABBR.get(dy, dy)
        for label in (n, p, d, dy_key):
            owners[label] = i
    return owners


def build_solution_table_html(rows: list[tuple[str, str, str, str]]) -> str:
    return build_newspaper_table_html(solution_cell(_owners(rows)))


def worksheet_wrapper(inner_table: str) -> str:
    gutter = "&#160;" * 26
    return f"""<div align="center">

<table>
<tbody>
<tr>
<td valign="top">{gutter}</td>
<td valign="top">

{inner_table}

</td>
<td valign="top">{gutter}</td>
</tr>
</tbody>
</table>

</div>
"""


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")
    for key in ("easy", "medium", "hard"):
        print(f"### {key.upper()} ###\n")
        print(worksheet_wrapper(build_solution_table_html(PUZZLES[key])))
        print()
