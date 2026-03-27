"""Smoke tests for newspaper-style stair logic grids."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from emit_solution_grids_html import PUZZLES, build_solution_table_html  # noqa: E402
from newspaper_logic_grid import blank_cell, build_newspaper_table_html  # noqa: E402


def test_blank_grid_has_96_working_cells() -> None:
    html = build_newspaper_table_html(blank_cell)
    # Style may include optional `border-top:3px solid #222;` on band boundaries.
    assert len(re.findall(r'min-width:1\.75em[^"]*">\?</td>', html)) == 96


def test_blank_grid_shaded_padding_cell_count() -> None:
    html = build_newspaper_table_html(blank_cell)
    # Pet band: 4×4 + Drink band: 4×8
    assert html.count("background-color:#e8e8e8") == 48


@pytest.mark.parametrize("key", ["easy", "medium", "hard"])
def test_solution_grid_check_and_cross_counts(key: str) -> None:
    html = build_solution_table_html(PUZZLES[key])
    assert html.count("&#10003;") == 24
    assert html.count("&#215;") == 72
