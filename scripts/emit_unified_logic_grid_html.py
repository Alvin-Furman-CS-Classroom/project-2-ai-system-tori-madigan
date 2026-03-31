"""Emit the *inner* HTML table for the blank newspaper-style logic grid.

Stair-step layout: each category pair appears once (Name×Pet, Name×Drink, …, Drink×Day).
Paste into `examples/ORIGINAL_4x4_LOGIC_PUZZLES.md` inside the centered gutter wrapper, or run
`python scripts/refresh_newspaper_grids_in_original_md.py` to update that file.
"""
from __future__ import annotations

from newspaper_logic_grid import blank_cell, build_newspaper_table_html


def build_table_html() -> str:
    return build_newspaper_table_html(blank_cell)


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")
    print(build_table_html(), end="\n")
