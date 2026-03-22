"""Build filled 16×16 solution grids (same layout as unified blank grid)."""
from __future__ import annotations

cats = [
    ("Name", ["Ava", "Ben", "Cleo", "Dana"]),
    ("Pet", ["Cat", "Dog", "Fish", "Bird"]),
    ("Drink", ["Tea", "Coffee", "Juice", "Water"]),
    ("Day off", ["Mon", "Tue", "Wed", "Thu"]),
]

DAY_ABBR = {
    "Monday": "Mon",
    "Tuesday": "Tue",
    "Wednesday": "Wed",
    "Thursday": "Thu",
}


def _flat_labels() -> list[str]:
    out: list[str] = []
    for _cn, items in cats:
        out.extend(items)
    return out


def _owners(rows: list[tuple[str, str, str, str]]) -> dict[str, int]:
    """Each row: (name, pet, drink, day) with day as Monday..Thursday or Mon..Thu."""
    owners: dict[str, int] = {}
    for i, (n, p, d, dy) in enumerate(rows):
        dy_key = DAY_ABBR.get(dy, dy)
        for label in (n, p, d, dy_key):
            owners[label] = i
    return owners


def build_solution_table_html(rows: list[tuple[str, str, str, str]]) -> str:
    flat = _flat_labels()
    owners = _owners(rows)

    def cell(ri: int, ci: int) -> str:
        r_cat, c_cat = ri // 4, ci // 4
        if r_cat == c_cat:
            return "&#8212;"
        rl, cl = flat[ri], flat[ci]
        if owners[rl] == owners[cl]:
            return "&#10003;"  # ✓
        return "&#215;"  # ×

    lines: list[str] = []
    lines.append('<table border="1" cellpadding="12" cellspacing="0">')
    lines.append("  <thead>")
    lines.append("    <tr>")
    lines.append('      <th colspan="2" scope="col"></th>')
    for cn, _items in cats:
        lines.append(f'      <th colspan="4" scope="colgroup">{cn}</th>')
    lines.append("    </tr>")
    lines.append("    <tr>")
    lines.append('      <th colspan="2" scope="col">row \\ col</th>')
    for _cn, items in cats:
        for it in items:
            lines.append(f'      <th scope="col">{it}</th>')
    lines.append("    </tr>")
    lines.append("  </thead>")
    lines.append("  <tbody>")
    for ri in range(16):
        r_cat, r_item_idx = divmod(ri, 4)
        rlab = flat[ri]
        rcn = cats[r_cat][0]
        lines.append("    <tr>")
        if r_item_idx == 0:
            lines.append(f'      <th scope="rowgroup" rowspan="4">{rcn}</th>')
        lines.append(f'      <th scope="row">{rlab}</th>')
        for ci in range(16):
            lines.append(f'      <td align="center">{cell(ri, ci)}</td>')
        lines.append("    </tr>")
    lines.append("  </tbody>")
    lines.append("</table>")
    return "\n".join(lines)


def worksheet_wrapper(inner_table: str) -> str:
    """Centered outer table with side gutters (no extra intro bands)."""
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


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")
    for key in ("easy", "medium", "hard"):
        print(f"### {key.upper()} ###\n")
        print(worksheet_wrapper(build_solution_table_html(PUZZLES[key])))
        print()
