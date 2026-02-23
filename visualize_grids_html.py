"""
HTML-based visualization script for puzzle grids at different difficulty levels.

This script generates puzzles for easy, medium, and hard difficulty levels
and creates HTML visualizations showing the solution grids.
"""

import sys
import os
import json

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from module1_puzzle_generator import generate_puzzle


def create_html_grid(puzzle, difficulty: str) -> str:
    """
    Create an HTML table visualization of the puzzle solution grid.
    
    Args:
        puzzle: Puzzle object with solution
        difficulty: Difficulty level string
        
    Returns:
        HTML string for the grid
    """
    entities = puzzle.entities
    attributes = list(puzzle.attributes.keys())
    solution = puzzle.solution
    constraint_count = len(puzzle.constraints)
    
    html = f"""
    <div class="puzzle-grid">
        <h2>{difficulty.upper()} Difficulty</h2>
        <p class="info">Grid Size: {len(entities)}x{len(attributes)} | Constraints: {constraint_count}</p>
        <table>
            <thead>
                <tr>
                    <th></th>
    """
    
    # Add attribute headers
    for attr in attributes:
        html += f'<th>{attr}</th>'
    html += "</tr></thead><tbody>"
    
    # Add rows
    colors = ['#E3F2FD', '#BBDEFB']
    for i, entity in enumerate(entities):
        html += f'<tr><th class="entity-label">{entity}</th>'
        for j, attr in enumerate(attributes):
            value = solution.get_value(entity, attr)
            bg_color = colors[(i+j) % 2]
            html += f'<td style="background-color: {bg_color}">{value if value else ""}</td>'
        html += '</tr>'
    
    html += """
            </tbody>
        </table>
    </div>
    """
    
    return html


def create_html_page(puzzles_dict: dict) -> str:
    """
    Create a complete HTML page with all three difficulty visualizations.
    
    Args:
        puzzles_dict: Dictionary mapping difficulty to puzzle object
        
    Returns:
        Complete HTML page as string
    """
    html_content = ""
    for difficulty in ['easy', 'medium', 'hard']:
        html_content += create_html_grid(puzzles_dict[difficulty], difficulty)
    
    html = f"""
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
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 30px;
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
    <h1>Puzzle Grid Visualizations - All Difficulty Levels</h1>
    {html_content}
</body>
</html>
    """
    
    return html


def main():
    """Generate puzzles and create HTML visualizations."""
    grid_size = 5
    
    print("Generating puzzles for each difficulty level...")
    puzzles = {}
    
    for difficulty in ['easy', 'medium', 'hard']:
        print(f"\nGenerating {difficulty} puzzle...")
        puzzle = generate_puzzle(grid_size, difficulty)
        puzzles[difficulty] = puzzle
        constraint_count = len(puzzle.constraints)
        print(f"  Generated puzzle with {constraint_count} constraints")
    
    # Create HTML visualization
    print("\nCreating HTML visualization...")
    html_content = create_html_page(puzzles)
    
    output_path = 'grid_visualizations.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\nHTML visualization created successfully!")
    print(f"  Saved to: {output_path}")
    print(f"\nOpen {output_path} in your web browser to view the grids.")


if __name__ == "__main__":
    main()
