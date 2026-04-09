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

#### Hair Color vs Age

| **Hair / Age** | **25** | **30** | **35** |
|---|---|---|---|
| **Blonde** |  |  |  |
| **Brunette** |  |  |  |
| **Black** |  |  |  |

#### Hair Color vs Pet

| **Hair / Pet** | **Dog** | **Cat** | **Bird** |
|---|---|---|---|
| **Blonde** |  |  |  |
| **Brunette** |  |  |  |
| **Black** |  |  |  |

#### Pet vs Age

| **Pet / Age** | **25** | **30** | **35** |
|---|---|---|---|
| **Dog** |  |  |  |
| **Cat** |  |  |  |
| **Bird** |  |  |  |

Clue: Alice has Blonde hair (Blonde is paired with Age 25 and Pet Dog).

#### Constraints (5 total)

1. **Equality:** Alice has Blonde hair.
2. **Inequality:** Bob does NOT have Blonde hair.
3. **Different Values:** Alice and Bob have different ages.
4. **Different Values:** Bob and Charlie have different pets.
5. **Relative Position:** Bob's age is 5 years more than Alice's age (Bob 30, Alice 25).

#### Complete Solution

#### Hair Color vs Age

| **Hair / Age** | **25** | **30** | **35** |
|---|---|---|---|
| **Blonde** | ✓ | × | × |
| **Brunette** | × | ✓ | × |
| **Black** | × | × | ✓ |

#### Hair Color vs Pet

| **Hair / Pet** | **Dog** | **Cat** | **Bird** |
|---|---|---|---|
| **Blonde** | ✓ | × | × |
| **Brunette** | × | ✓ | × |
| **Black** | × | × | ✓ |

#### Pet vs Age

| **Pet / Age** | **25** | **30** | **35** |
|---|---|---|---|
| **Dog** | ✓ | × | × |
| **Cat** | × | ✓ | × |
| **Bird** | × | × | ✓ |

Solution Summary: Blonde hair ↔ Age 25 ↔ Dog | Brunette hair ↔ Age 30 ↔ Cat | Black hair ↔ Age 35 ↔ Bird

---

### 4x4 Grid Example (Medium Difficulty)

#### Initial Puzzle State

Grid Size: 4x4 | Constraints: 10 | Initial Clues: 2

#### Hair Color vs Age

| **Hair / Age** | **20** | **25** | **30** | **35** |
|---|---|---|---|---|
| **Blonde** |  |  |  |  |
| **Brunette** |  |  |  |  |
| **Black** |  |  |  |  |
| **Red** |  |  |  |  |

#### Hair Color vs Favorite Food

| **Hair / Food** | **Pasta** | **Sushi** | **Burgers** | **Pizza** |
|---|---|---|---|---|
| **Blonde** |  |  |  |  |
| **Brunette** |  |  |  |  |
| **Black** |  |  |  |  |
| **Red** |  |  |  |  |

#### Hair Color vs Pet

| **Hair / Pet** | **Fish** | **Bird** | **Dog** | **Cat** |
|---|---|---|---|---|
| **Blonde** |  |  |  |  |
| **Brunette** |  |  |  |  |
| **Black** |  |  |  |  |
| **Red** |  |  |  |  |

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

#### Hair Color vs Age

| **Hair / Age** | **20** | **25** | **30** | **35** |
|---|---|---|---|---|
| **Blonde** | × | ✓ | × | × |
| **Brunette** | × | × | × | ✓ |
| **Black** | × | × | ✓ | × |
| **Red** | ✓ | × | × | × |

#### Hair Color vs Favorite Food

| **Hair / Food** | **Pasta** | **Sushi** | **Burgers** | **Pizza** |
|---|---|---|---|---|
| **Blonde** | × | × | × | ✓ |
| **Brunette** | × | ✓ | × | × |
| **Black** | × | × | ✓ | × |
| **Red** | ✓ | × | × | × |

#### Hair Color vs Pet

| **Hair / Pet** | **Fish** | **Bird** | **Dog** | **Cat** |
|---|---|---|---|---|
| **Blonde** | × | × | × | ✓ |
| **Brunette** | × | ✓ | × | × |
| **Black** | × | × | ✓ | × |
| **Red** | ✓ | × | × | × |

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

#### Hair Color vs Name

| **Hair / Name** | **Alice** | **Bob** | **Charlie** | **Diana** |
|---|---|---|---|---|
| **Blonde** | ✓ |  |  |  |
| **Brunette** |  |  |  |  |
| **Red** |  |  |  |  |
| **Black** |  |  |  |  |

#### Hair Color vs Age

| **Hair / Age** | **20** | **25** | **30** | **35** |
|---|---|---|---|---|
| **Blonde** |  |  |  |  |
| **Brunette** |  |  |  |  |
| **Red** |  |  |  |  |
| **Black** |  |  |  |  |

#### Age vs Name

| **Age / Name** | **Alice** | **Bob** | **Charlie** | **Diana** |
|---|---|---|---|---|
| **20** |  |  |  |  |
| **25** |  |  |  |  |
| **30** |  |  |  |  |
| **35** |  |  |  |  |

#### Complete Solution

#### Hair Color vs Name

| **Hair / Name** | **Alice** | **Bob** | **Charlie** | **Diana** |
|---|---|---|---|---|
| **Blonde** | ✓ | × | × | × |
| **Brunette** | × | ✓ | × | × |
| **Red** | × | × | × | ✓ |
| **Black** | × | × | ✓ | × |

#### Hair Color vs Age

| **Hair / Age** | **20** | **25** | **30** | **35** |
|---|---|---|---|---|
| **Blonde** | × | ✓ | × | × |
| **Brunette** | × | × | ✓ | × |
| **Red** | ✓ | × | × | × |
| **Black** | × | × | × | ✓ |

#### Age vs Name

| **Age / Name** | **Alice** | **Bob** | **Charlie** | **Diana** |
|---|---|---|---|---|
| **20** | × | × | × | ✓ |
| **25** | ✓ | × | × | × |
| **30** | × | ✓ | × | × |
| **35** | × | × | ✓ | × |

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
