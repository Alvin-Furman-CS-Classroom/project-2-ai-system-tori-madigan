"""
HTML / Markdown visualization for puzzle solution grids.

- **HTML:** full page with shared CSS (default: ``grid_visualizations.html``).
- **Markdown:** embedded inline-styled tables (default: ``grid_visualizations_generated.md``)
  so you do not overwrite the hand-crafted ``grid_visualizations.md``.

To change colors and borders, edit :class:`GridTableTheme` in
``src/grid_visualization_table.py``.
"""

from __future__ import annotations

import argparse
import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from grid_visualization_table import (  # noqa: E402
    DEFAULT_THEME,
    GridTableTheme,
    build_markdown_document,
    create_html_grid_classic,
    create_solution_table_inline_html,
)
from module1_puzzle_generator import generate_puzzle  # noqa: E402


def _create_html_page_multi(
    by_size: dict[int, dict[str, object]],
    grid_sizes: list[int],
) -> str:
    """Full HTML page with one section per grid size (each with easy/medium/hard)."""
    blocks: list[str] = []
    for gs in grid_sizes:
        blocks.append(
            f'<h1 class="size-heading">Grid size {gs}</h1>'
        )
        for difficulty in ["easy", "medium", "hard"]:
            p = by_size[gs][difficulty]
            blocks.append(create_html_grid_classic(p, difficulty))

    inner = "\n".join(blocks)
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Grid Visualizations</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1.page-title {{
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }}
        h1.size-heading {{
            text-align: center;
            color: #1565C0;
            margin: 36px 0 16px;
            font-size: 1.5rem;
        }}
        .puzzle-grid {{
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .puzzle-grid h2 {{
            color: #2196F3;
            margin-top: 0;
            text-align: center;
        }}
        .info {{
            text-align: center;
            color: #666;
            margin-bottom: 15px;
            font-size: 14px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 0 auto;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            font-weight: bold;
            text-align: center;
        }}
        th.entity-label {{
            background-color: #2196F3;
            color: white;
            width: 80px;
        }}
        td {{
            padding: 12px;
            text-align: center;
            font-weight: bold;
            border: 1px solid #ddd;
        }}
        tr:nth-child(even) td {{
            background-color: #f9f9f9;
        }}
    </style>
</head>
<body>
    <h1 class="page-title">Puzzle Grid Visualizations</h1>
    {inner}
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate puzzle grids as HTML and/or Markdown (entity × attribute tables)."
    )
    p.add_argument(
        "--format",
        choices=("html", "markdown", "both"),
        default="html",
        help="Output format (default: html).",
    )
    p.add_argument(
        "--grid-size",
        type=int,
        action="append",
        dest="grid_sizes",
        metavar="N",
        help="Grid size (repeat for multiple). Default: 5.",
    )
    p.add_argument(
        "--output-html",
        default="grid_visualizations.html",
        help="Path for HTML output when format is html or both.",
    )
    p.add_argument(
        "--output-markdown",
        default="grid_visualizations_generated.md",
        help="Path for Markdown output when format is markdown or both.",
    )
    p.add_argument(
        "--real-names",
        action="store_true",
        help="Use readable entity/attribute/value labels from the generator.",
    )
    p.add_argument(
        "--theme-preview",
        action="store_true",
        help="Print current DEFAULT_THEME field values and exit.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.theme_preview:
        t = DEFAULT_THEME
        print("GridTableTheme (edit in src/grid_visualization_table.py):")
        for field in GridTableTheme.__dataclass_fields__:
            print(f"  {field}: {getattr(t, field)!r}")
        return

    grid_sizes = args.grid_sizes if args.grid_sizes else [5]
    use_real = args.real_names

    difficulties = ["easy", "medium", "hard"]
    md_sections: list[tuple[int, str, str]] = []
    # grid_size -> difficulty -> puzzle (generate once per combo)
    by_size: dict[int, dict[str, object]] = {}

    for grid_size in grid_sizes:
        print(f"\n=== Grid size {grid_size} ===")
        by_size[grid_size] = {}
        for difficulty in difficulties:
            print(f"  Generating {difficulty}...")
            puzzle = generate_puzzle(grid_size, difficulty, use_real_names=use_real)
            by_size[grid_size][difficulty] = puzzle
            print(f"    Constraints: {len(puzzle.constraints)}")

            if args.format in ("markdown", "both"):
                frag = create_solution_table_inline_html(
                    puzzle,
                    difficulty=difficulty,
                    grid_size=grid_size,
                    theme=DEFAULT_THEME,
                )
                md_sections.append((grid_size, difficulty, frag))

    if args.format in ("html", "both"):
        if len(grid_sizes) > 1:
            print(
                "\nNote: HTML output includes easy/medium/hard for each grid size "
                "in one scrollable page."
            )
        html_content = _create_html_page_multi(by_size, grid_sizes)
        with open(args.output_html, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"\nHTML written to: {args.output_html}")

    if args.format in ("markdown", "both"):
        intro = [
            f"**Generator:** `visualize_grids_html.py`",
            f"**Real names:** {use_real}",
            f"**Grid sizes:** {', '.join(str(g) for g in grid_sizes)}",
        ]
        doc = build_markdown_document(sections=md_sections, intro_lines=intro)
        with open(args.output_markdown, "w", encoding="utf-8") as f:
            f.write(doc)
        print(f"Markdown written to: {args.output_markdown}")

    if args.format == "html":
        print(f"\nOpen {args.output_html} in your browser to view the grids.")


if __name__ == "__main__":
    main()
