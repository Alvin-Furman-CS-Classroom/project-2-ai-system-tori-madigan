"""Update blank + solution logic grids in ``ORIGINAL_4x4_LOGIC_PUZZLES.md``.

Earlier versions replaced pipe-table solutions with HTML. Grids now use the
newspaper stair layout; this entry point delegates to the refresh script.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from refresh_newspaper_grids_in_original_md import main  # noqa: E402

if __name__ == "__main__":
    main()
