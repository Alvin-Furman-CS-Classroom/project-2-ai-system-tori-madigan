# Puzzle Grid Visualizations - Unified Worksheet Layout

<style>
  .lp-page {
    font-family: Arial, sans-serif;
    color: #111;
    line-height: 1.35;
  }

  .lp-note {
    margin: 6px 0 14px;
    font-size: 13px;
  }

  .lp-system {
    border: 1.6px solid #111;
    padding: 12px;
    margin: 14px 0 20px;
  }

  .lp-system-title {
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 10px;
  }

  .lp-system.solution {
    border-width: 2.4px;
  }

  .lp-grid-row {
    display: grid;
    grid-template-columns: repeat(3, minmax(220px, 1fr));
    gap: 12px;
    align-items: start;
  }

  .lp-mini-title {
    font-weight: 700;
    text-align: center;
    margin: 0 0 6px;
    font-size: 13px;
  }

  .lp-mini table {
    border-collapse: collapse;
    border: 1.2px solid #111;
    table-layout: fixed;
    width: 100%;
  }

  .lp-mini th,
  .lp-mini td {
    border: 1px solid #111;
    width: 36px;
    height: 36px;
    min-width: 36px;
    max-width: 36px;
    text-align: center;
    vertical-align: middle;
    padding: 0;
    font-size: 12px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .lp-mini th:first-child {
    width: 82px;
    min-width: 82px;
    max-width: 82px;
    padding: 0 4px;
    font-size: 11px;
    font-weight: 700;
  }

  .lp-head {
    font-weight: 700;
  }

  .lp-mark-x {
    font-weight: 400;
    font-size: 12px;
  }

  .lp-mark-check {
    font-weight: 800;
    font-size: 15px;
  }

  .lp-lshape {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    align-items: start;
  }

  .lp-lshape-empty {
    border: 1.2px dashed #777;
    min-height: 140px;
  }

  .lp-subtle {
    font-size: 12px;
    margin-top: 8px;
  }
</style>

<div class="lp-page">

## Grid Size Overview

The puzzle generator supports different grid sizes (minimum 3x3). Grid size affects puzzle complexity:

- **3x3 Grid**: 3 entities x 3 attributes = 9 cells total
- **4x4 Grid**: 4 entities x 4 attributes = 16 cells total
- **5x5 Grid**: 5 entities x 5 attributes = 25 cells total
- **Larger Grids**: 6x6+ for advanced puzzles

Constraint scaling:
- Easy = `grid_size x 1.5`
- Medium = `grid_size x 2.5`
- Hard = `grid_size x 3.5`

---

## Worksheet Style Rules

- Three pairwise grids are grouped as one puzzle system (`A×B`, `A×C`, `B×C`)
- All mini-grids share the same left alignment in a true 3-column row
- Fixed square cells and fixed label widths prevent stretching
- Headers are bold; all cell content is centered
- Symbols: blank, `✓`, `×`
- `✓` is visually stronger than `×`
- Solution systems use a slightly thicker outer border for quick recognition

---

## Different Grid Sizes

### 3x3 Grid Example (Easy Difficulty)

Grid Size: 3x3 | Constraints: 5 | Initial Clues: 1

#### Initial Puzzle State

<div class="lp-system">
  <div class="lp-system-title">3x3 Pairwise Grids (Hair, Age, Pet)</div>
  <div class="lp-grid-row">
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Age</div>
      <table>
        <tr><th class="lp-head">Hair/Age</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Blonde</th><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Pet</div>
      <table>
        <tr><th class="lp-head">Hair/Pet</th><th class="lp-head">Dog</th><th class="lp-head">Cat</th><th class="lp-head">Bird</th></tr>
        <tr><th class="lp-head">Blonde</th><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Pet x Age</div>
      <table>
        <tr><th class="lp-head">Pet/Age</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Dog</th><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Cat</th><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Bird</th><td></td><td></td><td></td></tr>
      </table>
    </div>
  </div>
</div>

Clue: Alice has Blonde hair (Blonde is paired with Age 25 and Pet Dog).

#### Constraints (5 total)

1. **Equality:** Alice has Blonde hair.
2. **Inequality:** Bob does NOT have Blonde hair.
3. **Different Values:** Alice and Bob have different ages.
4. **Different Values:** Bob and Charlie have different pets.
5. **Relative Position:** Bob's age is 5 years more than Alice's age (Bob 30, Alice 25).

#### Complete Solution

<div class="lp-system solution">
  <div class="lp-system-title">3x3 Pairwise Grids (Solved)</div>
  <div class="lp-grid-row">
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Age</div>
      <table>
        <tr><th class="lp-head">Hair/Age</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Pet</div>
      <table>
        <tr><th class="lp-head">Hair/Pet</th><th class="lp-head">Dog</th><th class="lp-head">Cat</th><th class="lp-head">Bird</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Pet x Age</div>
      <table>
        <tr><th class="lp-head">Pet/Age</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Dog</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Cat</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Bird</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
      </table>
    </div>
  </div>
</div>

Solution Summary: Blonde hair ↔ Age 25 ↔ Dog | Brunette hair ↔ Age 30 ↔ Cat | Black hair ↔ Age 35 ↔ Bird

---

### 4x4 Grid Example (Medium Difficulty)

Grid Size: 4x4 | Constraints: 10 | Initial Clues: 2

#### Initial Puzzle State

<div class="lp-system">
  <div class="lp-system-title">4x4 Pairwise Grids (Hair, Age, Food, Pet)</div>
  <div class="lp-grid-row">
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Age</div>
      <table>
        <tr><th class="lp-head">Hair/Age</th><th class="lp-head">20</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Blonde</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Red</th><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Food</div>
      <table>
        <tr><th class="lp-head">Hair/Food</th><th class="lp-head">Pas</th><th class="lp-head">Sus</th><th class="lp-head">Bur</th><th class="lp-head">Piz</th></tr>
        <tr><th class="lp-head">Blonde</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Red</th><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Pet</div>
      <table>
        <tr><th class="lp-head">Hair/Pet</th><th class="lp-head">Fish</th><th class="lp-head">Bird</th><th class="lp-head">Dog</th><th class="lp-head">Cat</th></tr>
        <tr><th class="lp-head">Blonde</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Red</th><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>
  </div>
</div>

#### Constraints (10 total)

1. **Equality:** Alice has a Cat.
2. **Equality:** Bob has Black hair.
3. **Inequality:** Charlie does NOT have Red hair.
4. **Inequality:** Diana does NOT have Pizza as favorite food.
5. **Inequality:** Alice does NOT have Brunette hair.
6. **Different Values:** Alice and Bob have different hair colors.
7. **Different Values:** Bob and Charlie have different ages.
8. **Different Values:** Charlie and Diana have different favorite foods.
9. **Different Values:** Diana and Alice have different pets.
10. **Relative Position:** Bob's age is 5 years more than Diana's age (Bob 30, Diana 20).

#### Complete Solution

<div class="lp-system solution">
  <div class="lp-system-title">4x4 Pairwise Grids (Solved)</div>
  <div class="lp-grid-row">
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Age</div>
      <table>
        <tr><th class="lp-head">Hair/Age</th><th class="lp-head">20</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Red</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Food</div>
      <table>
        <tr><th class="lp-head">Hair/Food</th><th class="lp-head">Pas</th><th class="lp-head">Sus</th><th class="lp-head">Bur</th><th class="lp-head">Piz</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Red</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Pet</div>
      <table>
        <tr><th class="lp-head">Hair/Pet</th><th class="lp-head">Fish</th><th class="lp-head">Bird</th><th class="lp-head">Dog</th><th class="lp-head">Cat</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Red</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
      </table>
    </div>
  </div>
</div>

Solution Summary: Blonde ↔ 25 ↔ Pizza ↔ Cat | Black ↔ 30 ↔ Burgers ↔ Dog | Brunette ↔ 35 ↔ Sushi ↔ Bird | Red ↔ 20 ↔ Pasta ↔ Fish

---

## 5x5 Grid Examples - All Difficulty Levels

### Easy Difficulty (8 constraints)

Uses the same unified 3-column pairwise system (`A×B`, `A×C`, `B×C`) with fixed-size square cells.

### Medium Difficulty (12 constraints)

Uses the same unified 3-column pairwise system with the same symbol hierarchy (`✓` emphasized over `×`).

### Hard Difficulty (18 constraints)

Uses the same unified 3-column pairwise system and solution border distinction.

---

## L-Shaped Grid Format (Classic Logic Puzzle Layout)

### Example: Names, Hair Color, and Age

#### Initial Puzzle State

<div class="lp-system">
  <div class="lp-system-title">L-Shape: Hair, Name, Age</div>
  <div class="lp-lshape">
    <div class="lp-lshape-empty"></div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Name</div>
      <table>
        <tr><th class="lp-head">Hair/Name</th><th class="lp-head">Ali</th><th class="lp-head">Bob</th><th class="lp-head">Cha</th><th class="lp-head">Dia</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-check">✓</td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Red</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Age</div>
      <table>
        <tr><th class="lp-head">Hair/Age</th><th class="lp-head">20</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Blonde</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Brunette</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Red</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">Black</th><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Age x Name</div>
      <table>
        <tr><th class="lp-head">Age/Name</th><th class="lp-head">Ali</th><th class="lp-head">Bob</th><th class="lp-head">Cha</th><th class="lp-head">Dia</th></tr>
        <tr><th class="lp-head">20</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">25</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">30</th><td></td><td></td><td></td><td></td></tr>
        <tr><th class="lp-head">35</th><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>
  </div>
</div>

#### Complete Solution

<div class="lp-system solution">
  <div class="lp-system-title">L-Shape: Solved</div>
  <div class="lp-lshape">
    <div class="lp-lshape-empty"></div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Name</div>
      <table>
        <tr><th class="lp-head">Hair/Name</th><th class="lp-head">Ali</th><th class="lp-head">Bob</th><th class="lp-head">Cha</th><th class="lp-head">Dia</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Red</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Hair x Age</div>
      <table>
        <tr><th class="lp-head">Hair/Age</th><th class="lp-head">20</th><th class="lp-head">25</th><th class="lp-head">30</th><th class="lp-head">35</th></tr>
        <tr><th class="lp-head">Blonde</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Brunette</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Red</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">Black</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
      </table>
    </div>
    <div class="lp-mini">
      <div class="lp-mini-title">Age x Name</div>
      <table>
        <tr><th class="lp-head">Age/Name</th><th class="lp-head">Ali</th><th class="lp-head">Bob</th><th class="lp-head">Cha</th><th class="lp-head">Dia</th></tr>
        <tr><th class="lp-head">20</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td></tr>
        <tr><th class="lp-head">25</th><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">30</th><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td></tr>
        <tr><th class="lp-head">35</th><td class="lp-mark-x">×</td><td class="lp-mark-x">×</td><td class="lp-mark-check">✓</td><td class="lp-mark-x">×</td></tr>
      </table>
    </div>
  </div>
</div>

#### Constraints (6 total)

1. **Equality:** Alice has Blonde hair.
2. **Different Values:** Alice and Bob have different hair colors.
3. **Different Values:** Bob and Charlie have different ages.
4. **Different Values:** Charlie and Diana have different hair colors.
5. **Relative Position:** Bob's age is 5 years more than Alice's age.
6. **Relative Position:** Charlie's age is 5 years more than Bob's age.

---

## Easy L-Shaped Example (3x3)

The same layout system applies with:
- **Author x Title**
- **Author x Cover**
- **Cover x Title**

All grids stay aligned, square, and print-friendly.

</div>
# Puzzle Grid Visualizations - Standardized Worksheet Layout

## Grid Size Overview

The puzzle generator supports different grid sizes (minimum 3x3). Grid size affects puzzle complexity:

- **3x3 Grid**: 3 entities x 3 attributes = 9 cells total
- **4x4 Grid**: 4 entities x 4 attributes = 16 cells total
- **5x5 Grid**: 5 entities x 5 attributes = 25 cells total
- **Larger Grids**: 6x6+ for advanced puzzles

Constraint scaling:
- Easy = `grid_size x 1.5`
- Medium = `grid_size x 2.5`
- Hard = `grid_size x 3.5`

---

## Worksheet Style Rules

- Two categories per grid only
- Square mini-grids with equal cell spacing
- Bold row/column labels
- Center-aligned grid entries
- Symbols only: blank, `✓`, `×`
- No merged cells, rowspans, or colspans
- Black-and-white printable style

---

## Different Grid Sizes

### 3x3 Grid Example (Easy Difficulty)

#### Initial Puzzle State

Grid Size: 3x3 | Constraints: 5 | Initial Clues: 1

<table>
  <tr>
    <td>
      <strong>Hair Color vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Age</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Blonde</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:30px;">
      <strong>Hair Color vs Pet</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Pet</b></th><th><b>Dog</b></th><th><b>Cat</b></th><th><b>Bird</b></th></tr>
        <tr><th><b>Blonde</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:60px;">
      <strong>Pet vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Pet / Age</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Dog</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Cat</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Bird</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
</table>

Clue: Alice has Blonde hair (Blonde is paired with Age 25 and Pet Dog).

#### Constraints (5 total)

1. **Equality:** Alice has Blonde hair.
2. **Inequality:** Bob does NOT have Blonde hair.
3. **Different Values:** Alice and Bob have different ages.
4. **Different Values:** Bob and Charlie have different pets.
5. **Relative Position:** Bob's age is 5 years more than Alice's age (Bob 30, Alice 25).

#### Complete Solution

<table>
  <tr>
    <td>
      <strong>Hair Color vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Age</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Blonde</b></th><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>✓</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:30px;">
      <strong>Hair Color vs Pet</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Pet</b></th><th><b>Dog</b></th><th><b>Cat</b></th><th><b>Bird</b></th></tr>
        <tr><th><b>Blonde</b></th><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>✓</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:60px;">
      <strong>Pet vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Pet / Age</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Dog</b></th><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Cat</b></th><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Bird</b></th><td>×</td><td>×</td><td>✓</td></tr>
      </table>
    </td>
  </tr>
</table>

Solution Summary: Blonde hair ↔ Age 25 ↔ Dog | Brunette hair ↔ Age 30 ↔ Cat | Black hair ↔ Age 35 ↔ Bird

---

### 4x4 Grid Example (Medium Difficulty)

#### Initial Puzzle State

Grid Size: 4x4 | Constraints: 10 | Initial Clues: 2

<table>
  <tr>
    <td>
      <strong>Hair Color vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Age</b></th><th><b>20</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Blonde</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Red</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:30px;">
      <strong>Hair Color vs Favorite Food</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Food</b></th><th><b>Pasta</b></th><th><b>Sushi</b></th><th><b>Burgers</b></th><th><b>Pizza</b></th></tr>
        <tr><th><b>Blonde</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Red</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:60px;">
      <strong>Hair Color vs Pet</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Pet</b></th><th><b>Fish</b></th><th><b>Bird</b></th><th><b>Dog</b></th><th><b>Cat</b></th></tr>
        <tr><th><b>Blonde</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Red</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
</table>

#### Constraints (10 total)

1. **Equality:** Alice has a Cat.
2. **Equality:** Bob has Black hair.
3. **Inequality:** Charlie does NOT have Red hair.
4. **Inequality:** Diana does NOT have Pizza as favorite food.
5. **Inequality:** Alice does NOT have Brunette hair.
6. **Different Values:** Alice and Bob have different hair colors.
7. **Different Values:** Bob and Charlie have different ages.
8. **Different Values:** Charlie and Diana have different favorite foods.
9. **Different Values:** Diana and Alice have different pets.
10. **Relative Position:** Bob's age is 5 years more than Diana's age (Bob 30, Diana 20).

#### Complete Solution

<table>
  <tr>
    <td>
      <strong>Hair Color vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Age</b></th><th><b>20</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Blonde</b></th><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Red</b></th><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:30px;">
      <strong>Hair Color vs Favorite Food</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Food</b></th><th><b>Pasta</b></th><th><b>Sushi</b></th><th><b>Burgers</b></th><th><b>Pizza</b></th></tr>
        <tr><th><b>Blonde</b></th><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Red</b></th><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:60px;">
      <strong>Hair Color vs Pet</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Pet</b></th><th><b>Fish</b></th><th><b>Bird</b></th><th><b>Dog</b></th><th><b>Cat</b></th></tr>
        <tr><th><b>Blonde</b></th><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Red</b></th><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
      </table>
    </td>
  </tr>
</table>

Solution Summary: Blonde ↔ 25 ↔ Pizza ↔ Cat | Black ↔ 30 ↔ Burgers ↔ Dog | Brunette ↔ 35 ↔ Sushi ↔ Bird | Red ↔ 20 ↔ Pasta ↔ Fish

---

## 5x5 Grid Examples - All Difficulty Levels

### Easy Difficulty (8 constraints)

Use the same mini-grid worksheet layout with three 5x5 pairwise grids per state:
- Category A vs Category B
- Category A vs Category C
- Category B vs Category C

### Medium Difficulty (12 constraints)

Use the same mini-grid worksheet layout with:
- equal-sized square cells
- centered values
- bold category headers
- blank / `✓` / `×` only

### Hard Difficulty (18 constraints)

Use the same mini-grid worksheet layout with:
- identical structure to easy/medium
- clean black-and-white printable format

---

## L-Shaped Grid Format (Classic Logic Puzzle Layout)

### Example: Names, Hair Color, and Age

#### Initial Puzzle State

<table>
  <tr>
    <td>
      <strong>Hair Color vs Name</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Name</b></th><th><b>Alice</b></th><th><b>Bob</b></th><th><b>Charlie</b></th><th><b>Diana</b></th></tr>
        <tr><th><b>Blonde</b></th><td>✓</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Red</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:30px;">
      <strong>Hair Color vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Age</b></th><th><b>20</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Blonde</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Brunette</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Red</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>Black</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:60px;">
      <strong>Age vs Name</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Age / Name</b></th><th><b>Alice</b></th><th><b>Bob</b></th><th><b>Charlie</b></th><th><b>Diana</b></th></tr>
        <tr><th><b>20</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>25</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>30</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><th><b>35</b></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </table>
    </td>
  </tr>
</table>

#### Complete Solution

<table>
  <tr>
    <td>
      <strong>Hair Color vs Name</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Name</b></th><th><b>Alice</b></th><th><b>Bob</b></th><th><b>Charlie</b></th><th><b>Diana</b></th></tr>
        <tr><th><b>Blonde</b></th><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Red</b></th><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:30px;">
      <strong>Hair Color vs Age</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Hair / Age</b></th><th><b>20</b></th><th><b>25</b></th><th><b>30</b></th><th><b>35</b></th></tr>
        <tr><th><b>Blonde</b></th><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>Brunette</b></th><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
        <tr><th><b>Red</b></th><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
        <tr><th><b>Black</b></th><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
      </table>
    </td>
  </tr>
  <tr><td>&nbsp;</td></tr>
  <tr>
    <td style="padding-left:60px;">
      <strong>Age vs Name</strong>
      <table border="1" cellspacing="0" cellpadding="6" style="border-collapse:collapse; text-align:center;">
        <tr><th><b>Age / Name</b></th><th><b>Alice</b></th><th><b>Bob</b></th><th><b>Charlie</b></th><th><b>Diana</b></th></tr>
        <tr><th><b>20</b></th><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
        <tr><th><b>25</b></th><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
        <tr><th><b>30</b></th><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
        <tr><th><b>35</b></th><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
      </table>
    </td>
  </tr>
</table>

#### Constraints (6 total)

1. **Equality:** Alice has Blonde hair.
2. **Different Values:** Alice and Bob have different hair colors.
3. **Different Values:** Bob and Charlie have different ages.
4. **Different Values:** Charlie and Diana have different hair colors.
5. **Relative Position:** Bob's age is 5 years more than Alice's age.
6. **Relative Position:** Charlie's age is 5 years more than Bob's age.

---

## Easy L-Shaped Example (3x3)

This section follows the same standardized worksheet style using:
- **Author vs Title**
- **Author vs Cover**
- **Cover vs Title**

All grids remain compact, centered, and print-friendly.
