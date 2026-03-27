"""Replace the four inner logic-grid <table> blocks in ORIGINAL_4x4_LOGIC_PUZZLES.md."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from emit_solution_grids_html import (  # noqa: E402
    PUZZLES,
    build_solution_table_html,
)
from emit_unified_logic_grid_html import build_table_html  # noqa: E402

MD_PATH = ROOT / "examples" / "ORIGINAL_4x4_LOGIC_PUZZLES.md"

INNER_TABLE_RE = re.compile(
    r'<table border="1" cellpadding="\d+" cellspacing="0"[^>]*>\s*'
    r"<thead>.*?</thead>\s*<tbody>.*?</tbody>\s*</table>",
    re.DOTALL,
)


def main() -> None:
    text = MD_PATH.read_text(encoding="utf-8")
    matches = list(INNER_TABLE_RE.finditer(text))
    if len(matches) != 4:
        raise SystemExit(
            f"Expected 4 inner logic-grid tables in {MD_PATH}, found {len(matches)}"
        )
    replacements = [
        build_table_html(),
        build_solution_table_html(PUZZLES["easy"]),
        build_solution_table_html(PUZZLES["medium"]),
        build_solution_table_html(PUZZLES["hard"]),
    ]
    for m, rep in sorted(zip(matches, replacements), key=lambda x: x[0].start(), reverse=True):
        text = text[: m.start()] + rep + text[m.end() :]
    MD_PATH.write_text(text, encoding="utf-8")
    print(f"Updated {MD_PATH}")


if __name__ == "__main__":
    main()
