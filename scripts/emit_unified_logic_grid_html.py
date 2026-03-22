"""Emit the *inner* HTML table for the unified logic grid (16×16 cells).

Paste into `examples/ORIGINAL_4x4_LOGIC_PUZZLES.md` inside the centered wrapper table
that provides side gutters (see existing **Blank logic grid** section).
"""
from __future__ import annotations

cats = [
    ("Name", ["Ava", "Ben", "Cleo", "Dana"]),
    ("Pet", ["Cat", "Dog", "Fish", "Bird"]),
    ("Drink", ["Tea", "Coffee", "Juice", "Water"]),
    ("Day off", ["Mon", "Tue", "Wed", "Thu"]),
]


def build_table_html() -> str:
    rows: list[tuple[int, int, str, str]] = []
    for ci, (cn, items) in enumerate(cats):
        for ii, it in enumerate(items):
            rows.append((ci, ii, it, cn))

    def col_cat(j: int) -> int:
        return j // 4

    def cell(rci: int, cci: int) -> str:
        # Same category: no cross-pairing (newspaper grids often leave blank or use a dash)
        if rci == cci:
            return "&#8212;"
        return "?"

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
    for _ri, (rci, r_item_idx, rlab, rcn) in enumerate(rows):
        lines.append("    <tr>")
        if r_item_idx == 0:
            lines.append(f'      <th scope="rowgroup" rowspan="4">{rcn}</th>')
        lines.append(f'      <th scope="row">{rlab}</th>')
        for ci in range(16):
            cci = col_cat(ci)
            lines.append(f'      <td align="center">{cell(rci, cci)}</td>')
        lines.append("    </tr>")
    lines.append("  </tbody>")
    lines.append("</table>")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")
    print(build_table_html(), end="\n")
