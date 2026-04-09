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
