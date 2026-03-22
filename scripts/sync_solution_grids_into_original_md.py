"""Replace pipe-table ### Solution blocks in ORIGINAL_4x4_LOGIC_PUZZLES.md with unified HTML grids."""
from __future__ import annotations

from pathlib import Path

from emit_solution_grids_html import (
    PUZZLES,
    build_solution_table_html,
    worksheet_wrapper,
)

ROOT = Path(__file__).resolve().parents[1]
MD_PATH = ROOT / "examples" / "ORIGINAL_4x4_LOGIC_PUZZLES.md"

INTRO = """**Seats (1 = west … 4 = east):** Ava 1, Ben 2, Cleo 3, Dana 4.

**Legend:** **✓** = same person; **×** = ruled out; **—** = same category.

"""

OLD_EASY = """### Solution

| Name | Seat (1 = west) | Pet  | Drink   | Day off   |
|------|-----------------|------|---------|-----------|
| Ava  | 1               | Cat  | Tea     | Monday    |
| Ben  | 2               | Dog  | Coffee  | Tuesday   |
| Cleo | 3               | Fish | Juice   | Wednesday |
| Dana | 4               | Bird | Water   | Thursday  |

"""

OLD_MEDIUM = """### Solution

| Name | Seat | Pet  | Drink   | Day off   |
|------|------|------|---------|-----------|
| Ava  | 1    | Dog  | Juice   | Thursday  |
| Ben  | 2    | Fish | Water   | Monday    |
| Cleo | 3    | Bird | Tea     | Tuesday   |
| Dana | 4    | Cat  | Coffee  | Wednesday |

"""

OLD_HARD = """### Solution

| Name | Seat | Pet  | Drink   | Day off   |
|------|------|------|---------|-----------|
| Ava  | 1    | Fish | Coffee  | Thursday  |
| Ben  | 2    | Bird | Juice   | Monday    |
| Cleo | 3    | Cat  | Water   | Tuesday   |
| Dana | 4    | Dog  | Tea     | Wednesday |

"""


def fragment(key: str) -> str:
    inner = build_solution_table_html(PUZZLES[key])
    return "### Solution\n\n" + INTRO + "\n" + worksheet_wrapper(inner)


def main() -> None:
    text = MD_PATH.read_text(encoding="utf-8")
    for old, key in (
        (OLD_EASY, "easy"),
        (OLD_MEDIUM, "medium"),
        (OLD_HARD, "hard"),
    ):
        if old not in text:
            raise SystemExit(f"Expected block not found in {MD_PATH} for {key!r}")
        text = text.replace(old, fragment(key), 1)
    MD_PATH.write_text(text, encoding="utf-8")
    print(f"Updated {MD_PATH}")


if __name__ == "__main__":
    main()
