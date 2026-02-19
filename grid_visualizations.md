# Puzzle Grid Visualizations - All Difficulty Levels

## Grid Size Overview

The puzzle generator supports different grid sizes (minimum 3x3). Grid size affects puzzle complexity:

- **3x3 Grid**: 3 entities × 3 attributes = 9 cells total. Simple puzzles, ideal for beginners.
- **4x4 Grid**: 4 entities × 4 attributes = 16 cells total. Moderate complexity, good for intermediate solvers.
- **5x5 Grid**: 5 entities × 5 attributes = 25 cells total. Standard size, suitable for all difficulty levels.
- **Larger Grids**: Can be generated for advanced puzzles (6x6, 7x7, etc.)

Constraint counts scale with grid size: Easy = grid_size × 1.5, Medium = grid_size × 2.5, Hard = grid_size × 3.5

---

## Different Grid Sizes

### 3x3 Grid Example (Easy Difficulty)

#### Initial Puzzle State
<p style="text-align: center; color: #666; margin-bottom: 15px; font-size: 14px;">Grid Size: 3x3 | Constraints: 5 | Initial Clues: 1</p>
<table style="width: 100%; border-collapse: collapse; margin: 0 auto; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th rowspan="2" style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="3" style="background-color: #FFD700; color: #333; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FFD700;">Hair Color</th>
            <th colspan="3" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="3" style="background-color: #4ECDC4; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4;">Pet</th>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Bird</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Cat</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Dog</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th rowspan="3" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
        </tr>
        <tr>
            <th rowspan="3" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
        </tr>
        <tr>
            <th rowspan="3" style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4; writing-mode: vertical-rl; text-orientation: mixed;">Pet</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Dog</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Cat</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Bird</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Clues:</strong> Alice has Blonde hair (Blonde hair is paired with Age 25 and Pet Dog).</p>

#### Constraints (5 total)
<p style="text-align: left; color: #666; margin: 15px 0; font-size: 13px;">The puzzle is solved using the following 5 constraints:</p>
<ol style="color: #333; font-size: 13px; line-height: 1.8; padding-left: 20px;">
    <li><strong>Equality:</strong> Alice has Blonde hair.</li>
    <li><strong>Inequality:</strong> Bob does NOT have Blonde hair.</li>
    <li><strong>Different Values:</strong> Alice and Bob have different ages.</li>
    <li><strong>Different Values:</strong> Bob and Charlie have different pets.</li>
    <li><strong>Relative Position:</strong> Bob's age is 5 years more than Alice's age (Bob: 30, Alice: 25).</li>
</ol>

#### Complete Solution
<table style="width: 100%; border-collapse: collapse; margin: 20px auto 40px; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th rowspan="2" style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="3" style="background-color: #FFD700; color: #333; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FFD700;">Hair Color</th>
            <th colspan="3" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="3" style="background-color: #4ECDC4; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4;">Pet</th>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Bird</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Cat</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Dog</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th rowspan="3" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
        </tr>
        <tr>
            <th rowspan="3" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
        </tr>
        <tr>
            <th rowspan="3" style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4; writing-mode: vertical-rl; text-orientation: mixed;">Pet</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Dog</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Cat</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Bird</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td colspan="3" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>
<p style="text-align: left; color: #666; font-size: 12px; margin-top: 10px;"><em>Smaller grids (3x3) are simpler and faster to solve, making them ideal for beginners or quick puzzles.</em></p>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Solution Summary:</strong> Blonde hair ↔ Age 25 ↔ Dog | Brunette hair ↔ Age 30 ↔ Cat | Black hair ↔ Age 35 ↔ Bird</p>

---

### 4x4 Grid Example (Medium Difficulty)

#### Initial Puzzle State
<p style="text-align: center; color: #666; margin-bottom: 15px; font-size: 14px;">Grid Size: 4x4 | Constraints: 10 | Initial Clues: 2</p>
<table style="width: 100%; border-collapse: collapse; margin: 0 auto; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th rowspan="2" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="4" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="4" style="background-color: #9B59B6; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #9B59B6;">Favorite Food</th>
            <th colspan="4" style="background-color: #4ECDC4; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4;">Pet</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Pasta</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Sushi</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Burgers</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Pizza</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Fish</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Bird</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Dog</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Cat</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Red</th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Clues:</strong> Alice has a Cat (Cat is paired with Blonde hair, Age 25, and Pizza). Bob has Black hair.</p>

#### Constraints (10 total)
<p style="text-align: left; color: #666; margin: 15px 0; font-size: 13px;">The puzzle is solved using the following 10 constraints:</p>
<ol style="color: #333; font-size: 13px; line-height: 1.8; padding-left: 20px;">
    <li><strong>Equality:</strong> Alice has a Cat.</li>
    <li><strong>Equality:</strong> Bob has Black hair.</li>
    <li><strong>Inequality:</strong> Charlie does NOT have Red hair.</li>
    <li><strong>Inequality:</strong> Diana does NOT have Pizza as favorite food.</li>
    <li><strong>Inequality:</strong> Alice does NOT have Brunette hair.</li>
    <li><strong>Different Values:</strong> Alice and Bob have different hair colors.</li>
    <li><strong>Different Values:</strong> Bob and Charlie have different ages.</li>
    <li><strong>Different Values:</strong> Charlie and Diana have different favorite foods.</li>
    <li><strong>Different Values:</strong> Diana and Alice have different pets.</li>
    <li><strong>Relative Position:</strong> Bob's age is 5 years more than Diana's age (Bob: 30, Diana: 20).</li>
</ol>
<p style="text-align: left; color: #666; font-size: 12px; margin-top: 10px;"><em>Note: 4x4 grids have more constraints than 3x3 grids, requiring more inference steps but remaining manageable.</em></p>

#### Complete Solution
<table style="width: 100%; border-collapse: collapse; margin: 20px auto 40px; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th rowspan="2" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="4" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="4" style="background-color: #9B59B6; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #9B59B6;">Favorite Food</th>
            <th colspan="4" style="background-color: #4ECDC4; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4;">Pet</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Pasta</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Sushi</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Burgers</th>
            <th style="background-color: #9B59B6; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #9B59B6;">Pizza</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Fish</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Bird</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Dog</th>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Cat</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Red</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th rowspan="4" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E8DAEF; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;">✓</td>
            <td style="background-color: #D7BDE2; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #9B59B6;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #4ECDC4;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>
<p style="text-align: left; color: #666; font-size: 12px; margin-top: 10px;"><em>4x4 grids provide a good balance between complexity and solvability, suitable for intermediate puzzle solvers.</em></p>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Solution Summary:</strong> Blonde ↔ 25 ↔ Pizza ↔ Cat | Black ↔ 30 ↔ Burgers ↔ Dog | Brunette ↔ 35 ↔ Sushi ↔ Bird | Red ↔ 20 ↔ Pasta ↔ Fish</p>

---

## 5x5 Grid Examples - All Difficulty Levels

## EASY Difficulty (8 constraints)

### Initial Puzzle State (Given to User)
<p style="text-align: center; color: #666; margin-bottom: 15px; font-size: 14px;">Grid Size: 5x5 | Constraints: 8 | Initial Clues: 2</p>
<table style="width: 100%; border-collapse: collapse; margin: 0 auto; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th rowspan="2" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="5" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="5" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">40</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th colspan="5" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Red</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Gray</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">40</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Clues:</strong> Alice has Black hair. Eve has a Dog.</p>

### Constraints (8 total)
<p style="text-align: left; color: #666; margin: 15px 0; font-size: 13px;">The puzzle is solved using the following 8 constraints:</p>
<ol style="color: #333; font-size: 13px; line-height: 1.8; padding-left: 20px;">
    <li><strong>Equality:</strong> Alice has Black hair.</li>
    <li><strong>Equality:</strong> Eve has a Dog.</li>
    <li><strong>Inequality:</strong> Bob does NOT have Gray hair.</li>
    <li><strong>Inequality:</strong> Charlie does NOT have Pizza as favorite food.</li>
    <li><strong>Different Values:</strong> Alice and Bob have different ages.</li>
    <li><strong>Different Values:</strong> Bob and Charlie have different pets.</li>
    <li><strong>Different Values:</strong> Diana and Eve have different hobbies.</li>
    <li><strong>Relative Position:</strong> Bob's age is 20 years more than Diana's age (Bob: 40, Diana: 20).</li>
</ol>
<p style="text-align: left; color: #666; font-size: 12px; margin-top: 10px;"><em>Note: These constraints work together to uniquely determine the solution. The equality constraints provide direct clues, while inequality, different values, and relative position constraints eliminate possibilities and establish relationships.</em></p>

### Complete Solution
<table style="width: 100%; border-collapse: collapse; margin: 20px auto 40px; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th rowspan="2" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="5" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="5" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">40</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th colspan="5" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Red</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Gray</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">40</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>

---

## MEDIUM Difficulty (12 constraints)

### Initial Puzzle State (Given to User)
<p style="text-align: center; color: #666; margin-bottom: 15px; font-size: 14px;">Grid Size: 5x5 | Constraints: 12 | Initial Clues: 3</p>
<table style="width: 100%; border-collapse: collapse; margin: 0 auto; border: 2px solid #333;">
    <thead>
        <tr>
            <th rowspan="2" style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FFD700; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th rowspan="2" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="5" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="5" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">40</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th colspan="5" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Black</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Blonde</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Brunette</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Red</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Gray</th>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <td style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">40</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="5" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Clues:</strong> Alice has a Cat. Bob has Black hair. Diana is 20 years old. Eve's hobby is Photography.</p>

### Constraints (12 total)
<p style="text-align: left; color: #666; margin: 15px 0; font-size: 13px;">The puzzle is solved using the following 12 constraints:</p>
<ol style="color: #333; font-size: 13px; line-height: 1.8; padding-left: 20px;">
    <li><strong>Equality:</strong> Alice has a Cat.</li>
    <li><strong>Equality:</strong> Bob has Black hair.</li>
    <li><strong>Equality:</strong> Diana is 20 years old.</li>
    <li><strong>Equality:</strong> Eve's hobby is Photography.</li>
    <li><strong>Inequality:</strong> Charlie does NOT have Red hair.</li>
    <li><strong>Inequality:</strong> Bob does NOT have Sushi as favorite food.</li>
    <li><strong>Inequality:</strong> Alice does NOT have Gardening as hobby.</li>
    <li><strong>Different Values:</strong> Alice and Bob have different hair colors.</li>
    <li><strong>Different Values:</strong> Bob and Charlie have different ages.</li>
    <li><strong>Different Values:</strong> Charlie and Diana have different pets.</li>
    <li><strong>Different Values:</strong> Diana and Eve have different favorite foods.</li>
    <li><strong>Relative Position:</strong> Alice's age is 20 years more than Diana's age (Alice: 40, Diana: 20).</li>
</ol>
<p style="text-align: left; color: #666; font-size: 12px; margin-top: 10px;"><em>Note: Medium difficulty puzzles have more constraints than easy puzzles, requiring more inference steps to solve.</em></p>

### Complete Solution
<table style="width: 100%; border-collapse: collapse; margin: 20px auto 40px;">
    <thead>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;"></th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Hair Color</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Age</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Favorite Food</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Pet</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Hobby</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Alice</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Brunette</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">40</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Pizza</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Cat</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Gaming</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Bob</th>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Black</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">25</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Burgers</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Bird</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Cooking</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Charlie</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Blonde</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">30</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Sushi</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Fish</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Reading</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Diana</th>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Red</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">20</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Pasta</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Dog</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Gardening</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Eve</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Gray</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">35</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Salad</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Hamster</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Photography</td>
        </tr>
    </tbody>
</table>

---

## HARD Difficulty (18 constraints)

### Initial Puzzle State (Given to User)
<p style="text-align: center; color: #666; margin-bottom: 15px; font-size: 14px;">Grid Size: 5x5 | Constraints: 18 | Initial Clues: 4</p>
<table style="width: 100%; border-collapse: collapse; margin: 0 auto;">
    <thead>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;"></th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Hair Color</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Age</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Favorite Food</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Pet</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Hobby</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Alice</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Black</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Bob</th>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Charlie</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Diana</th>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Pasta</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Eve</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">?</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Photography</td>
        </tr>
    </tbody>
</table>
<p style="text-align: center; color: #666; font-size: 12px; margin-top: 10px;"><strong>Clues:</strong> Alice has Black hair. Diana's favorite food is Pasta. Eve's hobby is Photography. Bob is 40 years old.</p>

### Constraints (18 total)
<p style="text-align: left; color: #666; margin: 15px 0; font-size: 13px;">The puzzle is solved using the following 18 constraints:</p>
<ol style="color: #333; font-size: 13px; line-height: 1.8; padding-left: 20px;">
    <li><strong>Equality:</strong> Alice has Black hair.</li>
    <li><strong>Equality:</strong> Diana's favorite food is Pasta.</li>
    <li><strong>Equality:</strong> Eve's hobby is Photography.</li>
    <li><strong>Equality:</strong> Bob is 40 years old.</li>
    <li><strong>Inequality:</strong> Bob does NOT have Gray hair.</li>
    <li><strong>Inequality:</strong> Charlie does NOT have Pizza as favorite food.</li>
    <li><strong>Inequality:</strong> Alice does NOT have Salad as favorite food.</li>
    <li><strong>Inequality:</strong> Diana does NOT have a Cat.</li>
    <li><strong>Inequality:</strong> Eve does NOT have Gaming as hobby.</li>
    <li><strong>Different Values:</strong> Alice and Bob have different hair colors.</li>
    <li><strong>Different Values:</strong> Bob and Charlie have different ages.</li>
    <li><strong>Different Values:</strong> Charlie and Diana have different favorite foods.</li>
    <li><strong>Different Values:</strong> Diana and Eve have different pets.</li>
    <li><strong>Different Values:</strong> Alice and Charlie have different hobbies.</li>
    <li><strong>Different Values:</strong> Bob and Diana have different pets.</li>
    <li><strong>Relative Position:</strong> Bob's age is 20 years more than Diana's age (Bob: 40, Diana: 20).</li>
    <li><strong>Relative Position:</strong> Charlie's age is 5 years more than Diana's age (Charlie: 25, Diana: 20).</li>
    <li><strong>Relative Position:</strong> Eve's age is 15 years more than Diana's age (Eve: 35, Diana: 20).</li>
</ol>
<p style="text-align: left; color: #666; font-size: 12px; margin-top: 10px;"><em>Note: Hard difficulty puzzles have the most constraints, including multiple relative position constraints that create complex relationships requiring careful inference.</em></p>

### Complete Solution
<table style="width: 100%; border-collapse: collapse; margin: 20px auto 40px;">
    <thead>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;"></th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Hair Color</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Age</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Favorite Food</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Pet</th>
            <th style="background-color: #4CAF50; color: white; padding: 12px; font-weight: bold; text-align: center;">Hobby</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Alice</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Black</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">30</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Pizza</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Cat</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Reading</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Bob</th>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Blonde</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">40</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Sushi</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Bird</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Gaming</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Charlie</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Brunette</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">25</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Burgers</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Fish</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Cooking</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Diana</th>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Red</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">20</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Pasta</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Dog</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Gardening</td>
        </tr>
        <tr>
            <th style="background-color: #2196F3; color: white; width: 80px; padding: 12px; font-weight: bold; text-align: center;">Eve</th>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Gray</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">35</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Salad</td>
            <td style="background-color: #BBDEFB; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Hamster</td>
            <td style="background-color: #E3F2FD; padding: 12px; text-align: center; font-weight: bold; border: 1px solid #ddd;">Photography</td>
        </tr>
    </tbody>
</table>

---

## L-Shaped Grid Format (Classic Logic Puzzle Layout)

The L-shaped grid format displays pairwise relationships between three categories, creating an intuitive visualization for solving logic puzzles. This format shows multiple relationship grids in a single table, making it easier to track connections between categories.

### Example: Names, Hair Color, and Age

#### Initial Puzzle State
<p style="text-align: center; color: #666; margin-bottom: 15px; font-size: 14px;">Three Categories: Names, Hair Color, Age | Grid Size: 4x4 | Constraints: 6</p>

<table style="width: 100%; border-collapse: collapse; margin: 0 auto; border: 2px solid #333;">
    <thead>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="4" style="background-color: #FFD700; color: #333; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FFD700;">Names</th>
            <th colspan="4" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th rowspan="4" style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Diana</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Charlie</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Bob</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Alice</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Blonde</th>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Brunette</th>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Red</th>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Black</th>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th rowspan="4" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">?</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>

<p style="text-align: center; color: #666; font-size: 12px; margin-top: 15px;">
<strong>Grid Legend:</strong><br>
<span style="border: 3px solid #FFD700; padding: 2px 8px; margin: 0 5px;">Yellow border</span> = Names vs Hair Color relationships<br>
<span style="border: 3px solid #FF6B6B; padding: 2px 8px; margin: 0 5px;">Red border</span> = Names vs Age relationships<br>
<span style="border: 3px solid #4ECDC4; padding: 2px 8px; margin: 0 5px;">Teal border</span> = Hair Color vs Age relationships (in Age rows)<br>
<strong>Clue:</strong> Alice has Blonde hair (marked with ✓)
</p>

#### Complete Solution

<table style="width: 100%; border-collapse: collapse; margin: 20px auto; border: 2px solid #333;">
    <thead>
        <tr>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th colspan="4" style="background-color: #FFD700; color: #333; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FFD700;">Names</th>
            <th colspan="4" style="background-color: #FF6B6B; color: white; padding: 12px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B;">Age</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 12px; border: 1px solid #ddd;"></th>
        </tr>
        <tr>
            <th rowspan="4" style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #4ECDC4; writing-mode: vertical-rl; text-orientation: mixed;">Hair Color</th>
            <th style="background-color: #f0f0f0; padding: 8px; border: 1px solid #ccc;"></th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Diana</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Charlie</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Bob</th>
            <th style="background-color: #FFD700; color: #333; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FFD700;">Alice</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <th colspan="4" style="background-color: #f9f9f9; padding: 8px; border: 1px solid #ddd;"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Blonde</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Brunette</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Red</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #4ECDC4; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #4ECDC4;">Black</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;"></td>
            <td style="background-color: #FFE5E5; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FF6B6B;">✓</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th rowspan="4" style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 3px solid #FF6B6B; writing-mode: vertical-rl; text-orientation: mixed;">Age</th>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">20</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">25</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">30</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
        <tr>
            <th style="background-color: #FF6B6B; color: white; padding: 8px; font-weight: bold; text-align: center; border: 2px solid #FF6B6B;">35</th>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td style="background-color: #E3F2FD; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;">✓</td>
            <td style="background-color: #BBDEFB; padding: 10px; text-align: center; font-weight: bold; border: 2px solid #FFD700;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
            <td colspan="4" style="background-color: #f9f9f9; padding: 10px; border: 1px solid #ddd;"></td>
        </tr>
    </tbody>
</table>

<p style="text-align: center; color: #666; font-size: 12px; margin-top: 15px;">
<strong>Solution Summary:</strong><br>
Alice: Blonde hair, Age 25 | Bob: Brunette hair, Age 30 | Charlie: Black hair, Age 35 | Diana: Red hair, Age 20
</p>

#### Constraints (6 total)
<p style="text-align: left; color: #666; margin: 15px 0; font-size: 13px;">The puzzle is solved using the following 6 constraints:</p>
<ol style="color: #333; font-size: 13px; line-height: 1.8; padding-left: 20px;">
    <li><strong>Equality:</strong> Alice has Blonde hair.</li>
    <li><strong>Different Values:</strong> Alice and Bob have different hair colors.</li>
    <li><strong>Different Values:</strong> Bob and Charlie have different ages.</li>
    <li><strong>Different Values:</strong> Charlie and Diana have different hair colors.</li>
    <li><strong>Relative Position:</strong> Bob's age is 5 years more than Alice's age.</li>
    <li><strong>Relative Position:</strong> Charlie's age is 5 years more than Bob's age.</li>
</ol>

<p style="text-align: left; color: #666; font-size: 12px; margin-top: 15px;">
<strong>How to read L-shaped grids:</strong><br>
- Each sub-grid shows relationships between two categories<br>
- Mark ✓ where a relationship exists (e.g., Alice has Blonde hair)<br>
- The L-shape comes from having one category as rows and two categories as columns<br>
- This format makes it easier to see all pairwise relationships at once<br>
- The diagonal section (Age vs Age) is not used since categories don't relate to themselves
</p>

<p style="text-align: center; color: #999; font-size: 12px; margin-top: 30px;"><em>Note: These are sample visualizations. Actual puzzles are generated dynamically with varying initial clues based on equality constraints.</em></p>
