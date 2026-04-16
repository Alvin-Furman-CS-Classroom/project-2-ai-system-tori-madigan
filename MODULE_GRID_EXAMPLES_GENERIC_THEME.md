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

### Example A: 3x3 Easy

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows</th>
      <th colspan="3">A = Person ┃</th>
      <th colspan="3">┃ B = Drink</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td></tr>
  </tbody>
</table>

### Example B: 4x4 Medium

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows</th>
      <th colspan="4">A = Person ┃</th>
      <th colspan="4">┃ B = Drink</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey</th><th>Drew&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water</th><th>Soda</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Thu</strong></td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
  </tbody>
</table>

### Example C: 5x5 Hard

<table>
  <thead>
    <tr>
      <th rowspan="2">Rows</th>
      <th colspan="5">A = Person ┃</th>
      <th colspan="5">┃ B = Drink</th>
    </tr>
    <tr>
      <th>Alex</th><th>Blair</th><th>Casey</th><th>Drew</th><th>Emery&nbsp;┃</th>
      <th>┃&nbsp;Tea</th><th>Juice</th><th>Water</th><th>Soda</th><th>Milk</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>D Mon</strong></td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Tue</strong></td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Wed</strong></td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr>
    <tr><td><strong>D Thu</strong></td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr>
    <tr><td><strong>D Fri</strong></td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td></tr>
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

