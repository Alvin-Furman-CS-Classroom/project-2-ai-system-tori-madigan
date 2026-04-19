# Module Grid Examples (Generic Theme)

These examples use a consistent generic theme and are formatted for clean GitHub rendering.

## Variable Mapping and Required Order

- `A = Person`: Alex, Blair, Casey
- `B = Drink`: Tea, Juice, Water
- `C = Snack`: Muffin, Cookie, Fruit
- `D = Day`: Mon, Tue, Wed
- **Column order:** `A, B, C` (Person, Drink, Snack)
- **Row order:** `D, C, B` (Day, Snack, Drink)

Legend: blank = unknown, `✓` true match, `×` impossible.
Column separators are shown in headers with `┃` between variable groups.

---

## Module 1 - CSP Puzzle Generation

*Initial worksheet: candidate puzzle before logical translation.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>D Tue</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>D Wed</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Muffin</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

---

## Grid Size and Difficulty Examples

These examples follow your design scaling:

- **Easy:** `grid_size × 1.5` (rounded)
- **Medium:** `grid_size × 2.5` (rounded)
- **Hard:** `grid_size × 3.5` (rounded)

### Constraint Count Reference

| Grid Size | Easy | Medium | Hard |
|---|---:|---:|---:|
| 3x3 | 5 | 8 | 11 |
| 4x4 | 6 | 10 | 14 |
| 5x5 | 8 | 13 | 18 |

### Example A: 3 Variables (A, B, C) - Easy

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
  </tbody>
</table>

### Example B: 4 Variables (A, B, C, D) - Medium

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

### Example: 4×4 Medium — Pet type, Movie genre, Dream vacation, Hobby

*Grid size 4, difficulty **medium** (~10 constraints by `4 × 2.5` rounded). Variables: **A** = pet type, **B** = movie genre, **C** = dream vacation, **D** = hobby. Column order `A, B, C`; row order `D, C, B`.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="4">A = Pet type ┃</th>
      <th colspan="4">┃ B = Movie genre ┃</th>
      <th colspan="4">┃ C = Dream vacation</th>
    </tr>
    <tr>
      <th>Cat</th><th>Dog</th><th>Bird</th><th>Rabbit&nbsp;┃</th>
      <th>┃&nbsp;Comedy</th><th>Drama</th><th>SciFi</th><th>Horror&nbsp;┃</th>
      <th>┃&nbsp;Beach</th><th>City</th><th>Mtn</th><th>Cruise</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Reading</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Gaming</strong></td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Sports</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Cooking</strong></td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>C Beach</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C City</strong></td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Mtn</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cruise</strong></td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Comedy</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
    <tr><td><strong>B Drama</strong></td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>B SciFi</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>B Horror</strong></td><td>×</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
  </tbody>
</table>

### Example C: 5 Variables (A, B, C, D, E) - Hard

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (E,D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack ┃</th>
      <th colspan="3">┃ D = Day</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit&nbsp;┃</th>
      <th>┃&nbsp;Mon</th><th>Tue</th><th>Wed</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>E Red</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>E Blue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>E Green</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

## Module 2 - Propositional Logic Representation

*Same grid footprint, now interpreted as propositional relationships.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>D Tue</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>D Wed</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Muffin</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

## Module 3 - Inference / Solving

*Partially solved state during forward/backward chaining.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

## Module 4 - Solution Verification

*Solved grid validated against constraints and entailment checks.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

## Module 5 - Complexity Analysis

*Same verified solution structure used to compute density, branching, and other metrics.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

## Module 6 - Knowledge Representation / Explanation

*Final solved grid used as the visual reference for human-readable reasoning.*

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows (D,C,B)</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink ┃</th>
      <th colspan="3">┃ C = Snack</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water&nbsp;┃</th>
      <th>┃&nbsp;Muffin</th><th>Cookie</th><th>Fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
    <tr><td><strong>C Muffin</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Cookie</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td></tr>
    <tr><td><strong>C Fruit</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Tea</strong></td><td>×</td><td>✓</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Juice</strong></td><td>✓</td><td>×</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td><strong>B Water</strong></td><td>×</td><td>×</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

