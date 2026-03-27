"""Newspaper / puzzle-book logic grid: stair-step layout, each category pair once.

Four categories ordered Name < Pet < Drink < Day. Only blocks where row_category index
< column_category index are shown (Name×Pet, Name×Drink, Name×Day, Pet×Drink, Pet×Day,
Drink×Day). Mirrored blocks (e.g. Pet×Name) are omitted; padding cells use a neutral fill.

All bands share one HTML table with aligned columns so borders meet as one diagram.
"""
from __future__ import annotations

from collections.abc import Callable

# Order fixes which pairs appear (upper triangle in category space).
CATS: list[tuple[str, list[str]]] = [
    ("Name", ["Ava", "Ben", "Cleo", "Dana"]),
    ("Pet", ["Cat", "Dog", "Fish", "Bird"]),
    ("Drink", ["Tea", "Coffee", "Juice", "Water"]),
    ("Day off", ["Mon", "Tue", "Wed", "Thu"]),
]

N = 4  # items per category
NUM_CATS = len(CATS)
# Row bands: Name, Pet, Drink only (each pairs with strictly later categories).
NUM_ROW_BANDS = NUM_CATS - 1

TABLE_OPEN = (
    '<table border="1" cellpadding="10" cellspacing="0" '
    'style="border-collapse:collapse;border:2px solid #222;">'
)

def _pad_td(band_sep: str) -> str:
    return (
        '<td align="center" '
        f'style="background-color:#e8e8e8;border:1px solid #bbb;color:#aaa;{band_sep}">'
        "&#8212;</td>"
    )


def build_newspaper_table_html(
    cell_value: Callable[[int, str, int, str], str],
) -> str:
    """Build one inner <table>…</table> for the stair-step grid.

    ``cell_value(r_cat_idx, r_label, c_cat_idx, c_label)`` returns HTML cell *content*
    (entity or text), e.g. ``?``, ``&#10003;``, ``&#215;``.
    """
    lines: list[str] = []
    lines.append(TABLE_OPEN)
    lines.append("  <thead>")
    # Category band row — columns are only the "column" categories (Pet, Drink, Day).
    lines.append("    <tr>")
    lines.append('      <th colspan="2" scope="colgroup" style="border:1px solid #222;"></th>')
    for c_idx in range(1, NUM_CATS):
        cn, _items = CATS[c_idx]
        lines.append(
            f'      <th colspan="{N}" scope="colgroup" '
            f'style="border:1px solid #222;background:#f7f7f7;">{cn}</th>'
        )
    lines.append("    </tr>")
    # Item header row
    lines.append("    <tr>")
    lines.append(
        '      <th colspan="2" scope="col" '
        'style="border:1px solid #222;background:#fafafa;"> </th>'
    )
    for c_idx in range(1, NUM_CATS):
        for it in CATS[c_idx][1]:
            lines.append(
                f'      <th scope="col" style="border:1px solid #222;background:#fafafa;">{it}</th>'
            )
    lines.append("    </tr>")
    lines.append("  </thead>")
    lines.append("  <tbody>")

    for r_cat in range(NUM_ROW_BANDS):
        r_name, r_items = CATS[r_cat]
        for r_i, r_lab in enumerate(r_items):
            band_sep = "border-top:3px solid #222;" if r_i == 0 and r_cat > 0 else ""
            lines.append("    <tr>")
            if r_i == 0:
                rg_style = (
                    "border:1px solid #222;background:#f7f7f7;vertical-align:middle;"
                    + band_sep
                )
                lines.append(
                    f'      <th scope="rowgroup" rowspan="{N}" style="{rg_style}">{r_name}</th>'
                )
            lines.append(
                f'      <th scope="row" '
                f'style="border:1px solid #222;background:#fafafa;{band_sep}">{r_lab}</th>'
            )
            # Stair padding: column groups for categories not paired in this band.
            for _ in range(r_cat * N):
                lines.append(f"      {_pad_td(band_sep)}")
            for c_cat in range(r_cat + 1, NUM_CATS):
                for c_lab in CATS[c_cat][1]:
                    v = cell_value(r_cat, r_lab, c_cat, c_lab)
                    lines.append(
                        f'      <td align="center" '
                        f'style="border:1px solid #222;min-width:1.75em;{band_sep}">{v}</td>'
                    )
            lines.append("    </tr>")

    lines.append("  </tbody>")
    lines.append("</table>")
    return "\n".join(lines)


def blank_cell(_r: int, _rl: str, _c: int, _cl: str) -> str:
    return "?"


def solution_cell(
    owners: dict[str, int],
) -> Callable[[int, str, int, str], str]:
    def inner(r_cat: int, r_lab: str, c_cat: int, c_lab: str) -> str:
        if owners[r_lab] == owners[c_lab]:
            return "&#10003;"
        return "&#215;"

    return inner
