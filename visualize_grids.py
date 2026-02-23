"""
Visualization script for puzzle grids at different difficulty levels.

This script generates puzzles for easy, medium, and hard difficulty levels
and creates visualizations showing the solution grids.
"""

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.table import Table
import numpy as np

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from module1_puzzle_generator import generate_puzzle


def create_grid_visualization(puzzle, difficulty: str, output_path: str):
    """
    Create a visualization of the puzzle solution grid.
    
    Args:
        puzzle: Puzzle object with solution
        difficulty: Difficulty level string
        output_path: Path to save the visualization
    """
    entities = puzzle.entities
    attributes = list(puzzle.attributes.keys())
    solution = puzzle.solution
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')
    
    # Prepare data for table
    grid_data = []
    for entity in entities:
        row = []
        for attr in attributes:
            value = solution.get_value(entity, attr)
            row.append(value if value else "")
        grid_data.append(row)
    
    # Create table
    table = ax.table(
        cellText=grid_data,
        rowLabels=entities,
        colLabels=attributes,
        cellLoc='center',
        loc='center',
        bbox=[0, 0, 1, 1]
    )
    
    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # Color header cells
    for i in range(len(attributes)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Color row labels
    for i in range(len(entities)):
        table[(i+1, -1)].set_facecolor('#2196F3')
        table[(i+1, -1)].set_text_props(weight='bold', color='white')
    
    # Color data cells with alternating pattern
    colors = ['#E3F2FD', '#BBDEFB']
    for i in range(len(entities)):
        for j in range(len(attributes)):
            table[(i+1, j)].set_facecolor(colors[(i+j) % 2])
            table[(i+1, j)].set_text_props(weight='bold')
    
    # Add title
    constraint_count = len(puzzle.constraints)
    title = f'Puzzle Grid - {difficulty.upper()} Difficulty\n'
    title += f'Grid Size: {len(entities)}x{len(attributes)} | Constraints: {constraint_count}'
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved visualization to {output_path}")


def create_comparison_visualization(puzzles_dict, output_path: str):
    """
    Create a side-by-side comparison of all three difficulty levels.
    
    Args:
        puzzles_dict: Dictionary mapping difficulty to puzzle object
        output_path: Path to save the visualization
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    difficulties = ['easy', 'medium', 'hard']
    
    for idx, difficulty in enumerate(difficulties):
        puzzle = puzzles_dict[difficulty]
        ax = axes[idx]
        ax.axis('tight')
        ax.axis('off')
        
        entities = puzzle.entities
        attributes = list(puzzle.attributes.keys())
        solution = puzzle.solution
        
        # Prepare data for table
        grid_data = []
        for entity in entities:
            row = []
            for attr in attributes:
                value = solution.get_value(entity, attr)
                row.append(value if value else "")
            grid_data.append(row)
        
        # Create table
        table = ax.table(
            cellText=grid_data,
            rowLabels=entities,
            colLabels=attributes,
            cellLoc='center',
            loc='center',
            bbox=[0, 0, 1, 1]
        )
        
        # Style the table
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1, 1.8)
        
        # Color header cells
        for i in range(len(attributes)):
            table[(0, i)].set_facecolor('#4CAF50')
            table[(0, i)].set_text_props(weight='bold', color='white', size=8)
        
        # Color row labels
        for i in range(len(entities)):
            table[(i+1, -1)].set_facecolor('#2196F3')
            table[(i+1, -1)].set_text_props(weight='bold', color='white', size=8)
        
        # Color data cells with alternating pattern
        colors = ['#E3F2FD', '#BBDEFB']
        for i in range(len(entities)):
            for j in range(len(attributes)):
                table[(i+1, j)].set_facecolor(colors[(i+j) % 2])
                table[(i+1, j)].set_text_props(weight='bold', size=8)
        
        # Add title
        constraint_count = len(puzzle.constraints)
        title = f'{difficulty.upper()}\n'
        title += f'{constraint_count} constraints'
        ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    
    plt.suptitle('Puzzle Grid Comparison - All Difficulty Levels', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved comparison visualization to {output_path}")


def main():
    """Generate puzzles and create visualizations."""
    grid_size = 5
    
    print("Generating puzzles for each difficulty level...")
    puzzles = {}
    
    for difficulty in ['easy', 'medium', 'hard']:
        print(f"\nGenerating {difficulty} puzzle...")
        puzzle = generate_puzzle(grid_size, difficulty)
        puzzles[difficulty] = puzzle
        constraint_count = len(puzzle.constraints)
        print(f"  Generated puzzle with {constraint_count} constraints")
    
    # Create individual visualizations
    print("\nCreating individual visualizations...")
    for difficulty in ['easy', 'medium', 'hard']:
        output_path = f'grid_visualization_{difficulty}.png'
        create_grid_visualization(puzzles[difficulty], difficulty, output_path)
    
    # Create comparison visualization
    print("\nCreating comparison visualization...")
    create_comparison_visualization(puzzles, 'grid_visualization_comparison.png')
    
    print("\n✓ All visualizations created successfully!")
    print("\nGenerated files:")
    print("  - grid_visualization_easy.png")
    print("  - grid_visualization_medium.png")
    print("  - grid_visualization_hard.png")
    print("  - grid_visualization_comparison.png")


if __name__ == "__main__":
    main()
